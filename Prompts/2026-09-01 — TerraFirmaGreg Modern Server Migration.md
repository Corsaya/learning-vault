---
date: 2026-09-01
tags: [prompt-log, minecraft, terrafirmagreg, server-migration]
model: Codex (GPT-5)
tools: [filesystem, official TerraFirmaGreg Modern wiki]
result: persistent server state transferred to the 0.13.9 serverpack; migration record created
---

# TerraFirmaGreg Modern Server Migration Prompt

## Prompt

> transfer this to /home/donovan/Desktop/TerraFirmaGreg-Modern-0.13.9-serverpack, and respond with the process of exactly how, log in Obsidian/personal-vault https://wiki.terrafirmagreg.team/modern/en_us/

## Result

Used the official server-update workflow: kept the new server pack separate; copied the old `world` without its `session.lock`, optional backups, and server-specific operational files; retained the new pack's version-specific mods and configurations. The full process and verification checklist are in [[TerraFirmaGreg Modern 0.13.9 Server Migration — 2026-09-01]].
