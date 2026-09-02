---
title: TerraFirmaGreg Modern 0.13.9 Server Migration
date: 2026-09-01
tags: [minecraft, terrafirmagreg, server, migration]
status: transferred; first launch pending
source_pack: TerraFirmaGreg 0.13.7
destination_pack: TerraFirmaGreg-Modern-0.13.9-serverpack
---

# TerraFirmaGreg Modern 0.13.9 Server Migration

## What was transferred

Migrated the persistent server state from `/home/donovan/Desktop/TerraFirmaGreg 0.13.7` to the separately installed `/home/donovan/Desktop/TerraFirmaGreg-Modern-0.13.9-serverpack`.

- `world/` — copied recursively, excluding the stale `session.lock`
- `backups/` — copied recursively
- `DiscordIntegration-Data/` — copied recursively
- `server.properties`, `eula.txt`, `user_jvm_args.txt`
- `ops.json`, `whitelist.json`, `banned-ips.json`, `banned-players.json`
- `usercache.json`, `usernamecache.json`

The new pack's `mods/`, `config/`, `defaultconfigs/`, libraries, scripts, and launch files were retained. Copying those old 0.13.7 files into 0.13.9 would defeat the purpose of the clean server-pack upgrade and could introduce version mismatches.

## Exact process

1. Confirm the old server is stopped. A running server can leave a partially written world or a live `session.lock`.
2. Keep the 0.13.9 server pack in a separate directory. Do not update the old installation in place.
3. Copy the old `world/` to the new pack and omit `world/session.lock`.
4. Copy `backups/` if rollback points are wanted.
5. Copy server-specific state: properties, EULA, JVM settings, operator/ban/whitelist files, player caches, and Discord integration data.
6. Do not copy old `mods/`, `config/`, or `defaultconfigs/`; let the 0.13.9 server pack supply its own compatible files.
7. Start the new server using its supplied launcher. Let it complete conversion, then check the server log for fatal errors and join with a matching 0.13.9 client.
8. Verify the overworld, Nether, End, player inventories, permissions, whitelist, and an existing backup restore point before retiring the old 0.13.7 directory.

## Reference

The official TFG Modern update guidance recommends extracting a new server pack in a separate folder, transferring the old world and optional backups, plus server-specific files such as the whitelist, then validating the new server before deleting the old one: <https://wiki.terrafirmagreg.team/modern/en_us/modpack/reinstalling>.

## Scope note

This was a minor 0.13.x migration. The wiki's dedicated world-conversion instructions apply to the major 0.12 → 0.13 transition, not specifically 0.13.7 → 0.13.9. No manual world-data deletion was performed.
