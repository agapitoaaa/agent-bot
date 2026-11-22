# Ledger's curriculum and first experiments

Paper only. Education and research, not financial advice. Built from `strategies.md` and `sources.md` (Nova's research; snippets and abstracts only, so every figure is unverified until a primary source is read).

## 1. Study order (each module ends with a cited note in `trading/knowledge/`)
1. **Baselines and discipline:** buy-and-hold, equal weight (1/N), periodic rebalancing, dollar-cost averaging as risk management (not alpha). Why simple baselines are hard to beat (DeMiguel et al., 2009; Vanguard 2023).
2. **Costs, turnover and what retail loses to:** spread, slippage, fees, taxes; evidence that high-turnover traders lose mainly to costs (Barber and Odean). Turnover caps.
3. **Backtesting honesty:** look-ahead, survivorship, data snooping, the trial registry, Deflated Sharpe Ratio, Minimum Track Record Length, walk-forward, point-in-time data.
4. **Sizing and exits as a framework:** fixed-fractional and volatility-scaled sizing; fractional Kelly as a ceiling in theory only; pre-declared invalidation exits (stops help only when returns have momentum).
5. **Trend following on a fixed basket:** 10-month / 200-day moving-average rule and Faber-style asset-class rotation. The strongest, lowest-turnover family in the catalog, but contested (statistical disputes; a weak first half of 2025 per a secondary source), and its realistic benefit is lower drawdown, not beating buy-and-hold in bull markets.
6. **Information and risk context:** the source catalog and the evidence cards protocol (`docs/trader-intel-design.md`).
Later: dual momentum, factor ETFs, volatility targeting, breakout variants, crypto spot trend (BTC/ETH only). Avoid for now: short-term reversal/RSI, PEAD, calendar effects, risk parity, pairs/stat arb, candlesticks and chart patterns, news/LLM sentiment as a trigger, crypto dominance rotation, funding carry.

## 2. First pre-registered experiments (proposals; nothing is coded or run)
- **H0 Benchmark:** equal-weight buy-and-hold of the same basket, plus a simple 60/40 stock/bond mix. Everything must be compared with these, net of costs.
- **H1 Trend on a fixed basket:** a basket of 5-8 broad, liquid ETFs across US equity, international equity, bonds and real assets/gold (final list chosen and frozen at pre-registration). Monthly signal: hold an asset if it is above its 200-day (or 10-month) moving average, otherwise cash. **At most 3 parameter sets, fixed in advance.** Assumed costs stated up front. Success criteria stated up front: e.g. lower maximum drawdown than H0 at a comparable risk-adjusted return, net of costs, in walk-forward and out-of-sample periods. Every variant tried is logged to the trial registry.
- **H2 Sizing and exits:** on H1, compare fixed-fractional against volatility-scaled sizing and time-based against signal-based exits, with the same discipline.
- **H3 (later):** crypto spot trend on BTC and ETH only.
Expectation to set honestly: H1 produces only a handful of signals per year, so a 90-day paper test cannot prove anything. "Inconclusive" and "no edge found" are valid outcomes. The paper test mainly checks that the machinery works (data, guard, journal, reconciliation).

## 3. Cautions to carry
1. Published edges decay: reported total post-publication decline about 58%, of which about 26% data-mining and at least about 32% publication effect (McLean and Pontiff; my reconciliation, to verify). Hou, Xue and Zhang failed to replicate 64% of 447 anomalies at the 5% level. Plan for live results well below paper results.
2. Overtrading and costs are Ledger's known weakness; Novy-Marx and Velikov find most anomalies with under 50% monthly turnover survive costs, but their cost assumptions come from large managers.
3. After decay, costs, taxes and a small account, no single strategy here is likely to be distinguishable from zero in 90 days.
4. **Bias check:** Nova flagged that she may lean toward trend because it has the most literature. QA should challenge the whipsaw and crowding evidence before H1 is promoted.

## 4. Verify from primary sources first
McLean-Pontiff 32% vs 58%; Hou-Xue-Zhang 64% of 447; Do-Faff 0.86% to 0.37%; Duvinage 5 of 83; Harvey Sharpe 0.40 to 0.48-0.51; Vanguard 68%; plus any 2026 preprints. Also pending: official rate limits and terms of the data sources in `sources.md`.
