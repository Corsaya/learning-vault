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
- **2026-08-12** — **Reversed the 2026-07-05 and 2026-07-06 decisions above.**
  The vault split and the `private-vault-guard.py` hook are both retired: AI now
  has full read/write everywhere by default, and the only exclusion is a doc
  Donovan explicitly marks **"locked"**. Vaults restructured to `learning/`,
  `finance/`, `pytheas/`, `life/`, `agonizing-sentience/` (subtree merges, full
  history preserved). Rationale: the hard boundary cost more in friction than it
  bought in safety once the external-agent (OpenClaw) scope was pinned to named
  vaults instead. Recorded here so the log reads as a sequence, not a
  contradiction.
- **2026-08-25** — **Japanese grammar spine switched to Genki + JLPT books**,
  superseding the Tae Kim recommendation in
  `learning/Japanese/Resources/Genki vs Tae Kim.md`. Rationale: that note
  optimized for a proactive self-directed learner, but the honest record (kana
  still unfinished since May 2026) says the missing ingredient is external
  structure — which is exactly what Genki's chapters and workbook provide.
- **2026-08-25** — **Migrated off Claude Code to Codex / GPT-5.6.** Subscription
  ended 2026-08-26. `AGENTS.md` added at the vault root; claude-mem exported to
  markdown; ccdash/claude-mem/hook rules marked retired in `CLAUDE.md`. Full
  handoff now lives in `pytheas/Operations/Handoff/`.
- **2026-08-31** — **Long Codex work uses milestone handoffs instead of one
  indefinitely growing conversation.** At a completed phase, preserve the
  verified state, decisions, unfinished work, next action, and required files;
  then begin a new thread when the objective changes. Rationale: this keeps
  continuity auditable while reducing irrelevant context carried into future
  requests. Full protocol: [[Codex Usage and Context Protocol]].
