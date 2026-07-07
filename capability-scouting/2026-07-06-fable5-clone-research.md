---
date: 2026-07-06
tags: [capability-scouting, fable-5, skills, research]
---

# 2026-07-06 — Fable 5 clone research (videos + repos)

Session goal: scout 3 YouTube videos + 6 GitHub repos for anything useful to
the Claude/Jarvis setup, and find raw material for building a "Fable 5 clone"
(Opus running with Fable 5's system prompt / behavior patterns) to A/B test
against real Fable 5.

## Videos

| Video | Status | Takeaway |
|---|---|---|
| [nuwlyQXrADg](https://www.youtube.com/watch?v=nuwlyQXrADg) | **Unwatchable this session** — video-analysis tool returned 503 (high demand) on 3 retries. Retry later. | — |
| [8GRmLR__OGQ](https://www.youtube.com/watch?v=8GRmLR__OGQ) — Theo (t3dotgg) on Fable 5 | ✅ summarized | See "Theo's Fable 5 orchestration notes" below — **this is the main source for the clone's behavioral profile**, since the base system prompt (see below) doesn't encode agentic/orchestration behavior. |
| [DTCyvo6cC54](https://youtu.be/DTCyvo6cC54) — AI Second Brain, 5 levels | ✅ summarized | Directly relevant to this vault's own design. See "Second Brain levels" below. |

### Theo's Fable 5 orchestration notes (video 2)
- Fable 5 isn't "just smarter" than Opus — it's better at **breaking tasks down, testing, verifying, and delegating to subagents/cheaper models**.
- **Never go above "High" reasoning effort.** `xhigh`/`max` cause looping/overthinking — worse code, higher cost. This directly contradicts an assumption we could've made; worth remembering for Jarvis's model-router tiers.
- His `CLAUDE.md` ranks models on **Intelligence** (how hard a problem it can handle unsupervised), **Taste** (UI/UX/code style/API design quality), **Cost** (real $/token) — and routes work accordingly instead of defaulting everything to the top model.
- Workflows = deterministic scripts for fan-out; subagents = dynamic, spun up per sub-problem.
- "Judge the output, not the price tag" — escalating cost beats shipping mediocre work.
- Practical tip: split API traffic across multiple accounts ("Vibe Proxy") to avoid usage-limit walls — not something we're doing, flagged as unvetted/aggressive.

**Relevance to us:** this is the actual differentiator people are reacting to with Fable 5 — not a personality change, an **orchestration discipline** change. That reframes what "clone Fable 5" should mean (see below).

### Second Brain levels (video 3)
Five-level ladder for AI-backed knowledge systems: (1) folder + CLAUDE.md router, (2) curated wiki w/ cross-links, (3) semantic search/vector DB, (4) knowledge graph, (5) always-on autonomous Brain-OS. Order to build in: **Context → Connections → Capabilities → Cadence**. Core test: "can you find it again?" Climb a level only for a pain you've actually felt.

**Where we sit:** this vault is solidly **Level 2** (curated wiki, heavy cross-linking, no vector search) — matches the video's claim that most people's real needs stop at Level 1–2. No action needed now; worth a re-read if/when search-by-meaning becomes a felt pain (e.g. can't find a note by paraphrase).

## GitHub repos

| Repo | What it is | Verdict |
|---|---|---|
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | Leaked/extracted system prompts for every major AI product, incl. **`Anthropic/claude-fable-5.md`** (the actual claude.ai Fable 5 system prompt, ~48K tokens) and a diff vs Opus 4.8. | **Adopted as the clone's raw material** — see below. |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 24 production-engineering skills (spec→plan→build→verify→review→ship) as Claude Code slash commands + 4 reviewer personas. Google-engineering-practices flavored (Hyrum's Law, Beyoncé Rule, Chesterton's Fence). | **scouted** — a cleaner, more opinionated alternative to hand-rolling our own dev workflow skills. Candidate to adopt piecemeal (e.g. `code-review-and-quality`, `test-driven-development`) into `~/code/jarvis` later, not wholesale. |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 355 skills / 99 agents / 109 commands across 18 domains (engineering, marketing, C-suite advisory, compliance, research ops). Multi-tool (13 harnesses). | **scouted, not adopted** — mostly business/agency-scale skills we don't need; the `skill-security-auditor` (scans a skill for malicious code pre-install) is the one piece worth remembering if we ever install third-party skills wholesale. |
| [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | `/last30days <topic>` — searches Reddit/X/YouTube/TikTok/HN/Polymarket/GitHub in parallel, scores by real engagement (upvotes/likes/money), synthesizes one brief. Free tier (Reddit+HN+Polymarket+GitHub) needs no keys. | **Candidate to adopt** — genuinely useful for "what's actually happening with X person/topic/tool right now" (e.g. checking a repo's real reputation before adopting it, like we're doing in this very table). Low cost to try (`/plugin install last30days` in Claude Code, free sources only). Not installed yet — flagging for a future go-ahead. |
| [NousResearch/hermes-agent](https://github.com/NousResearch/hermes-agent) | Nous Research's self-improving agent — learns skills from experience, cron scheduling, multi-platform (Telegram/Discord/Slack/etc.), can migrate straight from OpenClaw config. Open standard `agentskills.io`. | **scouted** — this is a Jarvis competitor/alternative, not a component to bolt on. The "agent-curated memory + periodic nudges + autonomous skill creation" pattern is worth studying for Jarvis v2, but adopting Hermes itself would mean abandoning the custom Jarvis build already in progress. Park it as a reference architecture. |
| [affaan-m/ECC](https://github.com/affaan-m/ECC) ("Everything Claude Code") | A packaged plugin: 30 agents, 135 skills, 60 commands, hook workflows, plus a `SOUL.md` persona file (Agent-First, Test-Driven, Security-First, Immutability, Plan-Before-Execute). | **scouted** — same category as the two skills repos above (a big pre-packaged bundle). `SOUL.md`'s five-principle format is a nice compact template if we ever want a one-page persona/identity file for Jarvis, shorter than `donny-operating-system.md`. |

## The Fable 5 system prompt itself — what's actually in it

Pulled `Anthropic/claude-fable-5.md` from the leaks repo (full text saved locally
at `/tmp/.../scratchpad/fable5-system-prompt.txt` for this session — not
committed to the vault, it's Anthropic's leaked prompt text, not ours to
duplicate wholesale). Key finding:

**The system prompt is almost entirely the shared Claude constitution, not
Fable-5-specific.** Sections like `tone_and_formatting`, `essential_practices`,
`responding_to_mistakes_and_criticism`, `evenhandedness`, `user_wellbeing` read
like general Claude behavior (warm tone, minimal formatting unless needed,
own mistakes without self-abasement, present both sides of contested
positions, avoid diagnosing the user). The only Fable-5-specific bit found is
the `product_information` blurb: Fable 5 is described as the first model in
the new **Mythos-class tier**, sitting above Opus, "the most intelligent
generally available model," sharing weights with Claude Mythos 5.

**Conclusion: Fable 5's edge (per Theo's video) is not a personality
difference — it's raw capability + an orchestration/effort-discipline layer
that users build on top (CLAUDE.md model-routing, "never go above High
effort," subagent delegation).** So "cloning Fable 5" with Opus can't be done
by prompt-injecting personality traits alone — Opus is already tuned to the
same constitution. What *can* be cloned/approximated is the **behavioral
discipline**: task decomposition before coding, verify-before-handoff,
judging output over cost, single-question clarification, minimal formatting
unless complexity demands it.

See [[2026-07-06-fable5-clone-test-prompt]] for the resulting test setup.
