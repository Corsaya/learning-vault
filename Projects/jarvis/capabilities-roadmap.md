---
tags: [jarvis, roadmap, capabilities]
created: 2026-07-03
reference: https://www.instagram.com/p/DY4o8dluXdK/ (lukebuildsai "Jarvis", 343K likes)
---

# Jarvis — Capabilities: current, planned, and the gap to the viral builds

The reference (lukebuildsai's viral Jarvis, and the open-source builds like
isair/jarvis and Julian-Ivanov/jarvis-voice-assistant it resembles) is a
**voice-first desktop agent**: wake word → spoken conversation → it manages
your calendar, automates the OS, controls the browser, builds small apps on
command, greets you with weather + tasks, and remembers everything.

## What Jarvis can do today (v1, code-complete 2026-07-03)

| Capability | Status |
|---|---|
| Terminal chat with tiered model routing (`fast`/`standard`/`full` → Haiku/Sonnet/Fable 5) | ✅ live |
| Runs on the Claude subscription via `claude -p` subprocess — no API bill (DEC-011) | ✅ live |
| Long-term memory: `identity.md` + `/remember` facts, injected every session | ✅ live (identity.md still blank — you-task) |
| 10-turn conversation window | ✅ live |
| Usage/spend tracking: `/usage`, threshold warnings, per-turn spend log → `ccdash --watch` | ✅ live |
| Self-improvement: `jarvis improve "<request>"` proposes its own diffs (read-only agent), `--apply` gated by tests | ✅ built, first real run pending |
| 109/109 tests; committed at `~/code/jarvis` | ✅ |

## Already designed (architecture seams — next builds)

1. **DEC-013 — daily AI-news brief + weekly survey** on first launch of the
   day/week, any device. *Approved in principle; needs its design pass.* This
   is the "greets you with your briefing" feature from the reels.
2. **Obsidian read-only retrieval (v2)** — Jarvis answers from the second
   brain. The moat none of the viral builds have: 106 daily notes, school,
   card-flip data.
3. **Voice I/O** — an explicit extension point (I/O adapter at the CLI layer;
   everything below is text-agnostic). Local STT/TTS (whisper.cpp + piper)
   keeps it free, per launch-prep §5.
4. **Daemon mode** — socket/IPC server seam; prerequisite for wake-word and
   hotkey invocation.
5. **Semantic memory retrieval (v2)** — swap flat-load for retrieval when
   facts.md grows.
6. **Shell control with authority limits** (launch-prep §5, vierisid pattern)
   — "Jarvis, open my crew schedule" territory. Needs its own DECISIONS
   entry; v1 deliberately excludes autonomous actions.

## The honest gap to the Instagram Jarvis

| Viral-build feature | Our path | Effort |
|---|---|---|
| Voice wake word + spoken replies | Extension point exists; local STT/TTS | Medium (a weekend once daemon mode exists) |
| Morning greeting (weather/tasks/news) | DEC-013 is exactly this | Small — next build |
| Calendar/email | Planned for **Odysseus** (GUI layer, shared vault), not Jarvis | Medium (Docker install first) |
| OS/browser automation | Not in v1 by design (safety); needs authority-limits design | Medium-large |
| "Builds apps on command" | `jarvis improve` already self-modifies; general app-building = pass-through to Claude Code | Small (a `/code` meta-command that shells out) |
| Persistent everything-memory | facts.md + planned Obsidian retrieval — arguably better grounded | On track |

**Bottom line:** the spine the viral builds sit on is done. The showy 20%
(voice, morning brief, OS control) is layered on defined seams — briefing
first (DEC-013), then daemon + voice, then authority-limited shell control.
One honest note from the reference post's own comments: a top reply was
"and we're burning 10k on tokens" — our DEC-011 subprocess + tier routing +
ccdash exist precisely so that doesn't happen here.
