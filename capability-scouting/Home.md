---
date: 2026-07-03
tags: [capability-scouting, jarvis, claude, homelab]
status: active
---

# Capability Scouting — Home

The standing collection point for repos, videos, reels, and articles that
could improve the Claude/Jarvis setup — on this box, the ThinkPad, the
Alienware, and eventually the phone. This is the "simple Obsidian folder of
repo and media links" from the 2026-07-03 session; scouting runs append to
[[Links]].

## Why this exists

Priorities (2026-07-03):
1. Replicate as much Fable-5-class capability locally as possible, **or**
   make enough money + profit with it to justify paying for it.
2. Everything adopted here should be installable on the other devices too —
   definitely the ThinkPad, possibly the phone.

## Safe-adopt protocol (from fable-5-launch-prep §8B)

Never install a scouted repo straight into a live setup:

1. Clone into a **git worktree / sandbox directory**, not a live repo.
2. Read the code (at minimum: what it executes, what it phones home to).
3. Test in the sandbox.
4. Only then incorporate, and log the adoption in [[Links]] with the date.

**Now tool-backed (2026-07-08):** `repo-scout search "<query>"` ranks
candidates and `repo-scout adopt owner/repo` does step 1 + prints the review
checklist automatically (`~/code/repo-scout`, sandbox at `~/code/_sandbox/`).
The full loop lives in `~/code/jarvis/SELF-IMPROVEMENT.md`.

## Device matrix

| Device | Address | Status |
|---|---|---|
| Main box (CachyOS, fish) | this machine | primary — everything lands here first |
| Alienware | see private device list | claude-mem sync target |
| ThinkPad | see private device list | claude-mem sync target; second install target |
| Phone | — | future; unvetted path (see Links → Cross-device) |

## How entries get added

- Manual: paste a link into [[Links]] under the right section with a
  one-line "why".
- Scouting runs: a Claude session (later: Jarvis's GitHub-searcher
  component, master plan build #4) searches `gh` / web, ranks candidates,
  and appends them — marked **unvetted** until the safe-adopt protocol has
  run.

## Note index (dated subfolders)

- **2026-07-06/** — [[2026-07-06-fable5-clone-research|clone research]] ·
  [[2026-07-06-fable5-clone-test-prompt|hiragana A/B test prompt]]
- **2026-07-07/** — [[2026-07-07-blueprint-vault-and-moneymaking|Blueprint Vault + monetization]] ·
  [[2026-07-07-fable5-clone-content-brand-test-prompt|content-brand A/B test prompt]] ·
  [[2026-07-07-sideA-fable5-hiragana-plan|Side A: hiragana plan]] ·
  [[2026-07-07-sideA-fable5-content-brand-plan|Side A: content-brand plan]] ·
  [[2026-07-07-fable5-real-system-prompt-capabilities|real Fable 5 system-prompt capabilities]]
- **2026-07-08/** — [[2026-07-08-jarvis-v4-notebooklm-deep-dive|JARVIS V4 video + NotebookLM deep dive]]
- Root: [[fable5-clone-persona-v2]] — the paste-first Opus persona distilled
  from the real Fable 5 prompt (supersedes the v1 clone prompt)

Related: [[fable-5-launch-prep]] · [[claude-improvement-notes]] ·
[[needs-wants-interview-kit]] · [[compounding-loop-money-smart-healthy]] ·
`jarvis/` vault (pointer to `~/code/jarvis`)
