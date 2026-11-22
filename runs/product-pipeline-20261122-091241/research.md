# Research brief: P2 Local-first agent spend lens

Date: 2026-11-22. Author: Researcher (Nova). Scope: approved idea P2 only.
Method: WebSearch snippets only (7 searches). I did NOT open repos or docs pages, so activity, license and accuracy claims below are mostly unverified. "Fact" = stated in a cited search result; "Assumption" = my inference.

## 1. Recommendation (read first)

**Go with a narrower angle, or no-go on the generic version.** The generic pitch ("local tool that shows Claude Code cost by session/subagent from JSONL logs") is already well served by free tools, and the vendor is shipping native breakdowns. My scout note called the space crowded; the check confirms it is more crowded than I implied. I should not have rated it medium-confidence without this check.

What is still plausibly open (weakly evidenced):
1. **Per-task attribution** (cost of "a unit of work" such as a flow stage or a user-defined task boundary), rather than per-session/per-model/per-day. Several tools do session and subagent; "task" is mostly estimated or absent.
2. **Run-log-aware / flow-aware attribution** for people who orchestrate multi-agent flows like ours (stage = agent = cost line), joined with our own `runs/` event logs.
3. **Runaway/waste detection with explanations** (loops, repeated large re-reads, cache misses) as local heuristics. Some tools show cache efficiency; I found no clear evidence of runaway detection, but did not check deeply.

If the human wants a differentiated product, the narrow angle is "per-flow-stage cost for multi-agent workflows plus waste heuristics". If the goal is only a general spend viewer, no-go: use ccusage/agentsight.

## 2. Competitor check

| Tool | Link | Does | Does not (per snippets) | License / price | Activity |
|---|---|---|---|---|---|
| ccusage (ryoppippi) | https://npmjs.com/package/ccusage | CLI over local Claude Code JSONL: daily, monthly, per-session, 5-hour billing blocks, live view, JSON, per-model cost. Companion tools for Codex CLI, OpenCode, pi-agent. | No per-task or per-skill attribution found; web tool/image usage excluded from reports; multi-machine sync is manual. | Free, npm (version 15.7.0 seen; license not verified) | Many forks and ports (ccusage-rs, ccstat), suggests high adoption. Dates not verified. |
| agentsight (RealNerd) | https://github.com/RealNerd/agentsight | Reads `~/.claude/projects/` JSONL, CLI plus web dashboard, cache efficiency, optional cost, per-model comparison, session/project diagnosis, JSON output. Read-only. | Attribution method not verified; per-skill unknown. | Free, Homebrew/Rust (license not verified) | Not verified. |
| agent-cost-mcp | https://socket.dev/npm/package/@vk0/agent-cost-mcp | Local MCP server; `get_subagent_tree` gives parent plus subagent tree with per-branch cost. | MCP-only interface; no web report noted. | Free (license unverified) | Not verified. |
| tokenscope | https://mcpservers.org/servers/wartzar-bee/tokenscope | Read-only CLI/MCP: cost by model, subagent spend, context attribution. | Per-tool/per-file attribution listed as roadmap. | Free | Not verified. |
| CodeBurn | https://github.com/iquantecho/codeburn (several forks) | Hooks into Claude Code, Codex, OpenCode; real-time TUI with subagent hierarchy; listed on Product Hunt. Exchange-level attribution estimated by prompt-size weighting. | Estimated, not exact attribution. | Free (unverified) | Product Hunt "launched this week" snippet; date not verified. |
| agentacct | https://github.com/mikehasa/agentacct | Strict attribution: shows a gap when a link cannot be proven. | Details unverified. | Unverified | Unverified. |
| cc-token-usage (Rust) | https://docs.rs/crate/cc-token-usage/1.2.2/source/README.md | Parses all session files including subagent files in old and new layouts. | Unverified. | Free | Version 1.2.2 seen. |
| cast-observe, ContextAnalyzerTerminal (CAT) | via search snippet only; no URL verified | Hook-based; per-subagent-dispatch rows; CAT attributes cost per tool call by correlating hooks with statusline. | Needs hooks installed (not purely log-reading). | Unverified | Unverified. |
| Others seen in results | tokscale https://github.com/junhoyeo/tokscale ; ToolBurn https://github.com/CodePager/ToolBurn ; clawmetry https://github.com/vivekchand/clawmetry ; superbased-observer https://pypi.org/project/superbased-observer/1.28.0/ | Not examined. | | | |
| Claude Code OpenTelemetry | https://code.claude.com/docs/en/monitoring-usage | Official: metrics `claude_code.cost.usage`, `claude_code.token.usage`, custom attributes (team/cost center). | Needs a telemetry backend; third parties call cost an estimate. An issue (claudeissues.com #83430) reports subagent attribution missing from metrics; unverified. | Free feature | Official docs. |
| Claude Code native `/usage` breakdown | https://blog.serverworks.co.jp/2026/05/25/200000 ; https://dev.to/jessyt/claude-code-now-shows-exactly-where-your-usage-goes-32d7 | Per-category share of usage: skills, subagents, plugins, MCP servers (Pro/Max/Team/Enterprise). Sources disagree: CLI v2.1.149 (about 2026-05-22) vs VS Code v2.1.174 (June 2026). | Share of plan limits, not dollars per task; Claude Code only. | Included with plan | Shipped. |
| Opik cost intelligence (Comet) | https://www.comet.com/docs/opik/cost-intelligence/overview | Cost tracking for LLM apps. | Cloud/self-host platform, not local log reader (not examined deeply). | Unverified | Unverified. |
| Langfuse/Helicone-style | not searched this round | SDK/proxy-based tracing. | Require instrumentation, not log-reading. | n/a | Not verified; flagged as gap in my check. |

Also: Claude Code issue #22625 "Per-Subagent Token Usage Tracking" was opened 2026-02-02 and closed 2026-03-16 as Resolved (https://claudeissues.com/issue/22625-feature-per-subagent-token-usage-tracking). A SitePoint article claims an `--attribution` flag writing `.claude/attribution.json` with per-subagent cost (https://www.sitepoint.com/claude-code-june-2026-10-new-features-devs-need-to-know/). Single secondary source; unverified. If true, it further erodes the core gap.

### Gap assessment
- Per-session, per-model, per-day cost from local logs: **fully served, free.**
- Per-subagent: **served** by several free tools and likely by vendor features.
- Per-skill: **partly served** by native `/usage` (as plan-limit percentages), not as dollars from logs. Weak gap.
- Per-task (user-defined unit of work): **not clearly served**; this is the thin gap. Whether people want it is unproven.
- Runaway-session detection: **not clearly served**; unproven demand.
- Fully local: **already the norm** for ccusage, agentsight and others. Not a differentiator.
- Demand evidence: many DEV Community posts about hidden subagent costs (e.g. https://dev.to/openclawlabs/i-analyzed-my-claude-code-sessions-and-found-143-in-hidden-agent-costs-heres-the-breakdown-3d97, https://betterstack.com/community/guides/ai/claude-code-token-costs/) show interest, but many competing tools appearing is also a sign the niche is saturated. Caution: I may be mistaking buzz for demand (my known blind spot).

## 3. Target users and pain (assumption unless noted)
- Individual developers and small teams on API billing or capped plans who see a large bill or hit limits and cannot tell which session, subagent, skill or task caused it. Sourced: blog posts above describe exactly this; no survey data found.
- Multi-agent workflow builders (like this repo) who want cost per stage. Assumption; evidence is only our own use case.
- Not verified: willingness to adopt another tool when ccusage is the de facto default and `/usage` is native.

## 4. Log data available locally

Verified at doc/source-snippet level only; I did not inspect a real session file. The planner/builder must inspect real files from the installed version first.
- Location: `~/.claude/projects/<project-slug>/<session-uuid>.jsonl`, one JSON object per line, with `type` and `uuid` on every line (community doc: https://evilpiepirate.org/forge/kent/consciousness/raw/branch/master/doc/claude-code-transcript-format.md). Community, not official.
- Assistant entries hold the model response in a `message` object. Parser sources (e.g. https://docs.rs/crate/claude-code-transcripts/0.1.3/source/src/types.rs) show `is_sidechain` marks subagent messages.
- Subagent sessions appear as separate `agent-<id>.jsonl` files beside the main session (older flat layout) and a newer nested layout (per cc-token-usage README). Layout varies by version.
- Token fields: tools like ccusage and cc-token-usage clearly compute tokens and cost from the logs including cache tokens, so `usage` with input/output/cache data exists. I found **no field-level spec** and cannot confirm exact names. Assumption: `message.usage` with input, output, cache creation and cache read tokens, plus `message.model`.
- Tool calls and skill invocations: assumed to appear as `tool_use` content blocks (Task/Agent, Skill); unverified.
- Not in logs: hook-injected text is not captured (community doc). Cost in USD is not stored; it must be computed from a price table (assumption, consistent with ccusage's "estimated costs").
- Another caveat: issue claudeissues.com #48439 reports background subagent events missing usage data in stream-json; logs may have gaps. Unverified for JSONL.
- Other agents (Codex CLI, OpenCode): ccusage has companions, implying local logs exist; formats not examined.
- Stability: no official schema; community notes warn format can change between versions. Real risk.

## 5. Feasibility (assumptions)
- Small team, local CLI plus static/local HTML report, no cloud, no spend: **feasible**, effort M for a Claude-Code-only v1 (parser, price table, session/subagent/skill roll-up, simple report). Python or Node stdlib; no paid services.
- Demoable on this repo's own `runs/` logs and our own `~/.claude` data, only if present in the sandbox (not checked).
- Hard part: defining "task" boundaries and attributing shared context/cache cost fairly. CodeBurn estimates by weighting; agentacct refuses to guess. Pick one policy explicitly.
- Price table must be hand-maintained offline (no live fetch needed); stale prices are a risk. Cost is an estimate, not billing.

## 6. Risks
- Saturated space with free, adopted tools and a native vendor breakdown (high).
- Vendor may ship per-subagent attribution natively (SitePoint claim; #22625 closed as Resolved) (high).
- Undocumented, shifting log format (medium).
- Misleading numbers: cache/shared-context attribution is inherently approximate (medium).
- Privacy: logs contain prompts and code; report must stay local, never upload, and redact by default (medium).
- No evidence of demand specifically for per-task attribution (high unknown).

## 7. Constraints for the planner
- No spend: no paid APIs, services, hosting or subscriptions; no cloud account.
- No deploy; local CLI and local report only.
- No public posting (repo publish, package registry publish, Product Hunt, blog) without human sign-off.
- Read-only on user logs; never modify or transmit them; no network calls at runtime.
- Label all USD figures as estimates; document the price table date and the attribution policy.
- Test on synthetic or our own redacted logs; do not commit real personal transcripts.
- Verify the actual JSONL schema against a real file before designing the parser.

## 8. Open questions
1. Does the human want a general spend viewer (already served) or the narrow per-task / per-flow-stage plus waste-detection angle?
2. Is a reusable fit for this repo's own flows (stage cost in `runs/`) a sufficient goal on its own, even if not a market product?
3. Real field names for usage, model, skill and subagent calls in the installed Claude Code version (needs a sample file).
4. Do agentsight, agent-cost-mcp and CodeBurn already do per-task or runaway detection? (Read their READMEs; not done.)
5. Is `--attribution` / `attribution.json` real and in which version? Does it make local log parsing for subagents redundant?
6. Are the native `/usage` breakdown and OTel subagent attribution sufficient for the target users?
7. Licenses and maintenance dates of the competitors (not verified).
8. Langfuse/Helicone-class tools were not checked; likely instrumentation-based rather than log-based.
9. Support scope: Claude Code only, or also Codex/OpenCode?

## 9. Confidence
Competitor existence: high (multiple independent results). Competitor feature depth, license and activity: low (snippets only). Log schema field names: low. Demand for the narrow angle: low. Native-vendor erosion: medium (conflicting sources on version and platform).
