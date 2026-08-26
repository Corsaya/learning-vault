# Memory Export — Albums

Exported 2026-08-25 from claude-mem (`~/.claude-mem/claude-mem.db`) before the
Claude Code subscription ended. Machine-generated session records, preserved as
portable markdown. Not hand-written — treat as a log, not as authored notes.

## Session summaries

### 2026-08-06T01:59
- **Request:** Fix CurseForge not launching — app was silently blocked by a stale SingletonLock left by a crashed auto-updater process
- **Investigated:** Checked CurseForge installation location and .desktop file; confirmed it's an AUR package (v1.312.1_36055-1) installed at /opt/curseforge. Inspected ~/.config/CurseForge/logs/ to trace startup failures. Found the auto-updater downloads v1.316.0 from GitLab but fails to install it because it tries to use dpkg/apt (Debian tools absent on CachyOS/Arch). Confirmed stale SingletonLock files were blocking all subsequent launch attempts silently.
- **Learned:** - CurseForge's built-in Electron auto-updater hardcodes dpkg/apt for installation and cannot self-update on Arch-based systems
    - The update provider is GitLab (configured in /opt/curseforge/resources/app-update.yml)
    - A failed auto-updater can leave a stale SingletonLock in ~/.config/CurseForge/, silently blocking all future launches with no visible error
    - /opt/curseforge is root-owned, so even if dpkg were available, a user-space process couldn't write to the install directory
    - The AUR package (curseforge 1.312.1_36055-1) is the same version as what's installed — no AUR update is available yet for v1.316.0
    - The libva error (nvidia_drv_video.so init failed) and GPU process exit are non-fatal on this system — CurseForge recovers and runs normally
    - System is KDE on Wayland; wmctrl/xdotool are not installed and wouldn't work on Wayland anyway
    - Both yay and paru AUR helpers are available at /usr/bin/
- **Completed:** - Diagnosed CurseForge launch failure as a stale SingletonLock from a crashed auto-updater session
    - Killed the stuck CurseForge process tree
    - Cleared stale SingletonLock, SingletonSocket, and SingletonCookie files from ~/.config/CurseForge/
    - Relaunched CurseForge successfully — app reaches the HomePage and operates normally
- **Next steps:** Session appears complete — CurseForge is running. The auto-updater will continue to fail silently on each launch until the AUR package is updated to v1.316.0 and installed via `yay -S curseforge`.

### 2026-08-06T02:00
- **Request:** User asked how to keep CachyOS up to date — confirmed system is fully current with 0 pending updates
- **Investigated:** Ran `yay -Qu` to check for pending AUR and official repo updates; ran `checkupdates` to check official repo updates only. Both returned empty — system is fully up to date.
- **Learned:** - `yay -Qu` reports 0 pending updates — both official repos and AUR packages (including curseforge) are current as of this check
    - `checkupdates` (pacman-contrib tool) is available on the system for offline official-repo update checks
    - The CurseForge AUR package has not yet been updated to v1.316.0, confirming the in-app auto-updater is ahead of the AUR package maintainer
    - `yay -Syu` is the correct all-in-one update command for CachyOS (handles both pacman official repos and AUR packages)
    - Keyring errors on CachyOS are fixed with `sudo pacman -Sy cachyos-keyring` before retrying `yay -Syu`
- **Completed:** - Confirmed system is fully up to date (0 pending updates across all sources)
    - Explained the `yay -Syu` update workflow including PKGBUILD review prompts, pacman-only alternative, dry-run check command, and keyring error recovery
- **Next steps:** Session appears idle — awaiting user response on whether to run `yay -Syu` now or save it for later.

### 2026-08-06T02:00
- **Request:** User asked to run system updates — Claude Code cannot run sudo interactively, so user was instructed to run `yay -Syu` in their own terminal
- **Investigated:** Attempted `yay -Sy` from Claude Code's non-interactive shell; confirmed it fails because sudo requires a terminal for password input. No askpass helper is configured on the system.
- **Learned:** - All privileged pacman/yay operations requiring sudo cannot be executed from Claude Code's shell — must be run from an interactive terminal (Konsole, etc.)
    - System is fully up to date as of this session (confirmed by earlier `yay -Qu` returning 0 results)
    - `yay -Syu` is the correct single command to update both official repo packages and AUR packages on CachyOS
- **Completed:** - Confirmed system is fully up to date
    - Instructed user to run `yay -Syu` in their own terminal to perform updates
    - Offered to review any PKGBUILD diffs that appear during the update process
- **Next steps:** Waiting on user — session is idle pending user running `yay -Syu` in their terminal or issuing a new request.

### 2026-08-06T02:01
- **Request:** User ran `yay -Syu` in their terminal — system confirmed fully up to date, with several AUR packages flagged out-of-date by maintainers but no actual PKGBUILD updates available
- **Investigated:** Output of `yay -Syu` and `sudo pacman -Syu` reviewed. Identified AUR packages flagged as out-of-date (curseforge, mcreator, visual-studio-code-bin) and locally-ahead packages (pipewire/alsa-card-profiles at 1.6.8-1.1 vs repo 1.6.8-1, cider, electron38).
- **Learned:** - curseforge, mcreator, and visual-studio-code-bin are flagged "Out Of Date" on AUR but no updated PKGBUILD has been pushed — yay has nothing to install
    - The CurseForge in-app updater failure is directly caused by the AUR package not yet being updated to v1.316.0; this will persist until an AUR maintainer publishes a new PKGBUILD
    - pipewire and alsa-card-profiles are at version 1.6.8-1.1 locally (CachyOS rebuild) vs 1.6.8-1 in the Arch extra repo — harmless version skew that resolves itself when upstream catches up
    - cider and electron38 are also locally ahead of their AUR listings — normal behavior on CachyOS
    - Both `yay -Syu` and `sudo pacman -Syu` reported "nothing to do" — system is fully current
- **Completed:** - Full system update confirmed complete with no packages upgraded (already current)
    - Explained AUR "Out Of Date" flag vs actual available updates distinction
    - Explained pipewire/CachyOS version skew as harmless
- **Next steps:** Session is idle — all tasks complete. No pending work.

### 2026-08-06T02:04
- **Request:** Fix CurseForge not showing a window — discovered GPU crash (SIGILL) was causing invisible/broken launches; resolved with --disable-gpu flag
- **Investigated:** Examined CurseForge logs, journalctl, coredumpctl, and process state across multiple launch attempts. Traced the root cause to a SIGILL crash in the Chromium GPU process triggered by VAAPI/nvidia_drv_video.so initialization failure. Confirmed via coredumpctl that PID 52888 crashed with SIGILL (illegal instruction, truncated 10MB corefile). Tested --disable-gpu flag as a workaround.
- **Learned:** - CurseForge GPU process crashes with SIGILL (not SIGSEGV) due to NVIDIA VAAPI driver failure on this system
    - SIGILL in Chromium's GPU process typically indicates hardware-specific instruction execution failing when the GPU driver is in a broken state
    - `--disable-gpu` bypasses the entire GPU code path and prevents the crash — app runs stably in software rendering mode
    - KDE Plasma launches CurseForge via systemd user service (app-curseforge@*.service) — `systemctl --user` is the proper management interface
    - The existing core dump (PID 52888, SIGILL) is the only one in the system's coredump log — no new crashes since switching to --disable-gpu
    - CurseForge fully functional with --disable-gpu: reaches HomePage, loads ads, connects to API normally
    - qdbus5 absent but qdbus6 available; KWin DBus API accessible for Wayland window management if needed
- **Completed:** - Identified SIGILL GPU crash as cause of CurseForge not showing a window
    - Launched CurseForge with `--disable-gpu` (PID 61021) — running stably with no core dump for 19+ seconds
    - Confirmed app is functional: analytics calls succeeding, HomePage loaded, ads initialized
- **Next steps:** Waiting on user to confirm whether the CurseForge window is visible on screen. If confirmed working, next step may be making --disable-gpu permanent (e.g., user-level .desktop override at ~/.local/share/applications/curseforge.desktop).

### 2026-08-06T02:04
- **Request:** Fix CurseForge not showing a window — cleared app config/cache and instructed user to reinstall via yay to get a clean state
- **Investigated:** Confirmed ~/Documents/curseforge (2.8GB, Minecraft modpack data: Instances, Downloads, Install, Quickplay) is separate from app config and safe to preserve. Identified ~/.config/CurseForge and ~/.cache/curseforge-updater as the app config/cache directories that can be safely wiped.
- **Learned:** - CurseForge has two distinct data locations: ~/.config/CurseForge (Electron app config, Chromium profile, logs, SingletonLock) and ~/Documents/curseforge (game data: Minecraft instances, mods, downloads)
    - Wiping ~/.config/CurseForge resets app state cleanly without touching modpack installations
    - The SIGILL crash may be either a corrupted install or a fundamental NVIDIA driver/Wayland incompatibility
    - If crash persists after clean reinstall, next diagnostic is forcing XWayland with --ozone-platform=x11
    - `yay -R curseforge && yay -S curseforge` is the full clean reinstall command (requires interactive terminal for sudo)
- **Completed:** - Cleared ~/.config/CurseForge (all Electron app config, logs, SingletonLock, Chromium profile) 
    - Cleared ~/.cache/curseforge-updater
    - Preserved ~/Documents/curseforge intact (2.8GB Minecraft modpack data)
    - Instructed user to run `yay -R curseforge && yay -S curseforge` in their terminal for a clean reinstall
- **Next steps:** Waiting on user to run `yay -R curseforge && yay -S curseforge` in their terminal and report whether CurseForge launches successfully after the clean reinstall. If SIGILL crash persists, next step is testing XWayland mode (--ozone-platform=x11) or investigating NVIDIA driver configuration.

### 2026-08-06T02:10
- **Request:** Fix CurseForge not showing a window — root cause found and permanently fixed via user-level .desktop override with --ozone-platform=x11
- **Investigated:** Exhaustively traced CurseForge window creation failure through: process state, journalctl, coredumpctl, KWin scripting API window lists, CurseForge logs, app.asar strings, libEGL/VAAPI errors, XWayland vs native Wayland modes. Confirmed via KWin that CurseForge process was running but had zero Wayland surface registered with the compositor.
- **Learned:** - Root cause: NVIDIA RTX 4060 (PCI 10de:2786) has no working EGL driver under KDE Plasma's native Wayland DRI2 path — libEGL returns null driver, DRI2 screen creation fails, Chromium GPU process exits, no window surface is ever presented to KWin
    - `--ozone-platform=x11` forces Chromium to use XWayland (X11 compatibility layer) where NVIDIA's driver works correctly — window appeared immediately
    - `--disable-gpu` also prevents the crash (software rendering) but XWayland is better (uses GPU)
    - chmod 555 on ~/.cache/curseforge-updater prevents the 104MB update re-download on every launch (EACCES on mkdir pending/ aborts immediately)
    - CurseForge auto-updater fails because it downloads a .deb and tries dpkg/apt — not compatible with CachyOS (Arch-based)
    - KDE Plasma launches apps as systemd user services (app-curseforge@*.service)
    - KWin scripting via qdbus6 + loadScript is an effective tool for listing/managing windows on KDE Wayland
    - User-level .desktop files at ~/.local/share/applications/ take precedence over /usr/share/applications/ and survive package updates
- **Completed:** - Created ~/.local/share/applications/curseforge.desktop with `Exec=/opt/curseforge/curseforge --ozone-platform=x11 %U` — validated with desktop-file-validate, registered with update-desktop-database
    - CurseForge is now running with a visible 1496×816 window confirmed in KWin window list
    - User logged in to CurseForge successfully via Firefox OAuth
    - ~/.cache/curseforge-updater set to chmod 555 (read-only) to block wasteful 104MB update re-downloads
- **Next steps:** Session appears complete — CurseForge is working. No further active work.

## Observations

### 2026-08-06T01:56 · `discovery` — CurseForge Is Already Fully Installed System-Wide
A search for CurseForge on the system revealed it is already fully installed as a native system package — binary at /usr/bin/curseforge, app files at /opt/curseforge, and a system .desktop file already in /usr/share/applications/. This means it should already appear in the application launcher without any manual .desktop file creation needed. The investigation was likely prompted by a new user request related to CurseForge.

### 2026-08-06T01:56 · `discovery` — CurseForge Already Running as Active Process Since 21:52
When attempting to launch CurseForge to investigate its behavior, the process immediately exited because CurseForge was already running in the background (PID 22791, started ~4 minutes earlier). This is standard Electron single-instance enforcement. The app is working and accessible — no launcher fix is needed for CurseForge itself. A minor non-fatal issue was noted: xdg-mime could not find `qtpaths` when trying to register the curseforge:// protocol handler, but this does not affect normal app operation.

### 2026-08-06T01:57 · `discovery` — CurseForge Auto-Updater Broken on CachyOS — Tries to Install .deb on Arch-Based System
Inspection of CurseForge logs revealed a significant incompatibility: CurseForge's built-in auto-updater distributes updates as .deb packages and invokes dpkg/apt to install them. On CachyOS (Arch-based), neither tool exists, causing every update attempt to silently fail. The app continues to run on the old version (v1.312.1) with no user-visible error. To update, the user would need to manually install the newer version via the CachyOS/AUR package manager or by downloading and installing the updated package directly. The investigation also confirmed that wmctrl/xdotool window management tools are absent, and the Wayland session means X11-based window tools wouldn't work even if installed.

### 2026-08-06T01:57 · `discovery` — CurseForge Installed via AUR — Must Update via AUR Helper, Not Built-in Updater
Confirmed that CurseForge was installed through the AUR on CachyOS. This explains why the built-in auto-updater fails — the AUR PKGBUILD wraps the official binary, but CurseForge's internal updater doesn't know it was installed this way and tries to run dpkg. The correct upgrade path is `yay -Syu curseforge` (or equivalent AUR helper command), which will fetch and install the newer PKGBUILD when the AUR package is updated to match v1.316.0-37372. Until the AUR package is updated by its maintainer, the user is stuck on v1.312.1 regardless of approach.

### 2026-08-06T01:57 · `discovery` — CurseForge Uses GitLab as Update Provider; /opt/curseforge Is Root-Owned
The CurseForge update mechanism is doubly broken on this CachyOS system: first, the updater incorrectly assumes a Debian-based system (tries dpkg/apt); second, even if the right package manager were used, /opt/curseforge is root-owned so the running user process cannot overwrite installation files anyway. The update provider is GitLab (not apt repos), suggesting CurseForge actually downloads a new binary from GitLab releases and then tries to install it via dpkg as a post-download step. The correct fix remains using `yay -Syu curseforge` or `paru -Syu curseforge` once the AUR maintainer updates the package to v1.316.0.

### 2026-08-06T01:57 · `discovery` — No Known Community Fix Found for CurseForge "Neither dpkg nor apt" Error on Arch
A web search confirmed there is no widely-documented fix for the CurseForge built-in auto-updater failing with "Neither dpkg nor apt" on Arch/CachyOS. This appears to be an upstream issue in the CurseForge Electron app itself — the auto-updater assumes a Debian-based host. The correct workaround remains using `yay -Syu curseforge` to update via the AUR when the package maintainer publishes a new version.

### 2026-08-06T01:58 · `discovery` — CurseForge Launches and Functions Normally Despite Failed Auto-Updater
Running a fresh CurseForge instance confirmed the application works correctly end-to-end on CachyOS. It initialized, connected to the CurseForge API, reached the HomePage, and loaded ads — all successfully. The broken auto-updater is a nuisance (it fires and fails silently on each launch) but does not affect normal usability. The app is stuck on v1.312.1.36055 and will remain there until updated via `yay -Syu curseforge`.

### 2026-08-06T01:58 · `discovery` — CurseForge Exits Immediately When Launched via nohup/disown — SingletonLock Collision
An attempt to launch CurseForge persistently via nohup and disown failed because the prior test instance (launched with `timeout 20`) was still running and holding the Electron SingletonLock. CurseForge's single-instance enforcement caused the nohup launch to exit immediately. To launch CurseForge reliably, any existing instance must be terminated first, or the app should be launched from the KDE application launcher directly.

### 2026-08-06T01:59 · `discovery` — Multiple CurseForge Instances Running With Zombie Child Processes
Contrary to the previous observation, the nohup CurseForge launch (PID 54097) did succeed — the pgrep check after 6 seconds simply ran before the process was visible. Two CurseForge main processes are now running simultaneously, which is unexpected given Electron's SingletonLock mechanism. The shared Chromium profile directory (~/config/CurseForge) with LevelDB stores being accessed by two processes simultaneously could cause data corruption or crashes. Additionally, two defunct zombie zygote child processes (52891, 53605) are present, indicating their parent processes haven't reaped them yet.

### 2026-08-06T02:00 · `discovery` — yay/pacman Cannot Run System Updates from Claude Code — Requires Interactive Terminal for sudo
Attempting to refresh package databases via `yay -Sy` from Claude Code's shell failed because pacman requires sudo, and sudo requires an interactive terminal to read the password. This is a hard constraint for all privileged package management operations on this system when invoked from Claude Code. Users must run `yay -Syu` from a regular terminal emulator (e.g., Konsole) directly.

### 2026-08-06T02:01 · `discovery` — Full CurseForge Auto-Updater Error Stack Trace Captured from app.asar
The complete stack trace from the CurseForge auto-updater failure confirms the error originates deep in the startup sequence inside the bundled app.asar JavaScript. The updater runs synchronously during `loadApplication`, attempts to call `quitAndInstall`, which invokes `doInstall`, which checks for dpkg/apt and throws. The error is caught at the `setupAppUpdateService` level and the app continues normally. Patching this behavior would require extracting app.asar with `asar extract`, modifying the JavaScript, and repacking — not a practical fix. The correct solution remains waiting for the AUR package to be updated.

### 2026-08-06T02:02 · `discovery` — CurseForge VAAPI/libva GPU Process Failure Is a NVIDIA Driver Issue
The libva/VAAPI errors logged on every CurseForge launch are caused by the NVIDIA VA-API driver failing to initialize. Chromium's GPU process attempts hardware video acceleration via VA-API using the NVIDIA driver, fails, and exits. A second GPU process attempt also fails. The Electron/Chromium renderer then falls back to software rendering and the app works normally. This is a common issue on Linux systems with NVIDIA GPUs where the nvidia-vaapi-driver package is not properly configured or the driver version doesn't support the requested VA-API interface.

### 2026-08-06T02:02 · `discovery` — KWin DBus Interface Accessible via qdbus6 for Wayland Window Management
Investigation into Wayland-compatible window management tools found that qdbus6 can communicate with KWin via DBus, providing a path to programmatically raise or focus windows (like CurseForge) without wmctrl or xdotool. The KWin DBus API (org.kde.KWin) is confirmed reachable. KDE Plasma on this system is running with OpenGL compositing and tearing allowed. For window focus operations, KWin scripts or DBus calls via qdbus6 are the appropriate tools on this KDE/Wayland setup.

### 2026-08-06T02:02 · `discovery` — CurseForge Runs as a systemd User Service When Launched from KDE — Core Dump Occurred on Test Instance
Journalctl revealed that KDE Plasma manages CurseForge through systemd user services — each launch creates an `app-curseforge@<hash>.service` unit. This means `systemctl --user` is the proper tool for managing CurseForge lifecycle rather than manual process management. The session also produced a core dump from PID 52888 (the timeout-launched test instance), likely caused by running two CurseForge instances simultaneously sharing the same Chromium profile directory. The Fontconfig version skew (cache newer than binary) is a minor cosmetic warning that could be fixed by regenerating the font cache with the current fontconfig version.

### 2026-08-06T02:03 · `discovery` — CurseForge Launches Stably with --disable-gpu Flag — No Core Dump
Launching CurseForge with `--disable-gpu` produced a stable process with no core dump, in contrast to the earlier crash at PID 52888. This confirms the VAAPI/NVIDIA GPU initialization failure was responsible for the previous crash. For a mod manager application with no GPU-intensive UI, software rendering via `--disable-gpu` is a viable workaround that avoids both the crash risk and the libva error spam. The system .desktop file at /usr/share/applications/curseforge.desktop could be modified to include this flag in the Exec line, though that would require root access.

### 2026-08-06T02:03 · `discovery` — CurseForge Crash Was SIGILL (Illegal Instruction), Not a Segfault — Likely GPU Code Path Issue
The coredump details reveal that PID 52888 crashed with SIGILL rather than a typical segmentation fault. This is consistent with Chromium's GPU process attempting to execute hardware-specific instructions (AVX2, SSE4, or GPU shader compilation) that fail when the NVIDIA VAAPI driver is in a broken state. The `--disable-gpu` flag prevents this entire code path from running, resulting in a stable process. The truncated 10MB corefile suggests the system's coredump size limit was hit before the full crash state could be written.

### 2026-08-06T02:04 · `discovery` — CurseForge Data Directory Contains 2.8GB of Minecraft Modpack Data
The CurseForge data directory at ~/Documents/curseforge confirms the user primarily uses CurseForge for Minecraft modpack management. At 2.8GB it contains installed modpack instances, downloaded mod archives, and Minecraft install/runtime files. This directory is separate from the app configuration (~/.config/CurseForge) and persists independently of app reinstalls.

### 2026-08-06T02:05 · `feature` — CurseForge Successfully Relaunched with Fresh Config After Cache Wipe
Following the config/cache wipe of ~/.config/CurseForge and ~/.cache/curseforge-updater, CurseForge was relaunched and initialized a completely fresh configuration directory. The new instance (PID 68853) is running stably with no core dump produced. This confirms the app functions correctly after a clean state reset. The Minecraft modpack data in ~/Documents/curseforge was unaffected throughout.

### 2026-08-06T02:06 · `discovery` — CurseForge v1.316.0 Update Downloaded — AppImage Variant Available and Could Be Used Instead of .deb
A critical discovery: the CurseForge updater downloads both a .deb and an AppImage for v1.316.0-37372. The .deb is cached at ~/.cache/curseforge-updater/pending/CurseForge_1.316.0-37372_amd64.deb. The AppImage variant — if also present in that directory — could be made executable and run directly on CachyOS without needing dpkg. This provides a potential path to running v1.316.0 without waiting for the AUR package to be updated: locate the AppImage in the pending directory, chmod +x it, and run it. The UI is also showing an update button that the user could interact with.

### 2026-08-06T02:06 · `discovery` — KWin Window List Confirms CurseForge Has No Visible Window — Process Running but No Wayland Surface
The KWin window list script confirmed definitively that CurseForge has no visible window surface despite the main process (PID 68853) running. The app is starting, loading the HomePage in its renderer, making API calls, and downloading the update — but never presenting a window to the Wayland compositor. This is likely because the Wayland surface creation is failing or the window is being created off-screen/hidden. The "Failed to open DRM device" errors in KWin logs around the time of CurseForge's first launch attempt are suspicious and may indicate a GPU/DRM resource contention issue affecting window creation.

### 2026-08-06T02:07 · `discovery` — CurseForge Updater Checks Local Cache Before Network — v1.316.0 Was Available Locally
The CurseForge updater uses a two-stage check: first looks for a cached update in ~/.cache/curseforge-updater/pending/, then falls back to downloading from the network. The cache wipe earlier in the session forced a full re-download of the 104MB .deb. The GitLab download URL is not written to the structured log file, only to stdout/journalctl. This means the .deb at ~/.cache/curseforge-updater/pending/CurseForge_1.316.0-37372_amd64.deb is the authoritative copy and should not be wiped if wanting to avoid repeated large downloads.

### 2026-08-06T02:07 · `discovery` — node/npm Available but asar Module Not Installed — Cannot Patch app.asar Without Installing It
Investigation into patching the CurseForge app.asar to bypass the dpkg/apt check confirmed that while Node.js is available, the `asar` npm module needed to extract and repack the archive is not installed. This approach would also require root access to write back to /opt/curseforge. The CloudFront CDN finding confirms CurseForge's analytics backend is on AWS infrastructure (IPv6-only resolution observed), which is informational for network troubleshooting contexts.

### 2026-08-06T02:08 · `discovery` — AutoUpdaterWrapper Source Code Found in app.asar — autoInstallOnAppQuit=false, disableWebInstaller=true
Strings extraction from app.asar revealed the AutoUpdaterWrapper initialization code. The updater will only attempt to install when the user explicitly clicks the "update" button (quitAndInstall is called on user action, not automatically). The `disableWebInstaller=true` setting means there's no fallback path — it exclusively relies on the native package manager (dpkg on Linux). This confirms that ignoring the update button is safe and the app will continue running on v1.312.1 without any automatic forced update.

### 2026-08-06T02:08 · `change` — ~/.cache/curseforge-updater Made Read-Only to Block Update Download Caching
A creative workaround was applied: by making ~/.cache/curseforge-updater read-only, the electron-updater cannot write the downloaded update package to disk. This should prevent the sequence where the updater finds a cached .deb and immediately attempts to install it via dpkg on the next launch. The app will still run normally and the update button may appear in the UI, but clicking it will fail gracefully rather than triggering the dpkg error. This avoids repeated 104MB downloads and the potential for the dpkg error to cause instability.

### 2026-08-06T02:08 · `feature` — Read-Only Cache Dir Workaround Successfully Blocks Update Download — EACCES Instead of 104MB Download
The chmod 555 workaround on ~/.cache/curseforge-updater is confirmed effective. On this launch, the updater found the update metadata, tried to create the pending/ subdirectory, immediately hit EACCES, and aborted — all in under 2ms and with zero network download. This is a significant improvement over the previous behavior (104MB download followed by dpkg failure). The workaround is persistent across launches until manually reversed.

### 2026-08-06T02:08 · `discovery` — CurseForge Window Absent from KWin Due to EGL/DRI2 Screen Creation Failure on NVIDIA
The root cause of CurseForge's invisible window is now clear: the NVIDIA GPU (RTX 4060, PCI 10de:2786) has no EGL driver that works under Wayland's DRI2 path. When Chromium tries to create an OpenGL rendering surface via EGL/DRI2, it gets null for the driver and fails to create the DRI2 screen. Without an EGL surface, the Wayland compositor never receives an xdg_toplevel surface from CurseForge, so no window appears. This is a fundamental NVIDIA/Wayland/EGL compatibility issue on CachyOS — likely requiring either the proprietary NVIDIA EGL driver (libnvidia-egl-wayland) to be installed/configured, or using `--use-gl=swiftshader` or `--disable-gpu` to force software rendering.

### 2026-08-06T02:08 · `discovery` — CurseForge Process Exited — EGL Failure Causes App to Crash Without Showing Window
CurseForge exited without producing a window, consistent with the EGL/DRI2 rendering failure identified in the previous launch's logs. The app initializes enough to make API calls (analytics, update checks) but cannot create the Wayland surface needed to display the UI. The root issue — NVIDIA RTX 4060 (10de:2786) having no working EGL driver under Wayland's DRI2 path — needs to be resolved at the driver level, or bypassed with `--disable-gpu` or `--use-gl=swiftshader`. The `--disable-gpu` launch confirmed earlier in the session was the only successful approach that kept the app running.

### 2026-08-06T02:09 · `discovery` — CurseForge on Wayland/NVIDIA Requires --disable-gpu or Proper EGL Driver to Show Window
The CurseForge window visibility investigation is complete. The root cause is a missing or misconfigured NVIDIA EGL Wayland driver on CachyOS — without it, Chromium/Electron cannot create an EGL rendering surface under Wayland, so no window is ever presented to KWin. The `--disable-gpu` flag bypasses this entirely by using software rendering. The practical permanent fix is to create a user-level .desktop file override that includes `--disable-gpu` in the Exec line, making the app launcher always use this flag without requiring root access or surviving package updates.

### 2026-08-06T02:09 · `change` — CurseForge Launched with --ozone-platform=x11 to Test XWayland Mode
After confirming that native Wayland EGL fails (DRI2 screen creation error, no KWin window surface), XWayland mode is being tested as the next alternative. With `--ozone-platform=x11`, Chromium uses the X11 rendering path, which runs through XWayland on KDE Plasma. NVIDIA's proprietary driver traditionally has better X11 OpenGL support than native Wayland EGL, so this may resolve the invisible window issue without requiring `--disable-gpu` software rendering.

### 2026-08-06T02:09 · `sensitive` — CurseForge Overwolf API Key Visible in Process Arguments
The Curse.Agent.Host background process (CurseForge's local mod management daemon) launches with its Overwolf API key embedded in command-line arguments. On a single-user desktop this is low risk, but it's worth noting for awareness.

### 2026-08-06T02:09 · `discovery` — XWayland Mode (--ozone-platform=x11) Gets Further — Curse.Agent.Host Spawns — But Still No KWin Window
XWayland mode (`--ozone-platform=x11`) is more promising than native Wayland — the process stays alive longer and reaches the point where the Curse.Agent.Host plugin daemon launches. This is further than any previous native-Wayland launch got. However, the KWin window list hasn't been refreshed since this launch started, so it's not yet confirmed whether a window appeared. A fresh KWin script run is needed to check if the XWayland window is now visible to the compositor.

### 2026-08-06T02:10 · `feature` — CurseForge Window Successfully Appears with --ozone-platform=x11 (XWayland Mode)
The root fix for CurseForge's invisible window is confirmed: `--ozone-platform=x11` (XWayland mode). This bypasses KDE Plasma's native Wayland EGL path, which fails for NVIDIA RTX 4060 on this CachyOS system, and instead uses the X11 rendering path through XWayland where NVIDIA's driver works correctly. The app is now fully functional — the user logged in via Firefox OAuth. To make this permanent, a user-level .desktop override at ~/.local/share/applications/curseforge.desktop with `--ozone-platform=x11` in the Exec line needs to be created (no root required, survives package updates).
