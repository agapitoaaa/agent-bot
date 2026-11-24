# Hypotheses: how pre-registration works here

Owner: Ledger (trader). Reviewer: Vex (qa-engineer). Paper only; education and research, not financial advice.

## Why
A backtest is easy to bend until it looks good. Pre-registration fixes the rules, the data, the costs and the pass/fail bar BEFORE any result exists, so the result cannot quietly rewrite the question. Each trial we run, good or bad, is counted, because the more variants you try the more likely the best one is luck (Bailey and Lopez de Prado, Deflated Sharpe Ratio; Harvey and Liu).

## Files
- `H<n>-<slug>.md`: one hypothesis per file (exact rules, universe, period, costs, benchmark, success and rejection criteria, trial count).
- `trial-registry.jsonl`: append-only, one JSON object per line. Never edit or delete a line. A status change is a NEW line with the same `id` and a later `logged_at`; the latest line per `id` is the current state.
- Template: `trading/knowledge/strategies.md` section 3.

## Lifecycle
1. `draft`: being written; nothing has been run. May still change freely (no results exist).
2. `frozen`: QA has reviewed it and the freeze is recorded (date, git commit, reviewer) in the file's header. From here the rules, universe, periods, costs, criteria and trial list may NOT change.
3. `tested`: runs were executed exactly as registered; results appended to the registry and to a results note. Pass or fail is judged against the criteria as frozen.
4. `promoted` / `rejected` / `retired`: promotion beyond backtest needs QA review and owner approval (see `docs/departments/trading.md`).

## Changing a frozen hypothesis
Any change is a new version (`H1-v2`), never an edit. The file records: what changed, why, who asked, and whether any result had been seen when the change was made. Every v2 parameter set is a NEW trial and is added to the registry; the v1 trials stay and stay counted. A change made after seeing results is flagged `post_hoc: true` and its evidence is treated as exploratory only.

## Trial counting
- A trial = one distinct configuration (rule + parameters + universe + cost model) whose result could influence a decision. Re-running the same configuration on another window, under 2x costs, or on a held-out period is a RUN of that trial, not a new trial; runs are listed in the hypothesis and logged in the registry as `kind: run` lines.
- Discarded, failed, crashed and "just checking" variants all count. If unsure, count it.
- Benchmarks are registered (they are runs we report) but are flagged `counts_toward_dsr: false` because nothing is selected among them.
- The Deflated Sharpe Ratio for any strategy uses N = the number of `counts_toward_dsr: true` trials in the whole registry that share the same strategy family (currently the trend family, so every H1 trial and any later trend variant, such as breakout or vol targeting, adds to N). Report N next to every Sharpe-type number.
- Selection rule: the single pre-registered primary parameter set is the one judged. The others are reported, not substituted.

## Bias warnings that apply to all files
- The author's (an LLM's) knowledge of past market history is a contamination risk: a "held-out" period the author roughly remembers is not blind. Only forward paper data after the freeze date is truly out of sample. Say so in every file.
- Small samples: monthly signals produce few independent observations. "Inconclusive" and "no edge found" are valid, expected outcomes.
