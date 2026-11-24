# H0: Benchmark (equal-weight buy-and-hold of the H1 basket, plus 60/40)

Status: PRE-REGISTERED (not yet run). Registered 2026-11-24 by Ledger. PAPER ONLY. Research, not financial advice. No profit is claimed or expected.
office: stage=trading, desk=trader, sprite=ledger

## Purpose
H0 is the yardstick. Nothing (H1, H2, any later idea) is judged on its own; it is judged against H0, net of costs, over the same dates. H0 is also Ledger's default behaviour when no pre-registered signal fires (catalog 4.12, 4.26).

## Evidence status (read first)
All figures cited from `trading/knowledge/strategies.md` and `curriculum.md` are from abstracts and snippets only. **They are unverified until a primary source is read.** Nothing in this file depends on them being true; they only motivate the design (DeMiguel et al. 2009 on 1/N; Vanguard 2023 on lump-sum vs DCA).

## Universe (frozen; same as H1)
Risk sleeves (6 ETFs): VTI (US equity), VEA (developed ex-US equity), VWO (emerging equity), AGG (US aggregate bonds), GLD (gold), VNQ (US REITs, real assets).
Cash proxy (used by H1 only, listed here for completeness): BIL (1-3 month T-bills).
Tickers are chosen for liquidity and breadth. Inception dates and current liquidity are **unverified** (nothing fetched yet) and must be checked at data-pull time. If any ticker lacks history for the common window, the whole study starts at the latest inception date; no substitution after seeing results.

## Rules
- **H0-a: Equal-weight buy-and-hold of the basket.** Initial weights 1/6 each, rebalanced to 1/6 on the last trading day of each calendar year only (the only trades after day 1). No drift band, no signals.
- **H0-b: 60/40.** 60% VTI, 40% AGG, rebalanced annually on the same day.
- Execution: close of the first trading day on or after the start date; annual rebalance at the close of the last trading day of the year. Dividends reinvested (total-return series, point-in-time adjusted close).
- No parameters are tuned. There are exactly 2 benchmark variants, both logged in the trial registry.

## Costs
Same cost model as H1: 10 bps per side (spread plus slippage) on traded notional, 0 commission; stress run at 20 bps per side. Annual rebalance turnover is small, so cost impact should be tiny, but it is still deducted.

## Periods
Identical to H1: in-sample (design) window from the common start date to 2021-12-31; held-out window 2022-01-01 to the last month-end before the data pull. Forward paper period starts at the registration date of H1.

## Reported metrics (for H0 and H1, same code path, same dates)
Net CAGR, annualised volatility, net Sharpe (with cash rate stated), maximum drawdown and its dates, worst calendar year, Calmar (CAGR / max drawdown), annual turnover, total cost paid, and the 2022 stress period shown separately.

## Success criteria (for H0 itself)
H0 has no pass/fail; it is a reference. It is "valid" if it reproduces within a small tolerance when run by a second implementation (QA cross-check) on the same data.

## Kill rule
None (it is the benchmark). If a data problem makes H0 and H1 incomparable, the comparison is void and logged as such.

## Known limits
- The held-out window is not pristine: the author (an LLM) has general knowledge of 2022-2025 market history. Forward-only paper results are therefore the primary evidence; the backtest can reject an idea but not promote it.
- Past results say nothing certain about future returns.
