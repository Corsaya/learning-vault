# Melee Input Display

## Recommendation: M'Overlay

[M'Overlay](https://github.com/bkacjios/m-overlay) is the best fit for displaying live GameCube-controller inputs from Dolphin. It explicitly supports *Melee*, UnclePunch Training Mode, and Slippi, and can display controller ports 1–4.

### Downloads

- [Official repository and downloads](https://github.com/bkacjios/m-overlay)
- [Release history](https://github.com/bkacjios/m-overlay/releases)
- Windows: installer or portable ZIP
- Linux: `.love` package; requires LÖVE 11.3 x64
- macOS: unsupported by the project

### Basic use

1. Start Slippi Dolphin or UnclePunch.
2. Start M'Overlay.
3. Select the correct controller port with number keys `1`–`4`, the scroll wheel, or the settings panel opened with `Esc`.
4. Keep the overlay visible beside the game for practice, or capture it with OBS for recordings.

M'Overlay reads Dolphin rather than merely showing raw operating-system controller input. This makes it preferable for reviewing what the game actually received and supports both Slippi netplay and replay playback.

## Recording recommendation

For coaching review, record:

- The full game at its original speed
- Game audio if convenient
- M'Overlay in a corner without covering percent, stocks, or stage edges
- At least 720p and 60 fps when possible

The input display is helpful but optional. Ordinary gameplay video is enough for strategic review. A `.slp` replay is also worth preserving because Slippi stores replay data and supports playback and analysis.

## Alternative: OBS Gamepad Plugin

[obs-gamepad](https://github.com/P1n3appl3/obs-gamepad) provides a Melee-style controller visual directly in OBS and has Windows and Linux installation paths. It reads the connected gamepad rather than Dolphin memory, so M'Overlay is the default recommendation for Slippi-specific review.

## Status

- [x] Download M'Overlay Linux installer (`~/Downloads/m-overlay-x64-installer.love`)
- [x] Install native CachyOS LÖVE 11.5 runtime (`/usr/bin/love`)
- [x] Bypass the incompatible graphical installer and install the application manually
- [x] Create the `M'Overlay` KDE application launcher
- [ ] Confirm it detects the active Slippi/UnclePunch controller port while Dolphin is running
- [ ] Create an OBS scene with gameplay and input display
- [ ] Record a short test clip and verify 60 fps playback

### Local installation record

- M'Overlay installer SHA-256: `f080f25e353bc6c374c3cf2b4fa779cb1288500051af53a8d964cd4d934071f2`
- LÖVE AppImage SHA-256: `65a673406431eff7167a15a032bf7a2e4ba50108e091eb7b176465831f9b5e00`
- A rootless AppImage was tried first; the native CachyOS package was later installed when M'Overlay's required process capability proved incompatible with AppImage private-library loading.
- Launch from the KDE application menu as `M'Overlay`, or run `~/.local/bin/m-overlay`.
- Installed application: `~/.local/opt/m-overlay/application-linux.love`.
- Patched application SHA-256: `18b3165c5e3c052bd77e4ad0895374f867d48249e7cde9b7a9e5e5f6e1478ad4`.

### Linux installer failure and workaround

The upstream `.love` installer opened to an error stating that `ssl.core` could not be found:

![[Attachments/MOverlay Linux ssl.core Error 2026-08-28.png]]

The installer and main application start an HTTPS downloader thread that depends on the native LuaSec `ssl.core` module. That module is not included in the official standalone LÖVE 11.5 AppImage. The actual `application.love` release was therefore downloaded directly from the official M'Overlay GitHub release and patched so only the automatic-download/self-update component is disabled. Controller display functionality remains enabled. Future M'Overlay updates must be installed manually.

The first patched archive was rebuilt with `./` prefixes on its ZIP entries, causing LÖVE to report “No code to run” because it could not see `main.lua` at the exact archive root. It was rebuilt again with normalized paths and successfully launched.

A second `ssl.core` error came from a separate GitHub update-check thread:

![[Attachments/MOverlay Linux Web Thread and Permissions Error 2026-08-28.png]]

That network-only thread was also disabled. The window title additionally reported `Invalid permissions` because CachyOS uses `kernel.yama.ptrace_scope=1`, while M'Overlay needs to read Dolphin's process memory. The native CachyOS `love` package was installed and only `/usr/bin/love` was granted `cap_sys_ptrace=eip`. This avoids weakening the system-wide ptrace policy. The launcher now uses `/usr/bin/love`; both background SSL threads are disabled, and the corrected application launches without terminal errors.
