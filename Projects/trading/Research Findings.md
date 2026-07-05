---
tags: [trading, research, fable-5, findings]
created: 2026-07-03
status: draft — Donovan must edit/verify before acting (author of record)
model: claude-fable-5
---

# Research Findings — Trading & Investing for a Beginner

> Produced per [[Research Brief (Fable 5)]]. Every claim tagged
> [Certain] / [Likely] / [Guessing]. Sources at bottom. **You own the
> conclusions only after you've challenged them** — cross-check anything
> tagged [Guessing] before acting, per the brief.

## 1. Where market edges actually come from

An "edge" is a persistent reason someone on the other side of your trade
systematically hands you money. There are only a few real sources:

- **Speed** — HFT firms co-locate servers inside exchanges and pay for
  microwave links between Chicago and New York. They win the race to stale
  quotes. [Certain] You cannot compete here; your retail order takes
  milliseconds-to-seconds, theirs takes microseconds.
- **Information** — institutions have expert networks, satellite data,
  credit-card panels, and armies of analysts. Legal information edges cost
  millions to maintain. [Certain]
- **Flow** — market makers see order flow and earn the bid-ask spread on
  every trade. They are the house; retail is the player. [Certain]
- **Risk transfer / structural premia** — being paid to hold risk others
  want to shed (equity risk premium, insurance-like premia). **This is the
  only edge reliably available to retail**, and it pays over years, not
  days. [Likely → Certain for the equity premium itself]
- **Behavioral** — exploiting others' panic/greed (the root of value and
  momentum). Real but small, crowded, and psychologically hard to
  hold. [Likely]

Why edges decay: once known, capital floods in and arbitrages the excess
return away. McLean & Pontiff studied 97 published anomalies and found
**returns fall roughly half after publication** (~58bp → ~25bp/month;
Sharpe ratios of published strategies drop ~50%). [Certain — well-replicated]

**The uncomfortable summary:** as a student with a laptop, you have zero
speed, information, or flow edge. Any system you build competes against
firms whose *interns* have more data than you. Your realistic edges are
(a) time horizon (you can wait decades; funds can't), (b) small size (you
can trade things too small for funds to bother with — mostly relevant to
your TCG arbitrage, not equities), and (c) not paying fees. [Likely]

## 2. Active trading vs passive indexing — the evidence

- **SPIVA (S&P's own scorecard):** over the 15 years ending 2024, **not one
  of 22 U.S. equity fund categories had a majority of active managers beat
  their benchmark**. In 2025 alone, 79% of active large-cap funds
  underperformed the S&P 500 — the 4th-worst year in the scorecard's
  25-year history. [Certain] And these are *professionals* with Bloomberg
  terminals, before considering that surviving funds are the lucky ones.
- **Retail day traders, Taiwan (Barber, Lee, Liu & Odean — every trade on
  the exchange, 1992–2006):** ~80% of day traders lose money net of fees
  in any year; **under 1% earn reliable positive abnormal returns** across
  years. [Certain]
- **Retail day traders, Brazil (Chague, De-Losso & Giovannetti — all new
  futures day traders 2013–2015):** of people who persisted 300+ days,
  **97% lost money**; only 1.1% out-earned minimum wage; 0.5% out-earned a
  bank teller's starting salary — with far more risk. The paper's title is
  literally "Day Trading for a Living?" and its answer is no. [Certain]
- Individual investors as a class underperform the market by roughly
  1.5–6.5%/yr depending on study and period, mostly through overtrading,
  bad timing, and costs (Barber & Odean, "Trading Is Hazardous to Your
  Wealth"). [Certain for direction; magnitude varies]

Why: costs compound against you (spreads, fees, taxes on short-term gains
at ordinary income rates), you trade against better-informed counterparties,
and overconfidence causes overtrading. Markets are near-efficient *enough*
that after costs, the average active dollar must underperform the average
passive dollar — that's arithmetic (Sharpe, 1991), not opinion. [Certain]

## 3. Factor investing — what the evidence supports

The academically defensible factors, with honest post-publication sizing:

| Factor | Evidence | Post-decay expectation | Notes |
|---|---|---|---|
| **Market (beta)** | Overwhelming, 100+ yrs, global | ~4–6%/yr over cash | The one you get from indexing. [Certain] |
| **Momentum** | Strongest anomaly, ~200 yrs, all asset classes | ~2–4%/yr gross, less after costs | High turnover eats it; brutal crashes (2009). [Likely] |
| **Value** | Long history, global | ~1–3%/yr, decade-long droughts (2010–2020) | Cheap can stay cheap for your whole horizon. [Likely] |
| **Quality/profitability** | Good replication | ~1–2%/yr | Most robust of the "new" factors. [Likely] |
| **Low-vol** | Real but capacity-constrained | ~1%/yr risk-adjusted | Mostly a risk-adjustment story. [Likely] |
| **Size (small-cap)** | Weak alone | ~0–1%/yr | Largely disappears after quality controls; the weakest premium. [Likely] |

Key facts: McLean–Pontiff decay (~50% post-publication) applies to all of
these [Certain]; a 150-year study (Baltussen et al.) finds factor premia
persist out-of-sample but smaller than in-sample [Likely]; implementation
costs and taxes can consume most of a 2%/yr premium at retail scale
[Likely]. **Factor investing is a tilt on top of indexing that might add
~1%/yr if executed with discipline for decades — not a trading system.**
Cheapest implementation: factor ETFs (e.g., value/momentum funds), not
stock-picking. [Likely]

## 4. "Share your TradingView chart with AI and profit" — honest evaluation

**Verdict: content marketing riding survivorship bias. No demonstrated
edge.** [Likely → Certain for the marketing claim]

- **Live experiments say no.** Arcada Labs/Harvard gave frontier models
  (including Claude) $10k each to trade prediction markets live for 57
  days: **every model lost money**. Nof1's live test gave $10k each to
  Claude, GPT, Gemini, Grok et al.: the bot portfolio was **down 33% in
  two weeks**. [Certain — documented 2026 experiments]
- **The viral wins are outliers.** ~92% of Polymarket wallets lose money;
  the "$1,400 → $238,000 Claude bot" posts are the surviving lottery
  tickets, not the distribution. Nobody posts the bot that quietly bled
  out. [Certain for the wallet stat; Likely for the specific viral claims
  being unrepresentative]
- **Why it can't easily work:** an LLM reading a chart has *less*
  information than the market already priced in (a chart is public data,
  delayed, and technical patterns have never shown robust out-of-sample
  edge in academic tests). The LLM adds articulate narration, not private
  information. Pattern-recognition on price alone was arbitraged decades
  ago by quant funds with better data and execution. [Likely]
- **What would have to be true for it to work:** the AI would need
  information or speed the market lacks (it has neither — it's slower AND
  using public data), or a persistent behavioral mispricing too small for
  institutions but accessible to you (possible in tiny/weird markets;
  not in liquid stocks). [Likely]
- **Where AI *does* legitimately help:** writing/reviewing backtest code,
  explaining concepts, auditing your strategy for statistical sins,
  summarizing filings — i.e., **research labor, not signal generation**.
  That's exactly this project's design. [Certain]

## 5. Backtesting pitfalls — why good backtests fail live

The standard ways a backtest lies to you (your [[Verification Protocol]]
gates map to these):

1. **Overfitting / multiple testing** — test 100 parameter combos, one
   looks great by chance. With enough tries you can "discover" a winning
   strategy in random noise. Defense: hold-out data you touch once,
   pre-registered rules, distrust anything with >2–3 free parameters. [Certain]
2. **Look-ahead bias** — using information not available at trade time
   (closing prices for same-day signals, restated financials, index
   membership known only later). [Certain]
3. **Survivorship bias** — testing on today's S&P 500 constituents means
   testing only companies that *survived*. Free data (yfinance) is
   survivorship-biased; know this limitation. [Certain]
4. **Ignoring costs** — spread + slippage + commissions + short-term
   capital-gains tax (your marginal income rate!) can flip a winning
   backtest to losing. Model ≥0.1–0.2% per round trip for liquid stocks,
   more for anything thin. [Certain]
5. **Regime change** — a strategy fit to 2010–2021 (ZIRP, momentum tech)
   met 2022 and died. Markets are non-stationary; the data-generating
   process shifts. [Certain]
6. **Small samples** — 30 trades tells you almost nothing;
   a t-stat under ~3 on a discovered (not pre-registered) strategy is
   noise by multiple-testing standards (Harvey, Liu & Zhu). [Likely]

**Rule of thumb: assume live performance = half the backtest Sharpe, and
that's if you did everything right.** [Likely — practitioner consensus]

## 6. What a defensible approach looks like for you

Given: student, small capital (three figures? low four?), long horizon,
high skill-growth rate, existing income streams (lifeguarding, card-flip).

1. **Core (the actual money-maker):** automatic, boring, monthly
   dollar-cost averaging into a total-market index fund (VT/VTI-style) in
   a Roth IRA once you have earned income. At 18, $100/month at ~7% real
   is ~$380k in today's dollars by 65. Time is your one structural
   edge. [Certain for the mechanism; Likely for the return assumption]
2. **Learning sandbox (the education):** build the minimal backtester
   (Python/pandas/yfinance per [[Home]]), implement momentum and value
   yourself, run them through every gate in [[Verification Protocol]],
   paper trade the survivor. Budget: $0. Expected trading profit: ~$0.
   Expected value: the skills — quant literacy, statistics, coding — which
   are worth far more than any small-capital strategy returns. [Likely]
3. **The sellable asset (the income track):** the toolkit + build-in-public
   content (per [[Home]]'s money model). The honest lesson of this report
   — "I tested the AI-trading hype so you don't have to" — is itself
   better content than fake win-rate porn, and it's differentiated
   *because* it's honest. [Guessing on audience size; Certain that selling
   tools/content beats trading small capital on expected value]
4. **Hard rules:** no leverage, no options, no crypto perps, no
   day-trading, nothing you didn't build and verify, never money you
   can't lose. [Certain these protect you]

## 7. Realistic income expectations (year 1, small capital)

Honest numbers on, say, $1,000 of capital:

- **Indexing:** expected ~$70 (a good year could be +$250, a bad year
  −$200). [Likely]
- **A *successful* factor tilt:** maybe $10–30 *extra* per year. Real
  money at $100k scale; pocket change at $1k. [Likely]
- **Active/day trading:** expected **negative** — the Brazil data says a
  97% chance you lose money if you persist, plus hundreds of hours of
  time. [Certain per the evidence base]
- **Selling the toolkit/content:** $0 most likely, but the tail is
  meaningfully positive ($20–200/month is achievable for consistent niche
  content) and it compounds your skills either way. This dominates trading
  on expected value at your capital size. [Guessing on numbers; Likely on
  the ranking]

The brutal arithmetic: even a *world-class* 20%/yr edge on $1,000 is
$200/yr — $0.55/day. **Small capital means trading skill can't pay you;
only compounding time or selling skills can.** [Certain]

---

## (a) The 3 things most likely to lose you money

1. **Trading real capital before the Verification Protocol passes** —
   especially after a lucky paper-trading streak convinces you you're the
   0.5%. Variance masquerades as skill for months at a time.
2. **AI-signal hype** — trusting an LLM's chart read or a viral bot
   thread. The live experiments all lost; the winners you see are
   survivorship bias.
3. **Overfitting your own backtester** — iterating parameters until the
   equity curve looks good, then believing it. The more times you re-run
   with tweaks, the more the result is noise.

## (b) The single most evidence-backed strategy for your situation

**Dollar-cost averaging into a global/total-market index fund inside a
Roth IRA, automated, untouched for decades — while directing your active
energy at high-return skill-building (this toolkit, Jarvis, card-flip)
and selling what you build.** Nothing else in this report has one-tenth
of its evidence base. [Certain]

## (c) Reading list

1. Burton Malkiel — *A Random Walk Down Wall Street* (the foundation)
2. John Bogle — *The Little Book of Common Sense Investing* (indexing math)
3. Barber & Odean — "Trading Is Hazardous to Your Wealth" (retail evidence)
4. Chague, De-Losso & Giovannetti — "Day Trading for a Living?" (SSRN 3423101)
5. McLean & Pontiff — "Does Academic Research Destroy Stock Return
   Predictability?" (factor decay)
6. Harvey, Liu & Zhu — "…and the Cross-Section of Expected Returns"
   (multiple-testing / why most 'discoveries' are false)
7. Antti Ilmanen — *Expected Returns* (advanced; what premia exist and why)
8. SPIVA Scorecards (spglobal.com/spdji/en/spiva) — updated evidence, twice a year

## Sources (web, checked 2026-07-03)

- [SPIVA U.S. Year-End 2025](https://www.spglobal.com/spdji/en/spiva/article/spiva-us/) · [SPIVA scorecard summary](https://icfs.com/specialists-desk/spiva-scorecard-results)
- [Barber, Lee, Liu & Odean — Do Individual Day Traders Make Money? (Taiwan)](http://www.econ.yale.edu/~shiller/behfin/2004-04-10/barber-lee-liu-odean.pdf) · [Cross-Section of Speculator Skill](https://faculty.haas.berkeley.edu/odean/papers/day%20traders/Day%20Trading%20Skill%20110523.pdf)
- [Chague, De-Losso & Giovannetti — Day Trading for a Living? (Brazil)](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=3423101) · [Bloomberg coverage](https://www.investing.com/news/stock-market-news/day-traders-in-brazil-study-wouldve-done-better-with-9to5-job-2267260)
- [Cybernews — viral AI trading debunked; live models lost money](https://cybernews.com/ai-news/viral-ai-trading-debunk-model-lost-money-polymarket-kalshi/) · [Claude Polymarket claims skepticism](https://stuartglover.com/claude-ai-trading-bot-claims-on-polymarket-face-skepticism-what-we-know/)
- [Alpha decay modeling (arXiv 2512.11913)](https://arxiv.org/pdf/2512.11913) · [Momentum evidence & evolution](https://alphaarchitect.com/momentum-factor-investing/) · [CFA Institute — factor premiums](https://blogs.cfainstitute.org/investor/2024/10/04/factor-premiums-an-eternal-feature-of-financial-markets/)
