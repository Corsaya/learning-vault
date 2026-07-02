---
date: 2026-07-01
tags: [jarvis, session-wrap, claude-code]
---

# Jarvis Session Wrap — 2026-07-01

First implementation session. Repo went from design-only (16 tests, config.py
+ memory.py) to a nearly-complete v1 spine. **75/75 tests passing.** Every
component was proposed → approved → built via the propose/wait/implement
protocol in `~/code/jarvis/CLAUDE.md`, one at a time, with a chat-Claude
handoff loop for design review.

## Built this session

| Component | File(s) | Decision |
|---|---|---|
| Message type | `jarvis/message.py` | DEC-014 — frozen dataclass, str+tuple role validation (not Enum) |
| Prompt Builder | `jarvis/prompt.py` | DEC-015 — pure function, empty memory omits system block |
| Config timeout | `jarvis/config.py` | `llm.timeout_seconds` field, default 120 |
| LLM subprocess client | `jarvis/llm/{base,client}.py` | DEC-016 — `claude -p` invocation **verified against the live binary (2.1.198)**, not guessed. Full JSON schema, error taxonomy (`LLMNotFoundError`/`LLMTimeoutError`/`LLMResponseError`), real fixtures in `tests/fixtures/` |
| Model Router | `jarvis/llm/router.py` | DEC-017 — permissive explicit model ids (a typo'd tier silently becomes a bad model id → 404 at call time, accepted tradeoff) |
| Session Manager | `jarvis/session.py` | DEC-018 — window counted in messages not exchanges; record-after-response ordering (resolves an ambiguity in ARCHITECTURE.md's data-flow diagram vs the Prompt Builder's contract) |
| Usage Tracker | `jarvis/usage.py` | DEC-019 — **decided not to reuse ccdash** (`~/code/usage-monitor`); different layers (live Response-fed vs log-parsing), ccdash's integration point is the future Briefing component instead |

Also added: `HANDOFF.md` gitignored, 3 new `[Gotchas]` entries (don't pass
`--bare` to `claude -p` — breaks subscription auth; fixtures are 2.1.198
snapshots not a spec; parse stdout before trusting exit code), and — as of
this wrap — a standing instruction to write one of these summaries at the end
of every jarvis session.

## What's NOT done yet

**`jarvis/cli.py` — proposed but not approved, no code written.** This is the
last v1 component (wires config → memory → prompt → router → client → session
→ usage into the interactive loop). The proposal covers ~12 sub-decisions
(command set, unknown-command handling, empty input, `/model` did-you-mean,
failed-call behavior, per-turn memory reload, `/usage` rendering, `__init__.py`
exports, entry point). Two things need an explicit call before implementing:

1. **Confirm**: on a failed LLM call, don't record the turn to history at all
   (no `/retry` in v1 — user just retypes).
2. **Pick**: leave ARCHITECTURE.md's data-flow diagram as-is (high-level
   shorthand, precise ordering lives in DEC-015/018) vs. update the diagram to
   match. Recommended: leave it.

## Next session

1. Resume by pointing at `DECISIONS.md` DEC-014 → DEC-019 and this file — no
   need to re-derive anything.
2. Answer the two open items above, approve the cli.py design, implement it.
3. Once cli.py lands, v1 is code-complete. **First live end-to-end smoke test
   should run on `/model fast`, not full** — no reason to spend Fable-5 tokens
   confirming plumbing works.

Source of truth for full rationale: `~/code/jarvis/DECISIONS.md`.
