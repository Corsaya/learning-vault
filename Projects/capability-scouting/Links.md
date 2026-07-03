---
date: 2026-07-03
tags: [capability-scouting, links]
---

# Links

Status legend: **adopted** (in use) · **scouted** (read/ranked, not adopted)
· **unvetted** (candidate only — run the safe-adopt protocol first).

## Owned / built (already on this box)

- `~/code/jarvis` — the assistant itself. **adopted**
- `~/code/usage-monitor` (ccdash) — stdlib Claude usage dashboard. **adopted**
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

## To scout next

- [ ] Graphify (from improvement notes — install in `~/code/jarvis` first; confirm exact repo before adopting)
- [ ] MCP servers worth adding (filesystem watchers, calendar, home-lab control)
- [ ] Local deep-research stacks (compare against Odysseus's built-in one)
- [ ] NotebookLM workflows that pair with the vault (the NotebookLM + Obsidian + Claude strategy)
