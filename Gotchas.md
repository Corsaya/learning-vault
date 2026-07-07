---
title: Gotchas
tags: [ai-improvement, memory]
created: 2026-07-06
---

# Gotchas

One line per entry — things that bit before, so they don't bite twice.
Idea adapted from obsidian-mind's `brain/Gotchas.md`. Append, don't prune;
if something stops being true, note the date it was superseded rather than
deleting the line.

- **2026-07-06** — `personal/` in the vault is the private wall (Journal,
  Health, Daily, Work, Inbox); the CLAUDE.md-described rename to
  `personal-private/` hasn't happened yet — don't assume the folder name
  matches the doc until that migration lands.
- **2026-07-06** — Health work under `personal/Health/` is a standing,
  explicitly scoped exception to the private-vault wall (not a general
  license for all of `personal/`). Enforced now by
  `~/.claude/hooks/private-vault-guard.py` + its allowlist, not just prose.
- **2026-07-06** — Each Obsidian sub-vault (`personal`, `learning`,
  `ai-improvement`, `finance`, `jarvis`, `card-flip`, etc.) has its own
  `.obsidian/` — a plugin installed in one vault is NOT available in
  another. The obsidian-claude-code sidebar plugin had to be built once
  then copied into each target vault's `.obsidian/plugins/`.
