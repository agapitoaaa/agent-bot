# Ledger knowledge catalog: strategies, patterns, sizing and risk methods (evidence-graded)

Author: Nova (researcher), brief mode. Date: 2026-11-22. Education and research only; not financial advice. No strategy here is a recommendation to trade real money.

Scope: long-only, no leverage/margin/shorting/options/perps, daily or weekly horizon, small account, US stocks/ETFs and crypto spot, owner in the Philippines, paper first.

## 0. How to read this (and the honesty caveat)

- **Evidence basis:** every search returned abstracts, snippets and secondary summaries. I did not open any full paper. Every number below is "per snippet/abstract" and should be treated as **unverified until Ledger or QA reads the primary source**. Where I could not find something, I say so. Nothing is invented.
- **Fact vs assumption:** lines marked **[F]** are sourced claims; **[A]** are my assumptions or design suggestions.
- **Grades:** LEARN FIRST (simple, durable-looking, low turnover, cheap to test, fits constraints); LEARN LATER (plausible but costlier, thinner, or harder to implement); AVOID FOR NOW (weak/decayed evidence, cost-fragile, or incompatible with constraints).
- **Evidence strength** (my judgement, not a statistic): Strong = multiple independent samples/markets and survived replication debate; Moderate = good original evidence, contested or decayed; Thin = few/one source, snippets only, or practitioner claims.
- **Philippines:** tax and broker access are unresolved (see `docs/trader-live-readiness.md` section 12). Nothing here needs more than daily/weekly bars and a paper account.

## 1. Summary table

| # | Strategy / method | Grade | Evidence | Turnover | Key risk | Main link |
|---|---|---|---|---|---|---|
| 1 | Time-series (trend) momentum, 10-month / 200-day MA on ETFs | LEARN FIRST | Strong (multi-asset, long history), contested statistically | Low (monthly signals, a few trades per year per asset) | Whipsaw; long flat/losing stretches; weak after crises | [Hurst et al., AQR](https://www.aqr.com/insights/research/journal-article/a-century-of-evidence-on-trend-following-investing) |
| 2 | Asset-class trend rotation (Faber GTAA-style) | LEARN FIRST | Moderate-strong, simple | Low | Parameter fragility; cash drag | [Faber, SSRN 962461](https://papers.ssrn.com/abstract=962461) |
| 3 | Dual momentum (Antonacci GEM) | LEARN LATER | Moderate; little peer-reviewed OOS | Low | Few assets, few signals, long sample needed; single-source lore | [Alpha Architect](https://alphaarchitect.com/dual-momentum-with-stock-selection/) |
| 4 | Cross-sectional stock momentum (long-only) | LEARN LATER | Strong historically, crash-prone | Medium-high | Momentum crashes; costs; needs many stocks | [Daniel & Moskowitz](https://www.nber.org/system/files/working_papers/w20439/w20439.pdf) |
| 5 | Momentum/factor ETFs (momentum, value, quality, min-vol) | LEARN FIRST (as the cheap way to get factor exposure and as benchmark) | Moderate; factors have long droughts | Low for holder | Decade-long underperformance | [Arnott et al. FAJ 2021](https://ideas.repec.org/a/taf/ufajxx/v77y2021i1p44-67.html) |
| 6 | Short-term reversal / RSI-style mean reversion | AVOID FOR NOW | Moderate gross, weak net | High | Costs exceed profit; weaker after 2000 | [Avramov, Chordia, Goyal](https://ideas.repec.org/a/bla/jfinan/v61y2006i5p2365-2394.html) |
| 7 | Value factor (via ETFs) | LEARN LATER | Strong long-run, severe drought 2007-2020 | Low | Can underperform for 10+ years | [AQR](https://www.aqr.com/insights/perspectives/is-systematic-value-investing-dead) |
| 8 | Quality factor (via ETFs) | LEARN LATER | Moderate (I found no direct source this session) | Low | Unverified here; crowding | none verified |
| 9 | Low-volatility (via ETFs) | LEARN LATER | Moderate, challenged | Low | Explained by other factors; rate sensitivity | [Alpha Architect](https://alphaarchitect.com/chasing-low-beta-loses-alpha/) |
| 10 | Volatility targeting (single-asset, no leverage cap above 1x) | LEARN LATER | Moderate (equities only); contested OOS | Low-medium | Late de-risking; whipsaw; benefit mostly tail reduction | [Harvey et al. 2018](https://people.duke.edu/~charvey/Research/Published_Papers/P135_The_impact_of.pdf) |
| 11 | Risk parity (unlevered) | AVOID FOR NOW | Claim rests on leverage | Low | Return benefit disappears without leverage (disputed) | [AQR](https://www.aqr.com/insights/research/journal-article/leverage-aversion-and-risk-parity) |
| 12 | Periodic rebalancing and DCA | LEARN FIRST (as the baseline/discipline) | Strong for what it claims (small) | Very low | Lump sum beats DCA about 2/3 of the time; DCA is risk management not alpha | [Vanguard 2023](https://corporate.vanguard.com/content/dam/corp/research/pdf/cost_averaging_invest_now_or_temporarily_hold_your_cash.pdf) |
| 13 | Donchian / channel breakout | LEARN LATER | Thin direct evidence; same family as trend | Medium | Whipsaw; no direct source found | none direct |
| 14 | Post-earnings-announcement drift | AVOID FOR NOW | Strong historically, largely gone in non-microcaps | High | Decayed; needs earnings and estimates data | [Martineau 2022](https://ideas.repec.org/a/now/jnlcfr/104.00000122.html) |
| 15 | Turn-of-month / calendar effects | AVOID FOR NOW (log as a monitored curiosity) | Moderate, decaying | Medium | Small, decaying; tiny edge vs costs | [Etula et al. 2020](https://academic.oup.com/rfs/article/33/1/75/5494694) |
| 16 | Halloween / Sell-in-May | AVOID FOR NOW | Moderate, persistent in snippets, tax-unfriendly | Very low | One bet per year = a huge sampling problem | [Bouman & Jacobsen](https://pure.eur.nl/en/publications/the-halloween-indicator-sell-in-may-and-go-away-another-puzzle/) |
| 17 | Crypto spot trend/momentum (BTC, ETH, large caps) | LEARN LATER | Moderate-thin, short history | Low-medium | Short sample; fragile parameters; no OOS predictability for BTC in one study | [Liu, Tsyvinski, Wu](https://www.nber.org/papers/w25882) |
| 18 | Crypto dominance / altcoin rotation | AVOID FOR NOW | None found | Medium | No evidence found | none |
| 19 | LLM/NLP news sentiment | AVOID FOR NOW as a trading signal | Thin, look-ahead-prone | High | Training-data leakage; costs; small-cap concentration | [Lopez-Lira & Tang](https://arxiv.org/pdf/2304.07619v6) |
| 20 | Candlestick patterns | AVOID FOR NOW | Weak net of costs and data snooping | High | Snooping; costs | [Duvinage et al. via UCLouvain](https://dial.uclouvain.be/pr/boreal/en/object/boreal%3A136070/datastream/PDF_02/view) |
| 21 | Chart patterns (head-and-shoulders, flags), S/R | AVOID FOR NOW | Thin; subjective; I did not retrieve Lo-Mamaysky-Wang results | Medium | Discretionary, non-pre-registrable unless coded | [Park & Irwin survey](https://ideas.repec.org/a/bla/jecsur/v21y2007i4p786-826.html) |
| 22 | Pairs trading / stat arb | AVOID FOR NOW | Decayed; needs shorting | High | Requires shorting; costs kill it | [Do & Faff](https://ideas.repec.org/a/taf/ufajxx/v66y2010i4p83-95.html) |
| 23 | Fixed-fractional and volatility-based position sizing | LEARN FIRST | Method, not alpha; standard risk practice | n/a | Sizing can't fix a no-edge strategy | (see item) |
| 24 | Kelly / fractional Kelly | LEARN LATER (as theory; use only a small fraction as a ceiling) | Strong theory; estimates are the weak point | n/a | Estimation error causes over-betting | [MacLean, Thorp, Ziemba](https://escholarship.org/content/qt5mr5k8qj/qt5mr5k8qj.pdf) |
| 25 | Stop-loss / exit logic | LEARN FIRST (as pre-declared invalidation rules), not as alpha | Mixed; works only if returns have momentum | n/a | Stops can lower expected return in random walks | [Kaminski & Lo](https://dspace.mit.edu/handle/1721.1/114876) |
| 26 | Diversification (equal weight, 1/N) | LEARN FIRST | Strong | Low | Concentration; correlation spikes | [DeMiguel et al. 2009](https://econpapers.repec.org/RePEc:oup:rfinst:v:22:y:2009:i:5:p:1915-1953) |
| 27 | 52-week-high momentum | LEARN LATER | Moderate (from snippets) | Medium | Same as momentum | [Alpha Architect](https://alphaarchitect.com/the-secret-to-momentum-is-the-52-week-high/) |

## 2. Cross-cutting evidence (read this before any individual item)

**2.1 Strategy decay after publication.**
- [F] McLean and Pontiff (Journal of Finance, 2016) studied 97 published predictors. Returns decline after publication but do not vanish; the paper reports a lower bound on the publication effect of about 32% (per abstract summary) and finds rising volume and short interest after publication. [Link](https://econpapers.repec.org/RePEc:bla:jfinan:v:71:y:2016:i:1:p:5-32). Snippet-level; check exact figures in the paper.
- [F] Harvey, Liu and Zhu (RFS, 2016) argue new factors need a t-ratio above 3.0 because of multiple testing. [NBER](https://www.nber.org/papers/w20592).
- [F] Hou, Xue and Zhang, "Replicating Anomalies" (RFS, 2020): of 447 anomaly variables, 286 (64%) were insignificant at 5% once microcaps are tamed (NYSE breakpoints, value-weighted); 380 (85%) at the t of 3 cutoff. [NBER](https://www.nber.org/papers/23394). Same search noted Chen and Zimmermann (2018) estimate publication-bias-adjusted returns only about 12% below in-sample (snippet only), so the literature disagrees on how big decay is.
- [A] Ledger should assume any published edge it finds is **smaller live than in the paper**, and plan for roughly half or less as a working prior (this is my assumption, not a sourced figure).

**2.2 Costs and turnover.**
- [F] Novy-Marx and Velikov (2015): costs dramatically cut high-turnover anomalies; anomalies with under 50% monthly turnover mostly keep significant net spreads when designed to reduce costs. [NBER](https://www.nber.org/papers/w20721.pdf).
- [F] Frazzini, Israel and Moskowitz (AQR, 2012) find size, value and momentum survive real costs, using one large manager's live data, which is very likely cheaper than a retail account can get. [NBER conf. paper](https://conference.nber.org/conf_papers/f68262/f68262.pdf). The Novy-Marx/Velikov side disputes how generalisable that is.
- [F] Lesmond, Schill and Zhou (2004) argue relative-strength profits are bounded by transaction costs. [Link](https://www.bauer.uh.edu/rsusmel/phd/Lesmond_et%20al%20_2004_JFE.pdf).
- [F] Barber and Odean (J. Finance, 2000), 60,000+ US households 1991-1996: average turnover about 80%/year; gross returns near market, net returns well short; the most active traders did worst. Overtrading is Ledger's stated weakness. [Link](https://econpapers.repec.org/RePEc:bla:jfinan:v:55:y:2000:i:2:p:773-806). Old US sample, one broker.
- [A] For a small account in liquid ETFs the dominant costs are spread, slippage and (for the owner) any FX/funding and tax friction, not commissions. Alpaca states US stocks are commission-free; crypto has a per-trade fee that depends on volume and order type, and I did not find the numbers ([Alpaca docs](https://docs.alpaca.markets/docs/crypto-fees)). Ledger must use a conservative cost model and log it.

**2.3 Overfitting and multiple testing.**
- [F] Bailey and Lopez de Prado (Deflated Sharpe Ratio) and Harvey and Liu (haircut Sharpe) correct for number of trials; Harvey and Liu warn against a flat 50% haircut rule; the haircut depends on sample length, autocorrelation, trial count and correlation among trials. [DSR, SSRN](https://papers.ssrn.com/abstract=2460551), [Harvey & Liu](https://people.duke.edu/~charvey/Research/Published_Papers/P120_Backtesting.PDF).
- [F] A recent arXiv paper (2026, snippet) says backtest-engine implementation differences are a further, separate error source. [arXiv 2603.20319](https://arxiv.org/pdf/2603.20319).
- [A] With only about 10-25 distinct strategy families worth testing, the **most important defence is a small, fixed menu with fixed parameters**, not a big search.

**2.4 Retail edge reality.**
- [A, honest summary] After published decay (about a third or more, per McLean-Pontiff), costs, taxes, slippage and the owner's small size, the realistic edge from any single strategy here is **small and statistically indistinguishable from zero over a 90-day paper test**. The defensible benefits are mainly (a) lower drawdown than buy-and-hold via trend filters, (b) cheap diversified exposure, (c) avoiding self-harm from overtrading. I found no source that quantifies "retail edge after costs" in general; I am not going to invent one.

## 3. Common pre-registration template (applies to every item)

Each hypothesis file must fix before any test: (1) exact entry/exit rules and parameters (no free parameters left to tune); (2) universe, fixed in advance and including delisted/dead instruments where applicable; (3) in-sample period and a held-out period never touched during design; (4) cost model (spread plus slippage, fixed in bps, plus a 2x-cost stress run); (5) benchmark (buy-and-hold of an equal-risk or equal-weight index ETF; for crypto, equal-weight BTC/ETH or BTC only); (6) success criteria stated in net terms (e.g. net Sharpe or drawdown-adjusted return at least not worse than benchmark AND maximum drawdown meaningfully lower, or net return higher with a Deflated Sharpe above a pre-set threshold); (7) **trial counter**: every variant run, including discarded ones, goes into a trial registry, and the DSR uses that count; (8) a kill rule (what result retires the idea); (9) for LLM look-ahead: forward-only paper evidence is the primary evidence, backtest is only for rejecting ideas.
- [A] Suggested minimum: no strategy is "promoted" on a backtest alone; forward paper results get a MinTRL check measured in observations (months or weeks), not trade count.
- [A] Suggested trial budget: a maximum of 3 parameter sets per strategy (e.g. 100/150/200-day MA), all reported, none chosen post hoc; the pre-registered default is the one judged.

## 4. Strategy entries

### 4.1 Time-series (trend) momentum and moving-average rules  -- LEARN FIRST
- **Idea:** Hold an asset when its own past return (e.g. 12-month) is positive or its price is above a long moving average (e.g. 200-day or 10-month); otherwise hold cash/T-bills. Long-only version of the futures result.
- **Evidence for:** [F] Moskowitz, Ooi and Pedersen (JFE, 2012): significant time-series momentum across 58 liquid futures; persistence 1-12 months with partial reversal later. [SSRN](https://papers.ssrn.com/abstract=2089463). [F] Hurst, Ooi and Pedersen (AQR, 2017) extend to 67 markets back to 1880 and report consistent profitability over 110 years, strong in extreme years and in 8 of the 10 largest 60/40 drawdowns (snippet; AQR authors, self-interested). [AQR](https://www.aqr.com/insights/research/journal-article/a-century-of-evidence-on-trend-following-investing).
- **Evidence against:** [F] Huang and Li (per snippet) argue asset-by-asset regressions show little time-series momentum in or out of sample and that performance matches a strategy based on the historical mean (pooled-regression over-rejection). [F] A UCC paper finds trend following weak, on average, for about four years after the start of a financial crisis. [Link](https://www.ucc.ie/en/media/research/centreforinvestmentresearch/wp/TrendFollowingFeb2014.pdf). [F] SG Trend/CTA indexes had a poor first half of 2025: trailing 12-month about -15% at June 2025 per a trade-press report (secondary). [Link](https://www.alternativeswatch.com/2025/06/02/trend-following-hedge-funds-endure-more-pain-societe-generale-indices/). [F] Park and Irwin's survey says technical-rule profits in futures faded after the early 1990s (snippet). [Link](https://ideas.repec.org/a/bla/jecsur/v21y2007i4p786-826.html).
- **Decay / failure:** choppy sideways markets (whipsaw), V-shaped recoveries after crashes, crowding in managed futures, and the fact that futures evidence does not transfer one-for-one to a long-only ETF basket.
- **Turnover/cost:** low if signals are evaluated weekly or monthly with a band; high if daily and tight. Costs matter mainly through whipsaw count.
- **Data:** free daily adjusted prices (Yahoo-type sources, Stooq; the quality varies; adjusted-close handling must be point-in-time). **Unverified here:** current free-source licensing terms.
- **Fit:** Excellent: long-only, no leverage, daily/weekly, a handful of liquid ETFs (e.g. broad US equity, international equity, bonds, gold) plus cash/T-bill ETF. The "short" leg is simply "go to cash".
- **Pre-register:** Universe fixed list of 5-8 liquid ETFs (assumption, set before testing). Rule: month-end close above 10-month SMA = hold, else cash ETF; no other parameters. Period: longest available history for in-sample, last 3-5 years held out, then forward paper. Benchmark: buy-and-hold of the same ETF basket equal-weighted, and a 60/40. Success (assumption): lower max drawdown than benchmark and net return not materially lower; do not require higher Sharpe. Trials: log every MA length tried (limit 3: 100/150/200 days or 8/10/12 months).
- **Grade: LEARN FIRST.** Reasons: the most robust, simplest, lowest-turnover family; its realistic goal is drawdown control, which fits the "beat buy-and-hold after costs" bar only loosely, so expect it to lag in bull markets.

### 4.2 Asset-class trend rotation (Faber GTAA)  -- LEARN FIRST
- **Idea:** Five asset classes (US stocks, foreign stocks, bonds, real estate, commodities), equal weight 20% each when above the 10-month SMA, else T-bills.
- **For:** [F] Faber (Journal of Wealth Management, 2007; SSRN 962461, last updated 2013) reports equity-like returns with bond-like volatility and drawdown out of sample since 1973 (per summaries; Scribd copies only, official link unverified). [Quantpedia](https://quantpedia.com/strategies/asset-class-trend-following) cites follow-up work.
- **Against:** [F] A South African thesis replicated it locally (snippet). I found no independent peer-reviewed post-2013 out-of-sample test this session. [F] A 2020 Bitcoin MA study found small parameter changes cause large Sharpe swings (snippet), a reminder of parameter fragility.
- **Decay:** the paper is widely known (most-downloaded SSRN paper per a ThinkAdvisor article, 2015), so crowding and decay plausibly apply; 2022 (stocks and bonds fell together) is a stress test that I did not find results for.
- **Turnover/cost:** low (monthly, a few switches a year).
- **Data:** free ETF prices; commodity and REIT ETFs have shorter histories than the original index data.
- **Fit:** Excellent. Equivalent to 4.1 applied to a multi-asset ETF basket; run it as the first test.
- **Pre-register:** as 4.1, with exactly the five ETFs fixed in advance. Log trials. Treat 2022 as a named stress period.
- **Grade: LEARN FIRST** (merge with 4.1 as one "trend family" to avoid duplicate trials).

### 4.3 Dual momentum / rotation (Antonacci GEM)  -- LEARN LATER
- **Idea:** Compare US stocks vs ex-US stocks (relative momentum), and hold the winner only if its 12-month return beats T-bills (absolute momentum), else bonds.
- **For:** [F] An independent practitioner replication reports robustness to specification changes and live results in line with backtests (single blog, not peer-reviewed; snippet). [Link](https://algoedgeinsights.beehiiv.com/p/is-gary-antonacci-s-global-equity-momentum-strategy-robust).
- **Against:** [F] A 2024 arXiv paper on a related Zarattini-Antonacci industry strategy says weak robust validation undermines out-of-sample applicability. [arXiv 2412.14361](https://arxiv.org/html/2412.14361v1). [F] Keller and Keuning criticise in-sample threshold optimisation (snippet). I found no peer-reviewed out-of-sample study of GEM itself.
- **Decay/failure:** a handful of switches per decade means a tiny sample; looks good because of a few big calls (2000-02, 2008).
- **Turnover:** very low.
- **Data/fit:** free; fits constraints; long-only.
- **Pre-register:** exactly the published 4-asset GEM; no parameter tweaks. **Caution [A]:** with so few switches, the DSR/MinTRL calculation will say "inconclusive" for decades; that is the correct answer.
- **Grade: LEARN LATER**, after 4.1/4.2, because its extra complexity adds few independent observations.

### 4.4 Cross-sectional stock momentum (long-only)  -- LEARN LATER
- **Idea:** Buy the top decile/quintile of stocks by 12-1 month return, hold a month.
- **For:** [F] Documented since Jegadeesh-Titman (1993) and Asness (1994) (per Daniel and Moskowitz). [F] Novy-Marx and Velikov: momentum survives conservative cost estimates (per CEPR summary). Frazzini et al. also find it survives costs for a large manager.
- **Against:** [F] Daniel and Moskowitz, "Momentum crashes": sharp crashes after market rebounds; loser-decile betas above 3 after declines (that is the short leg, which Ledger doesn't have). [NBER](https://www.nber.org/system/files/working_papers/w20439/w20439.pdf). [F] Lesmond et al.: profits bounded by costs. [F] Kellogg-affiliated work (snippet): maximal fund sizes are small. [A] Long-only winners-only keeps market beta and crash risk with a smaller premium.
- **Turnover/cost:** monthly rebalancing of 20-50 stocks is expensive for a small account relative to the edge; needs survivorship-bias-free data (delisted names), which is **not free**.
- **Fit:** Poor for a small account (many positions, free survivor-bias-free data is hard); the cheaper route is a momentum ETF (see 4.5).
- **Pre-register (if ever):** S&P 500 point-in-time constituents (paid data likely); not recommended at this stage.
- **Grade: LEARN LATER.**

### 4.5 Factor ETFs (momentum, value, quality, min-vol) as the practical route  -- LEARN FIRST (as reading + benchmark; not as a trading edge)
- **Idea:** Get factor exposure by holding a broad factor ETF instead of trading single stocks.
- **Evidence:** see 4.7-4.9 for factor-specific results. [F] I did not retrieve long-run track records of specific ETFs (MTUM, USMV, etc.) this session, so no performance claim is made. **Unverified:** current expense ratios and multi-decade performance.
- **Fit/turnover:** holder turnover low; the fund does the trading.
- **Pre-register:** a "slow factor tilt" test: equal-weight 3-4 factor ETFs vs the broad index ETF over the common history (short, about 10-12 years for most ETFs) with the explicit expectation that the sample is too short to conclude. [A]
- **Grade: LEARN FIRST** as a benchmark-and-education item; outperformance claims are not expected.

### 4.6 Short-term reversal / RSI-style mean reversion  -- AVOID FOR NOW
- **Idea:** Buy last week's/month's losers (or RSI<30 oversold), sell on bounce.
- **For:** [F] Weekly/monthly reversals documented in NYSE/AMEX 1962-2002 (Avramov, Chordia, Goyal per snippets).
- **Against:** [F] Same paper: biggest reversals in high-turnover, low-liquidity stocks; contrarian profits smaller than likely transaction costs. [Link](https://ideas.repec.org/a/bla/jfinan/v61y2006i5p2365-2394.html). [F] Lewellen (snippet) reports reversals weakened for individual stocks after 2000; Collin-Dufresne and Daniel (2014) argue reversal is strong even in liquid stocks (disagreement).
- **Turnover:** high, the opposite of what Ledger needs. Catching falling knives is also the classic overtrading trap.
- **Fit:** long-only is feasible but costs and the temptation to over-trade dominate.
- **Pre-register (only if later revisited):** liquid large-cap ETF universe, RSI(2) style rules are not tested in the sources I found; no source found for RSI-specific retail evidence.
- **Grade: AVOID FOR NOW.**

### 4.7 Value factor (ETFs)  -- LEARN LATER
- **For:** [F] Long-run premium documented widely. **Against:** [F] Arnott, Harvey, Kalesnik, Linnainmaa (FAJ, 2021): HML drawdown of about -55%, attributed mainly to a collapse in relative valuation; fix by capitalising intangibles would have added about 2.2 pp/year since 2008 (snippet). [Link](https://ideas.repec.org/a/taf/ufajxx/v77y2021i1p44-67.html). [F] AQR: longest/deepest drawdown in HML history through 2020; interest-rate duration story. [Link](https://www.aqr.com/insights/perspectives/is-systematic-value-investing-dead). I found no data post-2021 this session.
- **Fit:** works as a passive tilt; it cannot be validated in a 90-day paper test. **Grade: LEARN LATER**; study, do not actively trade.

### 4.8 Quality factor  -- LEARN LATER (thinly sourced here)
- I did not retrieve a primary source on quality (e.g. "Quality minus Junk") this session; only a BlackRock commentary snippet suggesting the quality trend strengthened in the 21st century. Mark **unverified**. Alpha Architect's low-vol ETF analysis (below) notes alphas turn negative once quality is controlled, which implies quality may explain other anomalies (snippet). **Grade: LEARN LATER**, pending a proper source pass.

### 4.9 Low-volatility / min-vol ETFs  -- LEARN LATER
- **For:** [F] Anomaly in CAPM/three-factor world; lower drawdowns in bear markets (Wikipedia-level snippet).
- **Against:** [F] Alpha Architect (data March 2013 to Feb 2021): low-vol ETF alphas turn negative after controlling for quality and term. [Link](https://alphaarchitect.com/chasing-low-beta-loses-alpha/). [F] Swedroe/ETF.com: significance disappears after value and profitability controls (secondary). [F] Liu-Stambaugh-Yuan: beta anomaly arises from idiosyncratic volatility (per snippet). I did not find a Baker-Bradley-Wurgler result.
- **Fit:** fine as a passive holding, not a testable trading edge. **Grade: LEARN LATER.**

### 4.10 Volatility targeting  -- LEARN LATER
- **Idea:** Scale exposure inversely to recent realised volatility (cap at 100% for Ledger since no leverage; the rest sits in cash).
- **For:** [F] Harvey et al. (JPM, 2018): over 60+ assets from as early as 1926, vol targeting reduces extreme returns and vol-of-vol; equity Sharpe from 0.40 to about 0.48-0.51; for bonds/currencies/commodities the Sharpe effect is small (per summaries). [Link](https://people.duke.edu/~charvey/Research/Published_Papers/P135_The_impact_of.pdf).
- **Against:** [F] Cederburg et al. (103 strategies): vol-managed portfolios do not reliably beat unscaled in real time; regression alphas are not implementable (snippet). [F] DeMiguel, Martin-Utrera, Uppal (J. Finance, 2024): a conditional multifactor version does better out-of-sample net of costs. [Link](https://lbsresearch.london.edu/id/eprint/3716). The debate is open.
- **Fit:** the no-leverage cap means it can only de-risk, never lever up in calm markets; the benefit is mostly tail reduction. [A] Test it as an add-on to 4.1 only after 4.1 works.
- **Pre-register:** target vol (e.g. 10%) fixed, 20-day realised vol, weekly rebalance with a no-trade band, cap exposure at 100%. Log trials (limit 3 targets).
- **Grade: LEARN LATER.**

### 4.11 Risk parity (unlevered)  -- AVOID FOR NOW
- [F] Asness, Frazzini, Pedersen (FAJ, 2012): risk-parity beat market portfolio by about 4%/year over 1926-2010 for the leveraged, market-risk-matched version (AQR authors; AQR sells risk parity). [Link](https://www.aqr.com/insights/research/journal-article/leverage-aversion-and-risk-parity). [F] Goldberg, Anderson, Bianchi (FAJ, 2012) argue results come from leverage, not volatility targeting. [CFA blog](https://blogs.cfainstitute.org/?p=11010). I found no clean unlevered test.
- Without leverage, risk parity is a bond-heavy portfolio with lower expected return. It also failed in 2022 when stocks and bonds fell together (my knowledge; not sourced here). **Grade: AVOID FOR NOW.** Keep "equal weight across uncorrelated assets" (4.26) instead.

### 4.12 Periodic rebalancing and dollar-cost averaging  -- LEARN FIRST (as baseline and behavioural discipline)
- **Idea:** Fixed-schedule rebalancing to target weights; invest in fixed instalments.
- **Evidence:** [F] Vanguard (2012; updated Feb 2023, 1976-2022): lump-sum beat DCA about 68% of the time (about two-thirds); DCA beat holding cash; DCA reduces downside regret and wins in the worst scenarios. [Vanguard](https://corporate.vanguard.com/content/dam/corp/research/pdf/cost_averaging_invest_now_or_temporarily_hold_your_cash.pdf). Morningstar finds DCA better about one-third of the time (snippet). No source retrieved on the return benefit of rebalancing itself; mark **unverified**.
- **Decay/failure:** not an alpha source; DCA lags in rising markets. Rebalancing bands avoid unnecessary turnover.
- **Fit:** Ideal: very low turnover. It is Ledger's **benchmark and default behaviour**, i.e. what to do when no pre-registered signal fires.
- **Pre-register:** monthly or quarterly rebalance of a fixed ETF mix with a 5-pp drift band; compare with no-rebalance. Expect no significant difference. **Grade: LEARN FIRST.**

### 4.13 Breakout / Donchian channel  -- LEARN LATER
- **Idea:** Buy a new N-day high (e.g. 55-day), exit on an M-day low (e.g. 20-day).
- **Evidence:** [F] My search found **no direct source** on Donchian rules; Hurst et al. test a lookback-sign rule, not channels. Park and Irwin's review (snippet) says technical rules were profitable in futures to the early 1990s and then faded. It belongs to the trend family (4.1) and probably adds few independent bets. **[A]** Treat as a variant of 4.1; only test if 4.1 is promoted, and count it as extra trials.
- **Grade: LEARN LATER.**

### 4.14 Post-earnings-announcement drift (PEAD)  -- AVOID FOR NOW
- **For:** [F] Classic anomaly. [F] Chan and Marsh (2024 SSRN draft, snippet): drift can show up as overnight returns; reports significant overnight drift after extreme misses. UCLA Anderson says it "resurfaces" in two studies, critiqued by a third (snippet). [Link](https://anderson-review.ucla.edu/is-post-earnings-announcement-drift-a-thing-again).
- **Against:** [F] Martineau (Critical Finance Review, 2022): in modern markets prices reflect earnings surprises on announcement day; drift disappeared from non-microcaps by about 2006. [Link](https://ideas.repec.org/a/now/jnlcfr/104.00000122.html).
- **Data:** needs earnings dates, analyst consensus, announcement-time stamps (not free at point-in-time quality).
- **Fit:** event-time trades in stocks, high turnover, small caps where costs bite. **Grade: AVOID FOR NOW.**

### 4.15 Turn-of-month and other calendar effects  -- AVOID FOR NOW
- **For:** [F] Etula, Rinne, Suominen, Vaittinen (RFS, 2020): the monthly payment cycle produces patterns in liquid markets worldwide, tied to month-end liquidity needs. [Link](https://academic.oup.com/rfs/article/33/1/75/5494694). Futures show a similar pattern (Dzhabarov and Ziemba, snippet).
- **Against:** [F] One master's thesis finds the effect weaker in recent subsamples and gone in many markets; another finds it present 2007-2018 (both theses, low reliability). I did not verify pre-FOMC drift (not retrieved).
- **Why avoid:** small effect, a few days a month, high calendar-driven turnover, easily overfit by choosing the exact day window. **[A]** Useful only as a "test case" for the trial registry.
- **Grade: AVOID FOR NOW.**

### 4.16 Halloween / "Sell in May"  -- AVOID FOR NOW
- [F] Bouman and Jacobsen (AER, 2002): present in 36 of 37 countries, significant in 20, about 11 pp US gap Nov-Apr vs May-Oct; Maberly and Pierce say it vanishes without two outlier months; later out-of-sample tests (1998-2012) say it persists; Jacobsen and Zhang found it in 81 of 108 markets (all snippets). [Link](https://pure.eur.nl/en/publications/the-halloween-indicator-sell-in-may-and-go-away-another-puzzle/).
- Problem: one decision per year gives about 1 observation/year; the forward test would take decades. Sitting in cash half the year is also a bet against a rising equity premium. **Grade: AVOID FOR NOW.**

### 4.17 Crypto spot trend / momentum  -- LEARN LATER
- **For:** [F] Liu, Tsyvinski, Wu (J. Finance, 2022): a three-factor model (market, size, momentum) explains nine successful long-short strategies; momentum stronger among larger coins (per snippet; another paper found it stronger in small coins, a conflict). [NBER](https://www.nber.org/papers/w25882). [F] CTREND factor paper (JFQA, data April 2015 to May 2022) (snippet). [Link](https://www.cambridge.org/core/services/aop-cambridge-core/content/view/S0022109024000747). [F] A 2026 arXiv preprint claims Sharpe 2.41 and -12.7% max drawdown out of sample over 2022-2024 on 150+ pairs; **single group, preprint, likely includes shorts/leverage; do not trust**. [arXiv](https://arxiv.org/html/2602.11708v1).
- **Against:** [F] A Hull study finds no predictability for Bitcoin out of sample, though other coins retain it (snippet). [F] 2020 Bitcoin MA study: Sharpe highly sensitive to small parameter changes. [F] A 2026 paper warns of repeated optimisation on "out-of-sample" data (snippet).
- **Decay/failure:** the history is under 15 years and dominated by a few bull/bear cycles; regimes change (ETFs, institutions). Spread/fees vary: Alpaca crypto fee numbers not retrieved. Crypto is also exposed to the Philippine regulatory issues in `docs/trader-live-readiness.md` section 12.
- **Fit:** spot long-only trend (BTC and ETH above 100/200-day MA, else cash/stablecoin) is feasible; no funding/carry (perp-only, out of scope).
- **Pre-register:** BTC and ETH only, one MA length pre-set, daily close, weekly action, 2x-cost stress; benchmark = buy-and-hold BTC/ETH equal weight; success = lower max drawdown with return not much lower. Trial limit 3.
- **Grade: LEARN LATER** (after the equity/ETF trend version is understood).

### 4.18 Crypto dominance / altcoin rotation  -- AVOID FOR NOW
- My search found **no study** on Bitcoin-dominance signals or altcoin rotation. Do not proceed on blog lore. **Grade: AVOID FOR NOW.** Crypto carry/funding: perp-only, **out of scope**.

### 4.19 Sentiment / NLP / LLM news strategies  -- AVOID FOR NOW as a trading signal
- **For:** [F] Lopez-Lira and Tang: ChatGPT headline scores predict next-day returns out of sample, stronger in small stocks and after negative news; basic models (GPT-1/2, BERT) did not (snippet). [arXiv](https://arxiv.org/pdf/2304.07619v6). Tetlock (2007) is cited as foundation; I did not retrieve it directly.
- **Against:** [F] `docs/trader-bot-plan.md` already notes LLM look-ahead bias and recent frameworks (FINSABER, Look-Ahead-Bench) flag it; the predictability is concentrated in small, costly stocks; daily news trading means high turnover. **[A]** Ledger's own LLM would be both signal and test subject, the worst case for leakage.
- **Use instead:** sentiment as a read-only "context" note in the journal, never as a trade trigger. **Grade: AVOID FOR NOW.**

### 4.20 Candlestick patterns  -- AVOID FOR NOW
- [F] Duvinage, Mazza, Petitjean (2013): 83 candlestick rules on intraday US large-cap data; some short-term predictive power but not reliably exploitable after luck and risk adjustment; a summary says only 5 of 83 were significantly profitable net of 0.05% costs; the authors' abstract says 64% of bullish patterns had positive mean returns, three significant on a risk-adjusted basis. [Link](https://dial.uclouvain.be/pr/boreal/en/object/boreal%3A136070/datastream/PDF_02/view). Other tests (Thailand, a US 20-stock test) find little (snippets). [SAGE Open 2017](https://ideas.repec.org/a/sae/sagope/v7y2017i4p2158244017736799.html).
- Intraday data, not daily/weekly; a hand-picked pattern from dozens is the textbook data-snooping setup. **Grade: AVOID FOR NOW.**

### 4.21 Chart patterns (head-and-shoulders, flags, support/resistance)  -- AVOID FOR NOW
- [F] Park and Irwin (J. Economic Surveys, 2007) is the best survey I found, but my snippets show only that profits in futures faded after the early 1990s and (older review) 58 of 92 modern studies favoured profitability (cut-off snippet). I did **not** retrieve Lo, Mamaysky and Wang's results (kernel-regression pattern recognition) or Brock-Lakonishok-LeBaron's out-of-sample results. **[A]** Patterns are subjective; only a coded, mechanical definition is pre-registrable. Support/resistance as stop-placement reference is covered in 4.25.
- **Grade: AVOID FOR NOW.**

### 4.22 Pairs trading / stat arb  -- AVOID FOR NOW
- [F] Gatev, Goetzmann, Rouwenhorst: up to about 11% annualised excess return 1962-2002 (snippet). [NBER](https://nber.org/papers/w7032). [F] Do and Faff: monthly excess return fell from about 0.86% (1962-88) to 0.37% (1989-2002); after commissions, market impact and short-selling fees profits vanish. [Link](https://ideas.repec.org/a/taf/ufajxx/v66y2010i4p83-95.html). [F] Zhu (Yale, 2024): distance method averages 6.2%/year over the last twenty years (snippet; excess return, likely gross of short costs). [Link](https://economics.yale.edu/sites/default/files/2024-05/Zhu_Pairs_Trading.pdf).
- **Fit:** requires shorting, which Ledger cannot do; a long-only "long the laggard" version is just reversal (4.6). **Grade: AVOID FOR NOW** (infeasible under constraints).

### 4.23 Position sizing: fixed fractional and volatility-based  -- LEARN FIRST
- **Idea:** Risk a fixed small fraction of equity per trade (e.g. so a stop-out loses 0.5-1%), or size inversely to volatility (ATR) so each position contributes similar risk. Hard cap per position already set in the plan (5%).
- **Evidence:** this is risk-management practice rather than an alpha claim; I did not retrieve a primary study. [F] Harvey et al. on vol targeting (4.10) is the closest sourced evidence that volatility scaling reduces tail outcomes for equities.
- **Fit:** works with the guard (`limits.json`). **[A]** The guard, not Ledger, enforces the caps.
- **Pre-register:** compare equal-dollar vs ATR-scaled sizing on the same signals; metric = max drawdown and tail loss, not return. **Grade: LEARN FIRST.**

### 4.24 Kelly and fractional Kelly  -- LEARN LATER
- [F] MacLean, Thorp, Ziemba: Kelly maximises long-run growth but is very sensitive to parameter estimates (especially means); over-betting risks large drawdowns/ruin; fractional Kelly moderates estimation error. [Link](https://escholarship.org/content/qt5mr5k8qj/qt5mr5k8qj.pdf). [F] A 2025 arXiv paper shows fractional Kelly is equivalent to full Kelly with shrunk return estimates (snippet). [arXiv](https://arxiv.org/html/2503.17927v1). [Good/Bad Kelly](https://www.stat.berkeley.edu/~aldous/157/Papers/Good_Bad_Kelly.pdf).
- **Why Ledger shouldn't use it now:** Kelly needs the edge and variance, which Ledger cannot estimate from tiny samples; mis-estimating an edge that is actually zero makes Kelly bet too big. **[A]** Use as a teaching tool and as an upper bound; a fixed 0.25-0.5x Kelly of a *haircut* edge would still be larger than the 5% hard cap in most cases, so the cap binds.
- **Grade: LEARN LATER.**

### 4.25 Stop-loss and exit logic  -- LEARN FIRST (as invalidation rules)
- [F] Kaminski and Lo (J. Financial Markets, 2014): in a random walk, stop-losses always reduce expected return; with momentum they can add value; US monthly 1950-2004 tests showed certain stops added 50-100 bp/month during stop-out periods; benefit in momentum-like regimes. [MIT](https://dspace.mit.edu/handle/1721.1/114876). Their measure is expected return only, not full risk.
- **Use:** the plan requires every order to carry a pre-declared exit/invalidation rule. For trend strategies the MA cross *is* the exit. Avoid "tight stops" (intraday noise, whipsaw, spread). **[A]** Prefer time-based or signal-based exits and a portfolio-level drawdown stop (already in the guard).
- **Pre-register:** compare "no stop", "ATR stop (e.g. 3x ATR)" and "signal exit only" on 4.1; count as 3 trials. **Grade: LEARN FIRST.**

### 4.26 Diversification and equal weighting  -- LEARN FIRST
- [F] DeMiguel, Garlappi, Uppal (RFS, 2009): 14 optimised models vs 1/N on 7 datasets; none consistently beat 1/N on Sharpe, certainty equivalent or turnover; mean-variance needs on the order of 3000 months for 25 assets to beat it (US calibration). [Link](https://econpapers.repec.org/RePEc:oup:rfinst:v:22:y:2009:i:5:p:1915-1953). A 2023 JFQA paper argues 1/N is optimal for large N under a one-factor structure (snippet).
- **Fit:** equal weights across a small set of low-correlation ETFs; no optimiser needed. **[A]** Beware: in a crash correlations rise, so diversification across stocks/crypto helps less than assumed. **Grade: LEARN FIRST.**

### 4.27 52-week-high momentum  -- LEARN LATER
- [F] George and Hwang (2004): stocks nearest their 52-week highs earn higher returns; a later study says it explains much of momentum, disputed (snippets). [Alpha Architect](https://alphaarchitect.com/the-secret-to-momentum-is-the-52-week-high/). Same practical limits as 4.4 (single stocks, survivor-free data). **Grade: LEARN LATER.**

## 5. Suggested learning order for Ledger [A]
1. Baseline: buy-and-hold index ETF, periodic rebalance, DCA (4.12), equal-weight diversification (4.26).
2. Sizing and exits (4.23, 4.25) as a framework, not a signal.
3. One trend family: 4.1 + 4.2 on a fixed ETF basket, three parameter sets maximum.
4. Study-only: factor ETFs (4.5, 4.7-4.9), vol targeting (4.10).
5. Later, with a fresh trial budget: crypto trend (4.17), dual momentum (4.3), breakout variants (4.13).
Everything in the AVOID list stays on the shelf; its only job is to be the "this is why we don't" reference and the negative controls for the trial registry.

## 6. What I could not verify (consolidated)
- No full paper was opened; all figures are from abstracts, snippets, search summaries, theses or blogs. Notable exact numbers to verify before reuse: the 32% McLean-Pontiff figure, the Hou-Xue-Zhang 64%/85%, Do-Faff monthly returns, the Duvinage 5 of 83 count, Harvey et al. Sharpe 0.40 to 0.48-0.51, Vanguard 68%.
- Quality factor, rebalancing premium, RSI-specific evidence, Donchian-specific evidence, Lo-Mamaysky-Wang and Brock-Lakonishok-LeBaron results, pre-FOMC drift, Tetlock and Ke-Kelly-Xiu results, crypto dominance, long-run ETF track records (MTUM, USMV), and crypto trend after 2024: not found or not retrieved.
- Alpaca crypto fee levels, current free-data licensing, and which countries Alpaca crypto supports (Philippines unconfirmed).
- Whether any of this survives net of Philippine taxes and funding costs: not examined.
- The SG Trend 2025 figure is from trade press and is secondary.
