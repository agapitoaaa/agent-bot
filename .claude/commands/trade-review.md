---
description: Weekly Trading department review: scorecards, calibration, lessons gating, retros. Usage: /trade-review
---

Run the Trading department weekly review.
1. Run `python3 scripts/trade_memory.py scorecard` and `render`. Delegate to the `trader` agent to write `trading/journal/review-<date>.md`: per-strategy results net of costs vs benchmark with sample-size warnings, calibration, rule breaches or guard blocks, what he would do differently, and lessons to log (as observations unless the gates are met).
2. If any rule was broken, a drawdown limit was breached, or calibration is poor, run the `/retro` procedure with `trader` and the relevant agents.
3. If Ledger proposes promoting a lesson to `rule`, have `qa-engineer` review the evidence first; only then run `promote --qa-reviewed`.
4. Never change `trading/memory/policy.json` or risk limits; propose changes to the owner via an approval request.
5. Summarize for the user in a few lines; log events.
