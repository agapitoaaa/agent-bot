# Platform research for Ledger (paper first, real money only later with separate human approval)

Author: Nova (researcher). Date: 2026-11-22. Not financial or legal advice.

## Method and honesty notes
- Method: about 19 WebSearch queries. I saw search-result summaries and snippets only. I did NOT open full pages. Every claim below is therefore "S" (seen in a search result, with the source named) or "U" (unverified or conflicting). Sources are mostly official docs, but several are third-party blogs, which I flag.
- Most official pages carry no date in the snippets. I give a date only when one was shown (PDT rule: April 2026. Webull: 21 Jul 2026. Alpaca crypto regions: 9 Oct 2025).
- The human's country is unknown. Region availability is the biggest gap. Almost none of the country lists were retrievable from official pages.
- Nothing here is a recommendation to trade. Ledger's plan keeps paper-only as the default and real money behind gate G4.

## 0. PHILIPPINES (priority section; the human lives in the Philippines)
This section supersedes the generic shortlists in section 5 wherever they conflict. Sources are search snippets (second batch of 8 searches, 2026-11-22). Many are comparison/affiliate sites, flagged "(3rd-party)". I did not open IBKR's or Alpaca's official country lists. Eligibility is therefore "likely" or "unconfirmed", never "confirmed", unless stated.

### 0.1 Headline findings
1. The Philippine SEC and BSP are actively cracking down on offshore crypto exchanges. Coinbase and Gemini were reported blocked at ISP level in late 2025 (S: Cointelegraph/Yahoo/CCN, month not seen). Binance was blocked by the NTC on 25 Mar 2024 (S: Philippine SEC press release 29 Nov 2023 plus news). The SEC named OKX, Bybit, MEXC, KuCoin, Bitget, Phemex, CoinEx, BitMart, Poloniex and Kraken as unregistered in an advisory dated 4 Aug 2025 (S: Philstar 6 Aug 2025, Cointelegraph, Manila Bulletin 7 Aug 2025). Whether each is blocked is mixed. Using them is a legal-status and fund-access risk, and I would not build Ledger on them.
2. For crypto, the realistic live options are BSP-licensed local VASPs (Coins.ph, PDAX, GoTyme Bank via Alpaca). Practice crypto should be on a testnet or local simulator, where the testnet itself does not require a live account (Binance Spot Testnet access from the Philippines is unconfirmed, since the main site is blocked).
3. For US stocks, the credible route is Interactive Brokers (likely accepts Philippine residents, 3rd-party sources agree but one conflicts, IBKR official list not read), with Alpaca live uncertain.
4. No local PSE broker I found offers a documented retail API.

### 0.2 Philippine resident eligibility, by platform

| Platform | Philippine resident can open LIVE? | DEMO/paper from PH? | Evidence and confidence |
|---|---|---|---|
| Interactive Brokers | LIKELY YES. 3rd-party comparison sites say IBKR serves Philippine residents through overseas entities (S, 3rd-party: comparebroker, investingintheweb, QuantWheel). One 3rd-party page (BrokerChooser, Ukrainian version) says it does NOT accept Philippine clients (conflict). IBKR's official country list page and FAQ exist (interactivebrokers.ca open-account-country-list, FAQ 28216848) but the snippets did not show the Philippines. | Paper account requires a funded, fully open live account (S: IBKR docs). So demo is only available after live onboarding and funding. | Medium-low. Must confirm on IBKR's official list at signup. |
| Alpaca | UNCONFIRMED. Alpaca's non-US program was invite-only beta and "limited basis" (S: Alpaca blog, date not seen). Minimum deposit lifted (S: Alpaca support). Official "Countries Alpaca is available" page is dated Feb 2026 but the list was not visible to me. Country is based on the physical address entered (S: Alpaca forum staff). Separate: GoTyme Bank (Philippines) offers crypto via Alpaca's Broker API, a bank-channel product, not a direct account (S: Alpaca blog). | Paper availability for PH: UNCONFIRMED (earlier plan note says open globally, not re-verified). Try signing up for a paper account, which is free to test. | Low. Most important single check: Alpaca's official country page. |
| Tradier | NO / UNLIKELY. US-focused brokerage (U). Not named for the Philippines in any result. | Sandbox comes with a brokerage account, so not available without one (S: Tradier docs). | Low confidence, treat as excluded. |
| TradeStation | UNCONFIRMED. One 3rd-party aggregator lists it among brokers opening accounts for Philippine residents (S, 3rd-party, QuantWheel), with possible citizenship/visa checks. | SIM API requires API access via their business team or individual page (S). | Low. |
| tastytrade | UNCONFIRMED. 3rd-party lists say tastytrade opens options accounts for Philippine residents (S, 3rd-party, QuantWheel). | Sandbox is a separate cert registration (S: tastytrade docs), may be usable regardless of country, unconfirmed. | Low. |
| Schwab | UNLIKELY. Trader API requires a Schwab retail account and Schwab's international access is limited (U). A 3rd-party "Schwab Philippines" page exists but its content was not read. | No paper API. | Low. |
| Webull | NO. Two 3rd-party sources say Webull does not accept Philippine clients (S, BrokerChooser) and has no plan to return. | Webull OpenAPI paper launched Jul 2026 (S: PR Newswire) but country eligibility unknown. | Medium (3rd-party). |
| Trading 212 | UNCONFIRMED, probably NO. No source confirmed Philippine residents (only generic broker lists). It is a UK/EU-focused broker, and its API only works for Invest and ISA accounts (S: T212 docs). | Practice mode needs an account (U). | Low. |
| Saxo | PROBABLY YES via Saxo Markets Singapore, MAS-regulated (S, 3rd-party guide). Official page not read. Saxo's SIM environment is free, $100k, 24-hour token (S: Saxo docs). | SIM usable by developers who register for a simulation account (S: Saxo docs), country limits unknown. | Medium-low. Good fallback for stocks via API, minimums and fees unknown. |
| IG | UNCONFIRMED. One 3rd-party review says Philippine residents are served by offshore entities, another names IG International (Bermuda) (S, conflicting). Mostly CFD/spread-bet, so a poor fit and a regulatory-risk area (see 0.4). | Demo + API key (S). | Low. Skip. |
| OANDA | UNCONFIRMED. A review says entity differs by country, and I found none naming the entity for PH (S, 3rd-party). FX/CFD only. | Practice API (S). | Low. Skip (out of scope markets). |
| Binance | EFFECTIVELY NO. NTC ordered ISPs to block it on 25 Mar 2024 after the SEC warning of 29 Nov 2023 (S). Binance claimed it was licensed (S, Binance promotional content, conflicts). | Spot Testnet is a separate host and may still resolve (U), but using an exchange that regulators have warned against for later live use is not advisable. | High on regulatory status; unknown on testnet reachability. |
| Bybit | NO / HIGH RISK. Named in SEC advisory 4 Aug 2025 (S). | Demo/testnet reachability unknown (U). | High on status. |
| OKX | NO / HIGH RISK. Named in SEC advisory 4 Aug 2025 (S). | Demo reachability unknown (U). | High on status. |
| Kraken | NO / HIGH RISK. Named in SEC advisory 4 Aug 2025 (S). ISP block not confirmed in my results. PHP support limited (S, 2024-era guide). | No self-service spot sandbox anyway (see section 2). | High on status. |
| Coinbase | NO. Reported blocked in the Philippines in late 2025 (S: Cointelegraph, Yahoo, CCN). | Sandbox is mocked and static, not useful. | Medium-high, month not seen. |
| Gemini | NO. Reported blocked together with Coinbase (S, same sources). | Sandbox would be separate site, reachability unknown. | Medium-high. |
| Coins.ph | YES for Filipino residents (local). BSP-licensed: VASP and EMI licences from 2017 (S: BitPinas, BusinessWorld), plus an Advanced EPFS licence (S). Live risk: a Cointelegraph item dated 14 Oct 2026 reports Coins.ph saying its licence is intact amid reports of possible revocation linked to alleged offshore-gambling flows (S, snippet, verify newer news). | No demo mentioned in results (U). | Medium. |
| PDAX | YES, local, BSP-licensed non-bank VASP, licence dated Sept 2018 (S: BitPinas, undated list). Type A EPFS claim since Dec 2021 is unverified. | No demo found (U). | Medium. |
| GoTyme Bank (crypto via Alpaca) | YES, bank-channel crypto product on the BSP list ("14 licensed VASPs" per a report; several inactive) (S: Alpaca blog, CoinGeek). | No demo found. | Medium-low. |

BSP context (S): the BSP extended its moratorium on new VASP licences indefinitely (reported Sept 2025, Philstar/GMA). In June 2026 it ordered licensed VASPs to stop listing privacy coins and tightened listing oversight (S: Philstar/Manila Bulletin 12-14 Jun 2026). Crypto is a moving regulatory target here.

API for local crypto venues: CoinGecko lists Coins.ph as supporting trading via API/websocket/orderbook (S, 3rd-party aggregator). No official Coins.ph or PDAX developer docs were seen, so API availability, key permissions (withdraw-off), rate limits and testnet are UNCONFIRMED. This is the key unknown for the crypto live path.

### 0.3 Local Philippine Stock Exchange (PSE) brokers
- COL Financial: a 3rd-party review says no API or algorithmic trading, web and mobile only (S, forexpeacearmy, 3rd-party).
- BPI Trade: retail platform, no API mentioned (S, snippets).
- First Metro Securities: only institutional connectivity via SunGard, a 2010s-era report, no retail API (S, old).
- A BrokerChooser ranking praised an unnamed local broker for API trading, and QuantWheel lists "3 brokers with API for Philippine residents" but names only IBKR (S, 3rd-party). I found NO local PSE broker with a documented retail trading API. Ask COL/BPI/First Metro directly. Local PSE brokers also have no known paper-trading API (U).
- Local brokers may require a Philippine TIN and residency (S, 3rd-party guide).

### 0.4 Regulatory status: forex/CFD and crypto
- The SEC has issued advisories and orders against unauthorised CFD/forex-style platforms: Exness Global and HFM flagged Jan 2026 (S: Manila Bulletin 8 Jan 2026), XM cease-and-desist Dec 2025 (S: Manila Bulletin 12 Dec 2025). I found no formal rulebook for retail forex/CFD, only enforcement. Treat CFD/forex brokers (IG, OANDA, others) as a risk area, and out of scope for Ledger (no leverage anyway).
- Crypto: SEC advisory 4 Aug 2025 on 10 platforms (S); NTC block of Binance 25 Mar 2024 (S); Coinbase/Gemini blocks late 2025 (S). Official SEC/BSP lists were not opened. Check sec.gov.ph and the BSP VASP directory directly.
- Consequence for the plan: use only BSP-licensed venues for any later real-money crypto, and treat offshore exchanges as not usable.

### 0.5 Tax and cost basics (awareness only, not tax advice)
- PSE stock transaction tax: cut from 0.6% to 0.1% of gross selling price by RA 12214 (CMEPA), signed May 2025, implemented by RR 20-2025 (dated 5 Aug 2025 per Grant Thornton). The selling broker collects and remits it (S: DOF, PwC, Grant Thornton). RR 20-2025 also applies the STT to domestic shares listed and traded on a foreign exchange (S: PwC).
- Foreign listed stocks (e.g., US stocks sold on a foreign exchange): the 15% flat rate applies to unlisted shares of domestic or foreign corporations (S: PwC). Shares sold through a local or foreign exchange fall outside that rule. The tax treatment of gains from US-listed shares held by a Philippine resident is NOT settled in my results. Unverified, needs a BIR-aware tax professional.
- Crypto: no crypto-specific tax law; sources conflict (ordinary income vs a possible 15% rate) (S, 3rd-party guides). The Philippines is reported to begin automatic crypto tax data exchange in 2028 per the OECD (S: Manila Bulletin 9 Jun 2026).
- Withholding on foreign brokers (e.g., US withholding on dividends, W-8BEN treaty rate) was not searched. UNVERIFIED.
- Funding routes: IBKR allows funding and withdrawal via Wise, but only for certain IBKR entities (IBLLC, IB-UK, IBIE, IB-HK, IB-AU, IB-SG) (S: IBKR docs). Which entity serves PH is unconfirmed. Bank wires cost conversion plus the Philippine bank's USD wire fee (S, anecdotal forum, undated). IBKR gives 1-2 free withdrawals per month depending on entity, then a fee of about USD 4 on a US page (S, other entities' pages, not confirmed for PH). GCash/Maya funding of IBKR or Alpaca: NOT confirmed. Coins.ph funds via local e-wallet/bank rails (U, not explicitly checked, a likely benefit).

### 0.6 Philippines ranked shortlist (updated)
US equities/ETFs, demo practice:
1. Alpaca paper (if PH signup is allowed, check immediately, it is free to test).
2. Saxo SIM (free $100k, 24-hour tokens, so more manual) if the Singapore entity lets a PH developer register.
3. IBKR paper (requires a funded live account first, so it is a commitment).
4. Local simulator (Lumibot/NautilusTrader/our own) as a guaranteed fallback.

US equities/ETFs, real money LATER (separate approval, G4):
1. Interactive Brokers (best-supported, likely accepts PH residents, wide markets, mature). Confirm entity, Pro tier for API, funding via Wise or wire, and W-8BEN/withholding.
2. Saxo (Singapore entity) as a second option, minimums unknown.
3. Alpaca live only if its official list includes PH. Do not assume.
4. Local PSE brokers (COL etc.) only for manual investing, no API.

Crypto, demo practice:
1. Local simulator and public historical data (Binance public data via market-data only, not an account), because no PH-legal exchange with a known sandbox was found.
2. Exchange testnets (Binance Spot Testnet, Bybit testnet, OKX demo, Gemini sandbox) only as technical tests of order plumbing, with the reachability from the Philippines UNCONFIRMED and with the caveat that those exchanges are regulatory-flagged. Using a testnet does not itself trade money, but keep real accounts away.

Crypto, real money LATER:
1. Coins.ph or PDAX (BSP-licensed), IF they offer an official API with trade-only, no-withdrawal keys (unconfirmed, could be a deal-breaker). Check Coins.ph licence status first (Oct 2026 revocation reports).
2. GoTyme Bank crypto (via Alpaca): consumer app channel, probably no API for us.
3. Offshore exchanges (Binance, Bybit, OKX, Kraken, Coinbase, Gemini): not recommended given SEC/NTC/BSP actions.

Recommendation in one line: for Ledger the practical Philippines path is US equities via an IBKR (or Alpaca if eligible) account, with crypto deferred or limited to a local simulator until a licensed local venue shows an API.

### 0.7 Philippines unknowns (checks before any build)
1. Alpaca official country page: does it include the Philippines for paper and for live?
2. IBKR official country list: Philippines accepted? Which entity, which funding route (Wise/wire/GCash), PH withdrawal fees.
3. Coins.ph and PDAX: official API docs, key permissions, testnet, current licence status.
4. BIR tax treatment of US-listed stocks and crypto, and US dividend withholding (W-8BEN).

---

## 1. Comparison table (US equities/ETFs and general brokers)

| Platform | Markets | Demo/paper | Live API | Region notes | Key security | Constraints and maturity |
|---|---|---|---|---|---|---|
| Alpaca | US stocks/ETFs, options, select crypto | Free paper API, separate keys and host `paper-api.alpaca.markets` (S: Alpaca docs). Paper-only accounts get IEX data only (S: Alpaca docs). Fills use marketable-price logic, about 10% random partial fills, no market impact, queue, latency, dividends or fee modelling, and no size-vs-liquidity check (S: Alpaca docs via search). Forum reports of fill delays of 50-260 s (S: forum, user report). | Official REST/WebSocket. Commission-free stocks (S). Crypto has small per-trade fees (S). Non-US individual live accounts: $30k minimum lifted, "as little as $1" (S: Alpaca support), but older forum posts say non-US individuals were unsupported or waitlisted (S, possibly outdated). Country list exists on an Alpaca support page dated Feb 2026 but I could not read it (U). | Paper eligibility for non-US: U (my earlier plan note said "open globally", not re-confirmed). Crypto live is limited to certain US states, list updated 9 Oct 2025 but not retrieved (S/U). | Separate paper/live keys (S). Trading OAuth scopes exist (S). IP allowlisting: conflicting (broker API yes, Trading API unclear) (U). No documented trade-only vs withdrawal key split in what I saw (U). | Funding/regulation: US broker-dealer; SIPC not confirmed in my results (U). PDT: see section 4. Well-known API-first broker, raised $52M Series C in Apr 2025 (S: TechCrunch). |
| Interactive Brokers (IBKR) | Global stocks, ETFs, options, futures, FX, crypto (via partner) | Free paper account with its own login. API treats paper and live the same (S: IBKR docs). Paper uses "more simulated technologies" than live (S: IBKR TWS docs). Delayed data by default for paper (S, third-party blog). Live account must be fully open and funded to use paper API (S: IBKR docs). | Official TWS API (socket) and Trading Web API. Web API limit 10 req/s per session, 429 on excess, some endpoints tighter (S: IBKR docs). TWS API about 50 orders/s, 3 pacing violations can end the session (S, one source). Needs IBKR Pro, not Lite (S). | Wide international coverage. Country exclusions and API-by-country: U. | 2FA required (IB Key) (S). Weekly re-auth reported by QuantConnect for live (S, third-party). Gateway must stay running, awkward for unattended agents. Key-level trade-only permissions: U. | Large, mature, widely used. Minimum deposit and fees vary by region (U). Complex setup. |
| Tradier | US stocks, ETFs, options | Sandbox included with every brokerage account, no extra cost. Delayed data, simulated trades (S: Tradier docs). Account activity not available in paper (S: QuantConnect). Base URL discrepancy between sources (U). | Official REST API at no extra charge (S). Hosted MCP server reportedly launched July 2026 with PAPER_TRADING flag (S, snippet). | US-focused. Likely US residents only for brokerage (U). | Sandbox and prod tokens are not interchangeable, 401 on mismatch (S). Other key features: U. | Needs a US brokerage account. Fees and minimums: U. |
| TradeStation | US stocks, options, futures, crypto | SIM API identical to live except fake accounts, `sim-api.tradestation.com/v3` (S: TradeStation docs). Third-party reports inaccurate sim fills, especially options (S, blog). | Official v3 API, OAuth 2.0 (S). Individual API access via a separate page on tradestation.com (S). | Mostly US. Exclusions: U. | OAuth2 (S). Trade-only scopes and IP lists: U. | Established US broker. Fees and rate limits: U. |
| tastytrade | US stocks, options, futures, crypto | Sandbox is the "certification" environment `api.cert.tastyworks.com`, 15-minute delayed quotes, separate credentials, resets about every 24 h (S: tastytrade docs/listing). Custom fill simulation (fill, partial, live) (S). A third-party SDK author calls it of limited use for testing (S, competitor view). | Official Open API, no extra cost with an account (S, listing, text cut). OAuth2 (S). IP block of about 8 hours on abuse (S). | US-centric. Exclusions: U. | OAuth2 with refresh tokens (S). Scopes: U. | Options-centric broker. Sandbox is more for integration testing than market realism. |
| Schwab / thinkorswim | US stocks, ETFs, options | No official paper API found (U). thinkorswim desktop has paperMoney but that is not the Trader API (U, not searched). | Official Trader API, Individual tier for own account. Two separate approvals (developer account, then Trader API access), needs a Schwab retail self-directed account (S: third-party guides, not Schwab). | US residents with Schwab accounts. International: U. | OAuth, re-authorization rules: U. | Old TD Ameritrade credentials do not carry over (S). No paper = cannot practise via API here. Approval times unknown. |
| Webull | US stocks, ETFs, options, others | OpenAPI paper trading launched, 21 Jul 2026 press release (S: PR Newswire). Sandbox access approved in minutes, live in 1-2 business days (S, third-party QuantVPS). April 2026 GitHub issue about missing paper account in API response (S, one user). | Official OpenAPI exists (S). Rates and fees: U. | Webull operates in a limited set of countries, EU only Netherlands per affiliate sites (S, weak). OpenAPI by country: U. | Not retrieved. | New (2026) paper API, immature. |
| Trading 212 | EU/UK stocks, ETFs, also US-listed | Practice (demo) environment with separate keys, demo base URL reported `demo.trading212.com/api/v0` (S, third-party; U). API v0 is beta (S, third-party dated Sept 2026). | Official public API, Invest and Stocks ISA accounts only (S: T212 docs). Live only supports market orders via API (S). Per-endpoint per-account limits, e.g. 1 request per 30 s on account info, 50 pending orders per ticker (S: T212 docs). | Primarily UK/EU. US residents not served (U). | Keys tied to environment (S). IP restriction optional (S: T212 help). Permission categories (account, history, orders, portfolio) (S). Market-only live orders limit strategies. A user reported 401 errors on ISA (S). | Beta. Account protection (e.g. FSCS or equivalent) not confirmed in my results (U). |
| Saxo (OpenAPI) | Global stocks, ETFs, FX, CFDs, futures | Simulation environment, copy of live with $100,000 simulated, 24-hour token from developer portal (S: Saxo docs). Reporting and some market data not available in SIM (S). | Official OpenAPI. Live requires an approved app and full OAuth flow (S). Minimums and fees: U. | Europe/APAC focus. Country exclusions (US likely excluded): U. | OAuth (S). | Well-regarded mature API. 24-hour token is awkward for unattended runs, needs OAuth for longer. |
| IG | Spread bets, CFDs, FX, indices | Demo account with demo API key (S). | Official REST + streaming API. Limits: 60 non-trading req/min per app, 30 non-trading per account, 100 trading/min per account, 10,000 historical points per week (S: IG Labs FAQ). A UK page says around 40 trade requests/min (S, conflict). Demo limits are lower than live (S, third-party). | UK/EU/APAC. CFDs and spread bets are restricted or banned for retail in some places incl. the US (S, general knowledge, U for specifics). | Not retrieved. | Not suited for US stocks and ETFs. Leveraged products: poor fit for Ledger rules (no leverage). Probably skip. |
| OANDA | FX, some CFDs | v20 "fxTrade Practice" at `api-fxpractice.oanda.com`, live at `api-fxtrade.oanda.com` (S: OANDA docs). | v20 available to all divisions except OANDA Global Markets and OANDA TMS BROKERS S.A. (S). | See left. | Token-based (S). | FX/CFD, not stocks. Out of scope for the chosen markets. |

## 2. Crypto

| Platform | Demo/paper | Live API | Region notes | Key security | Notes |
|---|---|---|---|---|---|
| Binance (Spot) | Spot Testnet with free test funds, separate keys (S: Binance docs). Only `/api` endpoints, not `/sapi` (S). Resets roughly monthly, keys preserved since Aug 2020 (S: legacy docs). Prices and liquidity are not representative (S, common knowledge, flag as assumption). | Official REST/WebSocket. Fees, limits: U. | Binance.com prohibits the United States (prohibited list dated Feb 2024, may be stale) (S). Binance.US is a separate entity with a state list (NY, TX, WA, others named inconsistently) (S, mixed). Binance.US testnet: not found (U). | Ed25519 or HMAC keys (S). Key endpoint-type limits (S). IP restriction encouraged and required to enable withdrawals (S: Binance Academy). Trade-only key: standard feature, testnet-specific page not seen (U). | Best-documented testnet. The country issue is decisive. |
| Coinbase (Advanced Trade) | Sandbox at `api-sandbox.coinbase.com` is static and mocked, no auth, canned responses, only Accounts and Orders endpoints (maybe a few more) (S: Coinbase docs). It is NOT a realistic paper trading venue. Coinbase Exchange sandbox: U. | Official REST/WebSocket. Fees, limits: U. | Region: U (US, EU, UK and others have local offerings, not verified). | Key permission levels View / Trade / Transfer, plus portfolio scoping and IP allowlist (S: Coinbase docs). This is the clearest trade-only plus IP-allowlist feature set seen. | Good live security, weak practice. Pair with a local simulator. |
| Kraken | Futures demo at `demo-futures.kraken.com`, identical API to prod, resets periodically (S: new docs). But a support article says that demo was decommissioned and a qualified-client environment exists on request (S, conflict, U). Spot UAT is on request via account manager only (S). No self-service spot paper trading found (S). | Official Spot REST/WS API. | Region: U. Futures are derivatives and out of Ledger's phase-1 rules anyway. | Granular permissions: Query Funds, Query Orders, Create/Modify, Cancel; "Withdraw Funds" separate and can be left off (S: Kraken docs). Websocket access permission (S). | Strong key model, no usable free spot sandbox. |
| Bybit | Two options. Demo Trading uses production infra with virtual funds, keys for `api-demo.bybit.com`, not every API supported, demo orders kept 7 days (S: Bybit docs). Testnet is a separate environment at `api-testnet.bybit.com`, full features, new users may wait 48 h to create keys (S). | Official V5 API. Fees, limits: U. | Country availability: not found (U). Bybit has restricted several jurisdictions in the past (assumption, U). | Not retrieved (U). | Good parity but verify jurisdiction first. |
| OKX | Demo trading uses the live host with header `x-simulated-trading: 1` and a demo-specific API key (S: OKX FAQ). Demo websocket URLs differ (S). Feature limits: U. | Official V5 API. | Region: U. OKX has EEA-specific API FAQ pages (S), implying regional variants. | Third-party claim that trade keys without an IP binding are deleted after 14 days idle (U). | Practical, switchable demo. |
| Gemini | Separate sandbox site and separate account, `exchange.sandbox.gemini.com`, full functionality with test funds, independent prices and volume, no deposits or withdrawals (S: Gemini docs). | Official REST/WS API. | Region: U. | Role-based key permissions set per key, Trader role by default, recommend one key per app (S). | Easy and safe sandbox, but low-liquidity test book. |

## 3. Vendor-neutral options
- CCXT: `set_sandbox_mode(true)` swaps endpoints to a testnet only where the exchange has one. It errors where none exists (for example Bitstamp). Binance, Bybit and Coinbase are cited as supported. Sandbox usually needs different keys. Authoritative per-exchange list not retrieved. Check `exchange.has['sandbox']` and the version in use (S: CCXT docs/manual via search; U on the list). CCXT is crypto-focused, not a stock-broker abstraction.
- Open-source simulators and engines (maintenance status NOT verified, check GitHub activity before depending on them):
  - NautilusTrader: event-driven backtester with backtest/live code parity (S: project descriptions).
  - Lumibot: backtest and paper (`--paper`) on the same strategy code, GPL v3 (S: PyPI page).
  - LEAN (QuantConnect): open source, multi-asset, backtest and live (S).
  - Others seen in listings: StockSharp, Jesse, Blankly (S: SourceForge, weak).
  - Freqtrade dry-run: not confirmed in my results (U).
- A local simulator that Ledger controls fully (own fills, fees, slippage) is a strong complement because broker paper fills are known to be optimistic (Alpaca's own limits list above).

## 4. Constraints and rules worth knowing
- US Pattern Day Trader rule (US margin accounts): FINRA's amendments, approved by the SEC on 14-15 April 2026, effective 4 June 2026, replace the day-trading margin framework with an "intraday margin" standard. They remove the "pattern day trader" designation and the four-trades-in-five-days test (S: FINRA weekly archive 22 Apr 2026, FINRA Notice 26-10, Schwab, King & Spalding). E*TRADE's summary says the new minimum is $2,000, which I could not confirm against FINRA text (U). Brokers may implement on their own timeline (assumption). Ledger plans a swing/daily horizon with no leverage, so this rarely binds.
- Account types: Interactive Brokers needs Pro for the API (S). Trading 212 API only for Invest and Stocks ISA (S). Schwab needs a retail self-directed account (S).
- Practice vs live key separation is universal and is a useful safety feature: a paper key cannot move real money. Alpaca, Tradier, tastytrade and Trading 212 all state tokens or keys are environment-specific (S).

## 5. Ranked shortlists (generic, country-unknown; SUPERSEDED by section 0.6 for the Philippines. Coinbase, Kraken, Binance, Bybit, OKX, Gemini rankings below ignore Philippine blocks.)

### (1) Demo practice, US equities/ETFs
1. Alpaca paper: free, same API as live, separate keys, documented fill rules and limits. Caveats: IEX-only data, optimistic fills, region eligibility unconfirmed (U).
2. Interactive Brokers paper: best realism of API parity and reach, but needs a funded live account, Pro tier, gateway and 2FA friction.
3. Tradier sandbox: free with an account, delayed data. Needs a US brokerage account.
4. TradeStation SIM / tastytrade cert: solid mechanics testing. tastytrade sandbox is thin on realism. Webull paper API is too new.
Backup for all: a local simulator (NautilusTrader/Lumibot) with our own cost model.

### (2) Real money later, US equities/ETFs (only after separate human approval)
1. Alpaca live: API-first, commission-free stocks, same code as paper. Hurdles: eligibility by country (U), no confirmed trade-only/IP-allowlist key for the Trading API (U).
2. Interactive Brokers: widest country reach and mature regulation. Hurdles: gateway, weekly re-auth, Pro requirement, account minimums by region (U).
3. Tradier, tastytrade or TradeStation if the human is a US resident (confirm API terms).
4. Trading 212 (UK/EU only): beta API, market orders only in live, which is a bad fit for a risk guard that wants limit orders and stops.

### (1) Demo practice, crypto
1. Binance Spot Testnet (if the country allows Binance.com): best-documented testnet.
2. Bybit Testnet (not Demo) or OKX demo: depends on country.
3. Gemini sandbox: easy, separate, safe, but thin liquidity.
4. Coinbase sandbox is mocked and static, so use only for integration shape tests.
Plus a local simulator or CCXT sandbox mode for the venues that support it.

### (2) Real money later, crypto
1. Coinbase Advanced Trade: View/Trade/Transfer permission levels, portfolio scoping, IP allowlist (S) fit the "no withdrawal, ever" rule best.
2. Kraken Spot: granular permissions with withdraw left off (S). No free sandbox is the cost.
3. Binance.com (if available) with an IP-restricted, trade-only key. Withdrawals need IP restriction, so leave withdrawals off.
4. Alpaca crypto: limited US states, small fees, unified with the equities code, only if the human's state is covered.
Note: crypto live requires per-exchange fee and regulation checks that I did not complete.

## 6. Top 3 deal-breakers to check once the country is known
1. Eligibility: can a resident of that country open a LIVE account and get API access at each candidate (Alpaca, IBKR, Binance.com vs Binance.US, Coinbase, Kraken, Bybit/OKX, Webull), and can they use paper without live KYC? Official country lists were not retrievable, so verify on each signup page.
2. Key security fit with our rules: can we create a key that can trade but never withdraw, and can we IP-restrict it? Confirmed for Coinbase, Kraken and Binance (S). Not confirmed for Alpaca Trading API, IBKR and others (U). The Ledger rule "no transfers or withdrawals, ever" depends on this.
3. Regulatory and cost restrictions for that country: availability of crypto in the human's state or country, leveraged-product bans, tax reporting, investor protection (SIPC, FSCS or equivalent: not confirmed anywhere in my results), minimum deposit, and data-feed costs for anything beyond IEX.

## 7. Biggest unknowns
- Country-by-country eligibility lists (not retrievable).
- Investor-protection details (SIPC/FSCS/segregation) per platform, which I did not confirm.
- Current fees, minimum deposits and live rate limits for most venues.
- Alpaca Trading API IP allowlisting and trade-only keys; Webull API region support; Kraken Futures demo status; CCXT sandbox support list; maintenance of the open-source tools.
- Whether paper-fill realism is good enough to judge strategy P&L (it is not, per Alpaca's own limits). Treat paper as a plumbing and discipline test, not an edge test.

## 8. Key sources (all seen as search results only, none fully opened)
- Alpaca: https://docs.alpaca.markets/us/docs/paper-trading , https://alpaca.markets/learn/live-trading-account-non-us , https://alpaca.markets/support/what-regions-support-cryptocurrency-trading
- IBKR: https://www.interactivebrokers.com/docs/web-api/trading/usage-and-availability/pacing-limitations , https://www.interactivebrokers.com/docs/web-api/trading/getting-started/trading-access-for-individuals
- Tradier: https://docs.tradier.com/docs
- TradeStation: https://api.tradestation.com/docs/fundamentals/sim-vs-live
- tastytrade: https://developer.tastytrade.com/sandbox
- Schwab (third-party): https://www.quantvps.com/blog/schwab-api-thinkorswim-guide
- Webull: https://www.prnewswire.com/news-releases/webull-unveils-enhanced-paper-trading-experience-with-professional-grade-and-openapi-multi-asset-simulation-302830191.html
- Trading 212: https://docs.trading212.com/api/section/general-information/api-limitations
- Saxo: https://www.developer.saxo/openapi/learn/environments
- IG: https://trading-ig.readthedocs.io/en/latest/faq.html
- OANDA: https://developer.oanda.com/rest-live-v20/development-guide
- Binance: https://developers.binance.com/en/docs/products/spot/testnet/general-info , https://www.binance.com/en/legal/list-of-prohibited-countries/
- Coinbase: https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/sandbox , https://docs.cdp.coinbase.com/coinbase-app/advanced-trade-apis/rest-scopes.md
- Kraken: https://docs.kraken.com/exchange/guides/futures/introduction , https://docs.kraken.com/exchange/guides/rest/api-keys
- Bybit: https://bybit-exchange.github.io/docs/v5/demo
- OKX: https://www.okx.com/help/api-faq
- Gemini: https://developer.gemini.com/get-started/sandbox
- CCXT: https://docs.ccxt.com/docs/comparisons/ccxt-vs-okx-api
- PDT change: https://www.finra.org/rules-guidance/notices/26-10
