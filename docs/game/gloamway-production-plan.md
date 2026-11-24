# Gloamway: Production Plan

Author: Marlowe (planner). Date: 2026-11-24. Run: game-scout-20261124-161825.
Inputs: `game-design.md` (Sage), `g1-deep-dive.md` (Nova), `runs/game-slime-strip-20261124/plan.md` (earlier tick plan; M0 spike, kill criteria and Market-ready model reused and extended).
Owner decision A8 (already made): **Market scope C. No Steam Market in v1.** The item model is built Market-ready so Option A (tradable Keepsakes from Steam playtime drops, no server of ours) can be added as the clearly marked **v1.x Market milestone**.

office: stage=planning, desk=planner, sprite=planner

## 0. How to read this plan

| Tag | Meaning |
|---|---|
| [E] | Estimate. Agent-days are focused agent working days, uncertain by roughly plus or minus 40% for known work and worse for the window and Steam work. They are not commitments. |
| [U] | Unverified external behaviour (Godot on Windows, Steamworks, Valve rules). Nobody on this team has opened Steamworks pages or run Godot on Windows. Verify before relying on it. |
| [D] | A decision I made in planning. Owner can overrule. |
| [H] | Balance or performance hypothesis from Sage's design. Not tested. |

Plain statements up front:
1. This is a large game. Sage's full design (10 zones, 3 classes, 90-node tree, 40 uniques, about 95 code-drawn sprites) is a 1.x-sized game. This plan ships a **cut v1.0** and keeps the rest as v1.1 so the owner sees the whole path but the first release is reachable.
2. I cut aggressively by habit (my known blind spot). Every cut below is reversible and listed in section 1.3 with its cost to restore, so the owner can push back.
3. The biggest unknown is not content volume. It is whether the transparent click-through strip works reliably on Godot for Windows, and whether the art has charm. Both are tested before most work is spent (gates G0 and G1).

---

## 1. Scope tiers and the cut line

### 1.1 Tiers

| Tier | What is in it | What is NOT in it | Effort [E] agent-days | Exit gate |
|---|---|---|---|---|
| **M0 Window spike** | Transparent borderless always-on-top strip, click-through polygon, hide hotkey, sleep mode, CPU sampler, fullscreen-detect feasibility, DPI and 2-monitor pick, a stub "capsule and blob" so there is something to look at. Plus a headless Godot proof (core runs under `--headless`). | Any real game systems. | 4 to 6 (plus owner Windows time) | G0: written pass/fail with numbers |
| **Vertical slice (VS)** | Sim core (tick, combat, loot, affixes, equip, salvage, save, offline EV), zone 1 (Hearthside Verge) with mini-boss and boss, Wick and Gel first-pass art with expressions, strip HUD, panel with Inventory and Skills (Lampwright only), onboarding first 10 minutes, SFX stub, balance sim v1. Market-ready item model with the `grant()` choke point. | Other classes, passives, crafting beyond salvage and Rekindle, settings beyond monitor and hide hotkey, Steam. | 16 to 22 | G1: charm and fun check by the owner plus 5 outside viewers; sim passes determinism and offline-consistency tests |
| **Alpha** | Zones 1 to 3, 2 classes (Lampwright, Hush Archer), 45-node Constellation, full affix set, Rekindle/Kindle/Enhance, loot filter, Map panel with win-chance, settings screen (strip mode, monitor, size, opacity, FPS cap, hotkeys, quiet hours), full save migration test suite, Resting/Offline modes, synthesized SFX set, 8 sets/uniques, first soak test. | Zones 4+, Dusk Tiers, Steam, achievements. | 26 to 36 | G2: measured Windows perf pass; closed playtest on owner plus testers |
| **Demo ("Gloamway: Prologue")** | Zones 1 and 2 only, levels to 12, saves carry over, no Keepsake code, Steam page assets rendered from code, GodotSteam in a feature-flagged build (achievements and overlay only), Steam build upload checklist, demo-specific onboarding polish. | Everything past zone 2; Market. | 10 to 16 | G3: owner signs off Steam spend and identity (section 7); owner publishes |
| **1.0 (cut)** | Zones 1 to 6, 2 classes, 45 passive nodes, 20 uniques, 4 sets, Dusk Tier I, quests (story for 6 zones, dailies), 30 Steam achievements, music OFF (SFX only), cloud saves via Steam (if verified), full test matrix on real hardware, balance pass from simulation, store page, trailer assembled from captures. | Zones 7 to 10, Gel Tamer, Glimmer Rifts, festivals, Moth Night, music, Keepsakes and Market. | 38 to 54 | G4: release candidate passes launch checklist; owner signs off release |
| **v1.x Market (clearly marked, NOT in 1.0)** | Option A: Keepsake itemdefs, `playtimegenerator` and `TriggerItemDrop`, Steam inventory reader, Collection shelf, exchange recipes, kill switch, odds disclosure, economy sim. | Option B, A+ (tradable fixed uniques), any server, any paid random item. | 6 to 10 | G5: Steamworks facts verified, owner approves go-live |
| **v1.1 content** (planned, not scheduled) | Zones 7 to 10, Gel Tamer class, remaining passives (90 nodes), 20 more uniques, 2 more sets, Dusk Tiers II to V, Glimmer Rifts, Hearth Mastery 20 ranks, music, festivals. | | 30 to 45 | owner call |

### 1.2 Totals [E]

| Path | Agent-days | Calendar (working weeks of agent time, parallel roles) |
|---|---|---|
| M0 to demo | 56 to 80 | about 10 to 13 weeks |
| M0 to 1.0 | 94 to 134 | about 17 to 22 weeks |
| 1.0 plus v1.x Market | 100 to 144 | about 20 to 25 weeks |
| Full Sage design (adds v1.1) | 130 to 190 | about 28 to 36 weeks |

Calendar caveats, plainly:
- These weeks assume agents are worked continuously. Autonomous ticks (`/tick`) run one step at a time and the owner reviews daily at best, so real elapsed time may be 1.5 to 2 times longer.
- Steam review and waiting periods, bank and tax setup, and Next Fest registration are owner-side and outside these figures. I do not know Valve's current waiting periods; the owner must read them in Steamworks. [U]
- Roughly 20 to 25 percent of the days above are rework after test failures, which I have included inside the ranges.
- Agent-day estimates for a task type nobody has done here (Godot window layer, GodotSteam) are the weakest numbers in this plan.

### 1.3 Cut line and cost to restore

| Cut from 1.0 | Source | Cost to restore [E] |
|---|---|---|
| Zones 7 to 10 | Sage cut list 3 | 4 to 5 agent-days per 2 zones (content plus balance) |
| Gel Tamer class (Gel stays as a companion with flavour combat, 2 to 3 hits per fight, cosmetic) | Sage cut list, "two classes" | 5 to 7 (pet sim, skills, passives arm) |
| 45 of 90 passive nodes | Sage effort table | 3 |
| 20 of 40 uniques, 4 of 6 sets | Sage effort table | 3 to 4 |
| Glimmer Rifts, festivals, Moth Night, fourth class | Sage cut list 1 and 2 | 8 to 12 together |
| Music | Sage cut list 5 | 4 to 6 (generative loop plus tuning) |
| Dusk Tiers II to V | | 2 (data plus balance) |
| Rotating weekly pool (with Market) | Sage cut list 6 | 1 to 2 in v1.x |
| Side-edge docking (left/right/top taskbar), only floating mode and bottom dock | Sage 3.1 | 3 to 4 |
| Linux and macOS | Sage 1.6 | not estimated; not promised |

Things I deliberately did NOT cut because they are the product: the click-through strip, low CPU, offline progress, versioned atomic saves, random-affix loot with a filter, the hide-on-fullscreen behaviour, Wick and Gel charm, accessibility basics (shape plus colour rarity, reduce motion, text scale).

### 1.4 Non-goals (v1.0)
- No Steam Market, Steam Inventory calls, trading UI, Keepsake shelf or "coming soon" Market text in the player build. (A local economy sim is a QA tool.)
- No server, accounts, telemetry or network calls other than GodotSteam in the Steam build. Verified by test (T-QA-12).
- No prestige reset (Dusk Tier is a multiplier, never a reset). No paid random items, ever.
- No money spent and nothing published by agents.
- No AI-generated art or audio assets; all art and sound are produced in code.

---

## 2. Technical architecture (Godot 4)

### 2.1 Engine and version
- Godot 4.4 or later (needed for GodotSteam as a GDExtension; naming of compatible versions is inconsistent in our notes [U]). **Pin one exact version in M0** (`docs/engine-version.md`), record why, and never upgrade mid-milestone. Export templates for Windows required.
- Language: GDScript for everything in v1. A C++ GDExtension (godot-cpp) only for the native window helper if M0 proves it necessary. [D]
- Test framework: GUT or gdUnit4 (choose in M0 by whichever runs headless in this sandbox; both are GDScript addons [U on current compatibility with the pinned version]).

### 2.2 Project structure (`projects/gloamway/`)

```
project.godot
addons/                 test framework; later godotsteam (feature-flagged)
core/                   SIMULATION. No Node, no scene tree, no OS, no Time, no global RNG.
  rng/                  seeded PRNG implemented in script (own PCG or xoshiro, integer math)
  model/                ItemDef, ItemInstance, AffixDef, EnemyDef, ZoneDef, SkillDef, state structs
  combat/               tick stepper, damage formula, skill rule evaluation
  loot/                 roller, filter, salvage, craft
  progression/          xp, passives, zones, stage logic, dusk tiers
  economy/              currencies, sinks, grant() choke point
  offline/              expected-value model (Resting and Offline), caps, clock guards
  save/                 serialize, migrate, atomic IO interface (IO injected)
content/                DATA ONLY (JSON): items, bases, affixes, enemies, zones, skills, passives, quests, sets, uniques
  schema/               JSON schema docs and the content linter spec
  keepsakes/            v1.x only; excluded from the 1.0 export preset
game/                   RENDERING + INPUT (Nodes)
  strip/                strip scene, HUD, parallax, effects
  panel/                Inventory, Skills, Passives, Map, Craft, Quests, Settings
  art/                  procedural drawers: Wick, Gel, enemy grammar, icons, rarity frames
  audio/                synth and cache
platform/               WindowService interface, backends: windows/ (GDExtension), null/ (headless/Linux), steam/ (flagged)
tools/                  balance_sim.gd, perf_sample.ps1, content_lint.gd, icon_export.gd, replay.gd
tests/                  unit/, sim/, golden/, perf/, manual/ (checklists)
docs/                   engine-version.md, perf.md, content-schema.md, save-format.md, test-matrix.md, spike-report.md
```

### 2.3 Simulation core separated from rendering (the key design rule)
- `core/` is plain `RefCounted` classes. It never touches the scene tree, `OS`, `Time`, `randf`, files or the network. Time, IO and RNG seeds are injected.
- Interface: `Sim.step(ticks:int, inputs:Array) -> Array[Event]`. Fixed 10 ticks per second [D from Sage]. The renderer reads events (spawn, hit, die, drop, level, toast) and animates; it never decides outcomes.
- Because of this the same core runs: (a) in the game, (b) headless in a unit test, (c) in the balance simulator for 1000 simulated hours, (d) in offline catch-up.
- Determinism: own PRNG (not Godot's `RandomNumberGenerator`, whose sequence could change between engine versions); no iteration over unordered dictionaries where order affects outcome (sort keys); all rolls draw from named PRNG streams (`loot`, `combat`, `drops`) so adding a roll in one system does not shift others. Floating point: GDScript uses 64-bit doubles; golden hashes are guaranteed on one platform and engine pin only; cross-platform comparison uses tolerance. [U on exact cross-platform float behaviour]
- Enforcement: a lint test greps `core/` for forbidden tokens (`extends Node`, `OS.`, `Time.`, `randf`, `randi`, `get_tree`, `FileAccess`). Failing the lint fails CI.
- Awake, Resting, Offline: one economy, two stepping methods. Awake steps the real sim. Resting (30 s batches) and Offline use the expected-value model from Sage 4.3. **Consistency test**: EV result must be within a set tolerance (start at 5%) of the stepped sim over 1, 4 and 8 simulated hours for each zone band. This is the main guard against the two models drifting.

### 2.4 Data-driven content
- Format: **JSON files** under `content/`, loaded at boot into typed `RefCounted` objects by `ContentDB`. Reasons: agents can write and diff JSON, a linter can check it headless, no Godot editor needed to author, no `.tres` uid churn. [D]
- Every record has `id` (stable string, snake_case with dot namespace, e.g. `item.weapon.cinder_staff`), `schema` (int), and for anything that can ever be owned: never reused, never renamed, `retired:true` instead of deleting.
- `content_lint` (headless) checks: unique ids, all references resolve, affix tier ranges monotonic, drop odds sum to 1, no enemy without a zone, every item def has `tradable:false` and `marketable:false` in 1.0 data, every localizable string has a key.
- Strings live in `content/text/en.json` keyed by `name_key` and `desc_key`. Only English at 1.0. [D]
- Balance numbers live in `content/balance/*.json` (curves, caps, drop rates) so the simulator can tune without code edits.

### 2.5 Save system and versioning
- One JSON document in `user://saves/slot1.json` (readable and diffable; size is small). Fields: `save_version` (int), `game_version`, `content_version`, `created`, `last_seen_unix`, `rng_state`, `profile` (hero, level, currencies, passives, skills, zone progress), `inventory` (instances), `settings` (separate file `settings.json` so a bad save cannot wipe window settings), `unknown` (preserved blobs).
- Atomic write: write `slot1.json.tmp`, flush, rename over the real file; keep **3 rolling backups** (`.bak1` to `.bak3`), rotated on each successful write; plus a checksum field. Write at most every 30 s and on key events (equip, Legendary drop, quit). [from Sage 3.5]
- Load: validate checksum; on failure fall back to newest valid backup and show a one-line notice. Never silently reset.
- Migration: ordered functions `migrate_N_to_N+1`, each pure, each with a fixture file `tests/golden/save_vN.json`. Rule: adding a field = new version + migration + fixture, always.
- Unknown item or def ids on load are **preserved** (moved to `unknown`, restored when the def returns), never deleted. (Matters for Market-readiness and for downgrade.)
- Clock guards per Sage 4.4 (clock moved back = credit zero; cap applies).
- Steam Cloud (1.0, if verified): treat Steam as a copy target for the save file only. Conflict policy to be decided in T-BE-20; default: newest `last_seen` wins and the other is kept as a backup. [U]

### 2.6 Window management layer (`platform/`)
All OS-specific behaviour sits behind one interface, `WindowService`, so the game can run headless and so a fallback backend can be swapped in.

| Responsibility | Approach [U: all need Windows verification in M0] |
|---|---|
| Transparent borderless window | Project settings `per_pixel_transparency/allowed`, window flags borderless and transparent, `Viewport.transparent_bg`. |
| Always on top | Window flag `always_on_top`; test re-assert after focus loss and after clicks (known drop-behind pitfall). |
| Click-through with hit regions | `DisplayServer.window_set_mouse_passthrough(polygon)`. Regenerate only when hit regions change, at most 10 times per second. Hit regions: Wick, loot pickups, button toasts, the 20 by 20 handle. Fallback: Interact mode (hotkey toggles whole strip clickable for 10 s). |
| Size rule | Never within 8 px of the monitor size in both axes (exclusive-fullscreen flip). Default 640 by 96 logical px. |
| Docking above taskbar | Read the monitor's usable rect (`DisplayServer.screen_get_usable_rect`) to find the taskbar edge; dock to its top edge for a bottom taskbar. Auto-hide taskbar case is a test row. |
| Multi-monitor | Per-monitor remembered position; listen for screen changes; if the chosen monitor disappears, fall back to primary and notify once. |
| DPI | Project setting for per-monitor scaling; layout in logical px; test 100, 125, 150, 200 percent and mixed DPI. |
| Hide on fullscreen app | Preferred: Win32 `SHQueryUserNotificationState` through a small GDExtension (no Godot example found [U]). Fallbacks, in order: (1) user hotkey and tray toggle, (2) poll `tasklist` at most every 10 s against a user-maintained process list, (3) pause on lost focus. Hide only if the fullscreen app is on the same monitor (default, per Sage 12.6). |
| Sleep | Hidden: pause the tree, `low_processor_usage_mode`, FPS cap 1, sim continues in Resting batches every 30 s. |
| Tray, hotkeys | Godot has a status indicator API for tray [U on Windows behaviour]; global hotkeys need a native hook (Godot receives keys only when focused), which is another reason for the GDExtension. If the native route is rejected, hotkeys become tray-menu actions only. [U] |
| Linux backend | `null` backend for headless tests only. Wayland is not supported in 1.0. |

**Decision rule for the native helper:** a minimal Windows GDExtension (C++ via godot-cpp, built by the release-engineer on a Windows machine or on CI the owner approves) offering `is_fullscreen_app_foreground(monitor)`, `register_global_hotkey`, and `keep_topmost()`. Build only if M0 shows Godot-only routes fail. Cost: 3 to 5 agent-days plus a Windows build host. [E]

### 2.7 Performance budget and how to measure
Targets are Sage's hypotheses [H] adopted as the acceptance bar. Nothing is claimed publicly until measured.

| Budget | Target [H] | How measured | Where |
|---|---|---|---|
| Strip awake, 30 FPS, default | under 2% of one logical core average | `tools/perf_sample.ps1` samples process CPU time deltas every 5 s for 30 min (script computes percent of one core), logs to CSV; Godot `Performance` monitors (draw calls, objects, memory) written by an in-game debug logger | owner Windows laptop (reference machine, recorded in `docs/perf.md`) |
| Eco preset | under 1% | same | same |
| Resting (hidden) | under 0.3%, wakes once per 30 s | same | same |
| RAM | under 180 MB awake, 120 MB resting | Task Manager value logged by script (working set) | same |
| Draw calls | under 150 strip | Godot monitor | same, also software-rendered Linux for a coarse check |
| Sim speed | 10 simulated hours in under 60 s on the sandbox CPU [A] | `tools/balance_sim.gd` timing | headless, here |
| Sim memory | no growth over 100 simulated hours beyond a fixed bound set in M0 | headless soak | headless, here |
| Save size and time | save under 1 MB at 2000 items; write under 50 ms | unit/perf test | headless, here |
| Disk | under 400 MB install | export size check | build step |

Perf regression rule: any change to `game/` that raises draw calls or per-frame allocations over the budget fails the perf test where it can run headless (a script counts draw calls under a software renderer if the pinned Godot supports it; otherwise only the Windows check applies). [U]

### 2.8 Steamworks integration plan (GodotSteam)
- **1.0 (demo and release builds):** GodotSteam GDExtension behind a feature flag and a `SteamService` interface with a `NullSteam` default. Used for: init, achievements, (verified) Steam Cloud, overlay-compatibility test, rich presence optional. No Inventory API calls in 1.0.
- Local development never needs Steam: `NullSteam` makes all tests run headless.
- Real Steam testing needs an app ID and the owner's Steamworks login; Steam's test app 480 can be used for init smoke tests only, not for our itemdefs. [U on whether we may use 480 for dev; verify]
- Agents never log in to Steamworks, never upload builds, never press publish. Release-engineer prepares build folders, depot scripts and checklists; the owner runs the upload.
- **v1.x Market (later):** `playtimegenerator` itemdef, `TriggerItemDrop` called at most once per interval with exponential backoff, no polling, inventory read on launch and after a drop, exchange recipes, kill switch (flip `tradable`/`marketable` off then `FlushAssetAppearanceCache`). Every field name and limit here is [U] until verified in the Steamworks docs on the owner's account (task TM-1 is exactly that).

### 2.9 Market-readiness of the item model (built in 1.0, unused)
Design rules (all enforced by tests, none of them visible to players):

1. **Two kinds of item.** `kind=gear` (random affixes, permanently untradable, lives only in our save) and `kind=keepsake` (fixed definition, no affixes, the only future-tradable kind). Steam clears dynamic properties on trade [official snippet via research, U], so affixes are never on tradable things.
2. **Stable identity.** Definition: `id` (never reused or renamed), `schema`, `kind`, `rarity`, `slot` or `cosmetic_slot`, `tags`, `tradable:false`, `marketable:false`, `steam_def_id:null`, `drop_policy` (combat, recipe, timed), `retired:false`. Instance: `uid` (128-bit random, generated by the PRNG `uid` stream and checked for collision), `def_id`, `affixes[]`, `rolled_at_tick`, `origin` (combat, offline, resting, recipe, grant, steam), `bound:true`.
3. **One grant door.** All item creation goes through `Grants.grant(def_id, origin, qty)`. It is the place for caps, logging, a kill switch and later the Steam source. A test asserts nothing else constructs an `ItemInstance` outside loot rolling and load.
4. **Offline and Resting can never mint a `keepsake`.** Enforced inside `grant()` (origin check) and tested.
5. **`tradable` and `marketable` are data, not logic.** No game code branches on them in 1.0. One unit test asserts they are false for every 1.0 def; the export preset excludes `content/keepsakes/`.
6. **Cosmetic slots exist** (Gel hat, lantern flame colour, strip decoration, Wick idle) fed by Hearth Mastery cosmetics in 1.0, so the Keepsake equip path already works when v1.x adds a second source.
7. **Inventory adapter interface** `KeepsakeSource` with `get_owned() -> Array[{def_id, count}]`; 1.0 ships only `NullKeepsakeSource` returning empty.
8. **Economy sim already models timed drops, caps and exchange recipes** (as a pure-core module, disabled in game) so the Option A balance in v1.x starts from numbers, not guesses.

---

## 3. Build order, dependencies and Gantt

### 3.1 Dependency chain (critical path in bold)
**M0 spike -> G0** -> core skeleton (rng, model, save, content DB) -> **combat and loot sim** -> balance sim v1 -> VS game scene (needs M0 window layer) -> **G1 charm gate** -> content expansion (zones 2 and 3, class 2, passives, crafting) -> settings and window hardening -> Windows perf and matrix (needs owner hardware) -> **G2** -> demo build -> owner Steam setup (parallel from G1) -> **G3** -> zones 4 to 6, uniques, Dusk Tier I, achievements -> balance pass -> RC and launch checklist -> **G4** -> release -> v1.x Market (verification first).

Parallel lanes once the core skeleton exists: designer content tables and wireframes, backend core systems, frontend art and scenes, qa test harness. Parallelism limit: frontend cannot start the game scene until the M0 window layer exists; qa cannot close perf items without owner hardware.

### 3.2 Gantt-style table [E]
Week numbers are working weeks of agent time from start, assuming the owner provides a Windows machine within week 1. "W" = week. Shaded gates are in the Gate column.

| Phase | W1 | W2 | W3 | W4 | W5 | W6 | W7 | W8 | W9 | W10 | W11 | W12 | W13 | W14 | W15 | W16 | W17 | W18 | W19 | W20 | W21 | W22 | Gate |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| M0 spike | X | | | | | | | | | | | | | | | | | | | | | | G0 end W1 (K1 at 3 working days) |
| Core skeleton and content DB | | X | X | | | | | | | | | | | | | | | | | | | | |
| Combat, loot, save, offline (VS) | | X | X | X | | | | | | | | | | | | | | | | | | | |
| VS scene, art v1, onboarding | | | X | X | X | | | | | | | | | | | | | | | | | | G1 end W5 |
| Balance sim v1, VS tests | | | | X | X | | | | | | | | | | | | | | | | | | |
| Alpha: zones 2 to 3, class 2, passives, crafting, settings | | | | | | X | X | X | X | | | | | | | | | | | | | | |
| Alpha hardening, soak, Windows perf and matrix | | | | | | | | | X | X | | | | | | | | | | | | | G2 end W10 |
| Owner: Steam account, identity, Direct fee | | | | | X | X | X | X | X | X | | | | | | | | | | | | | owner lane (not agent time) |
| Demo build, Steam page assets, GodotSteam flagged | | | | | | | | | | X | X | X | | | | | | | | | | | G3 end W12 |
| 1.0 content: zones 4 to 6, uniques, Dusk I | | | | | | | | | | | X | X | X | X | X | | | | | | | | |
| Achievements, cloud save, quests, polish | | | | | | | | | | | | | X | X | X | X | | | | | | | |
| Balance pass, final test matrix, soak | | | | | | | | | | | | | | | X | X | X | | | | | | |
| RC, launch checklist, store page finish | | | | | | | | | | | | | | | | | X | X | | | | | G4 end W18 |
| Owner: Next Fest decision, release date, publish | | | | | | | | | | | | | | | | | X | X | X | X | | | owner lane |
| v1.x Market: verify, build, test | | | | | | | | | | | | | | | | | | | X | X | X | | G5 |
| Slack for rework and owner wait | | | | | | | | | | | | | | | | | | | | | X | X | |

Bottom line [E]: about 18 weeks of agent time to a release candidate, 20 to 22 with the Market milestone; real calendar probably 6 to 8 months once owner loops and Steam waiting periods are included. I mark this a rough estimate with an unknown owner-wait component.

---

## 4. Task list by agent role

Ordering IDs: P = planner/orchestrator, D = designer, FE = frontend-engineer, BE = backend-engineer, QA = qa-engineer, RE = release-engineer, HW = handoff-writer, R = researcher. Agents work in `projects/gloamway/`. "Headless" = can be done and checked in this sandbox if a Godot binary can be obtained (see section 5.1). "Windows" = needs a Windows machine. Every acceptance criterion below is a pass/fail check someone can run.

### 4.1 M0 (window and headless spike)

| ID | Role | Task | Acceptance criteria (testable) | Needs |
|---|---|---|---|---|
| T0-1 | RE | Check whether a Godot 4.4+ headless Linux binary and export templates can be obtained in this sandbox; pin the version; write `docs/engine-version.md` | `godot --headless --version` prints the pinned version in the sandbox, or `engine-version.md` states exactly why not and what the owner must install | Headless |
| T0-2 | D | Spec the strip: size rules, hit regions, handle, toast sizes, sleep/wake states, Interact-mode | `docs/strip-spec.md` lists each hit region with pixel size and a pass/fail test for each | Headless |
| T0-3 | FE | Scaffold project; transparent strip prototype with polygon passthrough, hide hotkey, tray toggle, blob "Wick" with squash and stretch | On a Windows machine: (a) a click on a window behind the transparent area activates that window; (b) a click on the blob does not; (c) after 20 clicks on other apps the strip stays on top; (d) strip size is at least 8 px smaller than monitor in both axes; recorded in `docs/spike-report.md` | Windows |
| T0-4 | BE | `tools/perf_sample.ps1` and in-game `DebugLogger` writing Performance monitors to CSV | Running the script for 10 minutes on the Windows laptop produces a CSV with CPU percent, working set and draw calls at 5 s intervals; method written in `docs/perf.md` | Windows |
| T0-5 | BE | Sleep-mode prototype (pause tree, FPS 1, Resting tick every 30 s) | Measured CPU awake vs asleep recorded with machine and Godot version; asleep target under 1% (K2 threshold) | Windows |
| T0-6 | FE + BE | Fullscreen-app detection feasibility: Godot-only route, tasklist poll, native GDExtension route | Each route has a written pass/fail with a test (open a fullscreen video or game, strip hides within 3 s on the same monitor only); recommendation recorded | Windows, 2 monitors for the same-monitor rule |
| T0-7 | FE | DPI and 2-monitor pick prototype | Strip positions correctly above taskbar at 100 and 150 percent; moves between monitors; survives hot-unplug (falls back to primary) | Windows, 2 monitors |
| T0-8 | BE | Headless proof: a stub `core/` with PRNG and a 10-tick sim runs under `--headless` with a unit test | `godot --headless -s tests/run.gd` exits 0 and prints a deterministic hash equal on two consecutive runs | Headless |
| T0-9 | QA | Spike test matrix and sandbox limits list | `tests/manual/m0-matrix.md` exists; each row marked Done-here, Needs-owner or Blocked | Headless |
| T0-10 | P | Go/no-go review against K1 to K3, owner notice | Decision written in `docs/spike-report.md` with the numbers; owner notified of any K trigger | none |

### 4.2 Vertical slice

| ID | Role | Task | Acceptance criteria | Needs |
|---|---|---|---|---|
| T1-1 | D | Content spec v1: zone 1 enemies, 20 bases, affix JSON tables from Sage 6.4, skill rules, onboarding script | `content/` JSON drafts pass `content_lint`; each affix has tier ranges that match Sage's table within rounding | Headless |
| T1-2 | BE | `core/`: PRNG, model, ContentDB, `grant()`, loot roller, filter, salvage, equip, Power Score | Unit tests: same seed gives identical 10,000 drops (golden hash); rarity rates over 1M rolls within 1% of table; no duplicate affix group on an item; `grant()` rejects keepsake with offline origin | Headless |
| T1-3 | BE | Combat tick stepper with damage formula, skill priority and rules, faint, boss timer | Scripted fights: hand-calculated damage matches formula in 20 cases; faint drops stage by 1 and loses no items; boss timeout resets with no penalty | Headless |
| T1-4 | BE | Save system: atomic write, 3 backups, checksum, migration scaffold, unknown-id preservation | Kill the process mid-write (fault-injection test): load still succeeds from backup; corrupt main file loads backup; fixture v1 loads; unknown def id round-trips | Headless |
| T1-5 | BE | Offline and Resting EV model with caps and clock guards | Consistency test: EV vs stepped sim within 5% over 1, 4, 8 h; 8 h cap enforced; negative clock delta credits 0; offline never produces keepsake or boss progress | Headless |
| T1-6 | BE | Balance sim v1 (`tools/balance_sim.gd`) | `godot --headless -s tools/balance_sim.gd --hours 100 --seed 1` prints items per hour by rarity, level curve, faint count, Dust income; output within Sage targets (items 36/h plus or minus 15%, Legendary one per 2 to 4 h) or the report lists the delta | Headless |
| T1-7 | FE | Wick, Gel, 6 enemy bases (code-drawn), strip HUD, loot arcs, toasts, hit regions from T0-2 | Screenshot test under a software renderer (if available) shows each of Wick's 8 expressions; strip hit regions rebuild at most 10 times per second (counter test); Wick readable at 96 px height reviewed by D | Headless screenshots if supported [U]; Windows for the real window |
| T1-8 | FE | Panel: Inventory (compare, equip, salvage, star), Skills (priority and rule editor) | Keyboard-only operation of equip and salvage works; equip delta matches `Power Score` function; panel is a separate normal window that closes without affecting strip | Windows |
| T1-9 | FE | Onboarding first 10 minutes per Sage 9.4 | Scripted run reaches level 3 and first Fine and Rare items on schedule within plus or minus 30 s in the sim; skippable at any step | Headless sim, Windows |
| T1-10 | D | Review and charm brief; run charm check with 5 outside viewers | Owner arranges viewers; D collects a short written reaction; pass if at least 3 of 5 would "keep it on their desktop" (G1) | Owner |
| T1-11 | QA | Test suite scaffolding, content lint in CI script, determinism and forbidden-token lint | `tests/run_all.sh` runs all headless tests, exit code nonzero on any fail; documented | Headless |
| T1-12 | RE | Reproducible Windows export script and version stamp | One command produces a folder with the exe; version string visible in Settings | Windows (export), headless for script check |

### 4.3 Alpha

| ID | Role | Task | Acceptance criteria | Needs |
|---|---|---|---|---|
| TA-1 | D | Zones 2 and 3, Hush Archer, 45-node Constellation, Rekindle/Kindle/Enhance, sets and 8 uniques, quests for 3 zones | Lint passes; balance sim shows each zone reaching on-curve clear time within plus or minus 30% of Sage's estimate | Headless |
| TA-2 | BE | Passive tree engine (data-driven nodes, respec), crafting systems, loot filter engine, quests/dailies (banked up to 3), Dusk Tier hook | Property tests: respec restores points exactly; Enhance +10 cost matches Sage formula; filter rule order deterministic; daily bank never exceeds 3 | Headless |
| TA-3 | BE | Save migration v2 and v3 (alpha schema changes) | Every previous fixture loads into current build; migration tests pass in CI script | Headless |
| TA-4 | FE | Passives panel, Map panel (win chance traffic light), Craft, Quests, Settings (all in Sage 9.3 settings list that exist in alpha) | Settings persist across restart; changing monitor moves strip within 1 s; hotkeys rebind and persist; text scale 100 to 200 percent keeps UI readable (screenshot review) | Windows |
| TA-5 | FE | Procedural audio synth and SFX set, quiet hours, Quiet button | All Sage 9.6 cues exist; no sound when hidden (test with audio bus meter); master default 25% | Headless audio-bus test, Windows listen |
| TA-6 | FE | Enemy grammar for zones 2 and 3, bosses, elite modifiers | 18 visually distinct silhouettes at 24 px verified by D's checklist; elite glow present | Windows |
| TA-7 | BE | Native helper (only if T0-6 chose it) | `is_fullscreen_app_foreground` returns correct value in 6 scripted cases (windowed, borderless, exclusive, other monitor, Win+D, lock screen) | Windows |
| TA-8 | QA | Soak and perf: 24 h wall-clock strip run; 1000-hour headless soak | Windows 24 h run: no crash, RAM growth under 20 MB per 24 h (bound confirmed in M0), saves valid; headless 1000 h sim: no memory growth beyond the M0 bound | Windows and headless |
| TA-9 | QA | Manual matrix run 1 (section 5.7) | `tests/manual/results-alpha.md` filled with pass/fail per row with date, machine, tester | Owner/tester hardware |
| TA-10 | RE | Playtest build distribution (zip, local), crash log capture to a file the tester can send | Tester can find and attach the log in under 3 steps (documented) | Windows |
| TA-11 | HW | Handoff doc for the owner: how to run, how to report bugs | One page; owner can follow it cold | none |

### 4.4 Demo

| ID | Role | Task | Acceptance criteria | Needs |
|---|---|---|---|---|
| TD-1 | FE | Demo build flag (zones 1 and 2, level cap 12, saves compatible with full game) | Demo save loads in the full build with progress intact (migration test) | Headless |
| TD-2 | FE | GodotSteam integration behind flag, `SteamService`, achievements (demo set of 8) | Without Steam: game runs identical, tests pass with `NullSteam`; with Steam client on the owner machine: init succeeds and one achievement unlocks | Owner Windows plus Steam app ID |
| TD-3 | D | Store page assets: capsule drafts, 5 screenshots, 3 GIFs, short and long descriptions, "What it will not do", odds-free (no Market in 1.0) copy | Asset sizes match Steamworks requirements as read from Steamworks docs by the owner or R [U]; every performance claim in copy has a matching measurement in `docs/perf.md` | Owner for upload |
| TD-4 | RE | Steam build checklist: depots, build scripts, branches, demo app setup steps, test install | Owner can follow the checklist to upload a build; QA verifies a clean install and uninstall on a fresh Windows user profile | Owner |
| TD-5 | R | Verify Steamworks facts relevant to launch: waiting periods, store review lead time, demo rules, Next Fest rules, AI disclosure form wording, capsule specs, tax and bank requirements | `docs/steam-facts.md` lists each fact with a source URL and date opened, or "could not open" | Web access if available; otherwise owner reads Steamworks |
| TD-6 | QA | Demo test pass (matrix rows for demo scope) and first-3-minutes timing test | First 3 minutes: no crash, first Rare within 2 minutes in 9 of 10 seeded runs | Headless and Windows |

### 4.5 1.0

| ID | Role | Task | Acceptance criteria | Needs |
|---|---|---|---|---|
| T10-1 | D | Zones 4 to 6, 12 more uniques, 2 more sets, Dusk Tier I rules, 30 achievements, story text | Lint passes; balance sim campaign clear in 12 to 20 simulated hours at on-curve play [H, Sage says 15] | Headless |
| T10-2 | BE | Dusk Tier I as multiplier (no reset), cloud-save wrapper (if T10-6 verified), final save migration pass | Tier toggling never changes level, gear or zone progress (property test); full migration chain from the first alpha fixture works | Headless |
| T10-3 | FE | Zone 4 to 6 art, boss rigs, polish pass, accessibility (reduce motion, colour-blind palettes, text scale, keyboard nav) | Accessibility checklist in `tests/manual/a11y.md` all pass; rarity distinguishable by shape in greyscale screenshot | Windows |
| T10-4 | QA | Balance regression gate in test script | `balance_sim` outputs compared to a stored baseline; run fails if a rate moves more than the stated tolerance without an updated baseline commit | Headless |
| T10-5 | QA | Full manual matrix on real hardware (section 5.7), Steam overlay on/off, 2 monitors, DPI mixes, 3 fullscreen apps | All rows pass or have a written, owner-accepted waiver | Owner/tester hardware |
| T10-6 | BE | Verify and implement Steam Cloud copy of the save | A save made on machine A appears on machine B in a two-machine test; conflict case keeps both | Owner, two machines [U] |
| T10-7 | RE | Release candidate build, version stamp, depot upload checklist, rollback plan (previous build can be re-set live) | Clean install test on 2 Windows versions; checklist signed per item | Owner |
| T10-8 | D | Store page final copy, trailer script and shot list; trailer assembled from captures | Every claim in copy mapped to evidence (measurement or feature in build) in a table | Owner for upload |
| T10-9 | HW | Launch handoff: owner runbook, support FAQ, known issues | Owner confirms they can run the release from the doc alone | Owner |

### 4.6 v1.x Market (do not start without owner go-ahead)

| ID | Role | Task | Acceptance criteria | Needs |
|---|---|---|---|---|
| TM-1 | R + BE | Verify Steamworks facts on the owner's partner account: itemdef fields, `playtimegenerator` semantics (`drop_interval`, `drop_window`, `drop_max_per_window`), Market enablement/approval, fees, trade holds, rate limits, whether exchange recipes can offer a choice | `docs/steam-market-facts.md` with source and date per fact, plus a list of what could not be verified. K6 triggers if Market is not self-serve | Owner |
| TM-2 | D | Keepsake roster (30 defs, 14 Common/10 Rare/6 Mythic per Sage), odds (owner confirms), rotation, recipes, disclosure copy | Odds table sums to 100%; expected supply and recipe sinks modelled in the economy sim | Headless |
| TM-3 | BE | `SteamKeepsakeSource`: `TriggerItemDrop` with backoff, inventory read, `grant()` Steam origin | In a private test app: one drop arrives per interval; failures retry with backoff; no call more than once per interval in a 24 h log | Owner test app |
| TM-4 | FE | Collection shelf, equip Keepsake in cosmetic slot, "View in Steam Inventory", next-drop line, toast | Keepsake equipped on Gel survives restart; shelf shows only what Steam reports; works offline with last known list | Owner Windows |
| TM-5 | QA | Economy sim, kill-switch drill, offline cannot mint test, 100% pass of Market-ready asserts | Drill: flip flags off in the test app, `FlushAssetAppearanceCache`, client shows items non-tradable within 10 minutes of restart [U]; sim shows no unbounded supply | Owner |
| TM-6 | RE | Itemdef upload checklist and go-live runbook | Owner can follow it; rollback is a documented one-step action | Owner |

---

## 5. Test strategy

### 5.1 What can and cannot be done in the sandbox
The sandbox is Linux and probably has no GPU, no display, and no Windows. I do not yet know whether a Godot binary can be downloaded through the proxy [U]; T0-1 answers this first.

| Can be built and tested headlessly here (if a Godot Linux binary is obtainable) | Needs the owner's laptop or a Windows machine |
|---|---|
| Entire `core/` simulation, PRNG, loot, affixes, combat, progression | Transparent window, click-through, always-on-top behaviour |
| ContentDB, content JSON authoring and lint | Fullscreen-app detection, tray, global hotkeys |
| Save system including fault-injection and migration fixtures | DPI scaling, multi-monitor, taskbar auto-hide |
| Offline and Resting EV model and its consistency test | Real CPU and RAM numbers (all perf claims) |
| Balance simulator, economy sim, determinism and replay tests | Visual judgement of charm and readability at 96 px |
| Item model Market-ready assertions, no-network grep | Audio listening |
| Procedural art code (screenshots only if a software renderer works [U]) | GodotSteam, overlay, cloud save, anything Steam |
| Windows export from Linux, if export templates can be installed [U] | Installer and uninstall test, clean-profile test |

If no Godot binary can be obtained, the fallback is: agents write GDScript and tests unexecuted, and the owner runs `tests/run_all` on the laptop. That slows every loop, so it makes obtaining the binary the first task. I will not mark any item "tested" unless it was executed and the output is saved in `runs/`.

### 5.2 Unit tests (headless)
Loot rarity tables, affix tier gating by ilvl, caps (crit 60, dodge 40, Pace 40, Find 100), diminishing Find, damage formula cases, DR formula, skill rule evaluation, XP curve, salvage and craft costs, filter rules, stash overflow, Power Score, `grant()` rules, Dusk Tier multiplier. Each system's tests ship with the system (a task is not done without them).

### 5.3 Headless balance simulator
`tools/balance_sim.gd` runs the real core with scripted "player policies" (default auto-play; cautious; bold; no-upgrade) for N simulated hours across seeds. Reports: items per hour by rarity, time to level, time per zone, faint rate, Dust and Wisp income against sinks, Legendary interval, build comparison (class A vs B power at the same time), stuck points. Output is compared to the baseline file (T10-4). Targets in Sage's design are [H]; the simulator tunes them, and results go into a `docs/balance-report.md` each milestone.

### 5.4 Determinism and replay
(1) Same seed, same inputs: identical state hash after 100k ticks, run twice. (2) Replay file (seed plus input log) reproduces a bug exactly. (3) Hash golden files per milestone; any intended change updates the golden with a reason in the commit. (4) Stream isolation test: adding a draw to the `combat` stream does not change `loot` results.

### 5.5 Save migration tests
Fixtures for every released and alpha save version. Test: load each fixture, migrate to current, then check invariants (item count, currencies, unknown ids kept, settings untouched). Fault injection: truncate file, flip bytes, kill between temp write and rename, missing backup. Downgrade: a save from a newer version is refused with a clear message and left untouched.

### 5.6 Performance tests
Headless: sim speed, sim memory over 1000 simulated hours, save size and time. Windows: CPU, RAM, draw calls per budget in 2.7, 30-minute and 24-hour runs, Eco and Resting presets, battery-saver toggle. Rule: perf numbers appear in `docs/perf.md` with machine, OS, Godot version, build id and date, or they do not exist.

### 5.7 Manual test matrix (owner or testers; QA writes it, owner runs or assigns)

| Axis | Values |
|---|---|
| OS | Windows 10 and Windows 11 (at least one each if available) |
| Monitors | 1 monitor; 2 monitors same DPI; 2 monitors mixed DPI (100 and 150 percent); hot-unplug and hot-plug the strip's monitor; swap primary |
| DPI scale | 100, 125, 150, 200 percent |
| Taskbar | bottom, auto-hide on and off; (side and top: out of scope for 1.0, expected to look wrong; record only) |
| Fullscreen apps | exclusive fullscreen game; borderless windowed game; video player fullscreen; PowerPoint slideshow; browser F11; fullscreen app on the other monitor (strip should stay) |
| Session events | alt-tab, Win+D, lock/unlock, sleep/wake, display off, RDP session |
| Steam | game launched from Steam vs directly; overlay on and off; offline mode (Steam client not running for non-Steam build) |
| Input | strip never steals focus while typing in another app; click-through verified over a text editor, a browser and a game |
| Hardware | integrated GPU laptop on battery; desktop with discrete GPU (discrete GPU must not wake) |
| Accessibility | greyscale screenshot rarity check, text 200 percent, reduce motion, keyboard-only panel |
| Saves | kill from Task Manager mid-play and relaunch; disk-full simulation; copy save between machines |

Who: QA writes rows and expected results; **owner or a tester executes on real hardware and sends results** (agents cannot); QA records and triages. Matrix run 1 at Alpha, run 2 on the demo build, run 3 on the release candidate. A row not run is "unverified", never "pass".

---

## 6. Demo and release path

Everything in this section that touches Steamworks is owner-only; agents prepare documents and builds. Nothing here states a date.

1. **Preparation (agents).** Name and trademark clash check for "Gloamway" (search steps listed for the owner; agents cannot be authoritative on trademarks). Capsule and screenshots drafted from the build. Store text drafted with only verified claims.
2. **Owner: Steamworks setup.** Partner account, identity and tax and bank forms, Steam Direct fee for the app (the fee is reported as $100 in our notes [U on current amount and refund rule]). Do this around G2, not earlier; it has waiting time I cannot size. [U]
3. **Store page ("Coming soon").** Owner uploads assets and submits for Valve review. Review times and minimum "coming soon" duration before release are unknown to me; TD-5 verifies them from the Steamworks docs. [U] Wishlists matter for visibility; I give no wishlist target.
4. **Demo.** Demo is a separate app or a depot setup per Steamworks rules [U: verify]. Owner uploads and presses publish. First 3 minutes must be light and clean (Sage 11.5).
5. **Next Fest.** Owner checks the Steamworks calendar for current Next Fest dates, registration rules and demo requirements. **I state no dates.** The notes say idle demos are crowded (almost 500 in a June 2026 Fest) [F in Sage], so the demo needs to stand out in the first minutes.
6. **Playtest.** Closed playtest with 10 to 30 testers recruited by the owner for the matrix and balance; agents prepare the test sheet.
7. **Launch checklist (release-engineer prepares; owner executes).**
   - RC build passes full test and matrix with waivers recorded.
   - `docs/perf.md` numbers match every performance claim on the store page.
   - Store page complete: description, tags (Idler/Incremental, Desktop Companion, Action RPG, Loot, Cute, Anime, Fantasy, Singleplayer, Casual, Relaxing, Indie, Atmospheric per Sage), age rating questionnaire, AI disclosure form (art and audio are code-generated; text is human or tool-assisted; owner answers the form), system requirements stated honestly (Windows only), price.
   - Achievements defined; cloud save tested; build uploaded to default and a beta branch; rollback plan.
   - Support plan: a single FAQ page, bug report template, owner decides where support happens.
   - Release timing and public announcements chosen by the owner.
8. **Legal and tax (owner and humans).** Business entity or sole proprietor choice; Steam tax interview and bank setup; local tax and VAT handling; privacy statement if the game collects nothing (state "collects no data" only if verified by T-QA-12); EULA text if wanted; font license check (Nunito or other SIL OFL font, verify at time of use); GodotSteam and Godot licenses acknowledged in credits (Godot is MIT, GodotSteam is MIT, per my knowledge, verify [U]). Agents flag these but give no legal or tax advice.
9. **Market (v1.x).** Separate go-live per section 4.6. Extra owner items: confirm odds and daily cap; read Valve's current rules for item stores and Market; decide whether to limit by region; legal review of loot-related rules (outside agent competence). Public text never promises prices or income.

### What only the owner can do (summary)
Create or log in to Steamworks and the partner account; provide legal identity, tax and bank details; pay Steam Direct; upload builds and press every publish button; approve the store page; read current Steam rules and dates; supply a Windows machine with two monitors and testers; run the manual matrix; confirm trademark clearance; decide price; approve any recurring cost; sign off every release step and the v1.x Market go-live.

---

## 7. Budget

| Item | Cost | Needed when | Who decides | Note |
|---|---|---|---|---|
| Godot, GDScript, GUT/gdUnit4, godot-cpp | $0 | now | n/a | open source; verify licences in credits |
| GodotSteam | $0 | demo | n/a | open source [U on license for current version] |
| Art, audio, fonts | $0 | always | n/a | code-drawn and synthesized; SIL OFL font if any |
| Agent time | $0 additional to the owner (existing session usage) | always | n/a | not tracked here |
| Windows test machine | $0 if the owner's own laptop; paid VM or hardware is optional and NOT assumed | M0 | owner | a cloud Windows VM would not test multi-monitor or real GPU well anyway |
| Steam Direct fee | reported $100 per app [F in notes; U on current amount and recoup rule] | before the Steam page and demo | owner only | pay as late as the plan allows (around G2) |
| Hosting, domains, servers | $0 | never in this plan | owner would have to approve | none for Options A and C |
| Code signing certificate for the exe | optional, cost unknown; Steam distribution does not require it as far as I know [U] | optional | owner | skip |
| Optional human polish of the capsule art or trailer | unknown; not assumed | before store page | owner | Sage flags code-drawn capsule as a risk; budget decision is the owner's |
| Optional commissioned music | unknown; not assumed | v1.1 | owner | default: none |
| Legal and tax advice | unknown; not assumed | before the Steam identity step and before Market | owner | outside agent competence |
| Market-related costs | $0 to build; Steam takes its documented fees on sales between players [F in notes, U] | v1.x | owner | no revenue forecast made |

Zero is the baseline until the Steam Direct step. Any item with unknown cost is marked unknown rather than guessed.

---

## 8. Risk register and go/no-go gates

### 8.1 Gates

| Gate | When | Pass criteria | If it fails |
|---|---|---|---|
| **G0 M0 window spike** | end of M0 | On Windows: stable transparent strip, click-through works, stays on top after 20 foreign clicks, asleep CPU under 1% of one core, hide-on-fullscreen works by at least one route, strip not at full-monitor size, headless core runs | Kill criteria K1 to K3 (below) |
| **G1 charm and slice** | end of VS | Owner approves look and feel; at least 3 of 5 outside viewers would keep it on their desktop; EV model within 5% of sim; determinism and save tests green | One iteration to fix; second fail: owner decides pivot (art budget, theme, stop) |
| **G2 perf on real hardware** | end of Alpha | Windows numbers meet 2.7 targets or the owner accepts revised targets; matrix run 1 has no open blockers | Fix cycle; if CPU cannot reach 5% awake idle, K2 |
| **G3 Steam spend and demo** | before Steam fee | Owner signs spend, identity and demo go-live | Stop at that step (K5) |
| **G4 release** | RC | Matrix run 3 passes, perf claims all measured, store claims all evidenced, owner signs release | No release; fix list |
| **G5 Market go-live** | v1.x | TM-1 facts verified, kill-switch drill passed, economy sim bounded, owner approves | Keep v1 as is (K6) |

### 8.2 Kill and pivot criteria
- **K1 (window):** after 3 working days of M0 there is no stable transparent, click-through, always-on-top strip on Windows in the pinned Godot with an acceptable workaround. Action in order: (1) try another pinned Godot minor version (1 to 2 days); (2) try the native GDExtension route for window styles and hit testing (3 to 5 days); (3) report to the owner for a Unity decision.
- **K2 (CPU):** asleep above 1% or awake idle above 5% of one core on the reference machine with no known fix.
- **K3 (testability):** no Windows hardware access by the end of M0. Action: continue only with every window and perf claim marked unverified, with owner consent.
- **K4 (fun):** G1 fails twice.
- **K5 (spend):** a step needs money or identity not approved.
- **K6 (Market):** TM-1 shows Market is not self-serve or Valve objects.

### 8.3 Unity fallback (needs owner approval; not planned)
What survives a switch: all design docs, all JSON content, balance baselines, test specs, art specs. What is lost: GDScript code and Godot scenes. Because `core/` is engine-free logic, porting it to C# is mostly mechanical translation. Estimate [E]: 12 to 18 agent-days to reach the VS state again, plus a UniWindowController-style window layer [U on licensing and behaviour]. Unity also has its own licensing and pricing terms the owner must check. The fallback is a real option, but I put Godot's native-extension route ahead of it because it costs less.

### 8.4 Risk register

| # | Risk | Likelihood / impact | Mitigation | Owner of mitigation |
|---|---|---|---|---|
| 1 | Godot transparent click-through is flaky on Windows [U] | Medium / High | M0 first; size under monitor; Interact mode; native helper; K1 | FE, RE |
| 2 | Charm gap: code-drawn art does not read as lovable, capsule weak | Medium-High / High | Wick and Gel built early in VS; G1 outside viewers; optional human capsule pass is an owner choice | D, FE, owner |
| 3 | Crowded idler market (1,566 releases in 2026 per notes) | High / High | Differentiate on clean strip, CPU, loot depth, demo quality; no revenue promise | D, P |
| 4 | Scope too large | High / High | Cut line section 1; tier gates; planner veto on additions; v1.1 bucket | P |
| 5 | Sandbox cannot run Godot or Windows tests | High / Medium-High | T0-1 first; write tests anyway; owner runs on laptop; never claim untested | RE, QA |
| 6 | Balance numbers are all [H] | High / Medium | Simulator-driven tuning, baseline gate, playtest | BE, D |
| 7 | EV offline model drifts from stepped sim | Medium / Medium | Consistency test in CI script | BE, QA |
| 8 | Save loss or corruption | Low / High | Atomic write, 3 backups, fixtures, preserve unknown ids | BE |
| 9 | Fullscreen detection needs native code | Medium / Medium | Fallback ladder in 2.6; native helper decision rule | FE, BE |
| 10 | Multi-monitor and DPI instability (Tiny Pasture complaint) | Medium / Medium | Day-one test case; matrix; hot-plug fallback | FE, QA |
| 11 | GodotSteam version mismatch with pinned Godot [U] | Medium / Medium | Choose Godot version with GodotSteam compatibility check in M0 (read repo releases); feature flag | RE |
| 12 | Steam waiting periods and review times delay release | Medium / Medium | Owner starts Steam setup early (around G2); TD-5 verifies | owner, R |
| 13 | Steam overlay and transparent window conflict [U] | Medium / Low | Overlay optional; test in matrix | QA |
| 14 | Name clash on "Gloamway" | Medium / Medium | Check before the store page; keep the name changeable (one string constant) | owner |
| 15 | Market migration later hurts saves | Low / Medium | Section 2.9 rules and tests | BE |
| 16 | Option A farming, dupes, inflation (v1.x) | Medium / Medium | Steam-enforced timing, caps, recipes as sinks, paid base game, kill switch, no paid random boxes | BE, D |
| 17 | Legal, tax or regional exposure | Low-Medium / High | Free timed drops only; owner gets human legal and tax advice; agents do not advise | owner |
| 18 | Agent unreliability on a long project (drift, half-finished systems) | Medium / Medium | Every task has executable AC; `tests/run_all.sh` is the arbiter; handoff-writer updates docs each milestone | P, QA, HW |
| 19 | I over-cut and strangle the game | Medium / Medium | Section 1.3 lists restore costs; owner can reverse any cut | P |

---

## 9. Environment prerequisites and first steps

### 9.1 Prerequisites on the owner's laptop
- Windows 10 or 11 (64-bit), a recent integrated or discrete GPU, ideally a second monitor attached for the M0 multi-monitor rows.
- Godot: the exact version pinned in `docs/engine-version.md` (to be written in T0-1), standard build (not .NET unless the pin says so), plus matching export templates. Download only from the official Godot site; do not run any other binary.
- Git (to pull the repo) and a terminal (PowerShell).
- Steam client installed and logged in (needed from the demo phase; not for M0).
- Optional later: Visual Studio Build Tools 2022 and Python 3 with SCons only if the native helper is needed.
- Repo checkout at the current branch; no admin rights needed for M0.

### 9.2 Exact first steps (owner, about 30 to 45 minutes once the build exists)
1. Agents first: T0-1 (engine pin), then T0-3 to T0-5 produce `projects/gloamway/spike/` and `tools/perf_sample.ps1`. The orchestrator tells you when it is ready. You do nothing before that except step 2.
2. Decide the Windows machine (decision 3 below) and make sure you can run PowerShell scripts you review (`Set-ExecutionPolicy -Scope Process Bypass` for one session only; read the script first).
3. Install the pinned Godot (unzip; no installer). Open the project (`projects/gloamway/project.godot`), press Play, or run the exported exe if agents provide one.
4. Run the 12-row M0 checklist (`tests/manual/m0-matrix.md`): click-through over a text editor, 20 clicks on other windows, strip stays on top, hide hotkey, play a fullscreen video and see if it hides, move to the second monitor, set Windows scale to 150 percent and relaunch.
5. Run `perf_sample.ps1` for 10 minutes awake and 10 minutes hidden. It writes a CSV.
6. Send back the CSV and the filled checklist (copy into the repo or paste in chat). Agents write the spike report and the G0 decision.
Nothing in this procedure creates accounts, spends money or touches Steam.

---

## 10. Decisions needed from the owner

Kept to what blocks progress. Defaults apply if you say nothing, except those marked "hard stop".

| # | Decision | Needed by | Default | Notes |
|---|---|---|---|---|
| 1 | **Windows test access.** Will you run the M0 spike and later matrices on your Windows laptop, ideally with two monitors, and can you recruit a few testers? | Before M0 can pass | Owner laptop, no extra testers until Alpha | Without it every window and perf claim stays unverified (K3). Hard stop for G0. |
| 2 | **Approve the cut line** (1.0 = 6 zones, 2 classes, 45 passive nodes, 20 uniques, no music; Gel Tamer, zones 7 to 10, Rifts, festivals in v1.1). | Before VS ends | Approve as written | Section 1.3 gives the restore cost of each cut. |
| 3 | **Theme and name.** Gloamway (lamplighters at dusk) vs Slime Kingdom; and who checks the name for clashes. | Before the Steam page; art direction depends on theme now | Gloamway | Wick and Gel are built either way; a switch after VS costs art rework. |
| 4 | **Price.** Sage proposes $7.99 [D]; alternatives $5.99 or free. | Before the store page | $7.99 placeholder, decided later with demo feedback | Free would weaken the anti-farming rationale for the later Market. |
| 5 | **Steam spend and identity.** Steamworks partner account, tax and bank setup, the app fee (reported $100). | Around G2 (about week 10) | Defer; do nothing until G2 passes | Agents cannot do any of it. Hard stop at G3. |
| 6 | **Unity fallback authority** if K1 triggers. | Only if K1 triggers | Try Godot fixes first (other minor version, native extension); stop and ask you before any Unity work | |
| 7 | **Art budget.** Any human polish for capsule or trailer? | Before the store page | $0, agent-rendered, revisit after G1 | Sage rates charm risk as high. |
| 8 | **Market (v1.x) go-ahead and when to ask Valve.** | After G4 | Start v1.x after release; ask Valve through Steamworks once the app exists | A+ (tradable fixed uniques) stays off. Keepsake odds and daily cap are reviewed then, not now. |

Items I deliberately did not ask now: Keepsake odds, region limits for the Market, music, side-docking, Next Fest participation. They are later-phase decisions.

---

## 11. First actions once approved
1. Orchestrator runs T0-1 (engine pin and sandbox Godot check), T0-2 and T0-8 in parallel.
2. FE and BE build the M0 spike per section 4.1; QA writes the matrix.
3. Owner runs the checklist (section 9.2); planner runs G0.
4. On pass: start the vertical slice. On fail: K1 playbook, then owner message.
