# H1: Trend filter on a fixed six-ETF basket (version 1)

Status: DRAFT (nothing run, no data downloaded; awaiting QA challenge and owner sign-off before freeze). Author: Ledger. Date: 2026-11-24. Approved scope: owner decision A5 (benchmark plus ONE trend experiment, at most 3 parameter sets, QA to challenge before promotion). Paper only; education and research, not financial advice. No claim of profit is made.

Freeze record (fill at freeze): date ____ ; git commit ____ ; QA reviewer ____ .

## 0. Honest framing first
Trend following is the family with the most literature in our catalog, and Nova flagged her own lean toward it for that reason. Literature volume is not evidence of a net edge for a small long-only ETF account. Evidence for: Moskowitz-Ooi-Pedersen 2012, Hurst-Ooi-Pedersen 2017 (AQR, a firm that sells trend products), Faber 2007. Evidence against: Huang and Li (asset-by-asset tests show little time-series momentum), post-crisis weakness, weak 2025 for CTAs (secondary source), post-publication decay (McLean-Pontiff), and the transfer from futures to long-only ETFs is unproven. All of these are snippet-level in `strategies.md` and unverified until read at source. Realistic goal: lower drawdown than the basket held passively, at a return not much lower. Expect it to lag in bull markets. "No edge found" is an acceptable result.

## 1. Hypothesis (one sentence)
Holding each ETF in a fixed six-ETF basket only while its price is above its own long-term trend (otherwise holding a short-term Treasury ETF), checked once a month, produces a meaningfully smaller maximum drawdown than holding the same basket passively, without giving up much net return, after costs.

Null: drawdown reduction is no better than what chance, or simply holding less risk, would give; or it is bought at a net return cost larger than the allowed amount.

## 2. Universe (frozen; owner may change the list BEFORE freeze only)
Six risk slots, each 1/6 of the portfolio, plus a cash sleeve.

| Slot | Ticker | Why (and what could be wrong with it) |
|---|---|---|
| US equity | SPY | Largest, most liquid US ETF, S&P 500, history since 1993. Tightest spreads. |
| Developed ex-US equity | EFA | Diversifier vs US; long established (2001). Highly correlated with SPY in crashes. |
| Emerging equity | EEM | Different cycle and a trending history (2003). Wider spreads, EM-specific shocks, high volatility and many whipsaws are plausible. |
| US government bonds | IEF | 7-10y Treasuries (2002). Intermediate duration: diversifies equity crashes but fell with stocks in 2022. |
| Gold | GLD | Real-asset/crisis hedge (Nov 2004). Hindsight risk: gold had a long bull run inside our window. Trend rules may also whipsaw it. |
| Real estate | VNQ | US REITs (Sept 2004); equity-like but different drivers; Faber used real estate. |
| Cash sleeve | SHY | 1-3y Treasuries (2002): holds the slot of any asset that is off-trend. Duration is not zero; it lost a little in 2022. |

Left out on purpose: broad commodities (DBC began 2006, tax-form and roll-yield complications, shortens history), TIPS, high yield, single stocks, crypto (H3 later), leveraged or inverse ETFs. Max basket size honoured: 6 risk ETFs plus the cash sleeve = 7 tickers.

Survivorship / selection caution: every ticker was chosen because it is large and still exists, picked by me with knowledge of how these asset classes behaved. No ETF in the basket has died or been merged, so the usual dead-instrument problem is absent by construction, which is itself selection bias. The basket cannot be tuned after any result.

## 3. Rules (exact)
Time convention: "month-end" = the last trading day of the calendar month, using the exchange trading calendar of the downloaded data.

**Signal (computed once per month at the month-end close using only data up to and including that close):**
For each risk ETF i, ON if the signal condition below holds, otherwise OFF. The condition depends on the parameter set.

**Allocation after the signal:**
- Each ON asset targets 1/6 of equity.
- Each OFF asset's 1/6 slot goes into SHY.
- No leverage, no shorting, no options. Total invested = 100% of equity in the research backtest (see section 9 for the guard-limited paper version).

**Execution assumption:** orders are placed after the month-end close and filled at the OPEN of the next trading day, with the cost in section 5 applied against us. (If only close data is available at test time, fill at the next trading day's close and record that this deviates from the registration; that would be logged, not hidden.) No intramonth signals, no stops, no discretionary override.

**Trade only on a state change:** an asset is traded only when its ON/OFF state flips at a month-end. Assets whose state did not change are not touched.

**Annual rebalance:** at the December month-end signal, all ON assets are reset to 1/6 (and SHY to the remaining slots), executed the next trading day. This is the same schedule as benchmark B1/B2.

**Minimum holding period:** by construction an asset cannot flip more than once per month, so the minimum interval between trades in one asset is about one month. No other holding rule.

**Parameter sets (exactly three, fixed now, none to be added):**
- **P1 (PRIMARY, the one judged): 10-month SMA.** ON if the month-end close is above the simple average of the last 10 month-end closes (including the current one). Source of the rule: Faber 2007 (SSRN 962461).
- **P2: 200-day SMA.** ON if the month-end close is above the simple average of the last 200 daily closes (including today's). The daily-data cousin of P1; deliberately expected to behave very similarly, which is a robustness check rather than independent evidence.
- **P3: 12-month absolute momentum.** ON if the total return of the ETF over the last 12 months (month-end to month-end) exceeds the total return of SHY over the same 12 months. Different mechanism (return sign, not price vs average). Source: Moskowitz-Ooi-Pedersen / Antonacci-style absolute momentum.

Signal series: the split-and-dividend-adjusted close from a single frozen data vintage (see section 8 for the known limitation). No tuning, no band, no filter. Anything extra (hysteresis bands, vol scaling, stops, a 100/150-day average) would be a new trial in a new version.

## 4. Period (frozen)
- Evaluation window for all trials and benchmarks: first trading day after the 2005-11 month-end (first date when all six ETFs have 12 months of history, driven by GLD) through the last trading day of 2026-10. About 20.9 years, about 250 monthly returns.
- Development window: 2005-12 to 2018-12. Used ONLY to test the code (reconciliation, unit tests, data checks), not to choose rules or parameters. Rules are already fixed.
- Held-out window: 2019-01 to 2026-10, evaluated ONCE per trial, after the code is QA-passed.
- Named stress windows (reported, not tuned): 2008 (2007-10 to 2009-03), 2020 (2020-02 to 2020-04), 2022 (calendar year).
- Contamination warning (important): I (an LLM) roughly know how markets behaved through my knowledge cutoff, and I have read the published trend literature. The "held-out" window is therefore not blind to me. Genuinely out-of-sample evidence is only (a) forward paper data after the freeze date and (b) an optional pre-2004 proxy-history check (index mutual funds or index data, e.g. 1990s onward) that the owner can approve later, noting Faber already published on that era. I will not call the held-out run "true out-of-sample" in any report.

## 5. Costs and slippage (stated numerically)
- 5 bps per side (buy or sell) of traded value on every ETF, covering half-spread plus slippage; deliberately above the quoted spread of SPY (about 1 bp) because EEM, VNQ, GLD, EFA, IEF are wider and market orders into the open slip.
- Stress run: 10 bps per side (2x).
- Commission: 0 on the intended paper broker (assumption; re-verify).
- Fund expense ratios are already inside the adjusted prices.
- Idle cash earns SHY return. No margin, no borrowing.
- Taxes, FX and funding costs: not modelled (awareness notes in section 10).
- Turnover cap for the research version: report average one-way turnover per year; flag if it exceeds 100% of equity per year. Expected much lower but unmeasured.

## 6. Benchmarks (from H0)
B1 equal-weight buy-and-hold of the same six ETFs with the same December rebalance; B2 60/40 SPY/IEF with the same rebalance; B0 = 100% SHY (reference only).

## 7. Success criteria (stated BEFORE any test; all judged on P1, net of costs)
All of the following must hold for H1 to be called "supported on backtest" (not "promoted"; promotion is a separate owner decision):

S1. Maximum drawdown (daily close basis) of P1 over the full evaluation window is at most 75% of B1's maximum drawdown.
S2. Net CAGR of P1 over the full window is at least B1's net CAGR minus 1.5 percentage points per year.
S3. Both S1 and S2 also hold on the held-out window taken alone (window is short; a pass there is weak).
S4. Both S1 and S2 still hold under the 10 bps per side stress run.
S5. Robustness to single episodes: with the 2007-10 to 2009-03 window removed, S1 still holds on the remainder (otherwise the result is one crash and nothing else).
S6. Average one-way turnover at most 100% of equity per year, and no asset averaging more than 3 round trips (in and out) per year.
S7. A stationary block bootstrap of monthly returns (12-month blocks, 5000 draws, P1 vs B1 resampled together) shows P1 maximum drawdown below B1's in at least 75% of draws. (Crude; the number of independent drawdown episodes is about three.)
S8. Reported, not a pass/fail gate: net Sharpe of P1, B1 and B2 with Deflated Sharpe Ratio at N = 3 (H1 trials; N is increased by any later trend-family trial) and the Probabilistic Sharpe Ratio. We are NOT claiming a higher-Sharpe edge; if P1's Sharpe is not higher than B1's, that is expected and fine for the stated drawdown goal. We will not retro-fit a Sharpe claim.

Also reported against 60/40 (B2): P1 should not have a worse maximum drawdown than B2; failing this is reported as a plain negative finding, and does not by itself change pass/fail.

P2 and P3 are reported alongside. They cannot rescue a failed P1 and cannot be substituted for it.

## 8. Rejection criteria (any one rejects H1 as stated; stated BEFORE testing)
R1. P1 maximum drawdown is more than 90% of B1's over the full window (drawdown barely reduced).
R2. P1 net CAGR trails B1 by more than 3 percentage points per year.
R3. S1 or S2 fails under the 10 bps stress run.
R4. S5 fails (benefit entirely from one episode).
R5. Held-out window: P1 maximum drawdown is worse than B1's.
R6. P1 average turnover exceeds the cap in S6, or the whipsaw record shows more than half of all flips reverse within 2 months (then costs and noise dominate).
R7. Any look-ahead, survivorship or data-handling defect found by QA in the pipeline voids the run; it is repeated, and the earlier run stays in the registry.
Results between "pass" and "reject" are reported as INCONCLUSIVE. Rejection retires H1 v1; it does not authorise searching for a better lookback; that would be a new hypothesis with new trial counts.

## 9. Walk-forward / out-of-sample plan
- No parameter is fitted, so there is nothing to walk-forward optimise. What replaces it: (1) fixed rules from the literature, registered before the data are touched; (2) rolling reports of P1-P3 vs B1 over 5-year windows (no re-fitting) to show how unstable the benefit is across eras; (3) held-out run once; (4) forward paper test from the freeze date; (5) optional pre-2004 proxy history, owner approval needed (extra data work).
- Held-out and rolling reports are for honesty about instability, not for choosing among P1-P3.

## 10. Data requirements and cautions
- Needed (nothing exists): daily OHLC, volume, raw close, adjusted close, dividends and splits for SPY, EFA, EEM, IEF, GLD, VNQ, SHY, 2004-01 to 2026-10, cached in `trading/data/` with source, download date and file hash.
- Look-ahead traps: (a) signal uses data up to the month-end close only, execution next open; (b) adjusted close is re-based every time a dividend is paid, so a later download slightly changes old values; use one frozen vintage and state it. The effect on a 10-month SMA is small but real, and QA should test it. (c) month-end calendar must use actual trading days. (d) no use of future constituents or future-known facts.
- Survivorship: see section 2. Free-data quality varies; cross-check two sources on a sample of dates; licensing and rate limits unverified.
- Backtester not yet written; nothing in this file has a result. Backtest-engine differences are a separate error source (arXiv 2603.20319, snippet), so QA should reproduce the series independently.

## 11. Number of trials to be logged
Three H1 trials (P1, P2, P3) plus two benchmark registrations (B1, B2), five in all; H1 DSR uses N = 3 now. Cost-stress and held-out runs are runs of the same trial, logged as run lines. Any extra variant anyone runs, including "just checking" ones, is appended to the registry and increases N. Total at this registration: see `trial-registry.jsonl`.

## 12. Minimum track-record logic: what a 90-day paper test can and cannot show
- Monthly signals: a 90-day test sees about three month-end evaluations after the initial allocation. Most months, no asset flips; I expect roughly zero to a few flips in total (unmeasured; the backtest will give a better estimate). Whatever happens, it is a handful of observations.
- The plan's gate G2 requires at least 90 days AND at least 100 trades. H1 cannot reach 100 trades in any realistic time (a few flips per month at most); at a rough 5-15 trades a year it would take most of a decade. Therefore G2 will read "inconclusive" for H1 by construction and I will say so, not argue around it.
- A back-of-envelope MinTRL (normal returns, no skew/kurtosis adjustment, one-sided 95%): to detect a true annual Sharpe of 0.3 against zero needs about (1.645 / (0.3/sqrt(12)))^2 = roughly 360 months, i.e. about 30 years. Real returns have fat tails, which makes it longer. Drawdown reduction cannot be tested forward unless a real drawdown happens, and it may not in any given 90 days.
- What the 90-day paper test CAN show: the machinery works (data fetch, month-end signal calculation, journaling before outcome, guard checks, order-vs-intended reconciliation, fills vs assumed cost, whether cost assumptions are realistic, no limit breaches). That is its job. It cannot show profitability, edge or drawdown benefit.
- Guard conflict to resolve with the owner (I cannot change it): the current limits are max 5% per position, max 50% total exposure, max 8 positions (`docs/trader-bot-plan.md` section 7; the guard is authoritative). H1 research weights are 16.7% per ETF and 100% invested, which the guard would block. A guard-compliant paper version would hold at most 5% per risk ETF (30% total risk exposure for six assets) with the rest in cash, so it is a different, much smaller-risk strategy. The planned approach is therefore: (a) the evidence comes from the full-weight "shadow" portfolio computed on paper (hypothetical fills), and (b) any guard-limited paper orders are labelled as a machinery test, not as evidence for the criteria. Whether SHY counts toward the exposure and position limits is a question for the owner/QA. If the guard blocks an order I log it and stop.

## 13. Cash handling, tax and cost notes (awareness only; unverified; not tax advice)
- Cash sleeve is SHY, a 1-3 year Treasury ETF. A true T-bill fund (BIL) is purer but starts 2007; using it would shorten the window, so it is not used. SHY's duration is an exposure, not zero risk.
- Switching an ETF off and on realises gains or losses at each flip. Tax treatment for the owner in the Philippines is unresolved (`docs/trader-live-readiness.md` section 12). For non-US persons holding US-domiciled ETFs, US withholding on dividends and US estate-tax exposure on US assets may apply; I have not verified current rules, so this is a question for a qualified adviser before any real money (which is not approved).
- Whole-share rounding on a small account matters: a 16.7% slot of a $10,000 account is about $1,670, so GLD or SPY lots are coarse.
- FX/funding and broker fees for the owner's eventual real route are outside this paper study.

## 14. Strongest argument against this
Every number in the case for trend is a snippet from papers whose authors often sell the product, and the long-only ETF version has about 20 years of data and only about three real drawdown episodes (2008, 2020, 2022). In 2020 a monthly signal probably sells after the fall and buys after the rebound; in 2022 both stocks and bonds fell, which a trend filter does not fix. The published edge has likely decayed. The basket was picked by me with hindsight (gold in particular), the success thresholds (75%, 1.5 pp) are my judgement rather than a sourced standard, and three nearly identical rules do not give three independent looks. A drawdown reduction can also be got for free by simply holding more cash or bonds, without any trend rule. It is entirely plausible that H1 shows nothing distinguishable from a 60/40 once costs, taxes and a small account are counted.

## 15. What would change my mind
- If QA reproduces the results independently and the benefit (S1) survives a different but defensible basket, a different cash proxy, and a lag of a few days in execution, I would call it a robust drawdown-control tool (still not alpha).
- If the drawdown reduction disappears when compared with a simple "same risk" benchmark (for example B1 blended with SHY to the same volatility), I would conclude the trend rule adds nothing beyond holding less risk and drop it. This extra control benchmark is proposed for QA to add before freeze, with its own registry line, if they agree.
- If forward paper results show the machinery's fills and costs are materially worse than 5 bps per side, I would re-run with realistic costs before believing any earlier result.
- If a result appears too good (for example drawdown cut by more than half with higher return), I would assume a bug or look-ahead first and ask QA to hunt for it.
