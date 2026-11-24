# Slime Strip: plan (stage 2, planner)

Author: Marlowe (planner). Date: 2026-11-24. Run: game-slime-strip-20261124.
Inputs: `runs/game-scout-20261124-161825/g1-deep-dive.md` (Nova), G1 pitch and shared notes in `ideas/backlog.md`, `ideas/focus.md`.
Owner decision A8: approve Slime Strip; Steam Market scope **C = no Market in v1**. The owner has also said they WANT Steam Market trading, so v1 is built Market-ready and a v1.x milestone for Option A is planned but NOT built in v1.

Marking: **[U]** = unverified (research saw search snippets only; nobody opened Steamworks pages or tested the Godot behaviours). **[A]** = assumption or estimate.

office: stage=planning, desk=planner, sprite=planner

## 1. Goals
1. Ship a playable Godot 4.x idle loot ARPG that lives on a thin, truly transparent, click-through strip above the taskbar.
2. Win on what reviews punish elsewhere: near-zero idle CPU (sleep when hidden or a fullscreen app is active), a resizable strip that does not block the taskbar, multi-monitor safety, offline progress, local-only saves.
3. Deep-enough loot: 4 rarities, random affixes, 6 equipment slots, salvage and reroll sinks.
4. Make a later Steam Market (Option A) cheap to add: stable item ids, per-definition metadata, an unused `tradable` flag, and an economy that can absorb a tradable layer without a rewrite.
5. All art and audio generated in code. No paid assets, no spend by agents.

## 2. Non-goals (v1)
- **No Steam Market, no Steam Inventory calls, no trading UI, no mock market screen shipped to players.** (A local sim of sinks/sources is a QA tool, not a feature.)
- No server, backend, accounts or cloud anything. No Option B (bridge) in any version before v1.x review.
- No prestige/rebirth in v1 (reviews cite prestige bugs).
- No paid random boxes, keys, or any real-money randomised items, ever.
- No GodotSteam, achievements, cloud saves in v1.0 playable milestones (store integration is M5, behind owner sign-off).
- No live AI-generated content in-game. No external art/audio assets.
- No mobile, web export, Mac/Linux polish (Windows is the target; others best effort) [A].
- No publishing, store page, trailer or posting without owner sign-off.

## 3. User stories
- As a player, I want a slim strip above my taskbar that I can see through and click through, so my work is not blocked.
- As a player, I want the game to cost almost nothing while I work or play a fullscreen game, so my laptop battery and framerate are fine.
- As a player, I want my slime to fight on its own and drop loot, so I get a reward when I glance down.
- As a player, I want to click the slime or a toast to open a compact equip popup, compare an item and swap it.
- As a player, I want progress while the game was closed (capped), so I come back to something.
- As a player, I want to pick which monitor and edge the strip uses, resize its height, and toggle it with a hotkey.
- As a player, I want my save to survive crashes and updates, so loot is never lost.
- As the owner, I want items to have stable ids and a `tradable` flag so Steam Market (Option A) can be added later without migrating saves.
- As the owner, I want a clear go/no-go on cost and sign-off before any money or publishing step.

## 4. Acceptance criteria (v1 playable = M1; Steam-ready = M4)
Window and performance (M0 gates these first):
- AC-W1: Window is borderless, transparent, always-on-top; transparent regions pass clicks through; only slime, loot toasts and a handle are clickable. Verified by hand and by an automated hit-test script where possible.
- AC-W2: Window is NOT full monitor size (kept slightly smaller to avoid the exclusive-fullscreen flip) [U, per forum reports].
- AC-W3: When hidden (hotkey) or covered/fullscreen app active, the game sleeps: tree paused, low FPS cap, simulation via offline model. Measured idle CPU recorded in `projects/slime-strip/docs/perf.md` with method and machine. Target: under 1% of one core when asleep, under 3% awake with no combat [A target; measure, do not claim].
- AC-W4: Strip survives focus loss and click events without dropping behind other windows (known Godot pitfall) [U].
Gameplay:
- AC-G1: 3 enemy archetypes (melee, ranged, tank), auto-combat, slime squash/stretch.
- AC-G2: 4 rarities; each item = base type + 1 to 4 random affixes drawn from data-file pools (deterministic with a seed for tests).
- AC-G3: 6 slots (weapon, hat, body, trinket x2, core); equip popup compares stats.
- AC-G4: Offline progress computed at launch, capped at 8 to 12 h, deterministic from last-seen time, never mints anything marked tradable.
- AC-G5: Salvage and reroll exist as sinks.
Data and save:
- AC-D1: Every item definition has a stable string id (never reused, never renamed), schema version, and metadata including `tradable` (default false, ignored by v1 logic) and `marketable` (default false).
- AC-D2: Save is versioned, written atomically (write temp, then rename), with one rolling backup; loading an older version migrates; corrupt save falls back to backup.
- AC-D3: Item instances reference definitions by id; affixes live on the instance; unknown ids on load are preserved, not deleted.
Quality:
- AC-Q1: Headless unit tests for loot rolls, affix pools, save/load/migration, offline calc. Balance simulation script runs N hours of simulated play and reports drop rates, power curve, sinks vs sources.
- AC-Q2: A soak test: 24 h wall-clock (or accelerated) with no memory growth beyond a set bound [A bound to be set in M0].
- AC-Q3: No network calls in v1.0 (verified by grep and a run with network blocked).

## 5. Market-ready item data model (v1 design, Market unused)
Designer + backend-engineer own this; frontend consumes it. Lives in `projects/slime-strip/data/items/` (JSON/tres, data-driven) with a schema doc.
- **Definition** (`ItemDef`): `id` (stable, e.g. `core.forest_ember`), `schema`, `kind` (gear | material | relic | core), `rarity`, `slot`, `base_stats`, `affix_pool_ids`, `name_key`, `desc_key`, `icon_recipe` (code-drawn icon parameters, so icons can be rendered to PNG later), `source_tags` (drop/exchange/salvage), `tradable: false`, `marketable: false`, `steam_def_id: null` (reserved), `drop_policy` (timed | combat | recipe), `sink_value`, `retired: false` (retire, never delete).
- **Instance**: `uid` (random 128-bit), `def_id`, `affixes[]`, `rolled_at`, `origin` (combat | offline | recipe | grant), `bound: true`. Gear instances carry random affixes and are permanently untradable by design (Steam dynamic props are cleared on trade [official snippet via research, U]).
- **Rules that keep Option A cheap later**: (1) tradable-candidate items are affix-less fixed definitions (relics/cores) kept in a separate `kind`; (2) all grants go through one `grant(def_id, origin)` function so a kill switch and a Steam-timed source can replace it; (3) offline gains cannot grant `kind=relic`; (4) no code reads `tradable` in v1 except a unit test asserting it is false everywhere; (5) a `economy_sim` script already models drop timers, caps and exchange recipes so Option A balance is not invented from nothing.

## 6. Milestones
Time figures are agent-effort estimates [A], not commitments.

### M0: window-tech spike (gate for everything else), about 2 to 3 days
Deliverable: `projects/slime-strip/spike/` plus `docs/spike-report.md`. Questions answered with measurements:
1. Transparent, borderless, always-on-top strip with `mouse_passthrough_polygon` and per-region click handling on Windows; behaviour on focus loss and after clicks [U].
2. Sleep when hidden: `low_processor_usage_mode`, FPS cap, paused tree. Measured idle CPU (method, machine, Godot version, awake vs asleep).
3. Fullscreen-foreground-app detection feasibility (GDExtension or a documented alternative); fallback is manual hide hotkey plus pause-on-lost-focus.
4. Strip sizing rules (not full monitor), DPI scaling, multi-monitor pick; note what cannot be tested in our sandbox (real multi-monitor, Windows hardware) [A: sandbox is likely Linux without a Windows display; this may require owner or tester machine time].
5. Steam overlay compatibility cannot be tested without a Steam build; mark as deferred to M4 [U].
Exit: written pass/fail on each question, with numbers. **See kill criteria K1 to K3.**

### M1: first playable, about 4 to 7 days after M0 passes
Strip window (from M0), 3 enemies, auto-combat, loot with 4 rarities and random affixes, equip popup, salvage/reroll, offline calc, versioned save, market-ready data model (section 5), unit tests and balance sim. Demo to owner as a local build or recorded capture. Zero spend.

### M2: depth and stability, about 1 to 2 weeks [A]
8 to 10 zones, bosses every N zones, mastery track, settings (monitor, edge, height, hotkey), synthesized audio, polish, soak tests, balance pass from simulation.

### M3: playtest hardening, about 1 week [A]
External or owner playtest on varied machines (multi-monitor, DPI, laptops). Fix CPU, focus and save issues. Perf doc finalised.

### M4: Steam-ready (needs owner sign-off BEFORE start)
GodotSteam (4.4+ GDExtension; versioning inconsistent [U]), store page assets rendered from code, achievements/cloud saves if wanted, Steam overlay compatibility test, AI-disclosure form review (code-drawn art; confirm at release [U]). Requires Steamworks partner account and $100 Steam Direct, both **owner-only**.

### M5: release (owner sign-off required)
Price decision applied, store page published by the owner, Next Fest/launch timing chosen by owner. Agents prepare checklists only.

### v1.x (MARKET) — NOT BUILT IN V1, owner-wanted, planned only
Option A: Steam Market via fixed definitions, no server. Start only after M5 (or M4 if owner prefers, a scope change) AND owner approval. Scope:
- 12 to 24 tradable, marketable affix-less relic/core item definitions in 3 to 4 rarities, uploaded as Steam itemdefs; granted via a `playtimegenerator` + `TriggerItemDrop` (Steam enforces intervals and per-user caps); weekly rotation; `ExchangeItems` recipes as sinks [official snippets, U].
- Wire `grant()` to Steam source; render relic icons from `icon_recipe`; flip `tradable`/`marketable` per def; kill switch (flip flags off, `FlushAssetAppearanceCache`) [U].
- First action is a verification task: open the Steamworks docs (owner's partner account) to confirm itemdef fields, limits, Market enablement/approval, fees (5% + 10% game fee assumed [U]), trade holds, and ask Valve via Steamworks about Market approval for a new app [U].
- Exit gate: economy sim plus a small real-money-free test with the owner account; owner approves go-live. Option B (server bridge) is out of scope and requires a separate plan.
- Known tradeoffs to tell the owner: affixes do not survive trade; earnings are unverified and likely modest; bot farming is limited only by Steam drop timing and the Steam $5 spend rule for players [U].

## 7. Ordered task list
Owners are roles; IDs are ordering. Tasks inside a milestone may run in parallel where noted.

M0
1. T0.1 designer: define strip dimensions, interaction regions (slime, toasts, handle), sleep/wake behaviour spec. (first)
2. T0.2 frontend-engineer: Godot project scaffold in `projects/slime-strip/`; transparent click-through strip prototype; focus-loss and drop-behind tests. (after T0.1)
3. T0.3 backend-engineer: measurement harness (CPU/memory sampling script, headless runner) and sleep-mode prototype. (parallel with T0.2)
4. T0.4 frontend-engineer + backend-engineer: fullscreen-app detection feasibility.
5. T0.5 qa-engineer: write the spike test matrix; run what the sandbox allows; list what needs real hardware; record numbers in `docs/perf.md`.
6. T0.6 release-engineer: confirm Godot version pin, export preset for Windows, CI/headless test command; confirm no spend.
7. T0.7 planner/orchestrator: go/no-go review against K1 to K3, then owner notification.

M1
8. T1.1 designer: item data model doc (section 5), rarity/affix tables, 3 enemy archetypes, equip popup wireframe.
9. T1.2 backend-engineer: `ItemDef`/instance schemas, `grant()` choke point, loot roller, affix pools, seeded RNG. (after T1.1)
10. T1.3 backend-engineer: versioned atomic save with backup and migration; offline calc. (after T1.2)
11. T1.4 frontend-engineer: auto-combat, slime/enemy code-drawn art, loot toasts, equip popup, salvage/reroll UI. (after T1.1, parallel with T1.2)
12. T1.5 frontend-engineer: integrate M0 window layer into the game scene.
13. T1.6 qa-engineer: unit tests (loot, affix, save, offline), balance simulation, assert `tradable` false everywhere, no-network check.
14. T1.7 release-engineer: reproducible local Windows build, version stamp, demo capture steps.
15. T1.8 designer: first-playable review checklist; owner demo notes.

M2 to M3
16. T2.x designer: zones, bosses, mastery, sinks balance; synthesized audio spec.
17. T2.x frontend-engineer: zones/bosses, settings UI, monitor/edge/height/hotkey, audio synth.
18. T2.x backend-engineer: mastery data, balance sim v2, save migration v2 tests.
19. T2.x qa-engineer: soak test, multi-monitor/DPI matrix, playtest session plan and bug log.
20. T3.x release-engineer: packaging, crash log capture, playtest build distribution (local, no publishing).

M4 and later (blocked on owner)
21. T4.1 release-engineer: Steam integration plan and checklist (no account actions by agents).
22. T4.2 frontend-engineer: GodotSteam integration behind a feature flag; overlay test with owner's build.
23. T4.3 designer: store assets generated in code; AI-disclosure notes.
24. T4.4 qa-engineer: Steam build regression, offline/online save sync tests.

v1.x Market
25. TM.1 backend-engineer: verify Steamworks facts (owner access), itemdef schema, `grant()` Steam source.
26. TM.2 designer: relic roster, rotation, exchange recipes, odds and disclosure copy.
27. TM.3 qa-engineer: economy sim (sources vs sinks, caps), kill switch drill.
28. TM.4 release-engineer: itemdef upload checklist, owner-approved go-live runbook.

## 8. Risks
| Risk | Likelihood / impact | Mitigation |
|---|---|---|
| Godot transparent click-through is flaky (passthrough polygon bugs, drop-behind, exclusive fullscreen flip) [U] | Medium / High | M0 spike gates all work; keep window slightly smaller than monitor; document workarounds; fallback to Unity UniWindowController only via owner decision |
| Cannot measure real CPU or multi-monitor in sandbox | High / Medium | Report sandbox limits honestly; ask owner/testers for hardware runs; do not claim unmeasured numbers |
| Fullscreen-app detection needs a native GDExtension, no Godot example found [U] | Medium / Medium | Fallbacks: hide hotkey, pause on focus loss, user setting; defer native detection to M2 if M0 shows cost |
| Crowded niche (1,566 idlers in 2026 per Steam Page Analyzer [U secondary]); median paid release earns little | High / High | Differentiate on CPU, strip UX, loot depth; set expectations that revenue is uncertain |
| Code-drawn art lacks charm and capsule appeal | Medium / Medium | Squash/stretch polish, strong rarity palette; early owner look at M1 |
| Market added later hits a migration problem | Low / Medium | Section 5 data model, single `grant()`, no tradable gear with affixes |
| Owner expectation gap: owner wants Market, v1 has none, and affix trading is not supported by Steam as documented [U] | Medium / Medium | Be explicit now; plan v1.x; show Option A tradeoffs |
| Option A bots/dupes/inflation at v1.x | Medium / Medium | Steam-timed drops, per-user caps, exchange sinks, kill switch, no paid random boxes; economy sim |
| Gambling/regional legal exposure | Low / High | Free timed drops only, disclose odds, no keys/boxes; legal review is outside agent competence and owner-owned |
| Steam overlay incompatibility with transparent window [U] | Medium / Low | Overlay optional; test in M4 |
| Save loss or corruption (the TBH lesson) | Low / High | Atomic writes, backup, migration tests, preserve unknown ids |
| Scope creep (prestige, trading, server) | Medium / Medium | Non-goals list; planner veto; changes go through owner decision |

## 9. Kill criteria
Stop and report to owner (do not push on) if any of these hold. Thresholds are proposals [A] for the owner to adjust.
- **K1 (window):** after 3 working days of M0, we cannot get a stable transparent, click-through, always-on-top strip on Windows in Godot 4.x (dropping behind windows, vanishing sprites, or clicks not passing through) with an acceptable workaround. Action: pause, report options (different Godot version, Unity, or stop). Switching engines needs owner approval.
- **K2 (CPU):** asleep CPU cannot be brought under 1% of one core on the reference machine, or awake idle exceeds 5%, with no path to fix. [A]
- **K3 (testability):** we cannot get any Windows-realistic measurement (owner or tester hardware) by the end of M0, so claims would be unverified. Action: proceed only with unverified flags and owner consent.
- **K4 (M1 fun check):** owner or QA playtest finds the loop not worth glancing at after the M1 demo and a one-iteration fix attempt.
- **K5 (spend):** any required step needs money or a legal identity not approved by the owner. Action: stop at that step.
- **K6 (Market, v1.x):** Steamworks verification shows Market listing is not self-serve or requires conditions we cannot meet, or Valve signals objection. Action: keep v1 as is and report.

## 10. Open owner decisions
1. **Price model:** free vs about $5 to $8 paid vs a higher band. Paid base raises bot-farm cost and helps with Steam's $5 spend rule for market access; free gets more installs but invites farming. Evidence is thin [U]. Needed before M4; recommend deciding before v1.x Market work.
2. **Steam Direct $100 and Steamworks partner account:** owner sign-off, and who holds the legal/tax identity. Agents never spend and never create accounts. Needed before M4.
3. **Publishing sign-off:** store page, Next Fest registration, release date and any public post. Needed before M5.
4. **v1.x Market go-ahead and timing:** approve Option A scope (affix-less relics, fixed definitions) and whether to ask Valve about Market approval earlier. Also confirm acceptance that rich random-affix gear stays untradable, with a kill switch and no paid random boxes.
5. **Hardware for testing:** can the owner (or a tester) run the M0 spike and M3 playtest on a Windows machine with 2 monitors? Without it, performance claims stay unverified.
6. **Engine fallback authority:** if K1 triggers, is the owner OK with evaluating Unity, or should we stop?
7. **Regional/legal:** whether to geo-limit the future Market; needs a human legal view, not agents.
