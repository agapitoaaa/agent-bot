# Ledger: what to improve before real money (roadmap)

Status: research and planning only. No live trading code exists or will be written until gate G4 is separately approved by the owner. Not financial advice.
Companion to `docs/trader-bot-plan.md`. Platform comparison: `runs/trader-research-20261122-093135/platforms.md`.

## 0. The evidence in one paragraph
In a public real-money test (Alpha Arena season 1, Oct-Nov 2025, crypto perpetuals), most of the AI models lost money. One report has OpenAI's model down about 63%, and the organizer said fees dominated results because agents over-traded and took tiny gains that fees erased. A second contest report says only 6 of 32 stock-trading results showed gains. Both are secondary news sources, not primary data. The lesson for Ledger: the dangerous behaviours are overtrading, cost blindness and overconfidence. Everything below is built around preventing those. ([Forklog](https://forklog.com/en/four-out-of-six-ai-models-suffer-losses-in-trading-tournament/), [Decrypt](https://decrypt.co/345006), [ThinkAdvisor, May 2026](https://www.thinkadvisor.com/amp/2026/05/06/why-ai-bots-arent-ready-to-replace-your-fund-manager/))

## 1. Improve how he decides (biggest win)
- **Split roles.** The LLM is the researcher and reviewer. Trades come from **pre-registered, rule-based strategies** run by deterministic code. The LLM may propose or retire strategies, never place free-form discretionary orders.
- **Cost-aware by design.** Every strategy has a turnover cap, a minimum holding period, and an expected-edge-must-exceed-cost check. Report results net of fees, spread and slippage.
- **Default to no trade.** Inactivity is a valid, profitable-by-avoidance outcome.
- **Strategy decay monitor.** If live or paper performance falls outside the backtested range for a set period, the strategy is auto-paused and a retro runs.

## 2. Raise the evidence bar
- **Count every trial.** Log every backtest, including discarded ones. Apply the **Deflated Sharpe Ratio**, which corrects for selection bias and multiple testing, and the **Minimum Track Record Length**, which says how many return observations are needed before a Sharpe is distinguishable from zero. Fat tails and skew demand longer records. MinTRL is measured in observations (bars, months), not trade count. ([Bailey and Lopez de Prado, SSRN 2460551](https://papers.ssrn.com/abstract=2460551), [MinTrackRecord docs](https://rdrr.io/cran/PerformanceAnalytics/man/MinTrackRecord.html))
- **Replace the plan's "90 days and 100 trades" with computed thresholds** per strategy; keep 90 days as a floor.
- **Beat the benchmark net of costs** (index fund buy-and-hold, equal-weight for crypto).
- **Test after the model's knowledge cutoff** or forward-only, because LLM look-ahead bias inflates historical tests. ([FINSABER](https://arxiv.org/html/2505.07078v4), [FinCAD](https://arxiv.org/abs/2605.24564))
- **Haircut paper results.** Paper fills usually ignore queue position, depth and latency. Add estimated spread, slippage and commissions, and expect live to be worse. ([Alpaca forum](https://forum.alpaca.markets/t/slippage-paper-trading-vs-real-trading/2801), [TradersPost](https://blog.traderspost.io/article/paper-trading-vs-live-results); vendor sources, treat numbers as unverified)

## 3. Execution realism
Limit or marketable-limit orders with price collars; handle partial fills, rejections and cancels; idempotent client order IDs so a retry never duplicates; market-calendar and halt awareness; stale-data and clock-skew checks; corporate-action handling for stocks; **daily reconciliation** of the broker's orders, fills and positions against our own ledger, with any mismatch halting trading. (I found no retail-specific reconciliation guidance; this follows institutional practice.)

## 4. Risk controls (extend the guard)
Industry practice (FIA automated-trading controls, 2024) centres on pre-trade checks: fat-finger and price-collar limits, position and exposure caps, order-rate limits, plus **kill switches** with defined scope: block new orders, cancel resting orders, or flatten. Write a playbook for who can trigger it and how trading is re-enabled in stages; log every rejection and every activation. ([FIA risk controls](https://fia.org/sites/default/files/2024-07/FIA_WP_AUTOMATED%20TRADING%20RISK%20CONTROLS_FINAL_0.pdf))
Add: a **loss budget** (the most the owner is willing to lose, fixed in advance); per-strategy and total drawdown stops; leverage, margin, shorting, options and perpetuals stay disabled unless separately approved.

## 5. Security and custody
- **Trade-only API keys with withdrawals disabled**, one key per system, **separate keys for paper and live**, never reused. Restrict by **IP allowlist** where the platform supports it. ([CCXT API-key checklist](https://docs.ccxt.com/blog/api-key-security), [Kraken](https://support.kraken.com/gb/articles/organizations-api-keys))
- **Caveat:** cloud sessions here have no fixed outbound IP, so IP allowlisting would need a small always-on host with a static IP (a cost to decide on).
- Secrets only in the environment's secret store; scrub logs; rotate every 60-90 days; revoke first if exposed; 2FA on the broker account.
- **Live keys never enter the agent's context.** A separate small executor process holds them, accepts only guard-approved order objects, and cannot place orders outside limits.
- Separate brokerage account used only for this, funded only with the loss budget.

## 6. Operations
Always-on runner (not ephemeral sessions), heartbeat and alerts to the owner (push), runbooks for API outage, data gaps and partial fills, incident retros, weekly review, token-cost tracking. Today's scheduled-task repo-access problem must be fixed first.

## 7. Legal, tax, regulatory (awareness; confirm per country)
- Personal account only. Managing other people's money is regulated; out of scope.
- US note: FINRA replaced the pattern-day-trader rule and $25,000 minimum with a risk-based intraday margin standard effective 4 June 2026, with a phase-in to 20 Oct 2027. Brokers differ; check yours. ([FINRA Notice 26-10](https://www.finra.org/rules-guidance/notices/26-10))
- Keep trade records suitable for tax reporting. Rules (wash sales, crypto gains, reporting) vary by country; not verified here.
- Read the broker's terms on automated trading and API use.

## 8. Staged live ramp (what gate G4 would require)
Each stage needs the owner's explicit approval and a review of the previous stage:
1. **Shadow mode:** live data and live-account connectivity, but orders are logged and never sent.
2. **Micro-live:** tiny fixed size (a small fraction of the intended capital), loss budget enforced, kill switch tested, daily reconciliation.
3. **Scale-up:** only after a stated period and metrics, in small steps; automatic demotion back a stage on breach.
Prerequisites before stage 1: live adapter reviewed by QA and a security review; executor isolated; alerting tested; kill switch drilled; runbooks written.

## 9. Backlog (add to plan phases)
- [ ] Rule-based strategy runner and cost-aware backtester with turnover caps
- [ ] Trial registry plus DSR / MinTRL calculators
- [ ] Reconciliation job and idempotent order layer
- [ ] Guard v2: collars, rate limits, staged kill switch, rejection log
- [ ] Strategy decay monitor
- [ ] Isolated executor design and secrets plan (host with static IP?)
- [ ] Alerting to the owner; weekly review report in the control room
- [ ] Shadow-mode harness
- [ ] Legal/tax checklist for the owner's country

## 10. Decisions needed from the owner
Country; loss budget; whether to pay for an always-on static-IP host; paper starting capital; whether crypto perpetuals/leverage are permanently off (recommended); weekly review owner.

## 11. Unverified
Alpha Arena and contest figures are from news coverage, not primary data; FIA guidance is institutional, not retail; the vendor claims on paper-versus-live differences are unverified; tax and regulation details are country-specific and not checked.

## 12. Philippines reality check (owner is in the Philippines)
Full research: `docs/trader-platforms.md` (Nova, search snippets only, many third-party sources). Headlines:
- **Crypto:** the Philippine SEC and BSP are cracking down on offshore exchanges. Binance was blocked by the NTC in March 2024. The SEC named OKX, Bybit, KuCoin, Kraken, MEXC, Bitget and others as unregistered in an Aug 2025 advisory (ISP blocks followed for several); more platforms were flagged through April 2026; Coinbase and Gemini were reported blocked in late 2025. New crypto-service-provider rules took effect 5 July 2025. Do not use offshore exchanges for real money. BSP-licensed local venues are Coins.ph, PDAX and GoTyme (bank channel). Coins.ph has official trading API docs (HMAC-signed trade endpoints, key and IP permissions); whether keys can be trade-only with withdrawals off is unconfirmed; a Coins.ph licence-revocation rumour in Oct 2026 was denied by the company (verify newer news). PDAX API: nothing found.
- **US stocks/ETFs:** Interactive Brokers' official "Available Countries and Territories" pages list the Philippines (confirm which IBKR entity and funding route applies). Saxo (via Singapore) is a probable alternative. Alpaca says to ask support about a specific country; paper signup should simply be tried. Webull does not serve Philippine clients; Tradier looks excluded.
- **Local PSE brokers (COL, BPI Trade, First Metro):** no documented retail API found, and no paper API.
- **CFD/forex:** the SEC has acted against unauthorised platforms (Exness, HFM, XM). Out of scope.
- **Costs and tax (not advice):** PSE stock transaction tax reported cut from 0.6% to 0.1% (RA 12214, RR 20-2025); tax treatment of US-listed stock gains and of crypto is unsettled in the sources; US dividend withholding not checked; funding routes (Wise, GCash, Maya) unconfirmed. Get a Philippine tax professional.

### Recommended path for the Philippines
1. **Now: paper trading, no live account needed.** Our own simulator and backtester on free data (guaranteed to work anywhere); try Alpaca's free paper signup and Saxo's simulator for realistic order APIs. Crypto practice via simulator on public data; exchange testnets may not be reachable.
2. **Assisted live (recommended first real-money step):** Ledger produces signals and written reasoning, **you place the orders yourself** through a licensed venue (IBKR, a local broker app, or a BSP-licensed crypto app). No API keys on a live account, nothing automated, and it still exercises the whole learning loop with a human safety net.
3. **API live only later**, after: eligibility confirmed with the platform, a tax professional consulted, trade-only keys verified, an always-on static-IP host, the G1-G3 gates, and a stage-1 shadow period. Stocks via IBKR or Saxo first; crypto only via a BSP-licensed venue whose API supports trade-only keys.

### Quick checks you can do on your phone (official pages)
- Alpaca: try the free paper signup with your Philippine address, and ask support about live eligibility.
- IBKR: on the account-opening page, pick Philippines and see which entity, funding and withdrawal options it shows.
- Coins.ph: read the API docs and key-setup article; see whether a key can be limited to trading.
- Ask a Philippine tax professional how US-listed stock gains and crypto gains are taxed for you.
