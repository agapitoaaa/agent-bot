---
description: Have Ledger analyze trends for instruments (descriptive, paper-only). Usage: /trade-analyze <symbols or CSV paths>
---

Delegate to the `trader` agent (Agent tool, subagent_type `trader`): analyze the trend state of $ARGUMENTS.

Instruct Ledger to: read `trading/memory/rules.md`, `memory/trader.md` and `memory/team.md`; get daily OHLC CSVs into `trading/data/` (use existing files, or fetch from a free public source and record an evidence card for the data source, time fetched and any limits); run `python3 trading/analysis/trend.py <files> --json` (use `--as-of` for any historical question); write a short dated note to `trading/analysis/notes/<date>-<topic>.md` covering trend state, momentum, volatility, drawdown, whipsaw count, data quality and history length, plus the strongest reason the picture could be misleading; and, ONLY if a pre-registered strategy's rules fire, log a paper decision with `scripts/trade_memory.py add-decision` (never otherwise). Remind him: descriptive only, no trade signals from this tool, no real money.

Log events with `scripts/log_event.py` (agent `trader`). Summarize to the user and link the note.
