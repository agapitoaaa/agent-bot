# H1: Monthly trend filter on a fixed ETF basket

Status: PRE-REGISTERED (not yet coded, not yet run, no data fetched). Registered 2026-11-24 by Ledger. Approved direction: human decision A5 (option baseline-trend). PAPER ONLY. Research, not financial advice. No profit is claimed or expected.
**QA must review this file (and the backtester) before any promotion beyond "registered". Ledger cannot self-promote.**
office: stage=trading, desk=trader, sprite=ledger

## Evidence status (read first)
Every number in the strategy catalog (`trading/knowledge/strategies.md`, sections 3, 4.1, 4.2, 4.12, 4.26) comes from abstracts, snippets and secondary summaries. **The catalog figures are unverified until a primary source is read.** That includes the 2025 CTA drawdown (secondary trade press), the Faber results, Hurst-Ooi-Pedersen, Huang-Li, and the decay figures (McLean-Pontiff, Hou-Xue-Zhang). This hypothesis is a design for an honest test, not a claim that the edge exists.

## Hypothesis
Holding each of six liquid ETFs only while its month-end close is above its long moving average, and holding T-bill ETF otherwise, will have a **lower maximum drawdown** than H0 (equal-weight buy-and-hold of the same basket), at a net risk-adjusted return not materially worse, after costs. It is **not** hypothesised to beat buy-and-hold in raw return; lagging in bull markets is expected.

## Universe (frozen at registration; no changes after any data is seen)
| Sleeve | Ticker | Role |
|---|---|---|
| US equity | VTI | risk asset |
| Developed ex-US equity | VEA | risk asset |
| Emerging equity | VWO | risk asset |
| US aggregate bonds | AGG | risk asset |
| Gold | GLD | risk asset |
| US REITs (real assets) | VNQ | risk asset |
| T-bills | BIL | cash proxy when a sleeve is out |

Each risk sleeve gets a fixed 1/6 slot. When a sleeve's signal is off, its slot sits in BIL (no re-weighting into other risk assets, no leverage, no shorting). Inception dates, liquidity and expense ratios are unverified; check at data pull. If history is short, the common window starts at the latest inception date. No substitution after results are seen (a substitution would be a new, logged hypothesis).

## Signal rule (exact)
- Evaluate once per month, on the last trading day's close, using only data up to and including that close.
- Sleeve is ON for the next month if close > SMA(window) of that sleeve's total-return-adjusted close; otherwise OFF (hold BIL). Strict inequality. No bands, no filters, no stops, no other parameters.
- Execution: trade at the **next trading day's close** after the signal (one-day delay to avoid look-ahead and to be implementable). Trades happen only when a sleeve's state flips.
- Minimum holding: a flipped state stands until the next month-end evaluation (no intramonth action).
- Turnover cap: no more than 1 flip per sleeve per month by construction; the guard's limits (read-only to Ledger) apply on top for any paper order.

## Parameter sets (at most 3, fixed now, all reported, none chosen after the fact)
| Id | Window | Status |
|---|---|---|
| P1 (primary, the only one judged) | 10-month SMA of month-end closes | pre-registered default |
| P2 | 200-trading-day SMA, evaluated at month-end | robustness |
| P3 | 12-month SMA of month-end closes | robustness |
P2 and P3 exist to show parameter fragility, not to pick a winner. If P2/P3 disagree sharply with P1 the verdict is "fragile", not "choose the best".

## Cost model (fixed in bps, before testing)
- Base: 10 bps per side (half-spread plus slippage) on traded notional, all tickers, 0 commission. Conservative for liquid ETFs for a small account; actual quotes unverified.
- Stress: 2x, i.e. 20 bps per side. Success criteria must hold at the base case; the stress run must not reverse the sign of the conclusion.
- Cash leg: BIL total return (no extra cost assumption beyond the trade cost above).
- Taxes, FX and funding costs for the owner (Philippines) are unresolved and excluded; they are noted as a reason live results would be worse.

## Periods (declared before any data is pulled)
- In-sample (design and bug-fixing): common start date through 2021-12-31.
- **Held-out:** 2022-01-01 through the last month-end before the data pull. It is run once, after code and parameters are frozen and QA has reviewed the backtester. No re-running after tweaks; any re-run is a new trial in the registry.
- Named stress periods reported separately: 2008-09 (if in the common window), 2020 Q1, 2022 (stocks and bonds fell together), and the first half of 2025.
- Honest caveat: the held-out window is not pristine, since the author knows broad market history. This is why forward paper evidence is primary.

## Benchmarks
H0-a (equal-weight buy-and-hold, annual rebalance) and H0-b (60/40). See `H0-benchmark.md`. Same dates, same cost model, same code path.

## Success criteria (net of costs, stated before testing)
All must hold for P1, on the held-out window (and not be contradicted in-sample):
1. Max drawdown at least 25% lower (relative) than H0-a (e.g. 20% vs 26.7% or better). Threshold is an assumption set now and not to be moved.
2. Net CAGR no more than 1.5 percentage points per year below H0-a, OR net Sharpe not worse than H0-a.
3. At the 2x cost stress, criteria 1 and 2 still hold.
4. Annual one-way turnover reported and below 150% of portfolio (cap on churn; a result above that is a "cost fragile" fail).
5. P2 and P3 do not reverse criterion 1 (parameter robustness).
6. Deflated Sharpe Ratio computed with the trial count from `trial-registry.md` (3 H1 trials plus H0 trials); reported, not used to pass a weak result.
Even if all pass, the status becomes "survived a backtest", never "validated". Promotion requires QA review plus forward paper evidence (below).

## Kill rule (retire H1)
Retire H1 (log in registry as "killed") if any of: (a) held-out max drawdown is not lower than H0-a's by any margin; (b) net CAGR gap exceeds 3 percentage points per year below H0-a at base cost; (c) the stress run reverses the conclusion; (d) forward paper: after 12 months, drawdown reduction is not observed AND the system shows more than 40 flips of cost with no benefit; (e) QA finds a look-ahead or data error that cannot be fixed without changing rules. "Inconclusive" and "no edge found" are valid outcomes and will be recorded as such.

## Forward-only paper note
Backtest can reject H1 but cannot confirm it. The primary evidence is a forward paper run starting after QA sign-off, with the monthly signal journaled BEFORE each trade (`scripts/trade_memory.py add-decision`) with rationale, the strongest counter-argument, invalidation rule and confidence. Expect only a handful of signals a year, so 90 days proves nothing; the first purpose is to check the machinery (data, guard, journal, reconciliation). Judge on observation count (months) with a Minimum Track Record Length check, not trade count. Default action stays NO TRADE when a signal has not changed.

## Challenge for QA (strongest arguments against H1)
QA, please attack these before promotion. Nova flagged she may lean toward trend because it has the most literature.
1. **Whipsaw.** In sideways, V-shaped or rapidly reversing markets (2018 Q4, 2020, 2022 for stocks and bonds together) a monthly MA rule sells low and buys back higher. Each flip pays 20 bps round trip plus the lost rebound. The whipsaw count may erase the drawdown benefit. Check it per sleeve, and note that the 10-month and 200-day rules will often flip together (P1/P2 are highly correlated, so "3 parameter sets" is closer to 1.5 independent trials).
2. **Crowding and decay.** 10-month/200-day on asset classes is among the most-publicised rules (Faber was reportedly a most-downloaded SSRN paper; unverified). Published edges decay (McLean-Pontiff, Hou-Xue-Zhang; unverified). A plausible prior is that any live edge is well below the backtest.
3. **Weak 2025.** A secondary source reports trend/CTA indexes had a poor first half of 2025 (about -15% trailing 12 months at June 2025; unverified). If the held-out window includes 2025, the test partially overlaps a known bad stretch; is that fair, or a convenient excuse either way?
4. **Futures versus ETF transfer.** The strongest evidence (Moskowitz-Ooi-Pedersen, Hurst et al.) is on liquid futures with shorting and cross-asset diversification across 58-67 markets, with AQR as an interested author. A long-only, 6-ETF, cash-when-off version is a different strategy: no short leg, little diversification, bonds and equities correlated in 2022, REIT and EM sleeves are equity-like. Huang and Li argue asset-by-asset evidence for time-series momentum is weak.
5. **Data-window risk.** Short common history (REIT/EM/T-bill ETF inceptions) may leave few independent cycles; two or three regime episodes cannot support a statistical claim.
6. **Held-out contamination and design bias.** Thresholds were set by someone who knows market history; the hold-out is not clean.
7. **Cost realism.** 10 bps may be too low for VWO/VNQ at the open and too high for VTI; tax, FX and funding for the owner are unmodelled.
8. **Benchmark choice.** Equal-weight 6-sleeve H0 includes gold and EM, which flatters or penalises depending on the era; ask whether H0-b (60/40) is the fairer yardstick.
QA should also confirm: adjusted-close point-in-time handling, no look-ahead at month-end, the one-day execution delay, and the trial counting.

## Trial registry
All trials (P1, P2, P3, plus H0-a/H0-b) are logged in `trial-registry.md` before they run.

## Not allowed
No parameter additions, no basket swaps, no new filters, no changing the success thresholds, no leverage, no shorting, no real money. Any such idea becomes a new hypothesis with its own registry entries.
