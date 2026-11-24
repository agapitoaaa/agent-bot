# Plan: agent-spend-lens (narrow direction, approved A2)

Date: 2026-11-24. Author: Planner (Marlowe). Input: research.md. Status: draft for human approval.
office: stage=planning, desk=planner, sprite=planner

## 1. One-line pitch
A local, read-only CLI plus static HTML report that attributes estimated USD cost to each stage/agent of a multi-agent flow run (joining this repo's `runs/*.jsonl` event logs with Claude Code session JSONL), and flags likely waste or runaway behaviour with explainable heuristics.

## 2. Goals
1. Per-flow-stage cost: for a given `run_id`, show estimated cost and tokens per step/agent.
2. Waste/runaway flags: a small set of transparent heuristics, each with the evidence lines that triggered it.
3. Fully local, read-only, no network at runtime, no spend.
4. Useful on this repo's own flows first; reusable by others only as a side effect.

## 3. Non-goals (what we are NOT doing)
- No general per-day/per-session/per-model viewer (ccusage and agentsight already cover it).
- No hooks, MCP server, OpenTelemetry, proxy or SDK instrumentation. Log-reading only.
- No Codex/OpenCode/other-agent support in v1.
- No live/real-time view, no web server beyond opening a static file.
- No billing-grade accuracy; no budgets, alerts or enforcement.
- No fetching live prices; no cloud, hosting, accounts, telemetry.
- No publishing (GitHub public repo, npm/PyPI, Product Hunt, blog) without explicit human sign-off.
- No office-view integration in v1 (only keep output keys compatible with `office:` roles).
- No market-validation work; demand for this angle is unproven and is accepted as a risk.

## 4. Constraints (from research, binding)
No spend; no deploy; read-only on logs, never modify/transmit; no runtime network; USD always labelled "estimate" with price-table date and attribution policy shown; tests use synthetic data only (no real transcripts committed); real log schema verified before parser design; redact prompt/code text by default in reports.

## 5. User stories
- U1. As a flow author, I run `spend-lens run <run_id>` and see cost per step/agent so I know which stage is expensive.
- U2. As a flow author, I see which Claude sessions/subagent files were matched to which step, and which could not be matched, so I can trust (or distrust) the numbers.
- U3. As a user, I get warnings like "step 4 re-read the same file 9 times" or "step 3 consumed 5x the median step cost", each with pointers to evidence, so I can fix a runaway.
- U4. As a privacy-conscious user, I am sure the tool never writes to or sends my logs and the report contains no prompt text unless I opt in.
- U5. As a reader of the report, I always see "estimate", the price-table date and the attribution policy.

## 6. Acceptance criteria
Schema and parsing
- AC1. A written `docs/spend-lens-log-schema.md` documents fields actually observed in a real local session file (usage/token fields, model, sidechain/subagent marker, tool_use for Task/Skill, timestamps, subagent file layout) and the `runs/*.jsonl` event schema (observed: `ts, run_id, type, flow, step, agent, msg`; types incl. `run_started, step_started, step_done, escalation`). Unknown/missing fields are listed as such.
- AC2. Parser tolerates unknown fields, malformed lines and missing usage (counted and reported, never crashes).
Attribution
- AC3. Attribution policy is written down and implemented as exactly one policy: assign a Claude message to a flow step when its timestamp falls in that step's `step_started`..`step_done` window (and, if present, subagent identity matches the step's agent). Anything outside any window or ambiguous goes to an explicit "unattributed" line, never guessed.
- AC4. Per-step totals plus unattributed sum exactly to the run total (tested).
- AC5. Cost = tokens x hand-maintained price table (input, output, cache write, cache read) in a dated data file; unknown model yields tokens with cost "unknown", not a guess.
Waste heuristics (v1 set, each toggleable and with thresholds in config)
- AC6. H1 repeated reads: same file/tool-call signature repeated >= N times within a step.
- AC7. H2 outlier step: step cost > K x median of other steps in the run (needs >= 3 steps).
- AC8. H3 low cache reuse: cache-read share of input tokens below a threshold on large contexts.
- AC9. H4 retry loop: same tool call + error pattern repeated >= N times consecutively.
- Each flag lists evidence (line numbers/message ids), not prompt text, and is labelled "heuristic".
Output and safety
- AC10. CLI prints a table; `--html out.html` writes a single self-contained static file (no external scripts/fonts/network); `--json` for machines.
- AC11. Tool opens log files read-only; a test asserts file hashes unchanged and that no network module is imported/used.
- AC12. All fixtures synthetic; a check fails if fixtures contain strings matching real-session path patterns.
- AC13. Demo on this repo's own `runs/` logs produces a report, reviewed by a human before anything leaves the repo.

## 7. Milestones
- M0 Schema first (gate). Inspect real local files (`~/.claude/projects/-home-user-agent-bot/*.jsonl`, subagent layout, `runs/*.jsonl`); write schema doc and attribution policy. Exit: AC1, AC3 on paper; human glance at policy.
- M1 Core engine. Parser, price table, step-window attribution, totals, CLI table. Exit: AC2, AC4, AC5, AC10 (CLI), AC11, AC12.
- M2 Heuristics. H1 to H4 with evidence. Exit: AC6 to AC9.
- M3 Report. Static HTML + JSON, estimate labelling, redaction default. Exit: AC10, U5.
- M4 QA + dogfood. Run on own runs, tune thresholds, final review. Exit: AC13, all ACs green. Stop; publishing is a separate human decision.

## 8. Ordered task list
Stack suggestion: Python 3 stdlib only (zero dependencies, no install cost). Frontend here = the static HTML report.

| # | Task | Owner | Depends | Milestone |
|---|------|-------|---------|-----------|
| 1 | Inspect real session + subagent files and `runs/*.jsonl`; write `docs/spend-lens-log-schema.md` (observed vs unknown) | backend | none | M0 |
| 2 | Write attribution policy + price-table format (dated, per-model, 4 token classes) in `docs/` | backend (review: qa) | 1 | M0 |
| 3 | Define test strategy and synthetic fixture generator (multi-step run, subagents, missing usage, bad lines, unknown model, overlap windows) | qa | 1 | M0 |
| 4 | Report/CLI output spec: table columns, estimate banner, unattributed line, flag presentation, redaction default (wireframe, light/dark, phone-width) | designer | 2 | M0/M1 |
| 5 | Tolerant JSONL parser for sessions and run events | backend | 1 | M1 |
| 6 | Price table data file + cost calculator, unknown-model handling | backend | 2 | M1 |
| 7 | Step-window attribution + unattributed bucket + sum invariant | backend | 5, 6 | M1 |
| 8 | CLI (`run <run_id>`, `--json`, `--html`) | backend | 7 | M1 |
| 9 | Tests for parser, cost, attribution invariants, read-only and no-network assertions | qa | 3, 5-8 | M1 |
| 10 | Heuristics H1 to H4 with evidence output + config thresholds | backend | 7 | M2 |
| 11 | Heuristic tests incl. false-positive cases on clean synthetic runs | qa | 3, 10 | M2 |
| 12 | Static HTML report from JSON (self-contained, accessible, no external assets) | frontend | 4, 8 | M3 |
| 13 | Report verification: opens offline, no network requests, redaction default, labels present | qa | 12 | M3 |
| 14 | Dogfood on this repo's `runs/`; review thresholds; list known limitations in README section | backend + qa | 10, 12 | M4 |
| 15 | Final review against AC1-AC13; hand to human | qa | 14 | M4 |

## 9. Risks
| Risk | Level | Mitigation |
|---|---|---|
| Log format undocumented and shifting by version | med | M0 gate; tolerant parser; record Claude Code version in report; unknown fields reported |
| Time-window attribution wrong when steps overlap or run in parallel, or subagent runs outlive step | med-high | Explicit unattributed bucket; show match confidence and counts; no guessing; document limitation |
| Misleading numbers (cache/shared context, stale prices) | med | "Estimate" labels everywhere; dated price table; unknown model shown as unknown |
| Heuristics produce noisy false positives | med | Few heuristics, evidence required, thresholds configurable, labelled "heuristic" |
| Product already covered/vendor ships native attribution (research: high) | high | Scope is own-flow use; no marketing effort; re-check vendor features before any publish decision |
| Run events may not include session ids, so join relies on timestamps/cwd | med | Verify in M0; if joining is too weak, report as a finding and ask human before continuing |
| Privacy: real transcripts leaking into fixtures, reports | med | Synthetic fixtures only, fixture check (AC12), redaction default |
| Demand for narrow angle unproven | high (unknown) | Accepted; goal is value for this repo; kill after M1 if stage attribution is not trustworthy |

## 10. Kill / pause criteria
- After M0: if run events and session logs cannot be joined without guessing, stop and escalate.
- After M1: if unattributed share on own runs is persistently large (suggest > 40%), stop and escalate rather than polish.

## 11. Open decisions for the human
1. Language/stack: Python 3 stdlib (recommended) vs Node?
2. Location: new top-level dir in this repo (e.g. `agent-spend-lens/`) vs separate repo later; and should it also have a `flows/` entry and `office:` role?
3. Is own-repo usefulness a sufficient success bar (per research Q2), with kill criteria in section 10?
4. Confirm v1 attribution policy (step time-window, unmatched = "unattributed") before M1 starts.
5. Any later publishing is out of this plan; confirm it stays a separate decision.
