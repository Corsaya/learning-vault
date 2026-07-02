---
tags: [project, trading, investing, money]
created: 2026-07-01
---

# Trading / Investing — research track

Priority #1 of the Fable 5 sprint. Approach: **learn → build → verify → paper →
(your call) capital.** You lead; AI assists with research, tooling, and rigor.
Nothing you didn't build and verify yourself ever sees real money.

> [!warning] The money model (be honest with yourself)
> The reliable money here is **(a) sound passive investing that compounds over
> years, and (b) selling the toolkit + content you build.** It is NOT day-trading
> AI signals. A verified backtest is *not* a live edge. If a strategy can't beat
> dollar-cost-averaging into a broad index *after costs and risk*, the correct
> move is the index. See [[Verification Protocol]].

## Roadmap

1. **Research (Fable 5):** what actually works, why retail fails, realistic
   return expectations. Run [[Research Brief (Fable 5)]].
2. **Rails:** internalize [[Verification Protocol]] before writing any strategy.
3. **Tooling (later):** a minimal, readable backtester you build yourself
   (Python + pandas + yfinance, free). Vibe-Trading (pip + local Ollama) is an
   optional power tool once you understand the fundamentals — not the starting point.
4. **Verify:** every strategy must pass ALL gates in the protocol.
5. **Paper trade:** live paper for weeks, matching backtest, before any capital.
6. **Capital:** your decision, your verified system, only what you can lose.

## What sells (the self-funding part)
- The **verified toolkit** (backtester + protocol + factor library) as a product.
- **Build-in-public content** showing Fable 5 building and stress-testing it.
- NOT "signals" or "picks" — that's liability and it doesn't work.

## Split
- Code: `~/code/trading/` (own git repo). Docker not installed → pip/Ollama path later.
- Research/journal/decisions: here in the vault.

## Status
- 2026-07-01: track opened. Research brief + verification protocol drafted. Awaiting
  Fable 5 research pass. Jarvis is priority #2 (see [[fable-5-launch-prep]]).
