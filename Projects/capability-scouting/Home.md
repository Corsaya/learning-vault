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

Priorities (Donovan, 2026-07-03):
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

## Device matrix

| Device | Address | Status |
|---|---|---|
| Main box (CachyOS, fish) | this machine | primary — everything lands here first |
| Alienware | 10.0.0.225 | claude-mem sync target |
| ThinkPad | 10.0.0.197 | claude-mem sync target; second install target |
| Phone | — | future; unvetted path (see Links → Cross-device) |

## How entries get added

- Manual: paste a link into [[Links]] under the right section with a
  one-line "why".
- Scouting runs: a Claude session (later: Jarvis's GitHub-searcher
  component, master plan build #4) searches `gh` / web, ranks candidates,
  and appends them — marked **unvetted** until the safe-adopt protocol has
  run.

Related: [[fable-5-launch-prep]] · [[claude-improvement-notes]] ·
`personal/Projects/jarvis/` (pointer to `~/code/jarvis`)
