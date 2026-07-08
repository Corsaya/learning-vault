---
date: 2026-07-03
tags: [capability-scouting, links]
---

# Links

Status legend: **adopted** (in use) · **scouted** (read/ranked, not adopted)
· **unvetted** (candidate only — run the safe-adopt protocol first).

## Owned / built (already on this box)

- `~/code/jarvis` — the assistant itself. **adopted** (v1 complete + api mode + briefing, 147 tests)
- `~/code/usage-monitor` (ccdash) — stdlib Claude usage dashboard, now with the Fable 5 weekly gauge. **adopted**
- `~/code/repo-scout` — repo search + safe-adopt sandbox (automates this file's protocol). **adopted 2026-07-08**
- `~/code/trading` — trading research track. **adopted**

## Jarvis / assistant patterns (scouted 2026-07-01, master plan)

- enochko/jarvis — source of the `claude -p` subprocess pattern (now DEC-011). **scouted**
- OpenJarvis (Stanford) — Morning Digest = reference for the daily-news component (DEC-013). **scouted**
- ethanplusai/jarvis · rezaulhreza/jarvis — surveyed for architecture ideas. **scouted**
- vierisid/jarvis — "authority limits" pattern for letting an assistant run shell commands safely. **scouted**; re-read before the computer-actions round.
- pewdiepie-archdaemon/odysseus — GUI/email/deep-research layer; decision: adopt as second front-end sharing the vault as memory. **scouted**, adoption pending (~1,400 open issues — daily driver, not critical infra).
- msitarzewski/agency-agents (The Agency, 232 agents) — agent bundle; also a candidate product template. **scouted**

## Usage / cost

- ryoppippi/ccusage — historical usage breakdowns (node). **scouted**; rejected as ccdash dependency, still useful standalone.
- Maciek-roboblog/Claude-Code-Usage-Monitor — live dashboard, burn-rate prediction. **scouted**; reference for ccdash watch mode.

## Trading

- HKUDS/Vibe-Trading — NL → backtests → Pine Script v6; free (Ollama + yfinance/OKX). **scouted**; backtest/paper only per Verification Protocol.

## Voice (for the Jarvis v2 voice round — DEC-005 deferred it)

All **unvetted** candidates; local-first per the paid-service-free goal:

- ggerganov/whisper.cpp — local STT, fast on CPU.
- SYSTRAN/faster-whisper — local STT, Python-native (fits Jarvis).
- rhasspy/piper — local TTS, lightweight.
- dscripka/openWakeWord — wake-word detection, if always-on ever wanted (DEC-005 ranked push-to-talk first).

## Local models / paid-service-free

- Ollama — local LLM runtime. **unvetted** here (referenced by Vibe-Trading and Odysseus); the "replicate Fable 5 locally" ceiling is much lower than Fable 5 — treat local models as the fast/free tier, not a replacement.

## Cross-device / phone

All **unvetted**:

- Tailscale — mesh VPN so devices reach each other off-LAN (current 10.0.0.x IPs are LAN-only).
- Syncthing — sync vault + Jarvis marker files (last_news_date etc.) across devices.
- Termux — terminal + Python on Android; plausible Jarvis-on-phone path. [Guessing] whether Claude Code auth works under Termux — verify before promising.
- Obsidian mobile — vault access on phone (official app).

## Scheduling / automation

- systemd timers (built into CachyOS, nothing to install) — the default answer for "schedule things" until a Jarvis daemon exists. **adopted-by-default**
- Claude Code `/schedule` (cloud routines) + `/loop` — already available in the harness. **adopted**

## Media / articles

- [[claude-improvement-notes]] — the compiled 22-reels + 39-screenshots analysis (2026-06-28). Source of the Gotchas pattern, anti-sycophancy prompt, SKILL.md conversions.

## Skills / agent bundles (scouted 2026-07-06)

- addyosmani/agent-skills — 24 production-engineering skills, spec→ship lifecycle, 4 reviewer personas. **scouted**; candidate to adopt piecemeal into `~/code/jarvis`.
- alirezarezvani/claude-skills — 355 skills/99 agents, mostly business/agency scale. **scouted, not adopted**; `skill-security-auditor` sub-tool worth remembering.
- mvanhorn/last30days-skill — `/last30days <topic>`, parallel Reddit/X/YouTube/HN/Polymarket/GitHub research scored by real engagement. **scouted — candidate to install** (free tier needs no keys); awaiting go-ahead.
- NousResearch/hermes-agent — self-improving agent, OpenClaw-migration path, cron + multi-platform. **scouted** as a Jarvis-alternative reference architecture, not a component to adopt (would mean abandoning custom Jarvis build).
- affaan-m/ECC ("Everything Claude Code") — 30 agents/135 skills bundle + `SOUL.md` 5-principle persona format. **scouted**; the SOUL.md format is a nice compact template idea.
- asgeirtj/system_prompts_leaks — leaked system prompts for every major AI product, incl. Claude Fable 5's actual claude.ai prompt. **adopted as research input** for [[2026-07-06-fable5-clone-test-prompt]].

Full writeup: [[2026-07-06-fable5-clone-research]].

## Monetization (scouted 2026-07-07)

- Blueprint Vault technique — Fable 5 mines a backlog into build-ready
  blueprints (goal/context/constraints/steps/definition-of-done) for cheap
  models to build later. **adopted as technique**, use before running out of
  Fable 5 access; see [[2026-07-07-blueprint-vault-and-moneymaking]].
- Whatnot card-breaking — profitable but capital-intensive and under active
  legal/gambling-classification scrutiny. **researched, not adopted.**
- Selling a Claude Skill on Gumroad — real $500–3,000/mo examples for a
  single validated skill, zero setup cost. **recommended path** to cover
  subscription costs; see full writeup for sources.

## NotebookLM / courses (scouted + adopted 2026-07-08)

- teng-lin/notebooklm-py — unofficial NotebookLM API/CLI/MCP + Claude Code
  skill; generates & downloads quizzes, flashcards, audio/video overviews,
  mind maps. **adopted 2026-07-08** (sandbox-reviewed; installed via
  `uv tool install --python 3.12 notebooklm-py --with rookiepy`; skill at
  `~/.claude/skills/notebooklm/`; auth = chromium cookie import; smoke-tested).
  Unofficial Google endpoints — can break; nothing income-critical on it.
- jacob-bd/notebooklm-mcp-cli — `nlm` CLI + MCP alternative. **scouted**, fallback if notebooklm-py breaks.
- Course Forge pipeline design: [[2026-07-08-jarvis-v4-notebooklm-deep-dive]] §4. Pilot = hiragana (notebook created).

## JARVIS V4 / presentation layer (scouted 2026-07-08)

- zubair-trabzada/brain-map — Obsidian vault → interactive knowledge graph,
  stdlib-only, local. **unvetted candidate** — superseded for now by our own
  `~/code/vault-atlas` (see Owned/built) which respects the private-folder
  boundary; re-visit for its growth animation if wanted.
- Zubair's free JARVIS prompt pack (skool.com/aiworkshop-lite signup) —
  **unvetted**; grab for voice/persona prompts. Full V4 is paid; skip.
- JuliusBrussee/caveman — token-cutting skill, 86k★, sitting in
  `~/code/_sandbox/caveman` awaiting checklist review. **unvetted**

## To scout next

- [ ] Graphify (from improvement notes — install in `~/code/jarvis` first; confirm exact repo before adopting)
- [ ] MCP servers worth adding (filesystem watchers, calendar, home-lab control)
- [ ] Local deep-research stacks (compare against Odysseus's built-in one)
- [x] NotebookLM workflows that pair with the vault — done 2026-07-08, see the NotebookLM section above
