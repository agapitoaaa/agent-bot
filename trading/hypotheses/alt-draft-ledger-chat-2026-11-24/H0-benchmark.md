# H0: Benchmarks (version 1)

Status: DRAFT (nothing run; awaiting QA review and freeze). Author: Ledger. Date: 2026-11-24. Approved scope: owner decision A5. Paper only; not financial advice.

Purpose: define what any active idea (H1 and later) must be compared against. A strategy that cannot beat these net of costs, on the criteria stated in its own file, is not interesting. Benchmarks are not trades to be made; they are reference series.

## Basket (shared with H1, frozen together)
Six "slots", each 1/6 (16.67%) of the portfolio:

| Slot | Ticker | Exposure |
|---|---|---|
| US equity | SPY | S&P 500 large caps |
| Developed ex-US equity | EFA | MSCI EAFE |
| Emerging equity | EEM | MSCI Emerging Markets |
| US bonds | IEF | 7-10 year US Treasuries |
| Gold | GLD | Physical gold |
| Real estate | VNQ | US REITs |

Cash proxy (H1 only, also reported as reference "B0"): SHY (1-3 year US Treasuries).
Reasons and inception caveats are in H1. Inception dates are from my memory and must be verified at data download (SPY 1993, EFA 2001, IEF/SHY 2002, EEM 2003, VNQ 2004, GLD Nov 2004).

## Evaluation window (same for every benchmark and every H1 trial)
- Start: first trading day of 2005-12 (so 12 months of history exist for GLD, the youngest ETF, and all H1 signals are computable). Exact first date is computed by code, recorded, and applied to all series.
- End: last trading day of 2026-10 (last full month before today, 2026-11-24).
- Development window: 2005-12 to 2018-12. Held-out window: 2019-01 to 2026-10 (run once; see H1).
- Rule changes after seeing any result are forbidden (see README).

## Benchmarks
**B1: equal-weight buy-and-hold of the same six ETFs.**
- Start with 1/6 in each at the first trading day's open. Rebalance back to 1/6 each on the first trading day after the December month-end. No other trades. No drift band (kept identical to H1's rebalance schedule so the comparison is like for like).
- Question it answers: what does the basket itself do with no timing? H1 must beat this on the H1 criteria.

**B2: 60/40 stock/bond mix.**
- 60% SPY, 40% IEF; same start; same December rebalance.
- Question it answers: what does a plain, widely known mix do? Convention uses an aggregate bond fund; IEF is used so the series reaches the same start date and matches the basket. Flagged as a design choice for QA.

**B0 (reference only): 100% SHY.** Shows the cash drag H1 will carry. No rules, no parameters.

Reported but NOT a selection: nothing is chosen among B1/B2; H1 is judged against both.

## Cost assumptions (stated numerically, same as H1)
- Per trade side (buy or sell): 5 bps of traded value for spread plus slippage on every ETF; commission 0 (US stocks/ETFs commission-free on the intended paper broker per Nova's catalog; an assumption to re-verify).
- Stress run: 10 bps per side.
- ETF expense ratios are already embedded in adjusted prices; no extra charge.
- Initial purchase and each rebalance trade pay the cost. Taxes: not modelled (see H1 notes).
- Fractional shares allowed in the backtest; whole-share rounding ignored (noted; at a small account it matters for a 16.7% slot).

## Metrics reported for every benchmark and trial
Net CAGR, annualised volatility, net Sharpe (excess of SHY return; N stated), maximum drawdown (month-end and daily), time under water, worst calendar year, calendar-year table, one-way turnover per year, number of trades, Calmar. Sub-windows: development, held-out, and the named stress windows 2008 (2007-10 to 2009-03), 2020 (2020-02 to 2020-04), 2022 (calendar year). Always with the sample-size caveat: about 250 monthly observations and only about three major drawdown episodes.

## Data needed (nothing exists yet)
For each of the 7 tickers: daily OHLC, volume, split-and-dividend adjusted close, raw close, dividend and split tables, 2004-01 to 2026-10 (earlier not needed). Free source (e.g. Stooq or a Yahoo-type download) cached as CSV in `trading/data/`, with download date, source and a file hash recorded. Check: no gaps, split handling, adjusted vs raw consistency, and that the adjusted series is a single frozen vintage (adjusted histories shift every time a dividend is paid, so re-downloading later changes old values slightly). Licensing terms of free sources unverified.

## Trial count
Registered runs: B1, B2 (plus reference B0). `counts_toward_dsr: false`. See `trial-registry.jsonl`.

## Strongest argument against this
The benchmark is not neutral. A hand-picked basket of six ETFs including gold and REITs is itself a bet: those survivors were chosen with hindsight and gold had a long bull run inside this window, so B1 may look better than a basket I could have chosen in 2005. Also 60/40 with IEF instead of an aggregate fund shifts the result, and the window starts after a 2003-2005 recovery and ends in a period I partly remember, so the benchmark is contaminated by my knowledge.

## What would change my mind
If QA shows the benchmark ranking flips with a trivially different but defensible choice (aggregate bond fund in the 60/40, a different REIT or commodity sleeve, a quarterly rebalance), I would conclude the benchmark is fragile, report both versions as separate registered runs, and stop making strong claims against either.
