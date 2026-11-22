# Idea backlog

Owned by the `researcher`. Statuses: `proposed` -> `approved` | `rejected` | `parked`. Only the human changes a status to approved/rejected.
Never re-pitch a rejected idea; check this file before every scouting round.

<!-- entries appended below: ### ID. Title [status] -->

Scout round 2026-11-22 (focus: broad). Search tool returned many vendor blogs; sources flagged where weak.

### P1. Agent-file Linter: drift and rot checker for AGENTS.md / CLAUDE.md / skills [proposed]
**Concept:** A CLI plus GitHub Action that checks agent instruction files against the real repo (referenced paths, scripts, packages exist), flags AGENTS.md vs CLAUDE.md divergence, bloat and contradictory rules.
- **Trend evidence:** Many posts describe "rules-file rot" and say no tool validates these files against reality: [Getunblocked, Rules-File Rot](https://getunblocked.com/blog/rules-file-rot), [Thoughtworks Radar, agent instruction bloat](https://www.thoughtworks.com/en-sg/radar/techniques/agent-instruction-bloat), [Addy Osmani, Audit your Agent files](https://addyosmani.com/blog/audit-your-agent-files/), [DEV, "Your CLAUDE.md is a lie"](https://dev.to/mjkloski/your-claudemd-is-a-lie-2h9j). An arXiv study ([2606.09090](https://arxiv.org/html/2606.09090)) reports AGENTS.md at about 43% and CLAUDE.md at about 30% of agent config files. Post dates were not visible in search results.
- **Who / pain:** Teams and solo devs using coding agents; stale instructions are trusted blindly and fail silently.
- **Why now:** Agent config files are now mainstream and growing; the "audit" advice exists but the tooling is manual.
- **Our angle:** We live this problem (this repo has CLAUDE.md, skills, agents, flows). Fully buildable and demoable as software, dogfood-able on our own repo, no spend or deploy needed to demo.
- **Effort:** M. **Main risk:** Thin moat; a big vendor (or a Claude Code/GitHub feature) could absorb it, and some free scripts may already exist (not checked).
- **Confidence:** Medium-high on the need; unverified: existing competing tools, actual willingness to pay or install.

### P2. Local-first agent spend lens: per-task token cost attribution from agent logs [approved]
**Concept:** Reads local coding-agent session logs and shows cost by task/skill/subagent, detects runaway or wasteful sessions, with no cloud account needed.
- **Trend evidence:** Complaints that token counts appear only at session end and are opaque ([WebProNews on Claude Code billing, undated](https://www.webpronews.com/claude-codes-hidden-cost-problem-developers-sound-the-alarm-over-anthropics-opaque-token-billing/)); bills rising despite lower token prices ([Elastic](https://www.elastic.co/blog/token-costs-ai-bills)); [LangChain, fix your coding agent bill](https://langchain.com/blog/fix-your-coding-agent-bill); [1Password, AI spend hangover](https://1password.com/blog/how-to-survive-the-ai-spend-hangover); [Kilo Code on spending caps](https://dev.to/kilocode/stop-looking-for-ai-coding-spending-caps-42d9). Enterprise vendors (Datadog, IBM, WorkOS) are also publishing on this.
- **Who / pain:** Individual devs and small teams who cannot see why a session was expensive.
- **Why now:** Agentic usage makes spend unpredictable; the discourse is loud.
- **Our angle:** Local, private, per-skill attribution fits our skill/subagent structure; demoable on our own run logs (`runs/`).
- **Effort:** M. **Main risk:** Crowded space with funded players; log formats vary by tool and may change.
- **Confidence:** Medium. Mostly vendor/blog sources, dates unclear; could not verify demand for a free local tool vs built-in vendor dashboards.

### P3. MCP config auditor: permission and trust scanner for local MCP setups [proposed]
**Concept:** Scans a user's MCP client configs and servers for over-broad scopes, unauthenticated or exposed endpoints, risky tool descriptions (poisoning patterns) and the "lethal trifecta" combination, then outputs a least-privilege report.
- **Trend evidence:** [Microsoft Security, State of MCP security in 2026](https://techcommunity.microsoft.com/blog/microsoft-security-blog/the-state-of-mcp-security-in-2026/4531327); [CSA, 7 MCP risks for CISOs (2026-06-15)](https://cloudsecurityalliance.org/blog/2026/06/15/7-mcp-risks-cisos-should-consider-and-how-to-prepare); CSA guide cites about 7,000 exposed MCP servers, roughly half unauthenticated, and 30+ CVEs in Jan-Feb 2026 (secondary citation, not verified at source).
- **Who / pain:** Developers and small security teams wiring many MCP servers with no review step.
- **Why now:** MCP adoption is wide and the security literature is converging on concrete checks.
- **Our angle:** Static analysis of config files is feasible without network access; clear checklist from public guidance.
- **Effort:** M. **Main risk:** Security tooling credibility; false confidence; fast-moving threat landscape and incumbents (gateway vendors).
- **Confidence:** Medium. Risk is well documented; unverified: whether individuals/SMBs want a scanner vs enterprise gateways.

### P4. AI Act "evidence pack" for SMEs: AI-use inventory, disclosure and vendor-request generator [proposed]
**Concept:** A guided web app producing an AI system inventory, written risk classification rationale, Article 50 disclosure text and vendor documentation request letters, exported as documents.
- **Trend evidence:** Article 50 transparency rules applied from 2 Aug 2026 ([TechRadar](https://www.techradar.com/pro/celebrating-the-ai-act-delay-the-eu-ai-acts-chatbot-and-content-rules-apply-this-week)); IAPP says SME gaps are operational proof (inventories, classification rationale, oversight assignments) ([IAPP](https://iapp.org/news/a/eu-ai-act-deployer-evidence-gaps-smes-will-miss-before-2-aug-2026)); high-risk deadlines delayed under the omnibus ([ACT](https://actonline.org/2026/08/06/what-european-startups-and-smes-should-know-as-the-ai-omnibus-enters-into-force/)); [DIGITAL SME Alliance](https://digitalsme.eu/why-delaying-ai-act-enforcement-is-essential-for-european-smes) says implementation tools are incomplete.
- **Who / pain:** EU-facing small businesses using chatbots/AI content with no compliance staff.
- **Why now:** Transparency duties are live; later deadlines are in flux, creating confusion.
- **Our angle:** Template/form-driven app is easy to build and demo; no spend needed.
- **Effort:** M. **Main risk:** Legal liability and accuracy (we are not lawyers); many vendor compliance platforms already exist; delay may reduce urgency.
- **Confidence:** Low-medium. Many sources are vendor or DEV posts; the omnibus effective date (one source says 2 Dec 2026) was not confirmed officially.

### P5. Accessibility-first quick-fix auditor for small EU sites (EAA) [proposed]
**Concept:** Scans a small business site for common WCAG 2.1 AA failures and generates plain-language, code-level fixes plus an accessibility statement draft.
- **Trend evidence:** EAA enforcement began 28 Jun 2025 per one source; notices in France, surveillance in Sweden, first lawsuits in French commercial court, per [Level Access](https://www.levelaccess.com/blog/european-accessibility-act/) and [AllAccessible 2026 update](https://allaccessible.org/blog/european-accessibility-act-one-year-on-2026-enforcement-update); [Eye-Able, 26 Jun 2026](https://eye-able.com/da/blog/one-year-of-the-eaa-where-businesses-still-fall-short) cites 91% of tested EU homepages with issues (automated, vendor study).
- **Who / pain:** Small web shops and agencies selling to EU consumers; most tools only list problems.
- **Why now:** Enforcement is starting, standard EN 301 549 update reported Sept 2026 (unverified).
- **Our angle:** Our pipeline builds and tests web products, so we can ship and test it; LLM-written fixes differentiate from checkers.
- **Effort:** M-L. **Main risk:** Very crowded (overlay and audit vendors); microenterprises are exempt; I found no verified fines against small firms.
- **Confidence:** Low-medium; fine claims and vendor stats unverified.

