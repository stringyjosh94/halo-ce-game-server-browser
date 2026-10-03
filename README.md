# Modified Halo CE Android: phone updates

This repository builds our modified Android app from the latest cybersecurity/halo-ce-universal **published Android release**. It preserves the custom package `com.halo.decomp.browser`, uses the existing custom signing key, includes Milenko listings under the in-game Servers button, hides that button during gameplay, and automatically joins the selected host's lobby. A saved player profile is reused; if none exists, choose a profile in the lobby.

The app downloads **the original android repo*, not the unmodified upstream APK. The workflow checks cybersecurity every six hours, applies `custom-halo.patch`, builds and signs the APK, and publishes a `build-N` release. The channel is embedded automatically from `GITHUB_REPOSITORY`. The installed modified app checks this channel on startup and opens Android's installer for newer builds. Android still requires confirmation to install an update.

## Builds and compatibility

An upstream release or a change to our patch/build files triggers a new custom build. Workflow version codes are `1000000 + GITHUB_RUN_NUMBER` and are higher than the initial custom APK's version. Keep this repository for future updates so build numbers remain increasing.

If upstream changes conflict with our patch, the job fails before publication. You keep the last working modified app; the failed patch needs repair. This cannot guarantee that every future upstream change merges automatically. If scheduled checks are delayed or disabled, use **Run workflow** on your phone to check manually.

`custom-halo.patch` is based on official build-74, commit `80d30410c8db28f4008b92f4e012a1b046ece14e`. Game assets are not included; use your existing Xbox Halo maps. No hosting is deployed by this template and no GitHub account/repository has been created for you.


