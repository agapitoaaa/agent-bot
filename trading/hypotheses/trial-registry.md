# Trial registry

Every variant run, including failed and discarded ones, is logged here BEFORE it is run, and its result is added afterwards. The Deflated Sharpe Ratio uses the total trial count. Ledger appends only; entries are never deleted or edited after a result (add a correction line instead). PAPER ONLY; research, not financial advice. Catalog figures behind these ideas are unverified.

Status values: planned, running, done, killed, void.

Columns: id | date registered | hypothesis | variant / parameters | period | cost (bps per side) | status | result (net) | notes

| id | registered | hypothesis | variant | period | cost | status | result | notes |
|---|---|---|---|---|---|---|---|---|
| T-H0a | 2026-11-24 | H0 | equal-weight buy-and-hold, annual rebalance, 6 ETFs | in-sample, held-out | 10 base, 20 stress | planned | n/a | benchmark; not a strategy trial but counted for transparency |
| T-H0b | 2026-11-24 | H0 | 60/40 VTI/AGG, annual rebalance | in-sample, held-out | 10 base, 20 stress | planned | n/a | benchmark |
| T-H1-P1 | 2026-11-24 | H1 | 10-month SMA, monthly, 6-ETF basket + BIL | in-sample, then held-out once | 10 base, 20 stress | planned | n/a | pre-registered primary, the only one judged |
| T-H1-P2 | 2026-11-24 | H1 | 200-day SMA at month-end | in-sample, then held-out once | 10 base, 20 stress | planned | n/a | robustness; highly correlated with P1 |
| T-H1-P3 | 2026-11-24 | H1 | 12-month SMA of month-end closes | in-sample, then held-out once | 10 base, 20 stress | planned | n/a | robustness |

H1 planned strategy trials: 3 (P1-P3). Total registry rows: 5. Any additional run, rerun after a fix, or variant adds a row before it executes.
