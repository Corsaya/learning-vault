---
tags: [trading, research, fable-5, prompt]
created: 2026-07-01
---

# Research Brief — run on Fable 5

This is the deep-reasoning, long-context task worth spending Fable 5 on. Switch
with `/model claude-fable-5`, then paste the prompt below. Save the output as
`Research Findings.md` in this folder. You edit and verify the findings — you're
the author of record.

## Why Fable 5 for this
It needs synthesis across a lot of conflicting evidence, honest reasoning about
what's real vs marketing, and citations. That's Fable 5's edge — not boilerplate.

## The prompt (paste verbatim)

> You are my rigorous, skeptical research analyst. Anti-sycophancy mode: tag every
> claim [Certain] / [Likely] / [Guessing], cite sources where possible, and tell me
> what's marketing hype vs evidence. Do not flatter my ideas.
>
> Produce a thorough, honest research report for a beginner who wants to build and
> verify a trading/investing system before risking any capital. Cover:
>
> 1. **Where market edges actually come from** (and why they're rare and decay).
>    Who has structural edges (HFT, institutions) and why retail usually can't.
> 2. **The evidence on active trading vs passive index investing** for retail —
>    real long-run numbers, after costs and taxes. What % of active retail
>    underperforms the index, and why.
> 3. **Factor investing** (value, momentum, quality, low-vol, size): what the
>    academic evidence actually supports, expected magnitude, and how much has
>    decayed since publication.
> 4. **The "share your TradingView chart with Claude/AI and profit" claims** —
>    evaluate them honestly. Is there any real edge, or is it survivorship bias
>    and content marketing? What would have to be true for it to work?
> 5. **Backtesting pitfalls** that make strategies look good but fail live
>    (overfitting, look-ahead, survivorship, costs, regime change, multiple testing).
> 6. **What a *defensible* approach looks like** for someone in my position (a
>    student with limited capital): realistic expected returns, time horizon,
>    risk, and the smallest sensible first steps.
> 7. **Realistic income expectations**: if I did everything right, what could this
>    plausibly earn in year 1 on small capital — and what's the honest downside?
>
> End with: (a) the 3 things most likely to lose me money, (b) the single most
> evidence-backed strategy for my situation, and (c) a short reading list.

## After the report
- Edit it, challenge it, add your own notes — you own the conclusions.
- Cross-check anything [Guessing] before acting.
- Then, and only then, move to building a minimal backtester (see [[Home]] step 3),
  and hold every strategy to the [[Verification Protocol]].
