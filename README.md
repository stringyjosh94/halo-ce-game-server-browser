# Modified Halo CE Android: phone updates

This repository builds our modified Android app from the latest cybersecurity/halo-ce-universal **published Android release**. It preserves the custom package `com.halo.decomp.browser`, uses the existing custom signing key, includes Milenko listings under the in-game Servers button, hides that button during gameplay, and automatically joins the selected host's lobby. A saved player profile is reused; if none exists, choose a profile in the lobby.

The app downloads **this repository's rebuilt APK**, not the unmodified upstream APK. The workflow checks cybersecurity every six hours, applies `custom-halo.patch`, builds and signs the APK, and publishes a `build-N` release. The channel is embedded automatically from `GITHUB_REPOSITORY`. The installed modified app checks this channel on startup and opens Android's installer for newer builds. Android still requires confirmation to install an update.

## One-time setup from your phone

1. Create a GitHub account and a **public** repository, for example `halo-ce-browser`, with default branch **main**. The app's download endpoint uses public releases; no account token is stored in the APK.
2. Unzip the supplied repository archive and upload its files into the repository. Upload the files, not the ZIP. Include `tools/update.py`, `custom-halo.patch`, and `.github/workflows/update.yml`. If your phone cannot upload the hidden `.github` folder, use **Add file → Create new file**, enter `.github/workflows/update.yml` as the filename, and paste the supplied workflow's text.
3. In **Settings → Secrets and variables → Actions**, add these repository secrets:
   - `BROWSER_KEYSTORE_BASE64`: paste the contents of the separately supplied **PRIVATE-browser-signing-key-base64.txt** file.
   - `BROWSER_KEYSTORE_PASSWORD`: `android`.
   Keep the key out of repository files and releases. It must remain the exact existing key so updates install over your current custom APK and preserve its data. Do not regenerate it.
4. Open **Actions → Update modified Halo Android → Run workflow**. If Actions asks you to enable workflows, enable them. Wait for a successful run.
5. Open **Releases**, download `halo-browser.apk`, and install it using **Update** over your current Halo CE Browser. This one-time install embeds your actual repository's update channel.
6. Later, open Halo CE Browser on your phone. When a modified update is published, accept its update prompt. The first time, Android may ask you to allow Halo CE Browser to install apps. Your maps, profiles and saves stay in this app's data folder; don't uninstall it first.

The APK delivered before your repository exists has no channel configured. The first APK built by your repository connects the updater automatically. No PC or locally hosted directory is needed after setup. The original Halo app, if installed, remains a separate package.

## Builds and compatibility

An upstream release or a change to our patch/build files triggers a new custom build. Workflow version codes are `1000000 + GITHUB_RUN_NUMBER` and are higher than the initial custom APK's version. Keep this repository for future updates so build numbers remain increasing.

If upstream changes conflict with our patch, the job fails before publication. You keep the last working modified app; the failed patch needs repair. This cannot guarantee that every future upstream change merges automatically. If scheduled checks are delayed or disabled, use **Run workflow** on your phone to check manually.

`custom-halo.patch` is based on official build-74, commit `80d30410c8db28f4008b92f4e012a1b046ece14e`. Game assets are not included; use your existing Xbox Halo maps. No hosting is deployed by this template and no GitHub account/repository has been created for you.

The local APK compiled and its signing key was verified. The GitHub workflow is prepared and its probe/patch logic is checked locally; a hosted Actions build is not verified until your first workflow run succeeds. Live lobby joining needs testing on your Android device.

GitHub instructions: [create a repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository), [run a workflow manually](https://docs.github.com/en/actions/how-tos/manage-workflow-runs/manually-run-a-workflow), [Actions secrets](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets).
