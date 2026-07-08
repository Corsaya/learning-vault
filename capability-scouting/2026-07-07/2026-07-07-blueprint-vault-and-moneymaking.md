---
date: 2026-07-07
tags: [capability-scouting, fable-5, monetization, jarvis]
---

# 2026-07-07 — Blueprint Vault technique + making Fable 5's last day count + $20/mo idea

Context: today is being treated as the last "free"/available Fable 5 day. Goal:
extract max value from a Fable 5 session tonight, and find a low-effort way to
cover the Claude subscription cost (~$20/mo floor).

## Video retry status

`nuwlyQXrADg` still 503'd on a 4th attempt (2 today, 2 last session) — the
video-analysis backend itself seems to be down/overloaded, not a fluke.
Flagging as **not worth further retries this session**; try again another day.

## 1. The Blueprint Vault technique (from downloaded doc)

Source: `BLUEPRINT - The Blueprint Vault.docx.md` (a shared prompt-pack, not
vetted for who wrote it — treat as a technique to borrow, not a vendor to
trust). The mechanism:

- **Why it fits tonight specifically:** Fable 5's actual edge (per the
  2026-07-06 research) is planning/hard-problems + an orchestration-discipline
  layer — not raw code-writing. This technique spends Fable exactly on that:
  turning a vague backlog into blueprints so exact a cheap model (Sonnet/
  Haiku) can build them later with zero judgment calls. That's the highest-
  leverage use of a scarce Fable session — you get months of cheap-model
  output out of one expensive planning pass.
- **Mechanism, 3 pieces:**
  1. **Mining prompt** — tells Fable not to write code, to ground itself by
     reading the real repo/backlog first, then interview you (gated behind a
     literal `QUESTIONS FIRST` line) before writing anything.
  2. **Blueprint template** — a fixed structure every blueprint fills in:
     Goal, Context the builder needs, Constraints, Step-by-step plan, Exact
     inputs, Definition of done, and an "ASSUMPTION:" escape hatch for
     genuine gaps instead of stalling.
  3. **Batch loop** — one blueprint at a time, confirm after each, resume
     safely if the session dies.
- **Direct tie-in to the 2026-07-06 clone research:** this technique *is* the
  discipline layer we identified (decompose before executing, verify before
  handoff, one round of clarifying questions, no guessing) operationalized as
  a literal copy-paste prompt. Worth keeping the Blueprint template itself as
  a reference alongside `2026-07-06-fable5-clone-test-prompt.md`.

### Recommended use of tonight's Fable 5 session

Given limited time, prioritize **backlog-mining over the hiragana A/B test** —
mining produces reusable build-ready specs (compounding value across weeks),
the hiragana test is a one-off comparison you can run with Opus alone later
(the clone side doesn't need real Fable 5 to be useful — that's the whole
point of Side B). Concretely:

1. Pick 1–2 real backlogs with an actual `BACKLOG.md` or informal list:
   `~/code/jarvis` and/or `card-flip/` (TCG ops) are the strongest
   candidates — both are active, both have real files to ground against.
2. Open Claude Code in that repo, switch to Fable 5, paste the Mining Prompt
   → Template → (answer its questions) → Batch Loop, exactly as documented
   above.
3. Save blueprints to `./blueprints/` in that repo (not in the Obsidian
   vault) — they're build specs for the codebase, not vault notes.
4. Spot-check the first 2–3 blueprints, and ideally have Sonnet/Haiku actually
   build one before trusting the rest (per the doc's own warning).

## 2. Whatnot card-breaking — verdict: not recommended as the $20/mo plan

Researched profitability and business-practice soundness:

- **Profitability is real:** sports cards are Whatnot's top category (6.4M+
  cards/mo), part-time breakers report $2–5K/mo, platform fees (~8%) beat
  eBay (~15%). [Card Breaking Business Guide](https://hallofcards.app/blog-posts/card-breaking-business-whatnot-2025)
- **But facing real legal/regulatory heat right now:** arbitration demands
  and legal challenges characterize randomized box breaks as unlicensed
  gambling, not entertainment. [Whatnot Faces Legal Challenges](https://www.si.com/collectibles/whatnot-faces-legal-challenges-over-breaking-practices) ·
  [Card Break Roulette gambling scheme coverage](https://hoodline.com/2026/03/card-break-roulette-whatnot-accused-of-running-a-gambling-scheme/)
- **Requires capital up front** (buying boxes wholesale before any sale) —
  a real barrier for a $20/mo floor, and a different risk profile than
  `card-flip/`'s existing single-card flip model.
- **Verdict:** skip breaking specifically. It's a legitimate business for
  people already capitalized and risk-tolerant, but it's the wrong shape for
  "cheapest way to cover a subscription" — capital-intensive and under
  regulatory scrutiny. `card-flip/`'s existing flip-only model stays the
  better fit; no changes recommended there.

## 3. Creative Claude Code monetization — researched alternatives

Ranked by fit for "just needs to clear ~$20/mo, low capital, plays to what's
already being built here":

1. **Sell a Claude Skill as a digital product (Gumroad).** Zero setup cost,
   Gumroad handles payment/delivery, buyer downloads a zip and drops it into
   their own Claude Code setup. Real examples: one creator cleared ~$3–5K in
   30–50 days selling a stack of ~20 skills at $7–99 each; individual
   specialized skills (framework-specific testing, code review, deployment
   automation) report $500–3,000/mo. [Claude AI Side Hustle $5K](https://ryandoser.com/claude-ai-side-hustle/) ·
   [How to Sell Claude Skills](https://ryandoser.com/sell-claude-skills/) ·
   [Monetize SKILL.md 2026 guide](https://www.agensi.io/learn/how-to-monetize-skill-md-skills-developer-guide-2026)
   - **Best fit here:** you already have real, tested skills from building
     Jarvis and this vault workflow (e.g. the Blueprint Vault technique
     above, once you've run and refined it once yourself, or something out
     of `capability-scouting/`). Packaging one polished skill you've already
     validated on yourself is the lowest-effort path to the $20/mo floor —
     you'd clear it with 2–3 sales total, not 2–3 sales *per month*.
2. **Micro-automation for a client (n8n/Claude-Code workflow, paid
   monthly to maintain).** Real pattern people report: build a small
   automation once, get paid $50–500/mo retainer to keep it running.
   Higher effort (needs a client), better ceiling than #1 long-term.
3. **X/social growth agents** — automation tools/agents for X growth
   report $200–500/mo in early recurring revenue for builders, but this is
   a crowded, tool-heavy category (TweetHunter, NoimosAI, etc. already
   exist) — not a quick win, skip for now.

**Recommendation:** go with #1. Concretely: after tonight's Blueprint-Vault
backlog-mining session, package *that technique itself* (mining prompt +
template + batch loop, refined with whatever you learn using it tonight) as
a Claude Code skill and sell it — you'll have already dogfooded it, which is
exactly the "actually validated on real work" signal the research says sells.

Sources: [Best Items to Resell 2026](https://www.underpriced.app/blog/best-things-to-flip-for-profit-2026) ·
[7 Ways People Are Making Money With AI 2026 (KDnuggets)](https://www.kdnuggets.com/7-ways-people-are-making-money-using-ai-in-2026)

## Bottom line for tonight

1. Run the Blueprint Vault loop against `jarvis` and/or `card-flip` with real
   Fable 5 — highest-leverage use of a scarce session.
2. Skip Whatnot breaking; keep `card-flip/`'s existing model.
3. After validating the Blueprint technique on yourself, package it (or
   another already-working skill) as a paid Claude Skill on Gumroad — lowest
   -effort path past the $20/mo line.
4. The hiragana A/B test from [[2026-07-06-fable5-clone-test-prompt]] doesn't
   need real Fable 5 for its Opus/clone side — safe to run that comparison
   anytime, not just tonight.
