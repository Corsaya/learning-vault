---
title: Key Decisions
tags: [ai-improvement, decisions]
created: 2026-07-06
---

# Key Decisions

Dated log of decisions worth recalling later, so reasoning isn't lost after
a session ends or buried in CLAUDE.md prose. Idea adapted from
obsidian-mind's `brain/Key Decisions.md`. One entry per decision — what was
decided, and why, in a sentence or two.

- **2026-07-05** — Vault split so OpenClaw (external agent) can be pointed
  at day-to-day reference vaults while `personal-private/` (journal,
  health, daily, identity-linked content) stays fully walled off from any
  AI. Rationale: external-agent exposure needed a hard boundary, not a soft
  one.
- **2026-07-06** — Crew 2k/weight goal: the new training plan's 6:30–6:38
  track is canonical over the old sub-6:10 @ 180 lb goal. Donovan's
  reasoning: flexible body comp (clean bulk/cut/dirty bulk all viable),
  priority is continuous time drops all summer and season, not one peak
  number. Full detail: [[../personal/Health/Proposals 2026-07-06/04 - Decisions Log|Decisions Log]].
- **2026-07-06** — Added `private-vault-guard.py` as a PreToolUse hook:
  converts the "no AI in personal-private" rule from a norm into an
  enforced block, with an explicit allowlist file for scoped exceptions
  (currently just `Health`). Rationale: a rule that only lives in prose can
  be forgotten or talked around across a long session; a hook can't.
- **2026-07-06** — Installed obsidian-claude-code (Roasbeef's Obsidian
  sidebar plugin) into `ai-improvement` and `learning` vaults only, not
  `personal`/private or `finance`/`jarvis`/`card-flip`. Rationale: smallest
  reasonable blast radius for a first install; expand later if useful.
