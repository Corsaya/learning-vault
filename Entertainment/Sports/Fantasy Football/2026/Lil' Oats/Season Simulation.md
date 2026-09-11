# Season simulation — 2026-09-11

This report supersedes earlier unsupported probability estimates and team ceiling/ranking claims. Those were not calculated forecasts. No roster transactions were made.

## Scope and interpretation

Executed 36,000 season paths: 4,000 paths in each of nine scenario combinations, through Week 17. Each path compares five fixed roster policies using the same player outcomes. This is a conditional sensitivity experiment. Percentages measure success inside the stated model; they are not calibrated probabilities of what will happen in the NFL. Scenario weights are equal for comparison, not evidence-based probabilities. A majority of scenarios depends on which scenarios were chosen.

Assumed redraft, one QB, two RB, two WR, one TE, one flex, K and DEF. All other roster slots remain fixed. No future trades, opponent waiver competition, replacement streaming, adaptive Monday adds, or learned role updates are modeled. Henderson stays unavailable for the opening week and is not cut; the user's Monday-only IR move remains an operational constraint. This experiment does not quantify the benefit of the additional IR-created roster spot.

No playoff or championship probabilities are reported: actual league schedule, future opponent management, and playoff matchup lengths are not established. Player season totals and starting-lineup contributions are the measured outcomes. Week 17 is a common comparison horizon, not a claim about this league's final playoff week.

## Inputs

Screenshot projections anchor Week 1. Price's 6.8 and Rams' 2 are fixed; Henderson is out. Healthy future means for Price (9), Henderson (10), and Rams (7) are illustrative assumptions, not retrieved season projections. Other baseline means repeat the screenshot Week 1 projection, which is a deliberately limited baseline.

Three role worlds are crossed with three injury intensities:

| Role world | Harrison/Wilson | Metcalf/Sadiq/Hunter | Lloyd starting window and mean | Montgomery/Marks |
|---|---|---|---|---|
| Screenshot baseline | 8 / 8.49 | 10 / 3.49 / 2.96 | 4 weeks at 8.57, then 4 | 14.25 / 8 |
| Challenger breakouts | 12 / 7 | 10 / 6 / 7 | 2 weeks at 9, then 4 | 10 / 12 |
| Incumbents hold; DK struggles | 6.5 / 11 | 8 / 7 / 2 | 14 weeks at 13, then 4 | 15 / 6 |

All numbers above are healthy expected points per game, not ceilings. Breakout/bust scenarios are deliberately chosen stress tests, not sourced projections. These bundled worlds do not exhaust independent combinations of every player's possible role.

Weekly injury-onset probability is 1.2%, 2.5%, or 4.5%, multiplied by 1.3 for RBs. Absences last 1/2/4/8 weeks with assumed probabilities 50/30/15/5%. Henderson initially misses 1/2/4 weeks with equal weights. Persistent player mean uncertainty uses a mean-normalized lognormal distribution with log SD .25. Weekly fantasy scores use gamma distributions (CV QB .4, RB .65, WR .75, TE .8, K .55, DEF .9) and a shared NFL-team environment with log SD .15. Scores are nonnegative, so negative QB/DEF/K outcomes are not represented. Byes come from screenshots.

Arizona WR and Houston RB role shares move in opposite directions by up to 25%; a modeled teammate's absence raises the other's expected production by 35%. These are assumptions, not fitted estimates. Lineups select eligible players using a noisy expected score (log SD .2), never the realized result. Forecasts know availability and much of the modeled role; this is more informed than real managers may be. Empty/absent positions score zero; streaming would soften roster-depth differences. Completed Week 1 slots are retained.

## Results

| Comparison | Player scores more over season | Move improves total starting-lineup points | Scenarios with >50% lineup improvement | Range across scenarios |
|---|---:|---:|---:|---:|
| Sadiq to Metcalf | 84.1% | 66.3% | 9/9 | 51.6–75.6% |
| Wilson to Harrison | 49.2% | 50.0% | 3/9 | 23.3–79.7% |
| Wilson to Marks | 47.4% | 44.9% | 3/9 | 13.3–80.8% |
| Hunter to Metcalf | 93.4% | 66.5% | 8/9 | 49.1–76.3% |

Individual points can remain on the bench. A move can also lose starting-lineup points if an imperfect forecast starts the new player during a bad week. This explains why Metcalf beating Sadiq in season points does not mean the roster move wins just as frequently.

## Decision

Under a redraft assumption, Sadiq to Metcalf is the most consistently supported of the previously discussed moves. It still loses in about one-third of simulated paths and only narrowly passes in the harshest role assumptions. Keep Wilson for now; neither Harrison nor Marks produces a robust majority across role worlds. Metcalf replacing Hunter also deserves consideration: the earlier statement that Hunter must be protected was too strong given the reported cornerback focus. The simulation does not decisively establish which of Sadiq or Hunter is the better drop; their lineup improvements are nearly identical and future keeper value is excluded.

Adding DK and starting DK over Lloyd are separate decisions. The season comparison is particularly sensitive to Lloyd's starting-window assumption; it cannot establish Week 1 superiority. Do not use the season aggregate as Week 1 start odds.

On Monday, use Henderson's IR opening only if the league permits it, and reassess the actual availability and Week 1 role evidence before another cut. Waiting carries the risk another manager adds a target; its probability is unknown and not simulated.

## Evidence and reproducibility

User-supplied Sleeper and NBC screenshots are the main inputs. Current reporting supports uncertainty around Lloyd's opportunity and the Arizona WR competition, without validating the numerical model parameters:

- https://www.fantasypros.com/nfl/news/604854/josh-jacobs-placed-on-commissioner-exempt-list.php
- https://www.fantasypros.com/nfl/players/michael-wilson.php

Run `python simulate.py` (NumPy required). Fixed seed: 20260911. Full per-scenario results: [[simulation-results.json]]. Source: [[simulate.py]]. Numerical checks confirm finite, nonnegative outputs; manual inspection checks fixed Week 1 results, legal starter positions, common player outcomes across policies, and selection before outcomes. Monte Carlo sampling error is approximately at most 1.6 percentage points per scenario at 95% confidence; uncertainty from assumptions is much larger. Paths across scenarios reuse random numbers and are not 36,000 fully independent evidence samples.

