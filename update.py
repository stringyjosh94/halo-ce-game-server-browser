#!/usr/bin/env python3
"""Probe official releases; build the patched Android app for this repository."""
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import urllib.error
import urllib.request
import zipfile

ROOT = Path(__file__).resolve().parents[1]
UPSTREAM = 'cybersecurity/halo-ce-universal'

def api(path):
    request = urllib.request.Request('https://api.github.com/' + path,
        headers={'User-Agent': 'Halo-browser-update-workflow', 'Accept': 'application/vnd.github+json',
                 'Authorization': 'Bearer ' + os.environ['GH_TOKEN']})
    with urllib.request.urlopen(request, timeout=30) as response: return json.load(response)

def output(name, value):
    with open(os.environ['GITHUB_OUTPUT'], 'a') as stream: stream.write(name + '=' + str(value) + '\n')

def probe():
    release = api('repos/' + UPSTREAM + '/releases/latest')
    tag = release['tag_name']
    if not re.fullmatch(r'build-[1-9][0-9]*', tag): raise RuntimeError('Unrecognized upstream release tag')
    if not any(a['name'] == 'halo-android-release.zip' for a in release['assets']):
        raise RuntimeError('Upstream release has no Android release')
    # Rebuild after either an upstream release or a change to our patch/build scripts.
    digest = hashlib.sha256()
    for name in ('custom-halo.patch', 'tools/update.py', '.github/workflows/update.yml'):
        digest.update((ROOT / name).read_bytes())
    fingerprint = tag + ':' + digest.hexdigest()
    previous = None
    try: previous = api('repos/' + os.environ['GITHUB_REPOSITORY'] + '/releases/latest')
    except urllib.error.HTTPError as error:
        if error.code != 404: raise
    required = {'halo-browser.apk', 'halo-android-browser.zip', 'upstream.json'}
    build = previous is None or fingerprint not in previous.get('body', '') or not required.issubset({a['name'] for a in previous.get('assets', [])})
    output('build', str(build).lower()); output('upstream', tag); output('fingerprint', fingerprint)
    (ROOT / 'upstream.json').write_text(json.dumps({'tag': tag, 'url': release['html_url'], 'fingerprint': fingerprint}, indent=2))

def run(args, cwd, env):
    subprocess.run(args, cwd=cwd, env=env, check=True)

def build():
    tag = os.environ['UPSTREAM_TAG']; repository = os.environ['GITHUB_REPOSITORY']
    if not re.fullmatch(r'build-[1-9][0-9]*', tag): raise RuntimeError('Invalid upstream tag')
    source = ROOT / 'source'
    env = os.environ.copy()
    run(['git', 'clone', '--branch', tag, '--single-branch',
         'https://github.com/' + UPSTREAM + '.git', str(source)], ROOT, env)
    run(['git', 'apply', '--3way', str(ROOT / 'custom-halo.patch')], source, env)
    # A clean conflict-free patch is required. Errors abort before publication.
    version = 1000000 + int(os.environ['GITHUB_RUN_NUMBER'])
    if version > 2100000000: raise RuntimeError('Version code too large')
    env.update(HALO_BROWSER_VERSION_CODE=str(version), HALO_UPSTREAM_BUILD=tag[6:],
               HALO_BROWSER_UPDATE_REPOSITORY=repository,
               HALO_ANDROID_KEY_ALIAS='androiddebugkey')
    sdk = os.environ['ANDROID_HOME']
    (source / 'port/android/local.properties').write_text('sdk.dir=' + sdk + '\n')
    run(['python3', 'configure.py', '--pgo', 'off', '--compiler-launcher', 'ccache'], source, env)
    run(['ninja', '-j', '4', 'android'], source, env)
    run(['./gradlew', '--console=plain', 'assembleRelease', '-PlocalBrowser'], source / 'port/android', env)
    apk = source / 'port/android/app/build/outputs/apk/release/app-release.apk'
    sdktools = Path(sdk) / 'build-tools/35.0.0'
    run([str(sdktools / 'apksigner'), 'verify', str(apk)], source, env)
    dist = ROOT / 'dist'; dist.mkdir(exist_ok=True)
    shutil.copyfile(apk, dist / 'halo-browser.apk')
    with zipfile.ZipFile(dist / 'halo-android-browser.zip', 'w', zipfile.ZIP_DEFLATED) as archive:
        archive.write(apk, 'halo-browser.apk')
        archive.write(ROOT / 'upstream.json', 'upstream.json')
        for file in (source / 'port/assets/fonts').glob('*OFL*'): archive.write(file, 'licenses/' + file.name)
        for file in (source / 'port/assets/fonts').glob('*LICENSE*'): archive.write(file, 'licenses/' + file.name)
        archive.write(source / 'port/third_party/extract-xiso/LICENSE.TXT', 'licenses/extract-xiso.txt')
        archive.write(source / 'port/third_party/miniupnpc/LICENSE', 'licenses/miniupnpc.txt')
    output('tag', 'build-' + str(version))

if __name__ == '__main__':
    {'probe': probe, 'build': build}[sys.argv[1]]()
