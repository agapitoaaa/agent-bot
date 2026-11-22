# Trader bot: plan

Status: PLAN ONLY. Nothing is built and no trading of any kind has happened. Needs the owner's sign-off (approval A3 in the office panel).
This is not financial advice. The goal is a learning and research agent that practises on a simulated account.

## 1. Goal and honest expectations
Build a new agent, the trader, who learns how markets work, forms testable ideas, tests them on history, then practises on a **paper (simulated) account** and keeps a journal. Success is measured against a simple benchmark (buy-and-hold an index fund), not against "making money".

Be realistic:
- Most active strategies fail to beat a plain index fund after costs. Finding an edge is hard even for professionals. Treat "no profitable strategy found" as a valid, useful result.
- Paper results are optimistic: simulated fills ignore much of the real slippage, queue position and liquidity limits.
- LLM agents have specific failure modes: confident but wrong analysis, overtrading, and look-ahead bias (the model's training data may already contain the "future" of a historical test). Recent work on this is mostly frameworks and warnings, not effect sizes.

## 2. Non-negotiable rules
1. **Paper trading only.** Real money requires a separate, explicit, written approval from the owner with hard limits (gate G4 below). Default is never.
2. **No transfers or withdrawals, ever.** The agent never gets credentials that can move money.
3. **Risk limits are enforced by code, not by the agent's judgment.** Every order passes a deterministic guard the agent cannot edit. Changing limits needs owner approval.
4. **Default action is "no trade".** Orders need a written rationale and a pre-declared exit/invalidation rule.
5. **Kill switch in the control room.** One tap halts all trading; the guard checks it before every order.
6. **Secrets stay secret.** Broker keys live in the environment's secret store, never in the repo, journal or chat.
7. No claims of guaranteed or expected profit in any output.

## 3. The agent
- Name/persona: **Ledger**, a methodical, skeptical slime who distrusts his own good luck. Blind spot: waits too long for certainty; over-fits a good-looking backtest. Accessory: bowler hat and monocle. Desk: a "trading desk" with several monitors in the office.
- File: `.claude/agents/trader.md` (tools: Read, Write, Edit, Bash, Grep, Glob, WebSearch). Reads `memory/trader.md` and `memory/team.md` first, like the others.
- Works with the existing team: the `researcher` can feed market/strategy research; `qa-engineer` reviews the guard and backtester; `/retro` runs on rule breaks or losing streaks; lessons go to memory.

## 4. How he learns (self-sufficient, with checks)
1. **Knowledge base** `trading/knowledge/`: short notes, each with sources, dates and a confidence level; no uncited claims. Curriculum: market structure and order types; costs, spreads, slippage; position sizing and risk of ruin; diversification; backtesting pitfalls (look-ahead, survivorship, data snooping, overfitting); strategy families (trend following, momentum, mean reversion, volatility targeting, simple rebalancing); behavioural pitfalls; taxes and regulation by jurisdiction (awareness only).
2. **Hypothesis loop** `trading/hypotheses/`: write the idea, exact rules, and success criteria BEFORE testing (pre-registration). Then backtest, then forward-test on paper. Reject ideas that only work in-sample.
3. **Forward-test journal** `trading/journal/`: every decision logged with rationale and timestamp before the outcome exists, then outcome and review. This is the honest evidence, since historical tests can leak.
4. **Review loops:** weekly review note; `/retro` on any guard block, rule break or drawdown breach; durable lessons appended to `memory/trader.md`.
5. **Self-quiz and challenge:** before promoting any strategy, he must write the strongest argument against it; QA reviews.

## 5. Architecture
| Part | What | Notes |
|---|---|---|
| Risk guard | `trading/risk/guard.py` + `limits.json` | Deterministic checks before every order; tested; agent has read-only access |
| Broker adapter | `trading/broker/` interface + paper implementation | Phase 1: paper only. Live adapter not written until gate G4 |
| Data layer | `trading/data/` free sources, cached, point-in-time | Prefer official/exchange data; avoid look-ahead |
| Backtester | `trading/backtest/` (vectorized, with fees and slippage) | Existing libraries like vectorbt are options; check maintenance first |
| Journal and metrics | `trading/journal/`, `trading/metrics.py` | Return, drawdown, Sharpe-like ratio, win rate, expectancy, turnover, vs benchmark |
| Runner | `/trade-tick` command (like `/tick`) | Reads state, proposes orders, guard validates, paper broker executes, journal and events written |
| Control room | Trading card in the office page | Equity vs benchmark, positions, P&L, halt button, approvals for promotions |
| Events | `trade_opened`, `trade_closed`, `risk_block`, `halt` via `log_event.py` | Slime animations: Ledger at the trading desk, alert on a risk block |

Where it runs: develop and test here and on your laptop. Unattended runs need the scheduled-task repo-access fix first. Secrets via the environment's credential store, and the environment's network allowlist for the broker and data hosts.

## 6. Market choice (decision needed)
| Option | Pros | Cons |
|---|---|---|
| **US stocks/ETFs on Alpaca paper** (recommended start) | Free paper API reported open to non-US users; realistic quotes; swing/daily strategies suit a slow, careful agent | Market hours; IEX-only data on paper-only accounts per one docs version; only US stocks and select crypto |
| **Crypto on exchange testnets** (Binance/Bybit testnet) | 24/7, fast feedback, free public historical data | Testnet prices and liquidity are not representative; very volatile; easy to overtrade |
| Both | Broader learning | Double the work; delay the first result |

Recommended: offline backtests on free data, then Alpaca paper for forward tests on a small whitelist of liquid ETFs/large caps, daily or weekly horizon. Crypto later.

## 7. Guardrails (initial limits, to be confirmed)
- Whitelist of instruments (liquid ETFs and large caps). No leverage, margin, options, shorting, futures or crypto perpetuals in phase 1.
- Max 5% of equity per position, max 50% total exposure, max 8 open positions.
- Daily loss limit 2% and max drawdown 10%: breach halts trading and triggers a retro.
- Max 10 orders per day; order size cap; no trades when data is stale or the market state is unclear.
- Every order must carry rationale, stop/invalidation rule, and strategy id; unmatched orders are rejected.

## 8. Evaluation and promotion gates
- **G1 Backtest:** pre-registered rules, costs and slippage included, walk-forward or out-of-sample test, compared to the benchmark. Not enough alone.
- **G2 Paper forward test:** at least 90 days and at least 100 trades (whichever is longer; otherwise "inconclusive"). Must not breach limits.
- **G3 Review:** QA and owner review of journal, drawdowns, and whether results beat the benchmark after costs and are not luck.
- **G4 (optional, only if you ever want it):** real money with a tiny, fixed amount, separate approval, live adapter written and reviewed, hard cap, kill switch tested. Not part of this plan's default scope.

## 9. Phases
0. **Decisions** (this plan): market, horizon, limits, data budget, who reviews weekly.
1. **Foundation:** agent file and persona, repo structure, journal schema, risk guard with tests, kill switch, events.
2. **Data and backtester:** free historical data, cost model, metrics, a baseline (buy-and-hold) to beat.
3. **Knowledge base and first hypotheses:** curriculum notes (with the researcher), 3-5 pre-registered hypotheses.
4. **Paper broker and forward test:** adapter, runner, journal, control-room card.
5. **Review loop:** weekly reviews, retros, memory updates; iterate or retire strategies.
6. **Evaluation:** apply gates G1-G3 and write an honest report, including "nothing worked" if so.

## 10. Risks
Overfitting and data snooping; look-ahead via the model's own memory; paper-versus-live gap; data or API outages; token cost of frequent runs; scope creep toward real money; legal and tax rules vary by jurisdiction (not advice); false confidence from a lucky streak.

## 11. Decisions needed from you
1. Market for phase 1 (see section 6).
2. Your location/jurisdiction (broker access, tax awareness).
3. Horizon: daily/weekly swing (recommended) or intraday (not recommended for an LLM agent).
4. Real money: confirm "never by default; only with a separate approval".
5. Paper starting capital (suggest a realistic amount such as $10,000 rather than the $100k default).
6. Free data only? (recommended)

## 12. What was checked and what was not
Checked by search snippets only (not full documents): Alpaca paper-trading API is free and described as open to anyone globally, supports US-listed stocks and select crypto, default $100k paper balance, IEX-only data for paper-only accounts per an older docs page ([Alpaca paper trading](https://alpaca.markets/blog/paper-trading-api), [docs](https://docs.alpaca.markets/us/v1.1/docs/paper-trading), [non-US live accounts](https://alpaca.markets/learn/live-trading-account-non-us)); Binance and Bybit testnets exist with faucet funds and separate keys, and Binance publishes free historical data ([guide](https://dev.to/paarthurnax_3f967358857ce/how-to-set-up-paper-trading-on-binance-testnet-complete-walkthrough-4pl5)); LLM backtests have look-ahead and data-snooping problems ([FINSABER](https://arxiv.org/html/2505.07078v4), [Look-Ahead-Bench](https://arxiv.org/pdf/2601.13770), [FinCAD](https://arxiv.org/abs/2605.24564)).
Not verified: current Alpaca signup terms for your country, data-feed limits today, vectorbt's maintenance status, any effect size for LLM-agent overfitting, and the statement that most active strategies trail an index (widely reported; no specific figure checked). Confirm on official pages before building.
