# Ledger: information source catalog (research brief)

Author: Nova (researcher). Date: 2026-11-22. Education and research, not financial advice.
Scope: free internet sources Ledger can use for US stocks/ETFs and crypto spot, daily/weekly horizon, long-only, paper first, owner in the Philippines.
Method: WebSearch result summaries only (no full documents fetched). Anything marked UNVERIFIED rests on a snippet, a secondary blog, or my own background knowledge. Official pages must be re-checked before building. Free-tier limits change often.
Companion docs: `docs/trader-bot-plan.md`, `docs/trader-live-readiness.md`.

## Tier key
- A: official/primary (regulator, exchange, central bank, issuer filing)
- B: reputable secondary (aggregator/vendor with clear methodology, peer-reviewed or well-known research)
- C: social/unverified (can be gamed; use only as a risk flag, never as a trigger)
- D: avoid

## 1. Summary table

| # | Source | Category | Access | Tier | Point-in-time? | Evidence of value (daily/weekly) | Key risk | Link |
|---|---|---|---|---|---|---|---|---|
| 1 | SEC EDGAR (submissions, XBRL APIs, full-text) | Filings/fundamentals | Free JSON REST on data.sec.gov; max 10 req/s; must declare User-Agent | A | Yes: filing has an acceptance timestamp (UNVERIFIED in this research; known from EDGAR design). Restated XBRL "facts" need care | Filings/earnings are the primary event data; headline surprise is priced in fast (see PEAD) | Using latest-restated financials in backtests; rate-limit blocks | [SEC](https://www.sec.gov/edgar/searchedgar/accessing-edgar-data.htm) |
| 2 | Form 4 insider filings (via EDGAR) | Filings | Same as EDGAR | A | Yes (filing date); due within 2 business days (UNVERIFIED here) | Purchases: modest abnormal returns historically (~6%/yr in one study); sales weak. Older samples | Small/illiquid names, clustering with news | [Jeng et al.](https://scholar.harvard.edu/sites/scholar.harvard.edu/files/rzeckhauser/files/insider_trading.pdf) |
| 3 | Form 13F (via EDGAR) | Filings | Same | A | Yes but stale: due ~45 days after quarter end (UNVERIFIED here) | Stale by design; weak daily/weekly value | Treating old holdings as current | [SEC](https://www.sec.gov/edgar/searchedgar/accessing-edgar-data.htm) |
| 4 | Issuer earnings releases (8-K exhibits) | Filings | EDGAR | A | Yes | PEAD largely gone for non-microcaps since ~2006 | Gap risk around events | [Martineau](https://cfr.ivo-welch.info/published/papers/martineau2021rest.pdf) |
| 5 | PSE EDGE (Philippines) | Filings | Website/app; no documented API (none found); ~2 years retention; 4pm daily cut-off | A | Yes (disclosure timestamps on site; UNVERIFIED) | Completeness only; Ledger does not trade PSE | Scraping terms unchecked | [PSE EDGE](https://edge.pse.com.ph/page/faqs.do) |
| 6 | FRED / ALFRED API | Macro | Free API key; vintage data via `realtime_start/end` | A (aggregator of official series) | Yes via ALFRED vintages | Macro surprises move markets in minutes; regime context only | Using revised data as if known at the time; API terms (personal use free, attribution) | [FRED real-time](https://fred.stlouisfed.org/docs/api/fred/realtime_period.html) |
| 7 | Federal Reserve FOMC calendar/statements/minutes | Macro | Public web pages (and RSS, UNVERIFIED) | A | Yes (dated releases); minutes 3 weeks after meeting | Event-risk calendar (avoid new entries around events); content priced in fast | Misreading tentative dates | [Fed calendar](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm) |
| 8 | BLS (CPI, jobs) releases and API | Macro | Free; API v2 key limits not verified | A | Yes (scheduled release times) | Event calendar; surprises priced in minutes | API limits UNVERIFIED | UNVERIFIED (no BLS source retrieved) |
| 9 | BSP policy rate/Monetary Board dates | Macro (PH) | bsp.gov.ph | A | Yes | Context only. 2026 meetings reported: Feb 19, Mar 26 (off-cycle), Apr 23, Jun 18, Aug 27, Oct 22, Dec 17 | Secondary reports conflict on rate path; verify at BSP | [BSP MPR Jun 2026](https://www.bsp.gov.ph/SitePages/PriceStability/FullReportMPR/MonetaryPolicyReport-Full-June2026.aspx) |
| 10 | Yahoo Finance via yfinance | Price/volume | Free, unofficial library; personal use only per README; no SLA | B- (convenient, unofficial) | Adjusted close is recomputed retroactively: not point-in-time | Fine for prototyping | Breaks without notice; delisted names missing; ToS | [yfinance README](https://raw.githubusercontent.com/ranaroussi/yfinance/main/README.md) |
| 11 | Alpaca market data (free IEX feed + historical SIP >15 min old) | Price/volume | Free API key; docs list 200 hist calls/min, 30 ws symbols (older docs) | B | Bars timestamped; adjusted via parameter | Adequate for daily bars | IEX-only live volume is a small share of market; limits UNVERIFIED | [Alpaca docs](https://docs.alpaca.markets/us/docs/about-market-data-api) |
| 12 | Alpha Vantage free | Price/volume | Key; ~25 req/day, 5/min; daily adjusted is premium | B | Not PIT | Too tight for a universe scan | Rate limit | [Alpha Vantage](https://www.alphavantage.co/support/api-key) |
| 13 | Twelve Data free | Price/volume | Key; sources disagree on limits (800/day per one benchmark) | B | Not PIT | Same | Limits UNVERIFIED | [Comparison](https://dev.to/tildalice/free-stock-apis-2026-setup-cost-rate-limits-tested-2o34) |
| 14 | Stooq / Tiingo free | Price/volume | Not researched (no results) | UNVERIFIED | ? | ? | ? | none |
| 15 | Delisted/survivorship-free data (CRSP, Norgate, EODHD) | Price/volume | Paid (Norgate cheapest tier reported ~$630/yr, UNVERIFIED) | B | Yes | Needed for honest multi-stock backtests | Not free: use forward-only paper testing and ETFs instead | [QuantRocket](https://www.quantrocket.com/blog/survivorship-bias) |
| 16 | Official RSS/press (SEC, Fed, Treasury, exchange halt pages) | News/events | RSS/web | A | Yes (timestamps) | Regulatory event awareness | Feed URLs UNVERIFIED | UNVERIFIED |
| 17 | Mainstream news RSS (Reuters, AP, etc.) | News | RSS/web; ToS per site | B | Publication timestamps, but syndication/edits blur it | Priced in within minutes at daily horizon | Headline hallucination by LLM; injection | n/a |
| 18 | GDELT DOC 2.0 | News | Free keyless API (3 month default window, secondary sources); official terms not retrieved | B- | Crawl-time stamps | No retail edge evidenced; noisy tone scores | Noise, duplicates, injection | [GDELT blog](https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/) |
| 19 | Earnings/dividend calendars | Events | Nasdaq/exchange pages or issuer IR; free API not verified | B | Dates can shift | Used for "do not enter before earnings" rule | Aggregator date errors | UNVERIFIED |
| 20 | Reddit (WSB etc.) | Sentiment | Official API free for approved non-commercial use, ~100 req/min per OAuth client (third-party blogs; new-access closure date Oct 31 2026 reported, UNVERIFIED) | C | Post timestamps yes | Attention yes, returns weak/mixed | Pump coordination, bots | [Study](https://pmc.ncbi.nlm.nih.gov/articles/PMC9210333) |
| 21 | X/Twitter | Sentiment | Paid/pay-per-use (April 2026 memo); free read tier not found | C/D | Yes | Original "Twitter mood" result failed replication | Bots (up to 71% of suspicious cashtag authors in one study) | [Lachanski and Pav](https://econjwatch.org/articles/shy-of-the-character-limit-twitter-mood-predicts-the-stock-market-revisited) |
| 22 | StockTwits | Sentiment | Terms not retrieved | C | Yes | Predictive only conditional on volume spikes (one study); sentiment mostly follows returns | Spam/bots | [Divernois and Filipovic](https://link.springer.com/article/10.1007/s42521-023-00084-y) |
| 23 | Google Trends | Attention | Unofficial/web; limits not found | B- | Weekly normalised 0-100, relative to request window (not PIT stable) | Original strategy failed net of costs in later test | Re-scaling, revisions | [Bijl et al.](https://econpapers.repec.org/RePEc:eee:finana:v:45:y:2016:i:c:p:150-156) |
| 24 | CNN Fear and Greed index | Sentiment | Website; no official API found | B- | Daily; history may be revised (UNVERIFIED) | Mixed; weaker 2021-24; small effects | Composite of price-based inputs (circular) | [Farrell and O'Connor](https://ideas.repec.org/a/eee/finlet/v72y2025ics1544612324015216.html) |
| 25 | Crypto Fear and Greed (alternative.me) | Sentiment | Free keyless API; attribution required for commercial use | B- | Daily | No evidence retrieved; treat as context | Methodology opaque | [API docs](https://alternative.me/crypto/api/) |
| 26 | CoinGecko API (Demo) | Crypto data | Free key; current docs say 100 calls/min, 10k calls/month; older docs 30/min; attribution | B | Aggregated prices, not PIT | Reference price/volume | Aggregation; wash-traded venues | [CoinGecko](https://docs.coingecko.com/docs/errors-and-rate-limits) |
| 27 | Exchange public market data (Binance data-api.binance.vision, Kraken, Coinbase Exchange) | Crypto data | Keyless public REST; IP-based limits (Binance 429, then 418 ban); Kraken ~1 req/s | A for that venue's own prints | Yes (trade/candle timestamps) | Core price source for crypto | Binance geo/legal status in PH (see section 5d); Coinbase limits UNVERIFIED | [Binance docs](https://developers.binance.com/docs/binance-spot-api-docs/faqs/market_data_only) |
| 28 | DefiLlama stablecoins | Crypto data | Free keyless API (secondary sources; rate limits UNVERIFIED) | B | Daily snapshots | Context (liquidity); no predictive evidence retrieved | Peg/depeg data lag | [Listing](https://apis.io/apis/defillama/defillama-stablecoins-api/) |
| 29 | Glassnode / on-chain | Crypto data | Free plan is display-only per one review; API paid; conflicting | B- | Metrics get revised (UNVERIFIED) | Evidence mixed/thin; popular metrics are mostly promoted by vendors | Overfitting; paywall | [Glassnode](https://docs.glassnode.com/) |
| 30 | Bitcoin ETF flows (Farside etc.) | Crypto | Web tables | B- | Daily, after US close | Flows follow price (corr 0.54 with past 5d, 0.03 with next 5d, one market maker study) | Small sample, causal confusion | [Forklog on DWF](https://forklog.com/en/news/dwf-labs-questions-whether-etf-flows-predict-bitcoin-future-price-moves) |
| 31 | Funding rate / open interest (exchange public endpoints) | Crypto risk gauge | Public futures endpoints (not verified per exchange) | A for the venue | Yes | Descriptive risk gauge only; not shown to forecast cascades | Funding is 8-hourly; signals event-specific | [arXiv preprint](https://arxiv.org/pdf/2607.27070) |
| 32 | Sell-side analyst ratings | Analyst | Mostly paywalled; free aggregators scrape | C | Rating dates ok, aggregators lag | No direct evidence retrieved (gap) | Conflicts of interest | n/a |
| 33 | Earnings call transcripts | Analyst/alt | Free full set not found; Seeking Alpha used by one study via RapidAPI | B- | Call date known | LLM/FinBERT signals show alpha in papers (2%/month FF5 alpha, 2026 preprint; S&P study 8.4%/yr), not independently verified | Look-ahead in LLMs, crowding | [S&P](https://www.spglobal.com/market-intelligence/en/news-insights/research/2025/09/familiar-signal-new-context-from-lexicon-to-llm-the-evolution-of-earnings-call-nlp) |
| 34 | Research feeds: SSRN, arXiv q-fin, Quantpedia, NBER | Learning | Free abstracts (Quantpedia partly paid, UNVERIFIED) | B | Publication date known | Published anomalies shrink ~58% after publication | Data-mined findings | [McLean and Pontiff](https://ivey.uwo.ca/media/3775549/pontiff.pdf) |
| 35 | Telegram/Discord "signal" groups, influencer posts, unregistered advisors | Social | Public | D | n/a | Documented pump venues | Fraud | [SEC alert](https://investor.gov/additional-resources/news-alerts/alerts-bulletins/updated-investor-alert-social-media-investing-0) |

## 2. Per-source notes by category

### 2.1 Price/volume (category 1)
Facts (sourced):
- Free sources exist but are unofficial or limited. yfinance README says personal use only and tells users to check Yahoo's terms; Yahoo's official API was decommissioned in May 2017; no SLA ([yfinance](https://raw.githubusercontent.com/ranaroussi/yfinance/main/README.md), secondary: [plainenglish](https://python.plainenglish.io/yahoo-finance-api-in-2026-is-there-still-an-official-api-633d2b89a85d)).
- Alpaca free plan gives IEX-only real-time; historical SIP bars older than 15 minutes are available free; exceeding recent-SIP requests errors unless `feed=iex` ([Alpaca docs](https://docs.alpaca.markets/us/docs/about-market-data-api)). Limits quoted (200/min historical, 30 ws symbols) come from older docs.
- Alpha Vantage free: 25 requests/day ([official support page](https://www.alphavantage.co/support/api-key)); daily adjusted series reported premium-only by a secondary source.
- Survivorship bias: free sources rarely keep delisted names and effectively project today's index members backwards; membership history is a separate bias; both inflate backtest returns ([QuantRocket](https://www.quantrocket.com/blog/survivorship-bias), [QuantConnect forum](https://www.quantconnect.com/forum/discussion/21226/would-you-pay-for-cheap-point-in-time-s-amp-p-500-data-survivorship-bias-free/)).
Assumptions (unverified): adjusted close from free vendors is recomputed whenever a new dividend/split occurs, so a stored adjusted series can embed the future. Safe pattern: store raw OHLC plus the corporate-action table with dates, and derive adjustments as of each test date. My search did not return a source on this specific point.
Recommendation: backtest on liquid ETFs (survivorship matters little for broad index ETFs) and a fixed large-cap list; treat multi-stock backtests on free data as biased upward; prefer forward paper testing. Use two independent price sources and halt on disagreement.
Not researched: Stooq, Tiingo, Polygon free tier.

### 2.2 Filings and fundamentals (category 2)
- EDGAR: 10 requests/second per user across machines; declare a User-Agent; SEC may block excess IPs; submissions and XBRL are JSON on data.sec.gov; no tech support ([SEC](https://www.sec.gov/edgar/searchedgar/accessing-edgar-data.htm), [rate-control notice](https://www.sec.gov/oit/announcement/new-rate-control-limits)). Ledger should cache, stay far below the limit (assume 2-3 req/s) and put a contact string in the User-Agent (the owner's decision; do not publish personal details by default).
- Point-in-time: use the filing acceptance time as "known at"; do not use period-end dates. XBRL company facts can contain later restatements: key by filing accession. (Design advice, assumption.)
- Insider purchases: Jeng, Metrick and Zeckhauser report >6%/yr abnormal returns for purchases and no significant return for sales ([paper](https://scholar.harvard.edu/sites/scholar.harvard.edu/files/rzeckhauser/files/insider_trading.pdf)); Lakonishok and Lee: 4.8% after size/BM controls, stronger in small firms (secondary summary). Samples are old; costs not addressed. Later work disputes the sales finding ([Wintoki](https://www.wichita.edu/academics/business/accountancy/documents/InsiderTradingPatternsWintokiNov2016.pdf)).
- 13F is stale by construction (quarterly, ~45 days; UNVERIFIED in this research).
- PEAD: since 2006 analyst earnings surprises no longer predict post-announcement drift for most stocks; microcaps are the exception ([Martineau 2021](https://cfr.ivo-welch.info/published/papers/martineau2021rest.pdf)); a later study reruns it with and without microcaps ([UCLA Anderson summary](https://anderson-review.ucla.edu/is-post-earnings-announcement-drift-a-thing-again)). Net-of-cost drift: not found.
- PSE EDGE: official disclosure system, mandatory since 27 Dec 2013, 4pm daily cut-off, ~2 years retention on the site, push-notification app, no API found ([FAQ](https://edge.pse.com.ph/page/faqs.do), [About](https://edge.pse.com.ph/page/aboutPseEdge.do)). Not needed for Ledger's US/crypto scope.

### 2.3 Macro and central banks (category 3)
- FRED API supports `realtime_start/realtime_end` and ALFRED stores vintages; FRED release dates may differ from the source's actual release; API has separate terms: personal use free, attribution, series owners' rights apply ([docs](https://fred.stlouisfed.org/docs/api/fred/realtime_period.html), [terms](https://fred.stlouisfed.org/docs/api/terms_of_use.html)). Always query with a realtime window equal to the simulated date.
- FOMC 2026 meetings reported: Jan 27-28, Mar 17-18, Apr 28-29, Jun 16-17, Jul 28-29, Sep 15-16, Oct 27-28, Dec 8-9; minutes three weeks after the decision. Dates are tentative until confirmed; read the Fed page ([Fed](https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm)). Next one from today: 8-9 Dec 2026 (per that list; verify).
- BSP: reported 2026 Monetary Board meeting dates above; next is 17 Dec 2026. The reported rate path (hikes to 5.50% by Oct 2026) comes from conflicting secondary reports; verify at bsp.gov.ph.
- BLS/PSA schedules: not retrieved; use official calendars.
- Value: macro releases are scheduled risk events. Evidence that retail can profit from reacting is absent from my sources; the sensible use is "reduce/avoid new entries in the window around the event" (design suggestion, not a tested rule).

### 2.4 News and events (category 4)
- GDELT DOC 2.0 is reported keyless with a 3-month default window ([GDELT blog](https://blog.gdeltproject.org/gdelt-doc-2-0-api-debuts/), secondary summary). The only terms page found was for a different product (GDELT Cloud); the Project's own terms were not verified.
- RSS for SEC/Fed: not verified by search. Check official pages.
- Earnings/dividend calendars: no free official API verified. Use issuer IR and exchange pages as truth; treat aggregator dates as hints.
- Evidence: news content is largely priced within minutes; at daily horizon the signal-to-cost ratio is poor (see section 3).

### 2.5 Sentiment and attention (category 5)
Evidence summary:
- Tetlock (2007): high media pessimism predicts downward price pressure, then reversion; interpreted as noise-trader/liquidity effects, not new information ([paper](https://www.columbia.edu/~pt2238/papers/Tetlock_Media_Sentiment_JF.pdf)). García: content predictability concentrated in recessions.
- Twitter mood (Bollen et al.): 87.6% direction accuracy claim; Lachanski and Pav could not reproduce and found no out-of-sample aid; the hedge fund built on it (Derwent) closed in early 2012 ([Econ Journal Watch](https://econjwatch.org/articles/shy-of-the-character-limit-twitter-mood-predicts-the-stock-market-revisited)). Other work (Mao, Counts, Bollen; ECB paper) reports bullishness predicting increases followed by reversal.
- Reddit/WSB: attention effect on short-window trading; no significant link to abnormal returns in a GameStop study; WSB-following yields no alpha in one study; some 10-day predictability in a dissertation; many sources are theses/preprints ([PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9210333)).
- StockTwits: predictive only around volume spikes; sentiment largely follows returns ([Divernois and Filipovic](https://link.springer.com/article/10.1007/s42521-023-00084-y)).
- Google Trends: Preis et al. 2013 reported profits; Bijl et al. (2008-2013) found profit before costs, not after; ticker search volume predicted weekly returns/volume in another study ([Preis](https://www.nature.com/articles/srep01684), [Bijl](https://econpapers.repec.org/RePEc:eee:finana:v:45:y:2016:i:c:p:150-156), [Joseph et al.](https://wintoki.ku.edu/myssi/_pdf/Online_Search_Returns_IJF_preprint.pdf)).
- CNN Fear and Greed: Granger-causes index returns 2011-2020, weaker 2021-24 ([paper](https://ideas.repec.org/a/eee/finlet/v72y2025ics1544612324015216.html)); CXO finds small coefficients that frictions may offset ([CXO](https://www.cxoadvisory.com/sentiment-indicators/cnn-fear-and-greed-index-as-return-predictor)).
- LLM sentiment: Lopez-Lira and Tang report GPT-4 headline scores predict next-day returns on post-cutoff data, with returns declining as LLM adoption rises ([arXiv](https://arxiv.org/abs/2304.07619)); an independent paper warns of look-ahead contamination inside the model's training window ([arXiv](https://arxiv.org/pdf/2512.23847)).
- Access: Reddit free tier limited to approved non-commercial use; X now pay-per-use; both per secondary sources. Scraping against ToS is a no.

### 2.6 Crypto data (category 6)
- CoinGecko Demo: 100 calls/min, 10k/month on current pages; older pages 30/min; paid plans carry the commercial license; attribution requirement from a competitor's article only (UNVERIFIED) ([CoinGecko docs](https://docs.coingecko.com/docs/errors-and-rate-limits)).
- Binance public market data without keys at data-api.binance.vision; IP-based limits, 429 then 418 bans; a secondary source says api.binance.com is geo-restricted. Binance also publishes bulk history (data.binance.vision, referenced in the repo plan; archive terms not verified in this research). Philippine NTC blocked Binance in March 2024 (from `docs/trader-live-readiness.md`); reading public data is a different matter from trading but check legality and reachability.
- Kraken public REST: keep to about 1 request/second; 100-200 ms delays for bulk pulls ([Kraken docs](https://docs.kraken.com/exchange/guides/rest/ratelimits.md)). Coinbase Exchange market data is public with its own Market Data Terms; limits not retrieved.
- Stablecoin supply: DefiLlama free keyless API per secondary sources. No predictive evidence retrieved.
- On-chain (MVRV, SOPR, NUPL): popular but promoted mainly by vendors; peer-reviewed evidence thin ([thesis](https://osuva.uwasa.fi/bitstreams/6575b90c-6140-44e7-a798-011a1793d134/download), unreviewed). Glassnode free plan scope unclear.
- ETF flows: Mazur and Polyzos report flows strongly track price levels (R-squared 95%); DWF Labs finds flows follow trends and carry almost no information about next-5-day returns ([Cointelegraph](https://cointelegraph.com/news/bitcoin-etf-flows-follow-price-trends-dwf-labs)). Different questions; short-horizon forecast value weak.
- Funding/OI: descriptive leverage gauges; a preprint finds funding too coarse (8-hourly) and signals differ by event; positive funding stayed elevated before the Oct 2025 crash ([arXiv](https://arxiv.org/pdf/2607.27070), [BeInCrypto](https://beincrypto.com/liquidation-cascade-onchain-technical-analysis/)). Use as a "reduce size when leverage is extreme" flag, not a forecast. Spot-only Ledger does not trade perps.

### 2.7 Analysts, transcripts, alternative data (category 7)
- Transcripts: LLM-based tone signals reported to beat lexicon ones (8.4% vs 4.2% per year long-short, S&P Global study; FinBERT section-weighted alpha 2.03%/month in a 2026 arXiv paper). These are single-source, gross-of-cost claims; treat as hypotheses. Free full transcripts not found.
- Sell-side: one paper reports LLM-read analyst narratives forecast returns; evidence on plain upgrades/downgrades not found.
- Alternative data (web traffic, card data, satellite): not researched; generally paid; out of budget.

### 2.8 Research feeds (category 8)
- SSRN, arXiv q-fin and Quantpedia are learning sources, not trading triggers. McLean and Pontiff: across 97 predictors returns fall 26% out-of-sample and 58% post-publication ([paper](https://ivey.uwo.ca/media/3775549/pontiff.pdf)); Sharpe ratios roughly halve after publication per an arXiv paper ([2105.01380](https://arxiv.org/pdf/2105.01380)); one study finds the US is the only market with a reliable post-publication decline. Rule: any published edge enters Ledger as a pre-registered hypothesis and is haircut at least 50%.
- Bailey and Lopez de Prado (DSR, already cited in `docs/trader-live-readiness.md`).
- Not verified: Quantpedia's free/paid split, feed formats.

## 3. Evidence verdict: do public news/sentiment signals give retail an edge after costs?
Short answer: probably not a reliable one, at least not one Ledger can capture with free data at daily/weekly horizon. Supporting facts:
1. Where signals work, they decay quickly or reverse (Tetlock reversion; Bollen/Mao bullishness followed by reversal; LLM-headline strategy returns declining with LLM adoption).
2. Famous results failed out-of-sample or net of costs (Twitter mood replication failure; Google Trends profitable only before costs; PEAD gone for most stocks since 2006; Fear and Greed weaker after 2020).
3. Many studies ignore costs; the ones that include them show turnover control is decisive (tweet-based study with 6.4% annualized return and Sharpe near 2.2 after costs is one positive outlier; not independently verified).
4. Published predictors lose about half or more of their return after publication.
5. Public information is largely priced within minutes; Ledger acts on a daily cadence, so he sees stale news.
6. Real-money AI contests (see readiness doc) found fees and overtrading, not information scarcity, as the killer.
Exceptions to keep as hypotheses (not conclusions): insider purchase clusters in small caps, microcap drift (illiquid, costly), event-conditional StockTwits volume spikes, LLM transcript tone. All need pre-registration, point-in-time data and cost-aware testing.
Recommended role of news/sentiment for Ledger: veto and risk-flag (avoid earnings days, avoid pumped microcaps, reduce size around FOMC), not entry trigger.

## 4. Manipulation: how it works and red flags
Facts:
- Pump-and-dump: promoters spread positive rumours to incite buying, then quickly sell their own holdings; crypto versions use memecoins and "pre-sales" promoted on social media; not limited to microcaps ([SEC investor alert](https://investor.gov/additional-resources/news-alerts/alerts-bulletins/updated-investor-alert-social-media-investing-0), [crypto scams](https://www.investor.gov/introduction-investing/general-resources/news-alerts/alerts-bulletins/investor-alerts/crypto-scams)).
- Crypto pump groups: Hamrick et al. counted 952 pumps on Discord and 2,469 on Telegram in 6 months of 2018 (about 2,000 coins); Xu and Livshits studied 220 Telegram pumps (returns up to about 80% within three weeks); admins decide targets, members rarely vote ([Doge of Wall Street](https://arxiv.org/html/2105.00733v2), [Telegram study](https://arxiv.org/pdf/2609.01176)).
- Bots: Cresci et al. found up to 71% of suspicious cashtag-tweet authors were bots; "cashtag piggybacking" rides popular tickers to promote low-value ones ([arXiv](https://arxiv.org/pdf/1804.04406)).
- Philippine scam patterns flagged by SEC PH: unsolicited social-media offers, pressure to join Viber/WhatsApp/Telegram groups, repeated requests to pay more before withdrawal, impersonation of firms, AI/deepfake endorsements (July 2025), recovery scams ([Inquirer](https://business.inquirer.net/588168/sec-flags-fake-shopwise-platform), [MB](https://mb.com.ph/2025/07/14/sec-warns-of-ai-generated-investment-scams)).
Red flags for Ledger's guard (design suggestions):
- Sudden mention/volume spike in a thin name with no filing or earnings catalyst.
- Low market cap, low average dollar volume, wide spread, new ticker or new token.
- Coordinated, repeated, templated messages; new accounts; cashtag spam; "guaranteed" or countdown language; Telegram/Discord origin.
- Price already up a large amount within days (late entry is the target of the dump).
- Mitigation: whitelist of liquid ETFs/large caps (already in plan), minimum dollar-volume rule, and sentiment-spike-in-illiquid-name = automatic exclusion.

## 5. Legal and ethical limits
(a) MNPI/insider trading. Facts (secondary summaries of RA 8799): Section 27 of the Philippine Securities Regulation Code bars insiders trading with material non-public information and tipping; once information is publicly disclosed the insider-trading issue ends ([RA 8799 text](https://lawphil.net/statutes/repacts/ra2000/ra_8799_2000.html), [commentary](https://pnl-law.com/blog/?p=5661)). US law is analogous (assumption; not researched here). Rule for Ledger: only use information that is public and obtainable by anyone; never trade on leaked documents, private chat "tips", or data of unclear origin; if a source smells like a leak, drop it and log it.
(b) Scraping/ToS. Respect robots.txt and site terms; use official APIs; EDGAR needs declared User-Agent and <=10 req/s; yfinance is personal-use-only per its README; Reddit free API is non-commercial with approval; FRED needs attribution; CoinGecko free is non-commercial/attribution (UNVERIFIED). Redistribution of vendor data is generally prohibited. Keep Ledger a private personal research tool.
(c) Philippine retail cautions (not legal advice): crypto platform legality, BSP/SEC enforcement and the tax questions are covered in `docs/trader-live-readiness.md` section 12 (Binance blocked March 2024; several offshore exchanges flagged in 2025-26). Public market-data calls to a blocked exchange may fail or breach local rules; prefer Coinbase/Kraken public data or CoinGecko for reference prices and check. Beware Telegram "signal" sellers and AI-deepfake endorsements (SEC PH advisories above). Do not manage others' money. Tax treatment of US-listed stock and crypto gains for a Philippine resident is unverified; use a professional.
(d) Prompt injection and data poisoning when an LLM reads web content.
Facts:
- Indirect prompt injection (instructions hidden in pages/PDFs/emails) is OWASP's LLM01 risk; a Cloud Security Alliance note reports a 32% relative increase in malicious injection content on web pages between Nov 2025 and Feb 2026; adaptive attacks defeated several defenses ([MITRE T1698](https://attack.mitre.org/techniques/T1698/), [OWASP cheat sheet](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html), [CSA note](https://labs.cloudsecurityalliance.org/wp-content/uploads/2026/04/CSA_research_note_indirect_prompt_injection_in_the_wild_20260426-csa-styled.pdf)). No complete fix exists.
- Finance-specific: invisible-markup and Unicode-lookalike headline attacks on LLM trading cut annual returns by up to 17.7 percentage points in simulation ([Rizvani et al.](https://arxiv.org/html/2601.13082v1)); two other 2026 papers study fake-news injection and agent-data poisoning (snippets only) ([Fake News, Real Crashes](https://arxiv.org/pdf/2610.26438), [Poisoning Agentic Alpha](https://www.alphaxiv.org/abs/2608.24069)).
Standard mitigations (from MITRE/OWASP plus design advice):
- Least privilege: the reading step has no tools, no secrets, no order authority. Orders only via the deterministic guard (already in plan).
- Treat all fetched text as data, never instructions; delimit it; strip hidden HTML/markup, zero-width and lookalike Unicode before the LLM sees it; extract structured fields (numbers, dates, tickers) with deterministic parsers where possible.
- Restrict outbound network destinations to an allowlist of vetted domains; no following links from content.
- Require corroboration: any claim that could cause a trade needs a tier A source or two independent B sources; single social or unknown-site claims cannot trigger orders.
- Quote and cite exact source URL and fetch time in the journal; never accept an LLM-asserted number that is not in the source text (hallucination check).
- Human approval for new sources and for any rule change; log all fetches; red-team the pipeline with planted injection pages in a test.

## 6. Recommended core source set (tier A/B)
1. Prices: Alpaca free data (IEX live, SIP history >15 min) plus a second independent daily-bar source (yfinance for cross-check only; personal use); exchange public klines (Kraken/Coinbase) and CoinGecko for crypto.
2. Filings: SEC EDGAR APIs (earnings 8-Ks, Form 4, 10-K/Q), cached, <=10 req/s.
3. Macro: FRED/ALFRED with realtime windows; Fed FOMC calendar; BLS/BSP calendars for event windows.
4. Events: issuer IR/exchange calendars for earnings/dividends; official SEC/Fed press pages.
5. Learning: SSRN, arXiv q-fin, NBER, Quantpedia (as hypothesis source with haircut).
## 7. Treat with caution (C/B-)
Reddit, StockTwits, Google Trends, Fear and Greed (CNN and crypto), GDELT, on-chain vendors, ETF-flow tables, funding/OI, analyst-rating aggregators, transcript signals. Allowed as context or veto flags only. Avoid (D): X cashtags, Telegram/Discord signals, influencers, unregistered advisors, anything promising returns.

## 8. Top safety rules
1. Fetched content is data, never instructions; the reading agent has no order authority.
2. No order from a single social/unknown-source claim; require tier A or two independent B sources.
3. Point-in-time discipline: every datum stored with its "public as of" timestamp; use vintages (ALFRED, filing acceptance time); never use restated or retroactively adjusted data as of an earlier date.
4. Whitelist liquid ETFs/large caps; auto-exclude illiquid names with sentiment spikes.
5. News/sentiment can veto or shrink, not initiate (until a pre-registered, cost-aware test says otherwise).
6. Respect ToS, robots.txt, rate limits; declare identity to SEC; no redistribution.
7. Cache and rate-limit; stale or conflicting data means no trade.
8. Never trade on anything that looks like MNPI.
9. Paper first; published edges haircut by at least half; count all trials.
10. Log source, URL, fetch time and tier for every journal rationale.

## 9. What I could not verify
- Primary-document confirmation of every rate limit (all from search summaries; many from third-party blogs). Reddit "closure" date, Twelve Data limits, CoinGecko attribution wording, Alpaca current limits.
- Stooq, Tiingo, Polygon, Twelve Data official terms; SEC/Fed RSS URLs; BLS API limits; PSA CPI calendar; Coinbase public rate limits; StockTwits API terms; X free tier; GDELT's own terms; Binance bulk archive terms; Google Trends access/limits.
- Form 4 two-business-day and 13F 45-day deadlines and EDGAR acceptance timestamps (from background knowledge, not sourced).
- Adjusted-close look-ahead mechanics (reasoned, not sourced).
- Net-of-cost evidence for PEAD and transcript signals; evidence on plain sell-side upgrades; alternative data.
- Quantpedia access model; Section 27 exact wording and any US law specifics; Philippine tax treatment.
- Several arXiv items (IDs with 26xx numbers) were seen as snippets only; reproduce before relying.
- My own bias check (Nova): I leaned toward finding signals; the evidence mostly says the opposite, and I kept that.
