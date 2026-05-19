# Cider labeled as Chromium in Audio Volume

Cider is built on Electron, which hardcodes `application.name = "Chromium"` and `application.icon-name = "chromium-browser"` in its audio initialization. This causes it to appear as "Chromium" in KDE's Audio Volume mixer.

The fix is a server-side PipeWire rule that overrides these properties when Cider connects.

## Fix

Create the drop-in config file:

```
mkdir -p ~/.config/pipewire/pipewire-pulse.conf.d
```

Create `~/.config/pipewire/pipewire-pulse.conf.d/rename-cider.conf`:

```
pulse.rules = [
  {
    matches = [ { application.process.binary = "Cider" } ]
    actions = {
      update-props = {
        application.name      = "Cider"
        node.name             = "Cider"
        application.icon-name = "cider"
        application.icon_name = "cider"
      }
    }
  }
]
```

Then restart PipeWire and relaunch Cider:

```
systemctl --user restart pipewire pipewire-pulse wireplumber
```

## Notes

- `application.process.binary = "Cider"` — the actual binary name; verify with `pactl list sink-inputs | grep binary` while Cider is playing
- Both `icon-name` (PipeWire style) and `icon_name` (PulseAudio style) are set for compatibility with different mixer widgets
- The `cider` icon ships at `/usr/share/pixmaps/cider.png` on Arch-based systems via the `cider` AUR package
- This fix survives PipeWire and WirePlumber updates since it lives in the user config drop-in directory
