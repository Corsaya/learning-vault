---
tags: [trading, verification, risk, protocol]
created: 2026-07-01
---

# Verification Protocol

The rules that stand between you and losing money. **Prime directive: no real
capital until a strategy passes every gate below, and even then only what you
can afford to lose entirely.** Backtests lie by default; this protocol is how
you catch the lies before they cost you.

## The gates (all must pass)

1. **Out-of-sample split.** Develop/tune on a *training* period only. Test once
   on a held-out period you never looked at. If you tune against the test set,
   the result is fiction.
2. **Walk-forward.** Re-fit and test rolling forward through time (e.g. fit on
   2 years, test on the next 6 months, roll). A strategy that only works on one
   fixed split is overfit.
3. **Realistic costs.** Subtract commissions, bid/ask spread, and slippage on
   every trade. Add taxes on gains. Many "winning" strategies die here.
4. **No look-ahead bias.** You may only use data that existed at decision time.
   No future prices, no restated fundamentals, no same-bar close-to-open magic.
5. **No survivorship bias.** Include delisted/bankrupt tickers. Testing only on
   today's survivors inflates every result.
6. **Overfitting checks.** Few parameters. Test parameter *sensitivity* — if a
   tiny change wrecks it, it's curve-fit. Correct for multiple testing (you
   tried many ideas; most "winners" are noise — see deflated Sharpe ratio).
7. **Beat the benchmark on risk-adjusted terms.** It must beat buy-and-hold of a
   broad index (e.g. VOO/SPY) *after costs* on **Sharpe** (return per unit risk)
   and on max drawdown — not just raw return. If it doesn't, just buy the index.
8. **Regime robustness.** Test across bull, bear, and sideways markets and
   multiple decades if possible. Working only in one regime = works until it doesn't.
9. **Enough trades.** A handful of trades proves nothing. Need a sample large
   enough that the result isn't luck (rule of thumb: 100+ independent trades).
10. **Live paper trade.** Run it live on paper for several weeks and confirm it
    matches the backtest before any capital. Divergence here = hidden bias found.

## Red flags (any one = stop)
- Equity curve too smooth / Sharpe > 3 on retail data → almost certainly a bug or leak.
- Results collapse when you add costs.
- Only works on one ticker / one period / one parameter set.
- You keep "fixing" it against the test set.
- You can't explain *why* the edge exists (what mistake are others making?).

## If you ever go live (risk rules)
- Only capital you can lose entirely. No borrowed money. No rent money.
- Max risk per position small (e.g. ≤1–2% of the account per trade).
- Predefined exit/stop discipline, written before entering.
- Journal every trade + the reason, review weekly ([[Home]]).
- Default alternative always on the table: DCA into a low-cost index fund.

## The honest baseline
Decades of evidence: most active retail traders underperform a simple index after
costs. If your verified system can't clearly beat that, the win *is* the index.
Building and verifying the system is still worth it — for the learning, the
toolkit you can sell, and the discipline. Just don't confuse the build with an edge.
