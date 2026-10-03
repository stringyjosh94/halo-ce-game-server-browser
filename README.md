# Halo CE Server Browser for Android

**Find a game. Tap Join. Play Halo.**

Halo CE Browser brings community multiplayer listings directly into Halo: Combat Evolved on Android. Open **Servers**, see the available lobbies, and join from inside the game—without copying an invite into another app or navigating to System Link yourself.

[**Download the latest APK**](https://github.com/stringyjosh94/halo-ce-game-server-browser/releases/latest) · [Report a problem](https://github.com/stringyjosh94/halo-ce-game-server-browser/issues) · 

## What you get

- **An in-game server browser:** community listings from [Puma @ Milenko.org](https://halo.milenko.org/) alongside broker-discovered rooms and saved invites.
- **Lobby details before joining:** reported player counts, map and game mode help you choose a game. Full, closed and incompatible listings are blocked from joining.
- **Join with a tap:** multiplayer networking starts automatically, connects to the selected host, and opens the lobby.
- **A clear screen while playing:** the Servers button hides during gameplay and returns in the menus.
- **Updates on your phone:** releases keep the browser modifications while following published releases of the upstream port.

## Start playing

1. Open [Releases](https://github.com/stringyjosh94/halo-ce-game-server-browser/releases/latest) and download **`halo-browser.apk`**. The ZIP contains the same APK with build information and licenses; you do not need it to install.
2. Install the APK on your Android phone. You may need to allow your browser or Files app to install apps.
3. On first launch, select your own Xbox Halo: Combat Evolved disc image when prompted so the app can extract its maps. Game data is not included.
4. Open **Servers**, choose an available lobby, and tap **Join**. Use or select your player profile when needed.

Already using Halo CE Browser? Install newer releases using **Update**, without uninstalling, to keep this app's maps, profiles and saves. The original cybersecurity app is a separate installation; its data does not automatically move into this app.

## How it works

The browser reads public lobby listings from [Halo Milenko](https://halo.milenko.org/) while the panel is open. It also supports rooms advertised through public MQTT discovery brokers and invite links you save. Counts and availability come from the listings and can change before you join.

When you tap Join, the app starts Halo's multiplayer networking and uses the selected room's invite to establish the upstream port's peer connection. It then waits for that specific host's game advertisement and enters its lobby automatically. The directory helps you find a room; gameplay uses the host connection rather than passing through this repository.

This browser cannot discover every person playing Halo or every private invite. A room needs to appear in a supported directory, be advertised through discovery, or have a shared invite. Browsing Milenko does not automatically publish your own room there. Hosts and players need compatible network versions; routers and NAT can still prevent some connections.

## Keeping the browser up to date

The app checks this repository's modified releases at startup and offers an update when one is available. Android asks you to confirm installation. Our GitHub workflow checks upstream every six hours and builds a new signed APK when the upstream release or our patch changes. If a patch no longer applies or a build fails, no new update is published.

Players only need the APK. Repository setup and signing secrets are for people maintaining their own builds; see [the build guide](docs/BUILDING.md).

## Credits

- **[cybersecurity / halo-ce-universal](https://github.com/cybersecurity/halo-ce-universal)** — the underlying Halo port, Android app, peer networking and upstream releases. This project adds browser and joining changes on top of that work.
- **[Halo Milenko](https://halo.milenko.org/)** — the community server directory that supplies public lobby listings used by this browser. Please visit and support the original service.
- **[bnunu/halo-1](https://github.com/bnunu/halo-1)** and **[punpckhdq/halo](https://github.com/punpckhdq/halo)** — the decompilation projects credited by the upstream port.
- **Bungie and Microsoft** — the original Halo: Combat Evolved game and its creators.

This is an independent community modification. It is not an official release from cybersecurity, Milenko, Bungie or Microsoft. Upstream and bundled dependency license notices remain applicable and are included with the build where supplied.

## Help improve it

Found a problem? [Open an issue](https://github.com/stringyjosh94/halo-ce-game-server-browser/issues) with your phone model, Android version, APK release number, and what happened when you tapped Join. Suggestions and patch contributions are welcome. If you enjoy it, star the repository and share the release link with other players.
