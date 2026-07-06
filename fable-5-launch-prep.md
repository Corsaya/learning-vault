---
date: 2026-07-01
tags: [claude, fable-5, jarvis, planning, launch-prep]
status: active
---

# Fable 5 Launch Prep — Master Plan

> Built 2026-07-01, the day Fable 5 went live globally. This is the ask-ready
> plan for the 7 goals from the braindump. Decisions locked in via survey are
> marked ✅. Open decisions are marked ❓.

## 0. Fable 5 — access (confirmed today)

- **Live now.** Global as of July 1, 2026.
- **Claude Code:** you're on v2.1.197 (needs ≥2.1.170 ✓). Switch with `/model`
  → pick Fable 5, or `/model claude-fable-5`.
- **claude.ai / Cowork:** available on Pro/Max/Team/Enterprise.
- **API:** model id `claude-fable-5`. 1M context, 128k output, $10/$50 per M tok.
- **Gotchas:** cybersecurity-flagged prompts silently fall back to Opus 4.8;
  free weekly allowance for Fable 5 tightens after July 7 (then usage credits).
- **Rule of thumb:** Fable 5 for architecture/hard reasoning/long-context; keep
  Opus 4.8 / Sonnet / Haiku for routine work to control cost.

## Locked-in decisions (from survey)

- ✅ **Repo structure:** mega-vault for notes + **split code into its own repos**.
  Jarvis, trading tool, teacher tool → `~/code/<name>`, each linked from a vault
  pointer note. Obsidian stays prose/second-brain only.
- ✅ **Day-one focus:** **Jarvis** (already architected, just needs code).
- ✅ **Daily AI news + weekly survey:** delivered **inside Jarvis** — fires on the
  first launch of the day (news) / week (survey) on *any* device.
- ✅ **Money ($20/mo):** open — pursue whichever of the tracks below lands first.

---

## Fable 5 build order (the sequence)

Ordered by dependency + urgency. The July 7 usage cliff pushes the usage monitor early.

| # | Build | Why here | Depends on |
|---|-------|----------|------------|
| 0 | Repo split + Jarvis `config.py` | Foundation | — |
| 1 | ✅ **Usage monitor** (`ccdash`, `~/code/usage-monitor`) | DONE — built stdlib-only instead of wrapping ccusage | nothing |
| 2 | Jarvis v1 core | The spine | config → memory → prompt → llm(subprocess) → router → session → usage → cli |
| 3 | Jarvis **daily-news + weekly-survey** component (DEC-013) | Your requested feature | Jarvis v1 running |
| 4 | **GitHub improvement-repo searcher** (safe adopt harness) | Feeds all future builds | gh + worktree pattern |
| 5 | Odysseus setup (GUI/email, shared vault) | Parallel, low-dependency | Docker |
| 6 | Teacher tool · Vibe-Trading · Linux audit | Later phases | Jarvis stable |

## Progress log

**2026-07-01 (afternoon pivot):** Fable 5 went live on account. New mission for the
7-day window: **make Fable 5 pay for itself.** Priority reordered by user:
**#1 Trading/investing research track** (build → verify → paper → capital, user-led),
**#2 Jarvis** (rename & ship as product later). Money model = sell the *verified toolkit +
content*, NOT trading signals. Capital only into a self-built, self-verified system.
- ✅ Rejected risking capital now (negative EV); user agreed to learn/build/verify first.
- ✅ Set up `~/code/trading/` (git) + `personal/Projects/trading/` with: Home (roadmap +
  money model), **Verification Protocol** (10 gates before any capital), **Research Brief
  (Fable 5)** (deep-research prompt teed up).
- ⏭ Next: user switches to `/model claude-fable-5` and runs the Research Brief.
- ⏸ Parked: ccdash web UI (`report.py` done; `cli.py` rewrite + `server.py` pending) —
  finish on Opus later; plain `ccdash` still works.

**2026-07-01**
- ✅ Moved `jarvis/` out of the vault → `~/code/jarvis/` (own git repo). Vault pointer updated.
- ✅ Logged DEC-011 (`claude -p` subprocess default), DEC-012 (`full` → `claude-fable-5`),
  DEC-013 (daily-news/weekly-survey approved in principle).
- ✅ Built Jarvis **`config.py`** — immutable Config, fail-fast validation, subprocess/api
  modes, tier resolution, cost table, secrets loader. `.venv` + `pip install -e .` + real
  `config.yaml`. **10/10 unit tests pass**; smoke test resolves `full → claude-fable-5`.
- ✅ Seeded a **[Gotchas]** section in `~/code/jarvis/CLAUDE.md` (improvement-note #1).
- ✅ **Build #1 shipped: `ccdash`** (`~/code/usage-monitor`, own git repo). Stdlib-only
  Claude usage dashboard reading `~/.claude/projects`: token/cost/burn-rate by window,
  model, and project; `--brief` one-liner for Jarvis; `--json`; optional weekly-budget
  headroom. 5/5 tests pass; runs clean on real logs. (Chose a from-scratch stdlib parser
  over wrapping ccusage — no node/npx dependency, and Jarvis can import it directly.)
- 🔎 **Finding from real data (last 7 days):** ~11M tokens across 3 models. **claude-mem's
  `observer-sessions` was the single biggest consumer (~37%)** before this vault. Worth
  deciding whether the background observer's cost is worth it — a real optimization lever.
- ✅ Jarvis **`memory.py`** built — MemoryStore: loads identity.md then facts.md (identity
  always first), `/remember` appends timestamped facts, never writes identity.md. 6 tests.
  Full jarvis suite now **16/16**.
- ⏭ Next Jarvis component = `prompt.py` (+ a shared `Message` type). One small design
  choice to settle first: where the `Message` type lives (used by prompt, session, llm).
  Proposed: a tiny `jarvis/message.py`. Then the `llm/` subprocess client (DEC-011) needs
  its own design pass (how to invoke `claude -p --output-format json`, parse usage).
  `memory/identity.md` is still blank — filling it is a you-task.

## 1. Repo split (done ✅) — home is `~/code/`

Move code out of the vault so git history and CI aren't tangled with notes.

```
~/code/
  jarvis/          # move from ~/Documents/Obsidian/jarvis/  (already its own git repo)
  learn/           # the teacher tool (goal #3), later
  money/           # trading + tools sandbox (goals #2, #5), later
```

- Vault keeps a **pointer note** per project (e.g. `personal/Projects/jarvis/`
  Home.md → "code lives at `~/code/jarvis`"). The vault's job becomes *notes about*
  the code, not the code.
- ❓ Confirm `~/code` as the home (vs `~/dev`, `~/projects`) before I move anything —
  moving a git repo needs your approval per vault rules.

---

## 2. Jarvis — the spine (day-one build)

Your `jarvis/` repo is **fully architected, zero code**. That's the whole job:
implement the 8 components in ARCHITECTURE.md, in dependency order.

### Borrow, don't reinvent
- **`claude -p` subprocess pattern** (from enochko/jarvis): run Jarvis through your
  **Claude Code subscription**, not a paid API key. Kills the "avoid paid services"
  problem for the core loop. This is a change from the current architecture (which
  assumes `ANTHROPIC_API_KEY`) → needs a **DECISIONS.md entry** before adopting.
- **Morning Digest concept** (from OpenJarvis): the model for the daily-news feature.

### Suggested build order (matches ARCHITECTURE.md seams)
1. `config.py` + secrets loading (fail-fast).
2. `memory.py` — identity.md + facts.md flat load. **Fill `memory/identity.md` first.**
3. `prompt.py` — system | history | input assembly.
4. `llm/base.py` + `llm/client.py` — start with Anthropic API OR the `claude -p`
   subprocess client (decide per DECISIONS entry above).
5. `llm/router.py` — fast/standard/full tiers (update `full` default to Fable 5? ❓).
6. `session.py` — 10-turn window.
7. `usage.py` — token + spend tracking.
8. `cli.py` — interactive loop + `/remember /usage /model /exit`.

### Ask-ready prompt (paste into jarvis repo session, on Fable 5)
> "Read ARCHITECTURE.md, DECISIONS.md, and CLAUDE.md. Confirm the build order for
> a v1 that runs. Then implement `config.py` only — propose the approach and wait
> for approval per the session protocol before writing code."

### Daily-news + weekly-survey feature (the part you asked for)
This is a **new capability** — current ARCHITECTURE.md lists "scheduled/triggered
execution" as a non-goal, so it needs an explicit DECISIONS.md entry and probably a
new component. Spec:
- **Trigger:** on Jarvis startup, check a `last_news_date` marker. If it's not today,
  generate the brief, print it, update the marker.
- **Cross-device "first launch of the day":** the marker must sync across Alienware
  (10.0.0.225) and ThinkPad (10.0.0.197). Reuse the existing claude-mem sync path, or
  a tiny synced file. Same idea for `last_survey_week` (weekly setup survey).
- **News source:** WebSearch/WebFetch over X + Reddit + Anthropic blog for Claude/AI
  news; summarize to ~10 bullets. (OpenJarvis's Morning Digest is the reference impl.)
- **Weekly survey:** a fabricated short questionnaire about your setup (what's working,
  what to automate next) — written to the vault for you to answer.

---

## 3. Money — $20/month (track picks, run whichever lands first)

Ranked by effort-to-first-dollar:
1. **Package & sell Claude assets** — turn your workflows into products: a skills pack,
   an agent bundle (see The Agency, 232 agents), or the improvement-notes as a paid
   guide. Lowest risk, uses what you already have. Aligns with "make repos for Claude."
2. **A tiny paid tool** — one narrow thing people pay a few $ for (a bot, a converter,
   a niche automation). Recurring potential; more build.
3. **Content outlet (chase.h.ai style)** — AI-tips shorts on IG/TikTok/X. Slow ramp,
   needs consistency; can feed #1 and #2.
4. **Trading** — treat as *learning-first, not income-first* (see §5).

Ask-ready prompt (Court-of-Claude style, for honesty):
> "Here are my skills and assets [list]. Propose 5 concrete ways to earn a reliable
> $20/month within 30 days. For each: effort, time-to-first-dollar, and the single
> biggest reason it fails. Tag each claim [Certain]/[Likely]/[Guessing]. No cheerleading."

## 4. The teacher tool (goal #3)

Adaptive tutor that tracks what you know/don't, your strengths/weaknesses, and teaches
by the most efficient method per subject (immersion for language, spaced repetition for
memorization). You already have a **Japanese learning tracker** in the vault — that's the
first proving ground.
- **Design later** (after Jarvis v1). Likely a `~/code/learn/` repo whose "student model"
  is a set of Obsidian notes Jarvis can read.
- Core loop: assess → pick method → drill → log result → update the student model.
- Reuse: Genki vs Tae Kim comparison + N5→N1 benchmarks already in `personal/.../Japanese/`.

## 5. Linux control + harness the machine (goal #4)

Make this box maximally capable and paid-service-free.
- Jarvis is the front door (it can run shell commands within defined authority — see
  vierisid/jarvis for the "authority limits" pattern).
- Replace paid services with local/free: Ollama (local LLM), local TTS/STT for voice,
  free market data (see §5), self-hosted anything.
- Ask-ready prompt:
> "Audit my Linux setup [CachyOS, fish shell]. List paid services I use and a free/local
> replacement for each. Then propose 5 ease-of-access wins (aliases, hotkeys, launchers,
> automations) ranked by daily-time-saved. [Certain]/[Likely]/[Guessing] tags."

## 6. Trading with Claude (goal #5)

- **Vibe-Trading (HKUDS)** is the backbone: natural-language → backtests → strategies,
  exports **TradingView Pine Script v6**, and **runs free** (Ollama + yfinance/OKX).
- **Do it in paper/backtest mode only** to start. The reels showing "huge profit" are
  survivorship-biased marketing — backtest results ≠ live results (the repo says so).
- Path: install Vibe-Trading (Docker) → run free backtests → learn what the factors do
  → *then* consider paper trading. Real capital is a later, deliberate decision.

## 7. Act on the improvement notes (goal #1 follow-through)

The notes are compiled; these are the un-done actions from the session wrap.
Re-checked 2026-07-05:

- [x] Add a **[Gotchas]** section to CLAUDE.md files (40%→98% accuracy pattern).
  Already done — `~/code/jarvis/CLAUDE.md` has a live `## Gotchas` section
  (9 entries, last updated 2026-07-03 covering `--tools` allowlist and
  `--no-session-persistence` log behavior).
- [ ] ⚠ Install **Graphify** (`github.com/safishamsi/graphify`) in `~/code/jarvis`.
  Not done — installing a third-party tool that modifies Claude Code config
  needs your go-ahead first (per the "no new dependency without approval"
  rule). Say the word and it's a 2-minute job.
- [~] Convert repeating tasks to **SKILL.md**.
  - card-flip logging: already effectively covered — `card-flip/SKILL.md`
    (both in the vault and at `~/card-flip/`) is a full context-restore doc
    serving the same purpose.
  - sync mc-mirror: **blocked** — `sync-reference.sh` referenced in the root
    CLAUDE.md doesn't exist on this machine, and `~/minecraft-event` (the
    shared crew repo) isn't cloned here either. Can't convert a script that
    isn't present on this device.
- [x] Build the **4-System/Claude.md** dynamic-context file — **decision: fold
  into Jarvis memory, don't duplicate.** Jarvis already has this exact concept
  (`memory/identity.md`, read first every session) — a separate Obsidian
  "4-System" file would just be a second source of truth to keep in sync.
  Action: fill in `~/code/jarvis/memory/identity.md` (still blank per the
  progress log above) instead of building a new file.
- [ ] Add the **7-rule anti-sycophancy** prompt to key Claude.ai Projects.
  Can't do this one from here — it's a paste into claude.ai's web UI
  (Projects → Custom Instructions), not a file. Prompt is ready to copy from
  [[claude-improvement-notes#7-Rule Anti-Sycophancy Advisor Prompt]] whenever
  you're at claude.ai.

---

## 8. First two Fable 5 builds (concrete, do after Jarvis v1 skeleton)

Both are mostly "wrap existing tools," not build-from-scratch.

### Build A — Usage optimizer / monitor
Goal: see tokens left **today** and **this week** before hitting the cap, and **what
it's being spent on**, so you can adjust.
- Claude Code enforces a **5-hour rolling window + a weekly cap**, shared across Claude
  Code, claude.ai, and Cowork.
- **Don't write a counter.** Wrap:
  - `npx ccusage` — historical daily/weekly/monthly + per-session/per-model breakdown.
  - `Claude-Code-Usage-Monitor` (Maciek-roboblog) — live dashboard, ML burn-rate,
    time-to-limit prediction.
- Your build = thin layer: "left today / left this week" + top consumers, and it feeds
  **one line into Jarvis's daily brief**.

### Build B — GitHub improvement-repo searcher
Goal: find repos that improve your Claude/AI setup and incorporate them **safely**.
- Search: `gh search repos` + WebFetch to rank READMEs (MCP servers, skills, agents,
  Claude Code tools).
- **Safe adopt harness** ("without problems"): clone into a **git worktree sandbox** →
  read → test → only then incorporate. Never install straight into a live repo.
- Seed list from [[claude-improvement-notes]] (Graphify, The Agency, etc.).

## 9. Odysseus (PewDiePie) — GUI layer, not a Jarvis competitor

[github.com/pewdiepie-archdaemon/odysseus] — MIT, ~77k★, self-hosted, no telemetry.
Chat/agents/MCP/skills/shell/memory + deep research + writing editor + IMAP/SMTP email.
Runs on local Ollama models (free) or Anthropic API.

- **[Likely] Role:** Odysseus = GUI + email triage + deep research. Jarvis = terminal +
  OS control + automation + daily brief. Complementary.
- **[Certain] Rule:** point **both at the same Obsidian vault** so there's one memory,
  two front-ends. Do not let each grow its own memory.
- **[Guessing] Risk:** ~1,400 open issues, young project — daily driver, not critical infra.

## 10. Locked mega-vault — honest limits

Goal: a mega-vault (incl. personal) where Claude cannot see chosen parts.
- **[Certain] `.claudeignore` and `permissions.deny` are NOT reliable locks** — documented
  2026 cases of Claude reading `.env` despite them, and deny bypassed via absolute paths.
- **[Certain] The only real lock is physical separation:**
  - Keep truly-private content **outside any dir Claude is launched from** (e.g. `~/private/`), OR
  - **Encrypt it** (age/gpg / encrypted folder) so a read returns ciphertext.
  - Use `.claudeignore` + `permissions.deny` as defense-in-depth on top, never alone.
- Structure: build the mega-vault; the "locked" folders live in a separate encrypted/
  excluded location, linked by note reference, not by being readable in-tree.

---

## Decisions — all confirmed ✅ (2026-07-01)

1. ✅ Repo home: **`~/code/`** — move `jarvis/` there first.
2. ✅ Jarvis LLM client: **`claude -p` subprocess** (subscription, no API bill).
   → requires DECISIONS.md entry (overrides current API-key architecture).
3. ✅ `full` tier default: **`claude-fable-5`**.
4. ✅ Daily-news + weekly-survey: **new Jarvis component** (non-goal exception approved).
5. ✅ Odysseus: adopt as GUI/email layer, shared vault memory.
6. ✅ First builds: **usage monitor** + **GitHub searcher**.

## Sources scouted
- enochko/jarvis · OpenJarvis (Stanford) · ethanplusai/jarvis · rezaulhreza/jarvis
- HKUDS/Vibe-Trading · msitarzewski/agency-agents (The Agency)
- pewdiepie-archdaemon/odysseus (GUI layer)
- ryoppippi/ccusage · Maciek-roboblog/Claude-Code-Usage-Monitor (usage build)
- Claude Code file-exclusion: `.claudeignore` + `permissions.deny` (unreliable — see §10)
- [[claude-improvement-notes]] · [[claude-session-wrap-2026-06-28]]
