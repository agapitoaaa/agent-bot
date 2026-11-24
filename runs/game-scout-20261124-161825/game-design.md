# Gloamway: Full Game Design Document

Author: Sage (designer). Date: 2026-11-24. Run: game-scout-20261124-161825. Inputs: `memory/designer.md` and `memory/team.md` (both empty of lessons), `ideas/backlog.md` (Game track), `g1-deep-dive.md`. office: stage=design, desk=designer, sprite=designer.

## How to read this document: labels

Every non-trivial statement carries one of these tags, so the owner can tell sourced fact from invention.

| Tag | Meaning |
|---|---|
| [F] | Fact taken from the repo notes (backlog.md, g1-deep-dive.md). Those notes are search-snippet level, never opened-page level, so [F] means "reported in our notes", not "verified". |
| [D] | Design choice. We made it up on purpose; the owner can overrule it. |
| [H] | Hypothesis to playtest or simulate. A number I believe is sensible but have not tested. All balance numbers are [H] unless stated. |
| [U] | Unverified external behaviour (Godot, Steamworks, Valve rules) that needs a spike or the Steamworks docs. |

No market numbers are invented here. Where I give a price or a target, it is tagged [D] or [H] and says so.

Blind-spot warning from Sage: I tend to design lovely things that are expensive to build. Section 12 has a "scope cut list" and an effort table so the owner can see what to cut first.

---

# 1. Pitch

## 1.1 Working title: three options, one pick

| Option | Why | Risk |
|---|---|---|
| **Gloamway** (pick) | A "gloam" is dusk light; the "way" is the road along your taskbar. Short, pronounceable, evocative, suits a lantern theme. | Not yet checked for existing Steam titles or trademarks; the owner or a human must check before the store page. [U] |
| Lantern Strip | Tells you exactly what it is (a strip, a lantern hero). | Reads as generic; "Strip" has an unfortunate adult-content reading in search. |
| Taskbar Tale | Clear and cute; echoes the genre name. | Sounds like a cozy story game, not a loot ARPG; close in feel to "Task Bar Hero" (a TBH-style name invites confusion). [F: TBH exists] |

**Pick: Gloamway.** The rest of this document uses it. Title and any name are [D].

## 1.2 Logline
A tiny lamplighter walks the dusk road along the bottom of your screen, fighting the dark and dropping loot while you work, and you shape the build when you glance down.

## 1.3 Elevator pitch
Gloamway is a desktop-companion idle ARPG. A chibi lamplighter named Wick and a slime familiar named Gel patrol a thin, transparent strip above your taskbar. They auto-fight, auto-collect, and drop gear with random affixes like a proper loot ARPG. You choose skills, passives, gear and when to push a boss. The strip uses almost no CPU, hides itself when a fullscreen app runs, and never steals your clicks. Every hour of play also earns a free, fixed-design collectible "Keepsake" through Steam playtime drops, which can be traded on the Steam Market (Option A below). No paid loot boxes, no server of ours.

## 1.4 Design pillars [D]
1. **Glance, don't stare.** Every important event must be readable in under 2 seconds at 96 px height. Nothing demands attention.
2. **A desktop guest, not a squatter.** Tiny CPU, click-through by default, vanishes when you need the screen. Respect beats retention tricks.
3. **Real ARPG loot, real choices.** Random affixes, sets, uniques, and build-defining passives, not just "number goes up".
4. **Charm from code.** A lovable character built from shapes, motion and sound; squash and stretch carry the personality.
5. **An honest economy.** Free timed drops, fixed odds shown on the store page, no paid random boxes, a kill switch.

## 1.5 Target player [D, with [F] context]
- Primary: PC players (age roughly 18 to 40) who work or study at a computer with a second monitor or idle screen region, who like Diablo-style loot and idle games, and who like anime-flavoured cute characters.
- They already know the pattern: Task Bar Hero, Deskrawl, Desktop Defender, Rusty's Retirement, Tiny Pasture. [F]
- What they punish (from review summaries in our notes [F]): CPU/GPU/battery drain, strips that are too large or block the taskbar, second-monitor instability, buggy prestige systems, shallow repetition, outages and lost loot, bots in the market.
- Secondary: cozy-idle players who like a companion and ignore the loot depth. They must be able to leave the game on "set and forget" and still feel progress.

## 1.6 Platform [D / U]
- Windows 10/11 PC first (the desktop-companion window tricks are best supported there). Steam release. Godot 4 (4.4+ so GodotSteam GDExtension is available [F: GodotSteam GDExtension exists for 4.4+, version naming inconsistent]).
- Linux and macOS: not promised for v1. Wayland has reported drag problems with transparent windows [F]. Treat as post-launch.
- Steam Deck: not a target (desktop strip concept does not fit). Not tested.

## 1.7 Comparable games and how we differ (repo facts only)
| Game | What the notes say [F] | Gloamway difference [D] |
|---|---|---|
| Task Bar Hero (free, optional $20 DLC) | Peak about 526k to 546k concurrent in mid-June 2026; Mixed reviews (about 50 to 53%) over outages, lost loot, cheater crackdown, market strain. Reported "Trade Ship" bridging in-game and Steam inventory. | No server, no bridge. Rich gear stays local; only fixed-design collectibles trade. Lost loot cannot happen to Steam-held items. |
| Deskrawl (Idle ARPG, Sep 28 2026) | Very Positive (271 reviews, snippet), 43k+ concurrent Oct 16 2026 per one article. One tradable "mob" item per 60 minutes, 95% / 4.99% / 0.01% rarity, weekly Monday rotation. Reviews complained the strip is too large, blocks the taskbar, cannot be resized or made transparent. | Same safe drop pattern, but a small, resizable, truly transparent, click-through strip, a deeper loot layer (affixes, sets, crafting), and a stronger character. |
| Desktop Defender ($4.99, Very Positive) | Auto-battler; complaints of buggy rebirth/prestige and shallow repetition. | Our "prestige" (Dusk Tiers) never resets state, so it cannot corrupt progress. More build depth. |
| Rusty's Retirement | About 200k sales in first weeks, 96 to 97% positive, $6.99; cozy, no loot economy. [F] | We borrow the lesson: audience pays for charm. Charm is pillar 4. |
| Tiny Pasture ($5.99, Very Positive) | 5,640 concurrent hours after launch; one complaint of second-monitor instability. | Multi-monitor is a day-one test case. |

Honest note: 1,566 Idler-tagged releases so far in 2026 and "many look eerily similar" [F]. Our standing out depends on charm, a clean strip, and loot depth, not on the genre label. This is the central risk.

---

# 2. Concept and fantasy

## 2.1 Two theme options

| | **Option 1: Slime Kingdom** | **Option 2: Gloamway (lamplighters at dusk)** |
|---|---|---|
| Premise | You keep a slime hero in a gelatin-and-goo fantasy world. | The bottom edge of your screen is a road between worlds; a tiny lamplighter keeps the dark back with a lantern-staff. |
| Strengths | Matches backlog G1; slime anatomy is easy to code-draw; instantly cute. | Cute, but with a stronger visual identity (warm light against dusk). Light as a mechanic (the lantern radius), a natural "idle at dusk, glance at it" tone. Slimes still fit as a faction. |
| Weaknesses | Slime-hero idlers are a visual commodity; one-note palette; harder to make a cast with emotional range. | Needs more distinct shapes (humanoid hero) to code-draw; slightly more build effort. |
| Anime appeal | Mascot appeal only. | Chibi hero, expressive familiar, guild, seasonal festivals, scarf and lantern silhouettes. |
| Loot fit | Equipment on a slime is awkward (it has no body parts). | Humanoid hero makes 8 gear slots visible on screen. |

**Decision: Option 2, Gloamway.** Slimes survive as the Jellyfolk faction and Gel, the hero's familiar. Choice is [D]. The compromise if the build cost bites: Wick can be drawn as a simple bean body with a hat and scarf, a "costume" instead of anatomy (see section 10).

## 2.2 Setting and lore in brief [D]
Long ago the Great Lamp over the Hollow Kingdom went out. The dusk never ended; things that live in the dark crept toward the bright places. The world's edge became a long, thin road called the Gloamway, lit by lanterns. People now live in the glow of the "above" (this is your screen, your desktop, your work). The Lamplighters Guild keeps the road. Wick is a junior lamplighter, newly sent down the road with an old lantern-staff, a slime familiar and not much else. The goal across the campaign: relight ten Beacons, one per zone, and finally the Great Lamp in the Unlit Court. After that, the dusk deepens (Dusk Tiers) because the dark learns.

## 2.3 Tone
Warm, gently funny, quietly melancholy (dusk), never grim. Short barks ("The dark is just shy.") and tiny text. Humour from Gel's expressions and Wick's deadpan optimism.

## 2.4 Main characters and companions [D]
| Character | Role | Look (code-built) | Personality |
|---|---|---|---|
| **Wick** | Hero, the player's avatar. Name and look-slots (hair accent, scarf, outfit colour) are customisable. | Chibi: head about 55% of height, round eyes with highlight, scarf that flows (6-point rope), lantern-staff. Walk cycle by sine bob. | Earnest, a bit clumsy, sleepy after dark. |
| **Gel** | Slime familiar. Carries loot (visual), reacts to events, is a combat "pet" for the Gel Tamer class. | A jelly blob via metaball-ish `_draw()` or shader; wobbles; wears equipped cosmetic Keepsakes. | Loyal, hungry, communicates in squeaks and facial expressions. |
| **Orla Moth** | Crafter and merchant NPC at the Hearth (a UI character, appears in the expanded panel and onboarding). | Wide soft wings, round glasses. | Brisk, fond of scrap. |
| **Grandma Cinder** | Quest-giver, narrates the story in 3-line notes. | Silhouette by a stove, ember eyes. | Proud, teasing. |
| **The Unlit** | Final antagonist (the dark's will). | Shapeless void with a single bright "eye" lantern. | Curious more than evil; ending twist: it wants a lamp too. |

## 2.5 Factions [D]
| Faction | Role |
|---|---|
| Lamplighters Guild | The player's faction. Rank track (Hearth Mastery, section 7) unlocks convenience and cosmetics. |
| Jellyfolk (slimes) | Neutral to allied in Mossbottle Marsh; feral Jellyfolk are enemies elsewhere. Gel's people. A cameo and a class (Gel Tamer). |
| Hollowkin | Bone, bell and candle-wax undead; the main enemy line in mid zones. |
| Thornwild | Wild fae and bramble beasts. |
| Brassworks | Clockwork enemies from Brassgear Hollow; Spark theme. |
| The Unlit | The dark itself; late zones. |

## 2.6 Why it charms an anime fan [D]
- A chibi hero with big expressive eyes and a flowing scarf who visibly reacts to loot (sparkle eyes on a Legendary).
- A mascot familiar (Gel) with an emotion set and cosmetic hats.
- Seasonal festivals, a tiny cast with catchphrases, a "Hearth" home screen you can customise.
- Light, gentle melancholy and the "journey with a companion" fantasy.
- Collectible Keepsakes that read like tiny enamel pins of the cast and monsters.

---

# 3. Desktop companion design

## 3.1 Window modes [D]
| Mode | Behaviour | Default size |
|---|---|---|
| **Strip (docked)** | Borderless, transparent window docked to the bottom edge of the chosen monitor, directly above the taskbar. Anchor left, centre or right with X offset. | 640 x 96 logical px; resizable width 320 to 100% minus 8 px (never full-monitor-size; see risk below) and height 64 to 192. |
| **Floating** | Same window, free-dragged anywhere, remembers position per monitor. | Same. |
| **Hidden / tray** | No window. Tray icon only; simulation runs at the "Resting" rate. | n/a |
| **Panel (expanded)** | Separate normal window (inventory, skills, map, settings). Opens from click on the handle or a hotkey. Not click-through. | 960 x 600, resizable, min 800 x 520. |

- Full-monitor-size transparent windows can flip to exclusive fullscreen in Godot [F], so the strip is always at least 8 px smaller than the monitor in both axes. [D]
- Docking: the strip reads the taskbar edge. If the taskbar is on the side or top, the strip docks to that edge and rotates its layout (rotated version is v1.1; v1 supports bottom taskbar only plus floating mode). [D]

## 3.2 Always-on-top and click-through rules [D, tech [U]]
1. Always-on-top defaults to ON (the strip would otherwise be hidden behind windows).
2. Click-through everywhere except: Wick's hitbox, visible loot pickups (while on screen), toasts with buttons, and a 20 x 20 px "handle" tab at the strip edge. Implemented with Godot `mouse_passthrough_polygon`, regenerated only on change and at most 10 times per second. [F: supported Godot 4.2+; pitfalls reported]
3. Known pitfalls to test in the first-playable spike [F]: polygon made a sprite disappear in 4.6.1; window can drop behind others after a click; Wayland drag problems.
4. Fallback if the polygon is unreliable on a given machine: "Interact mode" (hotkey Ctrl+Alt+G toggles whole strip as clickable for 10 s, otherwise fully click-through).
5. Hotkeys: Ctrl+Alt+G toggle strip visibility; Ctrl+Alt+P open panel; rebindable.
6. The strip never takes keyboard focus unless the player clicks on Wick or the handle. It must never steal focus from a typing app.
7. Steam overlay and transparency compatibility is [U]; spike it. The overlay is optional for us. [F]

## 3.3 How Wick walks, fights and idles on screen [D]
- Wick stands at roughly 25% of the strip's width and "walks in place" while the parallax background scrolls left (cheap: no wide world to render).
- Encounter rhythm (target): a pack of 3 to 4 enemies enters from the right every 10 s on average [H]: 3.5 s walking, 5.5 s fighting, 1 s loot pop.
- Fight staging: Wick lunges (melee) or fires (ranged). Hit effects are simple shapes. Gel hovers, bounces, pounces.
- Loot: items arc out of defeated enemies in small icons and are picked up automatically (magnetised to Wick). Rare and better items show a rarity ring and a short sound; Legendary shows a toast with a "keep" button.
- Idle states (rotating, 8 to 30 s each, 4 variants each): pause to tie a scarf, drink from a thermos, stretch, sit and swing legs, read a map. Idling happens between zone transitions or while "waiting for the next pack". Never while the player is hovering over Wick.
- Hover behaviours: pets (click-and-hold on Wick gives a heart and a Gel purr), drag to relocate in floating mode.
- Time of day: the lantern glow follows the system clock (warmer at night). Purely cosmetic. [D]

## 3.4 Fullscreen apps, games, sessions
- Detect fullscreen foreground app: on Windows through `SHQueryUserNotificationState` via a small GDExtension or helper. [U: no Godot example found; this is a first-playable spike] Fallbacks: manual tray toggle, hotkey, and "pause while these processes run" list the player maintains.
- When detected (or locked screen, or display off, or on battery saver if the player enabled it): the strip window is hidden and the scene tree is paused. The game enters **Resting** mode (see section 4.8). Wake automatically when the fullscreen app ends, with a 3-second fade-in.
- Never overlay on top of exclusive fullscreen. Never "peek". [D]

## 3.5 Performance budgets [H targets; must be measured]
| Budget | Target | Method |
|---|---|---|
| Strip active, 30 FPS cap, default settings | under 2% of one logical core average on a mid-range laptop; no discrete GPU wake | profile on owner-provided machine; Godot low-processor mode; draw calls under 150 |
| Strip active, "Eco" preset (15 FPS, no particles) | under 1% of one core | same |
| Resting (hidden) | under 0.3% of one core, wakes once per 30 s | tick scheduler |
| RAM | under 180 MB active, under 120 MB resting | measure on Windows; Godot baseline is not in our notes [U] |
| Disk | under 400 MB install (no big assets) | code-drawn art |
| Power | no GPU use when hidden; honour "battery saver" toggle | setting |
| Save | write at most once per 30 s and on key events; atomic write (temp file then rename) with 3 rolling backups | prevents lost loot [F: TBH lost loot] |

Frame cap options: 60 / 30 / 15 FPS. Default 30. A 1 FPS paused state is used when the strip is hidden. [F: one forum report of about 1% CPU at 1 FPS paused tree]

## 3.6 Multi-monitor [D / U]
- Settings let the player choose monitor and edge. Remembers per monitor; reattaches when a monitor is added or removed (listen for screen change; fall back to primary).
- DPI: scale UI per monitor; layout in logical px with 100/125/150/200% scale tested.
- We cannot test real multi-monitor hardware in our sandbox. [F] Plan: ask the owner or testers to run a 2-monitor checklist (appendix list in section 12). Mark multi-monitor stable only after it is passed.

## 3.7 Notifications
- In-strip toasts only, small (max 220 x 36 px), with a 4-second fade. Types: Legendary drop, boss ready, level-up (silent by default), Keepsake received, offline summary.
- No Windows system notifications unless the player enables them; default: off. Never flashing the taskbar icon.
- Batching: no more than 1 toast per 3 seconds; extras collapse into a counter ("+6 items").
- Quiet hours setting: no sound or toasts between chosen times.

## 3.8 "Never be annoying" rules [D]
1. No sound at install default except tiny SFX at low volume (master 25%, music off). Music is opt-in.
2. Never move or resize the player's windows. Never steal focus.
3. Never ask for ratings or reviews more than once, and only after 10 hours of play.
4. No pop-ups, no "come back" push, no streak-loss guilt. Daily tasks do not expire in a punishing way (they bank up to 3).
5. Never block the taskbar: default offset keeps clear of the notification area and system buttons.
6. Never play loud sounds on rare events; instead use pitch and a visual flash.
7. A single "Quiet" button in the tray silences everything for 1 hour.

## 3.9 Accessibility [D]
- Colour: rarity is never colour only; each rarity has a frame shape (see 10.4). Colour-blind palettes (3) supplied.
- Text: minimum 12 px logical in the panel, 10 px in the strip; text scale 100 to 200%.
- Motion: "Reduce motion" turns off screen shake, flash and squash intensity to 30%.
- Sound: visual indicators for every audio cue (a small ring pulse), subtitle-style toast for bosses.
- Input: full keyboard navigation in the panel; no time-limited actions; one-handed possible.
- Photosensitivity: no flashes above 3 per second; flash intensity under 40% opacity.

---

# 4. Core loop

## 4.1 Loop by timescale [D]
| Scale | What the player sees and does |
|---|---|
| **10 seconds** | A pack enters, Wick auto-fights, enemies burst, loot arcs up and is picked up. Wick may flare (an auto-skill), Gel pounces. Optional: click the handle. Nothing is required. |
| **1 minute** | About 6 encounters (about 20 kills). XP bar creeps; 1 to 3 items drop; Plain/Fine are auto-salvaged by the filter, Rare+ show a rarity ring. A stage counter ticks. |
| **10 minutes** | Roughly 60 encounters. A stage clears; a mini-boss appears around stage 10; one or two Rare drops to check. A glance to equip or compare; maybe a level-up and a passive point. |
| **1 hour** | 3 to 6 stages; 10 or so Rare+, 2 to 3 Epic, a Legendary about every 3 hours on average [H, see 6.3]. Craft or enhance with salvage Dust; push a boss; receive one Keepsake (timed drop, section 8). |
| **1 day** | 2 to 6 hours of strip uptime for a typical office player; one zone's worth of progress early game; 3 daily quests; a few crafting sessions; up to 6 Keepsakes (cap; section 8). |
| **1 week** | Weekly Beacon boss (world boss), weekly Keepsake rotation on Monday, one zone completed or a Dusk Tier push, weekly quests, build experiments, trading surplus Keepsakes (optional). |

## 4.2 Time model [D / H]
- Simulation tick: 10 per second (fixed step); rendering at the FPS cap.
- Encounter cadence: 1 pack per 10 s average, 3.3 enemies per pack: **20 kills per minute** at default Pace. [H]
- Pace stat (gear and passives) adds up to +40% encounters per minute (cap).

## 4.3 Awake, Resting and Offline: three states, one formula
Let `K` = kills per minute at the player's current farm stage, `R` = reward per kill (XP, Wisps, drop table).

| State | When | Efficiency `e` | Notes |
|---|---|---|---|
| **Awake** | Strip visible | 1.00 | Full simulation with animation. |
| **Resting** | Strip hidden, tray mode, fullscreen app, locked screen | 0.60 | Simulated in 30-second batches with the expected-value model (below). Steam playtime still accrues because the app is running (so Keepsake drops continue; see section 8). |
| **Offline** | App closed | 0.40 base, 0.55 with "Lantern Hearth II" (Mastery) | Capped; computed on launch. |

Gains formula for a duration `T` minutes in a state with efficiency `e`:
- `Kills = T * K * e`
- `XP = Kills * XPkill`; `Wisps = Kills * Wispkill`; `Items = Kills * p_gear` (see 6.2), but bounded (4.4).
- `K` is evaluated at the **safe farm stage**: the highest stage where the hero's simulated win chance is at least 90% (computed by the same Power Score model the game shows), minus 1 stage as margin. [D]

## 4.4 Offline caps and rules [D / H]
| Rule | Value |
|---|---|
| Max credited offline time | 8 h base; 10 h at Hearth Mastery rank 5; 12 h at rank 10 |
| Efficiency | 0.40 base (0.55 with upgrade) |
| Max items rolled and delivered per offline session | 60 (anything beyond converts directly to Dust at the salvage value) |
| Bosses and mini-bosses | Never progressed offline; no stage push |
| Quests | Kill-count and "collect" objectives credit; boss objectives do not |
| Keepsakes | **Never granted by our code.** Offline is not playtime, so Steam grants nothing; this is automatic. |
| Clock tampering | If the system clock moves backwards, credit 0 for that session and keep the previous timestamp. If a gap exceeds the cap, credit the cap only. Local-only game, so cheating hurts only the cheater; this guard just prevents accidents. |
| Summary | A one-screen "While you were away" card: time credited, kills, XP, items kept versus auto-salvaged, with an "Open" button. |

Example: 8 h offline at farm stage with K = 20 and e = 0.40 gives 8*60*20*0.40 = **3,840 kills**, 0.6 items/min nominal * 0.40 * 480 min = about 115 items rolled, capped to 60 delivered, the rest to Dust. Check: Resting for 8 h at e = 0.60 would give 5,760 kills. [H]

## 4.5 Flow of a session
First run: onboarding (9.4). Later: launch, offline summary if away more than 10 minutes, strip appears, play resumes. Closing the panel returns to the strip. Quitting from the tray saves and exits.

---

# 5. Combat

## 5.1 Auto-combat model [D]
- 1D lane, deterministic seeded simulation at 10 ticks per second. Hero at the left; enemies enter from the right and stop at a "contact distance" (melee) or at their range.
- Attack interval, skills with cooldowns, resources:
  - **Basic attack** (weapon, interval 1.0 s base, modified by Attack Speed).
  - **Skills (auto-cast)**: 4 active slots + 1 ultimate slot. Each skill has a cooldown 3 to 20 s. The hero casts the first ready skill in the player-set priority order, subject to a rule per skill (see 5.5).
  - **No mana.** Cooldowns only (simpler to simulate and to run offline). [D]
- Damage formula:
  - `Hit = ATK * SkillMult * (1 + Σ%Damage) * (CritRoll ? CritMult : 1) * (1 + ElemBonus) * (1 - EnemyRes)`
  - `ATK` is the weapon's flat DPS-equivalent plus flat ATK affixes.
  - `CritMult = 1.5 + CritDmg%` (base crit chance 5%, cap 60%).
  - `Dodge` cap 40%.
- Mitigation: `DR = Armor / (Armor + K(eL))`, with `K(eL) = 50 * 1.13^(eL - 1)`, capped at 75%. [H]
- Elements: Physical plus Ember, Frost, Venom, Spark. Enemy weaknesses and resistances in the roster (each enemy has one weakness at -25% resistance, one resistance at +25%).
- Death: **Faint**, not death. Wick drops to the previous stage, a 10 s "relight" countdown, no item or XP loss. A "stuck" hint suggests an upgrade (e.g., "Your Armor is low for Candlewood"). [D]

## 5.2 Target power and enemy curve (sample values)
Let `eL` be the enemy level and `S(L) = 1.15^(L-1)`.
- Enemy HP = `25 * 1.15^(eL-1)`; enemy hit = `4 * 1.13^(eL-1)`; both multiplied by archetype factor (table 5.3).
- Target: time to kill a normal pack member about 4 s on-curve; hero survives about 20 on-level hits before mitigation. [H]

| eL | S = 1.15^(eL-1) | Enemy HP | Enemy hit | Target hero DPS (HP/4) | Target hero HP (20 hits) |
|---|---|---|---|---|---|
| 1 | 1 | 25 | 4 | 6 | 80 |
| 10 | 3.5 | 88 | 12 | 22 | 240 |
| 20 | 14.2 | 356 | 41 | 89 | 820 |
| 30 | 57.6 | 1,440 | 138 | 360 | 2,760 |
| 40 | 233 | 5,820 | 470 | 1,455 | 9,400 |
| 50 | 942 | 23,550 | 1,596 | 5,890 | 31,900 |
| 60 | 3,813 | 95,300 | 5,396 | 23,800 | 107,900 |

These are first-pass targets. A simulation script must tune gear tables against them (see risks).

## 5.3 Enemy types (archetypes, all procedurally skinned per zone) [D]
| Archetype | HP x | Hit x | Speed | Behaviour | Counter-play |
|---|---|---|---|---|---|
| Skitter | 0.7 | 0.8 | fast | Rushes, dodges 10% | Multi-hit and AoE skills |
| Bruiser | 1.8 | 1.2 | slow | Absorbs, knockback | Burst and Armor Pierce |
| Slinger | 0.8 | 1.0 | static, ranged | Hits from range | Reach, fast kill |
| Hexer | 0.9 | 0.6 | static | Casts curse: -20% your damage 5 s | Cleanse passive, burst |
| Swarmling | 0.3 | 0.4 | fast | Arrive in groups of 6 | AoE and chain |
| Shielded | 1.2 | 1.0 | medium | Shield absorbs 30% max HP, regens | Element weakness, shield break |
Elite = any archetype x4 HP, x1.6 hit, one modifier from the 12-modifier list (Burning, Frozen, Venomous, Static, Fast, Armored, Vampiric, Thorny, Splitting, Shielding, Regenerating, Swift Casting). Elite chance: 1 in 40 packs. [H]

## 5.4 Bosses [D]
- Boss = HP x30, hit x2.5, 2 to 3 phases, with a telegraphed attack shown by a ring on the strip (a 1.5 s warning). Two mechanics per boss max, both handled by stats, not reflexes (so idle-safe): e.g., "Enrages after 60 s" (needs DPS), "Summons adds at 66% HP" (needs AoE), "Applies a curse" (needs Cleanse).
- Boss timer: 90 s. On timeout, Wick retreats, boss resets, no penalty.
- Boss pushes are the only moments the player must actively choose to proceed (button on the strip or panel; or an "Auto-push when win chance is 80%+" toggle). [D]

## 5.5 Skills [D]
Skills belong to class or shared pools. Each class has 7 class skills + shared pool. Each skill has 5 ranks (Wisps) and 2 mods unlocked at rank 3 and 5 (choose 1 of 2 per tier).
Skill rule (set per skill): Always, On elite or boss, When HP below 50%, When 3+ enemies, Never. This is the primary agency of an auto battler.

Sample skill table (class skill examples):
| Skill | Class | Cooldown | Effect (rank 1) | Scaling per rank |
|---|---|---|---|---|
| Flare | Lampwright | 6 s | 220% ATK Ember burst to front enemy and 2 behind | +25% |
| Wick Dash | Lampwright | 9 s | Dash and hit all enemies in path for 160% ATK | +20% |
| Hush Arrow | Hush Archer | 4 s | 180% ATK single, +30% crit chance for this shot | +20% |
| Frost Volley | Hush Archer | 10 s | 5 arrows 90% ATK each, Frost slow 20% | +10% each |
| Gel Pounce | Gel Tamer | 8 s | Gel leaps for 200% ATK Venom, heals Wick 3% max HP | +25% |
| Jelly Wall | Gel Tamer | 14 s | Gel absorbs the next 5 hits | +1 hit |
| Lamp Nova (ultimate) | All, class-flavoured | 45 s | 600% ATK to all enemies | +60% |

## 5.6 Player agency: what the player decides
1. Class and skill set (4 + ultimate) and each skill's rule.
2. Gear, affix rerolls, enhance, which Legendary build to chase.
3. Passive tree points (respec costs Wisps, reduced early).
4. Where to farm (any cleared stage; the "Farm here" pin) and when to push a boss.
5. Aggression dial (3 settings): **Cautious** (-15% damage dealt, -25% damage taken, +0% loot), **Steady** (neutral), **Bold** (+20% enemy HP and hit, +25% XP and +15% Find). Bold risks fainting, giving faster yet less safe progress. [H]
6. Loot filter rules and auto-equip.
7. Optional: tap the handle to trigger Lamp Nova manually (always works; also auto-casts when ready if "Auto ultimate" is on).
Nothing requires attention minute to minute. [D]

## 5.7 Classes (3 at launch; a 4th later) [D]
| Class | Fantasy | Weapon | Element | Playstyle | Signature passive |
|---|---|---|---|---|---|
| **Lampwright** | Melee torch-bearer | Lantern-staff or hammer | Ember | Burn damage over time, sustain on kill | "Kindling": each kill adds +2% damage for 6 s (stacks to 10) |
| **Hush Archer** | Quiet ranged scout | Bow | Frost | Crit, slows, long-range safety | "Steady Aim": +1% crit chance per 1 s without taking damage (max 20%) |
| **Gel Tamer** | Summoner with Gel | Staff or whistle | Venom | Gel pets deal 40% of damage; wide AoE | "Split": Gel spawns a mini-Gel every 12 s (max 3) |
A fourth class, Spark Tinker (Spark, turrets), is a post-launch candidate. Respec of class is allowed at no cost before level 10, then costs Wisps.

## 5.8 Passive tree outline: "The Constellation" [D]
- 90 nodes: 18 in the central ring (shared), 24 in each of three class arms (72), total 90.
- Points: 1 per level from 2 to 60 (59), plus 6 from main-story quests = 65, plus Dusk Tier bonus points (1 per tier, up to 5) = 70.
- Node types: 60 minor (+3 to 8% of a stat), 24 notable (+15% of a stat or a small effect), 6 keystones (2 per class), e.g., Ember: "Cinder Heart: burn damage can crit, -20% Armor".
- Central ring: Vigor (HP), Brightness (Find), Pace (encounter speed), Frugal (Wisps), Resolve (Faint relight time), Archivist (stash).
- A full tree view is panned and zoomed on the panel; node count keeps it implementable (data-driven JSON).

---

# 6. Loot

## 6.1 Slots (8) [D]
Weapon, Offhand (lantern, shield or quiver by class), Head, Chest, Boots, Amulet, Ring A, Ring B. Plus a non-power "Companion" display slot used by Keepsakes (cosmetic).

## 6.2 Rarities and drop rates [D / H]
Per gear drop (not per kill). Gear-drop chance per normal kill is 1.5%; elite packs drop 2 items; bosses drop 5 with at least 1 Rare or better.

| Rarity | Frame shape | Normal drop odds | Elite drop odds | Affix count | Colour |
|---|---|---|---|---|---|
| Plain | circle | 55.0% | 20.0% | 1 | grey `#B8B2C8` |
| Fine | rounded square | 30.0% | 40.0% | 2 | green `#6FD08C` |
| Rare | diamond | 11.5% | 30.0% | 3 | blue `#5AA9FF` |
| Epic | hexagon | 3.0% | 8.5% | 4 | purple `#B77CFF` |
| Legendary | star | 0.5% | 1.5% | 4 + unique effect | amber `#FFB547` |

Rates at default: normal gear drop 20 kills * 1.5% = **0.3 items/min**; elite packs 1/40 of 6 encounters/min = 0.15/min * 2 items = **0.3 items/min**; total **0.6 items/min = 36 items/hour**. Rare or better about **10 per hour**, Epic or better about **2.5 per hour**, Legendary about **0.36 per hour (one per 2.8 hours)**, before Find. [H, computed from the table above]

Find stat: multiplies the chance of non-Plain rarities by `(1 + Find)`; cap +100% total, taken from the Plain share. Diminishing: effective Find = `F / (1 + F/2)` when F is above 50%. [D]

Boss unique chance: each zone boss has a 10% chance to drop its named unique. [H]

## 6.3 Item level and base values
- `ilvl` = enemy level (equals the zone level at drop).
- Base item types by slot, with 3 base types per slot per band, 5 bands = about 120 bases (data-driven). Example weapon base DPS = `2.0 * S(ilvl)`; armour piece base Armor = `0.6 * S(ilvl)`.
- Flat affixes scale with `S(ilvl) = 1.15^(ilvl-1)`; percent affixes use tiers gated by `ilvl`.

## 6.4 Affix pools: example tables
**Flat affixes** (value = roll in range * S(ilvl), rounded):
| Affix | Range (x S) | ilvl 1 | ilvl 20 | ilvl 40 | ilvl 60 | Slots |
|---|---|---|---|---|---|---|
| +ATK | 0.35 to 0.60 | 0 to 1 | 5 to 9 | 82 to 140 | 1,334 to 2,288 | Weapon, Ring, Amulet, Offhand |
| +Max HP | 2.5 to 4.5 | 3 to 5 | 36 to 64 | 583 to 1,050 | 9,533 to 17,159 | Chest, Head, Boots, Amulet |
| +Armor | 0.8 to 1.5 | 1 | 11 to 21 | 186 to 350 | 3,050 to 5,720 | Chest, Head, Boots, Offhand |
| +HP regen per s | 0.05 to 0.10 | 0.1 | 0.7 to 1.4 | 12 to 23 | 190 to 380 | Chest, Boots, Ring |
Percent affixes (tiers T1 to T5 gated by ilvl 1, 13, 25, 37, 49):
| Affix | T1 | T2 | T3 | T4 | T5 | Cap | Slots |
|---|---|---|---|---|---|---|---|
| % Damage | 4 to 8 | 8 to 14 | 14 to 22 | 22 to 32 | 32 to 45 | none (diminishing at +300%) | Weapon, Amulet, Ring |
| Crit chance % | 1 to 2 | 2 to 3 | 3 to 4.5 | 4.5 to 6 | 6 to 8 | 60 total | Weapon, Ring, Head |
| Crit damage % | 6 to 10 | 10 to 16 | 16 to 24 | 24 to 34 | 34 to 48 | none | Weapon, Amulet |
| Attack speed % | 2 to 4 | 4 to 6 | 6 to 9 | 9 to 12 | 12 to 16 | +100 total | Weapon, Offhand, Boots |
| Find % | 3 to 6 | 6 to 10 | 10 to 15 | 15 to 21 | 21 to 28 | +100 total | Head, Amulet, Ring |
| Pace % | 2 to 4 | 4 to 6 | 6 to 8 | 8 to 10 | 10 to 12 | +40 total | Boots, Ring |
| Dodge % | 1 to 2 | 2 to 3 | 3 to 4 | 4 to 5 | 5 to 6 | 40 total | Boots, Chest |
| Elemental damage % (Ember, Frost, Venom, Spark; one affix each) | 5 to 9 | 9 to 15 | 15 to 23 | 23 to 33 | 33 to 46 | none | Weapon, Offhand, Amulet |
| Skill cooldown % | 2 to 3 | 3 to 4 | 4 to 5.5 | 5.5 to 7 | 7 to 9 | 40 total | Head, Offhand |
| Wisp gain % | 4 to 8 | 8 to 14 | 14 to 22 | 22 to 32 | 32 to 45 | +150 total | Ring, Amulet |
Rules: no duplicate affix group on one item; Legendary rolls its 4 affixes at one tier above the normal band cap per ilvl (T5 max). A "Perfect" roll (top 10% of a range) shows a gold dot. [D]

## 6.5 Crafting, upgrading, recycling [D / H]
Currencies and materials:
| Name | Source | Use |
|---|---|---|
| Wisps | kills (about `3 * 1.14^(eL-1)` per kill) | skill ranks, passive respec, enhance fee |
| Dust | salvage | reroll, enhance |
| Glow | elites (20% chance per elite), bosses (3 to 5) | rarity upgrade |
| Echo | salvaging a Legendary (1) | reroll legendary affix |

Dust from salvage = `base * (1 + ilvl/20)`; base Plain 2, Fine 6, Rare 20, Epic 80, Legendary 300 (+1 Echo).
| Action | Cost | Rule |
|---|---|---|
| **Salvage** | free | Destroys the item, gives Dust |
| **Rekindle** (reroll one affix) | `40 * (1+ilvl/20)` Dust, x1.5 per use on that item; locking one affix doubles the cost | Reroll within the allowed tier for the ilvl |
| **Kindle** (upgrade rarity) | Fine to Rare: 150 Dust + 1 Glow; Rare to Epic: 800 Dust + 3 Glow | Adds a random affix; Legendary cannot be crafted, only dropped |
| **Enhance** +1 to +10 | `30 * (1+ilvl/20) * 1.6^n` Dust + Wisps | Each +1 gives +3% to the base stat of the item; 100% success, no destruction. |
| **Transmute** | 100 Dust | Re-roll the base type within the same slot, keeping rarity and ilvl, once per item |
Sample sink: at ilvl 30, Dust per hour about 820 (36 items/h at about 22.8 Dust each) [H]. Enhance +1 costs 75, +5 costs 786, +10 costs 8,240 Dust. Kindle Rare to Epic costs 800 Dust + 3 Glow.

## 6.6 Sets and uniques [D]
- **Uniques (Legendary)**: 40 at launch; each has a fixed named effect plus 4 rolled affixes. Examples:
  - *The Last Match* (weapon): Flare also leaves a burning ground for 4 s.
  - *Moth-silk Scarf* (head): +1 Dodge per 2 kills (max 20, resets on hit).
  - *Gel's Lunchbox* (offhand): Gel pets also collect and heal 1% HP per item pickup.
- **Sets**: 6 sets of 4 pieces, dropped as Epic variants (25% of Epic drops in their zone band). Bonuses at 2, 3, 4 pieces.
  | Set | Zone band | 2 pcs | 4 pcs |
  |---|---|---|---|
  | Hearthkeeper | 1 to 2 | +10% HP | Flare cooldown -20% |
  | Mossbottle Regalia | 2 to 3 | +15% Venom damage | Gel pets +1 |
  | Brasswright | 4 to 5 | +12% Spark damage | Chains hit 2 more |
  | Candle Choir | 6 to 7 | +10% Armor | Heal 3% on kill |
  | Frostbell Watch | 6 to 8 | +20% Frost | Slow also reduces enemy damage 20% |
  | Dawnwalker | 9 to 10 | +10% all damage | Lamp Nova ready on boss start |

## 6.7 Loot filter [D]
A rule list evaluated top to bottom. Condition fields: rarity, slot, ilvl range, contains affix, "power score better than equipped by X%". Actions: Keep, Auto-salvage, Auto-equip, Highlight (adds a bright ring), Mute. Default filter:
1. Legendary or Epic: Keep and highlight.
2. Anything better than the equipped item by 10% or more: Keep.
3. Rare: Keep for 30 minutes, then auto-salvage unless starred.
4. Fine and Plain: Auto-salvage.
Stash starts at 100 slots, +20 per 2 Hearth ranks to 200. Overflow auto-salvages the oldest unstarred item (with a toast).

## 6.8 Inventory UI
See wireframe 9.3. Power Score is a single number comparing items (`simulated DPS * effective HP` index) so a casual player can decide at a glance; advanced players read the tooltip. A green up arrow with percent shows delta against the equipped slot.

---

# 7. Progression and content scale (v1)

## 7.1 Zones (10), each 20 stages [D]
Stage 20 is the boss; stage 10 is a mini-boss.
| # | Zone | Levels (eL) | Theme and enemies | Boss | Est. hours at on-curve power [H] |
|---|---|---|---|---|---|
| 1 | Hearthside Verge | 1 to 6 | Meadow, tutorial; Gloomlings, wild Jellyfolk | Old Wicker (scarecrow) | 1.5 |
| 2 | Mossbottle Marsh | 7 to 12 | Marsh; feral and friendly Jellyfolk, frogs | Queen Gloop | 2.5 |
| 3 | Candlewood | 13 to 18 | Waxy forest; Thornwild, wisps | The Wax Stag | 2.8 |
| 4 | Brassgear Hollow | 19 to 24 | Clockwork; Spark | The Mainspring | 3.0 |
| 5 | Cinder Quarry | 25 to 30 | Ember rock, magma slimes | Foreman Slag | 3.0 |
| 6 | Frostbell Pass | 31 to 36 | Snow, bells; Frost | Lady Rime | 3.0 |
| 7 | Sunken Bellfry | 37 to 42 | Hollowkin undead, bells | The Drowned Sexton | 3.0 |
| 8 | Stormglass Heights | 43 to 48 | Storm, glass spires; Spark | Stormwing | 3.0 |
| 9 | The Underlake | 49 to 54 | Dark water, deep slimes | The Lampreyking | 3.0 |
| 10 | The Unlit Court | 55 to 60 | The Unlit, shadows of earlier bosses | The Unlit | 3.5 |
Total about 28 hours to clear the campaign if the player is online or resting efficiently (consistent with 7.5). [H]

Level for enemy at zone `z`, stage `s` (1 to 20): `eL = 6*(z-1) + 1 + floor((s-1)*5/19)`.

## 7.2 Enemy roster counts (v1) [D]
| Item | Count | How made |
|---|---|---|
| Base enemy variants | 60 (6 archetypes x 10 zones, each skinned) | Shape grammar + palette per zone |
| Elite modifiers | 12 | Shader/colour overlays and a small effect |
| Mini-bosses | 10 | Bigger composite shapes |
| Zone bosses | 10 | Hand-composed shape rigs, 2 to 3 phases |
| Weekly world bosses ("Beacon" challenges) | 3 (rotating) | Reuse boss rigs with new palettes and mechanics |
Total distinct sprites to construct by code: about 95; because they are grammar-driven this is a small-asset, mid-code job.

## 7.3 Events, quests, achievements [D]
- **Events**: Weekly Monday rotation (Keepsake pool and a weekly modifier such as "Venom Week: +25% Venom damage for everyone"); 4 seasonal festivals per year (the player sees themed decorations and a limited cosmetic); "Moth Night" random event, once per day: a lantern moth runs across; clicking it gives a small bonus.
- **Quests**: 40 story quests (2 to 4 per zone), 3 daily quests (kill N, craft N, salvage N), 3 weekly quests; dailies bank up to 3 so missing a day never punishes. Rewards: Wisps, Dust, Glow, a passive point from 6 key story quests.
- **Achievements (Steam)**: 60. Examples: first Rare, 100 salvaged, clear each zone, equip a full set, 10 Legendaries, reach Dusk Tier III, first Keepsake, "Leave the strip untouched for 8 hours".

## 7.4 Endgame, prestige-equivalent, mastery [D]
- **Dusk Tiers** (instead of a reset prestige): after zone 10, pick a tier I to V. Each tier adds enemy HP and hit `x(1.8)^tier` over base, raises item level cap by 8 per tier (ilvl 68 at tier 1; the formulas above extend), +10% Find per tier, and unlocks new drops (tier-only uniques, 10 more). **No reset of level, gear or zones.** Corruptible-state risk is small because it is a multiplier. This is a deliberate answer to complaints about buggy rebirth systems [F: Desktop Defender summary].
- **Glimmer Rifts** (endgame content): a timed 10-minute run with 3 random modifiers; reward chests scale with rift level; auto-run from the panel; leaderboard is local (no server in v1).
- **Hearth Mastery** (account track; points never reset): rank 1 to 20, XP from any activity. Unlocks: offline cap increases, extra stash, loot filter slots, cosmetics, the Gel hat selection. Capped, convenience only, no power beyond +5% Wisp gain.
- **Weekly Beacon boss**: one world boss with a modifier; rewards a cosmetic and a bonus Legendary roll chance (+5%).

## 7.5 XP and difficulty curve formulas [D / H]
- XP to reach level `L+1`: `XPneed(L) = round(40 * L^1.9)`. Total XP to level 60 about 1.97 million.
- XP per normal kill: `1.3 * eL`, x4 elite, x25 boss. Newcomer bonus: x3 while below level 10.
- Kills to level at on-curve power: `XPneed / XPkill = 30.8 * L^0.9`.
| Level | XP to next | XP per kill (normal) | Kills to level | At 20 kills/min |
|---|---|---|---|---|
| 1 | 40 | 3.9 (with newcomer x3) | 10 | 0.5 min |
| 5 | 1,150 (approx) | 19.5 | 59 | 3 min |
| 10 | 3,177 | 13 | 244 | 12 min |
| 20 | 11,750 | 26 | 450 | 23 min |
| 30 | 25,600 | 39 | 660 | 33 min |
| 40 | 44,900 (approx) | 52 | 860 | 43 min |
| 50 | 68,300 (approx) | 65 | 1,050 | 53 min |
| 59 | 91,700 (approx) | 77 | 1,200 | 60 min |
(Newcomer bonus applies below level 10; rows above level 10 omit it. Approximate rows are rounded estimates [H].)
- Hours-to-level-60 estimate: sum of the "At 20 kills/min" column over all levels is roughly 27 to 30 hours [H]. This matches the zone table in 7.1.
- Soft gate: a stage's win chance is shown on the map as a traffic light; the game never hard-locks levels, only boss pushes warn.

---

# 8. Economy and Steam Market

## 8.1 Sources and sinks (local economy) [D / H]
| Currency | Sources | Sinks |
|---|---|---|
| Wisps (soft) | Kills, quests, salvaging | Skill ranks (rank n costs about `50 * 1.5^n * (1 + level/10)`), respec, Enhance fee |
| Dust | Salvage (about 820/h at ilvl 30) | Rekindle, Kindle, Enhance, Transmute |
| Glow | Elites, bosses | Kindle |
| Echo | Legendary salvage | Legendary reroll |
Design intent: nothing local is tradable, so no local inflation hurts a market. All progression currencies are earned; none sold for real money. [D]

## 8.2 Option A: tradable Keepsakes (default) [D, based on F]
- **What trades:** only "Keepsakes", fixed-definition Steam inventory items. They are collectibles (cosmetic), not power. Random-affix gear is never tradable. [F: random affixes do not survive trade; dynamic properties cleared on trade and not shown on Market]
- **How they are granted:** a Steam `playtimegenerator` item definition plus `TriggerItemDrop`, with no server of ours. Steam tracks playtime and caps. [F]
- **Drop timing [D, field semantics [U]]:** 1 drop per 60 minutes of playtime; max 6 per 24 hours per player; the intended weekly maximum is 42. Configure with `drop_interval = 60`, a per-window cap through `drop_window` and `drop_max_per_window` (1,440 minutes, 6), and a lifetime `drop_limit` is left unset in v1. The exact field behaviour must be checked in the Steamworks docs before use. [U]
- **Playtime includes Resting but not Offline.** The game calls `TriggerItemDrop` at most once per interval, with exponential backoff on failure. It never loops or polls. [F: Valve strain from careless calls (TBH)]
- **Rarities and odds:** Common 90%, Rare 9.5%, Mythic 0.5%. [D, odds are our own; they are not copied from Deskrawl's 95 / 4.99 / 0.01 [F]] At 6 drops/day, a Mythic arrives on average once per 33 days for a maxed-out player. No pity system is possible without server state; say so on the store page. [D]
- **Pool design:** 30 Keepsake definitions at launch: 14 Common, 10 Rare, 6 Mythic. A weekly rotation selects 8 Common, 5 Rare, 3 Mythic as the "active" pool; the remainder is out of rotation but remains tradable. Rotation requires the developer to update the generator definition each Monday (manual action or Steam Web API from a machine of ours; needs owner sign-off and a verified mechanism [U]).
- **Caps:** per-user daily cap 6; no sources besides playtime drops and recipes.
- **Recipes (Steam exchange, validated by Steam, no server [F]):**
  | Recipe | Input | Output | Intent |
  |---|---|---|---|
  | R1 | 10 Commons from the same zone | 1 Rare of that zone (player-chosen among 2 to 3 [U: whether choice is possible]) | Sink and set completion; about parity with the 10.5 drops a Rare takes |
  | R2 | 12 Rares from the same zone | 1 Mythic of that zone | Mythic by drop needs about 200 drops (1 in 200); recipe costs about 126 drops' worth, so Mythics are obtainable but not cheap |
  Recipes inherit the latest trade restriction of any input. [F]
- **Item definition sketch (names illustrative):**
  | Zone | Common (examples) | Rare | Mythic |
  |---|---|---|---|
  | Hearthside Verge | Wicker Pin; Dew Drop; Tiny Scarecrow | Lamp-Moth Pin; Gel Pup | Wick's First Lantern |
  | Mossbottle Marsh | Frog Hat; Moss Bean; Gloop Charm | Queen's Crown; Marsh Lantern | Queen Gloop Plush |
  | Candlewood | Wax Drip; Acorn Lantern; Hushed Owl | Wax Stag Antler; Candle Fox | Candle Choir Bell |
  | (continues for 10 zones: 3 definitions per zone at launch on average) | | | |
  Fields per definition: `itemdefid`, `name`, `description`, `type` (item), `tradable: true`, `marketable: true`, `icon_url` (rendered from our code; PNG, uploaded by the owner), `background_color`, `tags` (zone, rarity), and for generator `bundle` weights.
- **What Keepsakes do in game (all cosmetic):** shown on the Hearth shelf; equippable on Gel (hat or trail), a coloured lantern flame, a strip decoration, a unique idle animation for Wick. A Keepsake does not change stats. A Collector's Book shows owned definitions; the book never grants stats. [D] Verification: the client reads the Steam inventory, so ownership is whatever Steam says.
- **A+ variant (owner decision, off by default):** fixed unique Legendary items as tradable definitions. Fixed stats survive trade; it creates pay-for-power incentives and a stronger bot target. Not in v1 without the owner's explicit choice.

## 8.3 Anti-bot and anti-dupe (Option A)
| Risk | Defence | Honest limit |
|---|---|---|
| Multi-account farming | Steam enforces per-player interval and cap; paid base game (cost per farm account); Steam's own spend requirement for Market access [F: about $5, unverified detail]; weekly rotation; recipes consume supply; kill switch | Farms can still run multiple accounts; no server means no detection. Keepsakes are low-value collectibles, so the incentive is limited by design (hypothesis). |
| Duping | No custom grant path; no bridge; items exist only in Steam; recipes validated by Steam | Depends on Steam being correct. |
| Client tampering | The client only calls `TriggerItemDrop`; it cannot name items. Local gear is untradable. | A cheater can inflate local stats, but this affects only themselves. |
| Bug in source (the TF2 crate lesson [F]) | Kill switch: set `tradable` and `marketable` false for affected definitions and call `FlushAssetAppearanceCache` [F]; ship odds as data; test in a private app first | Needs owner-held Steamworks access to act quickly. |
| Overloading Valve | One drop call per interval; no polling; inventory read on launch and after a drop | Real rate limits [U]. |
| Reputation | Public odds and caps on the store page [F: Deskrawl discloses odds] | n/a |

## 8.4 How Option B and Option C differ
| Area | A (default) | B: server-authoritative | C: no Market in v1 |
|---|---|---|---|
| Tradable items | Fixed Keepsakes | Fixed definitions minted from our database; gear affixes re-attached from our DB (cleared on trade [F]) | None; data model has stable ids |
| Random-affix trading | No | Yes, via bridge | No |
| Grants | Steam playtime drops | `AddItem` from our server (publisher key) | n/a |
| Server | None | Required: auth via Steam tickets, database, loot rolls, logs, admin | None |
| Loot rolls | Local | Server for tradable gear (local for the rest) | Local |
| Offline gains | Local | Must be computed server-side for tradable gear | Local |
| Risk | Low to medium | High: duping, desync, outages, lost loot (TBH [F]) | Lowest |
| Effort (estimate [F: Nova]) | About 1 week beyond base game | 3 to 6 weeks plus ops | None |
| Cost | $0 to build; Steam Direct $100 at publishing, needs owner approval [F] | Hosting is a recurring cost, needs owner approval | Same as A |
| UI changes | Keepsake shelf, Market link | Adds a "Trade Ship" screen, gear listing flow, server status banner | Shelf hidden; "coming later" absent |
| Design impact | Gear stays personal; drives chase via crafting | Gear becomes a commodity; economy tuning becomes full-time | Cleaner, but less differentiating from TBH and Deskrawl |
Switching A to C is trivial (hide the shelf). A to B is a re-architecture of item identity and a migration, so design items with stable ids from day one (`item.uid`, `def.id`). [D]

## 8.5 No paid random boxes [D]
No keys, no crates, no sold Keepsakes, no purchasable drops. Real money touches the game only in the base price, optional cosmetic DLC with fixed contents, and Steam Market purchases between players. This keeps us away from the loot-box dispute [F: NY AG suit against Valve, Feb 2026, status unverified].

## 8.6 Fees as reported
Steam transaction fee 5% (minimum $0.01) plus a game-specific fee set by the publisher, reported at 10%, combined 15% widely quoted. [F: Steam Support FAQ snippet; developer earnings per sale unverified; our share is [U].] We make no revenue forecast from Market fees. Market payouts are Steam Wallet credit only. [F]

## 8.7 What the player sees
- On the Hearth shelf: Keepsakes with a rarity border and a count; a "View in Steam Inventory" button that opens the Steam Community inventory page; a gentle line: "Keepsakes can be traded on the Steam Community Market if your Steam account is eligible".
- A "Next Keepsake in 37 min" line (reads Steam playtime estimate; if unknown, shows "about 1 per hour"). When a drop arrives: a small toast "A Keepsake arrived!" with the item and rarity.
- No prices inside the game. The game never handles money and never lists items. [D]
- Text explaining odds and the daily cap (so players don't feel scammed).

---

# 9. UI/UX

## 9.1 Screen list
1. Strip HUD (always visible).
2. Panel: Hearth (home: summary, shelf), Inventory, Skills, Passives (Constellation), Map, Crafting (Orla), Quests and Achievements, Collection (Keepsakes), Settings.
3. Offline summary card; Boss intro card; Legendary toast.
4. Onboarding overlay (first run only).
5. Tray menu: Show/Hide, Quiet 1 h, Open Panel, Pause, Quit.

## 9.2 Strip HUD wireframe (640 x 96 logical)
```
+----------------------------------------------------------------------------+
|[=]  Z2-14 ███████░░░ 62%           (·_·)>  *   o o o                 Lv 23|
|                                    Wick+Gel  pack                    +loot|
|  ~~ parallax hills (scrolling) ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ |
|  HP ████████░░   XP ███░░░░░░░░                     [Nova 12s] [!] x6 new|
+----------------------------------------------------------------------------+
 [=] handle (click opens panel)   [!] items awaiting review count
```
- Top line: stage and progress (zone-stage, percent to clear), level on the right. All text under 10 px is avoided: minimum 10 px.
- Bottom line: HP and XP slim bars, the ultimate cooldown, a review badge.
- Everything but Wick, the handle and toasts is click-through. Opacity of HUD bars is adjustable (default 80%). A "Minimal" skin shows only Wick and one thin bar.

## 9.3 Expanded panel wireframes (960 x 600)
Inventory:
```
+--------------------------------------------------------------------------------+
| Hearth | INVENTORY | Skills | Passives | Map | Craft | Quests | Collection | ⚙ |
+--------------------------------------------------------------------------------+
| EQUIPPED               | STASH (84/100)                | COMPARE                 |
|        [Head]          | [o][o][◇][o][⬡][o][o][◇][o][o]| Ember Lantern  ◇ Rare   |
| [Wpn] [Chest] [Off]    | [o][◇][o][o][o][★][o][o][o][o]| ilvl 31  +Enhance 3     |
|  [Rg] [Boots] [Rg]     | [o][o][o][⬡][o][o][o][◇][o][o]| +412 ATK                |
|        [Amu]           | ...                           | +18% Damage   (T3)      |
| Power Score 18,420     | Filter: [Rarity ≥ Rare ▾]     | +4.2% Crit chance       |
|                        | [Auto-equip upgrades: off]    | +9% Find                |
|                        |                               | Power Score: ▲ +12%     |
|                        |                               | [Equip] [Salvage] [★]   |
+--------------------------------------------------------------------------------+
```
Skills:
```
+--------------------------------------------------------------------------------+
| SKILLS  Class: Lampwright                                  Points: 3 Wisps: 4,210
| Active slots                                  Skill pool
| [1] Flare    r3  rule: Always      [↑][↓]     Flare       r3 [Upgrade 640w]
| [2] Dash     r2  rule: 3+ enemies  [↑][↓]     Wick Dash   r2
| [3] Cinder   r1  rule: Elite/Boss  [↑][↓]     ...
| [4] (empty)                                   Mods at r3: (A) Burn longer (B) Wider
| [U] Lamp Nova r1 rule: Auto/Manual                                            |
| Aggression: (•) Cautious ( ) Steady ( ) Bold                                   |
+--------------------------------------------------------------------------------+
```
Map:
```
+--------------------------------------------------------------------------------+
| MAP: Mossbottle Marsh                   Zone 2 of 10          [Farm here: 2-14]|
| Stage: 1 2 3 4 5 6 7 8 9 [10:Warden] 11 12 13 14 15 16 17 18 19 [20:Boss]      |
|        ● ● ● ● ● ● ● ● ● ●           ● ● ● ○ ○ ○ ○ ○ ○ ○        ◌               |
| Win chance at stage 15: ● green (88%)         Next boss: Queen Gloop  (red 41%)|
| [Push stage]  [Auto-push at 80%: on]     [Zones: 1 ✔ 2 ► 3 🔒 ... ]            |
+--------------------------------------------------------------------------------+
```
Settings:
```
+--------------------------------------------------------------------------------+
| SETTINGS  General | Strip | Performance | Sound | Accessibility | Steam          |
| Strip mode: (•) Docked  ( ) Floating  ( ) Tray only                             |
| Monitor: [Display 2 ▾]   Edge: Bottom   Anchor: [Left|Centre|Right]  X: [  0 ]  |
| Width [====|====] 640   Height [==|======] 96    Opacity [========|] 80%        |
| Click-through: (•) On (except Wick/handle)   Always on top: [x]                |
| Hide when fullscreen app runs: [x]   Pause processes: [Edit list]               |
| FPS cap: ( )15 (•)30 ( )60   Eco preset [ ]   Battery saver: [x]                |
| Notifications: Toasts [x] Windows notifications [ ] Quiet hours [22:00-07:00]   |
| Master 25%   SFX [====|=====]   Music (off)   Colour-blind palette: [Default ▾] |
+--------------------------------------------------------------------------------+
```

## 9.4 First 10 minutes: onboarding script [D]
| Minute | What happens | Teaching goal |
|---|---|---|
| 0:00 | Launch: a soft dusk fade-in. The strip appears at the bottom; Wick walks in; Gel bounces out of his bag. Caption: "Hi. It gets dark here. Let's keep it bright." | Characters, tone |
| 0:15 | The strip is click-through: a bubble says "Click me, I'm solid." Click Wick: heart. "Everything else lets your clicks through." | Click-through explained |
| 0:30 | First pack of 2 Gloomlings. Wick hits; XP appears. | Auto-combat |
| 1:00 | First item drops and arcs. Gel catches it. A toast: "Rare! Look closely?" (guaranteed Fine for the first drop, Rare for the second) | Loot |
| 1:30 | Panel opens by force once (a one-time arrow to the handle). Orla shows how to equip; compare arrow. | Equip |
| 2:30 | Level up (guaranteed by the newcomer bonus). One passive point; open the Constellation and pick a node; class choice at level 3 is delayed to 5 min. | Passives |
| 4:00 | Class pick (Lampwright, Hush Archer, Gel Tamer), 5-second preview of each skill in the strip. | Build identity |
| 5:00 | First elite: a bigger glow, drop of 2 items, a Glow. Orla explains Salvage and Kindle in 2 lines. | Crafting |
| 7:00 | Stage 5 of Hearthside Verge; the map opens once and shows the win-chance traffic light (no staged faint). | Map |
| 9:00 | "Strip settings" offer: size, opacity, hotkey, hide on fullscreen. Default Yes to hide-on-fullscreen. | Respect |
| 10:00 | Tray hint: "Close the panel; I'll keep working. Quit from the tray." Optional: "Open Steam inventory to see Keepsakes" explanation appears once only when the first Keepsake arrives (in about 1 hour, not onboarding). | Set-and-forget |
Onboarding is skippable at any time; all hints are re-readable in a Help tab. [D]

## 9.5 Juice and feedback [D]
- Squash and stretch on every hit (hero, enemies, loot), with a 3-frame anticipation on skills.
- Hit-stop: 40 ms on boss hits only; no screen shake beyond 2 px at default.
- Loot arcs with a rarity ring pulse; Legendary leaves a vertical light beam on the strip for 2 seconds.
- Level-up: a ring of light from Wick; Gel does a flip.
- Numbers: damage numbers off by default (strip is tiny); aggregated "per-second" mini-readout optional.
- Crafting success: Orla's wings flutter, a tiny chime, the item "settles" with a bounce.
- Idle flavour: the lantern flame responds to the strip's recent damage (bigger flame after kills).

## 9.6 Sound moments [D]
Kill (soft tick, pitched by combo), loot pickup (pentatonic blip; pitch rises with rarity), Rare ring (two-note), Epic (three-note shimmer), Legendary (low bell plus chord, 1 s, quiet), level up (arpeggio), boss telegraph (low pulse), faint (soft descending), craft (wooden click), Keepsake (bell chime), UI (clicks). No sound plays when the strip is not visible. All stems under -12 dB peak by default.

---

# 10. Art and audio direction (all producible by code)

## 10.1 Palette [D]
| Role | Hex |
|---|---|
| Night (bg dark) | `#14111F` |
| Dusk (panels) | `#2A2240` |
| Plum (mid) | `#4B3A6B` |
| Lantern amber (accent, UI highlights) | `#FFB547` |
| Ember | `#FF7A45` |
| Moss | `#7FD6A0` |
| Frost | `#8EC9FF` |
| Venom | `#B38CFF` |
| Spark | `#FFE76B` |
| Bone (text) | `#F2E9DA` |
| Danger | `#E5586B` |
Rarity colours in 6.2. Three alternative colour-blind palettes shift hue pairs (green/red, blue/purple).

## 10.2 Character construction (procedural) [D]
- Wick: 2D, drawn by `_draw()`/`Polygon2D` with a 2 px dark outline; parts: head circle, hair-accent polygon, eyes (two ellipses plus highlight dot, blink every 3 to 6 s), body rounded rectangle, arms/legs as thick lines with round caps, lantern-staff, scarf as a 6-point verlet rope. Eight expressions by morphing eye and mouth parameters (happy, focus, surprise, sleepy, sparkle, sad, smug, hurt).
- Squash and stretch: apply `scale = (1 + s, 1 - s)` anchored at the feet with area preserved; walk cycle `bob = sin(t * 2π * 2)`, leaning with velocity.
- Gear visibility: head, chest and offhand variants are palette and shape swaps (hat shapes: cap, hood, helmet; capes; shoulder pads). The 120 base types map to about 18 visual shapes by slot and band. [D]
- Gel: a circle rendered as a polygon with 24 spring-driven vertices; wobbles on movement; face with two dots and a mouth arc; hat slot. Cheap, charming, and reusable for the Jellyfolk.
- Pixel vs vector decision: **smooth vector with chunky shapes**, no pixel art, because shape-based motion looks better with squash and scale, and pixels need nearest-neighbour care across DPI. [D]

## 10.3 Enemy design language [D]
Shape grammar: a base silhouette (blob, tall body, wide body, tiny swarm) plus modules (eyes, horns/antlers, shells, bells, gears, candle flames) coloured from the zone palette. Rule: silhouette reads at 24 px; every enemy type has one unique silhouette feature; elites add a glow outline; bosses are 3 to 4x larger with a face. Telegraphs are rings, not text.

## 10.4 Tile and zone look [D]
Three parallax layers (far shapes, mid silhouettes, near ground) scrolled with cheap offsets; each zone has a palette shift, 6 prop shapes (trees, lamps, rocks), a weather effect (fireflies, snow, steam) limited to 20 particles on strip and 100 in the panel. Lamp posts mark stage progress. Rarity frames are shape plus colour (see 6.2).

## 10.5 UI style [D]
Soft rounded panels (corner radius 8), dusk colours with lantern-amber accents, bold shapes, a single typeface (Godot default is fine for dev; final choice a free SIL OFL font, e.g., Nunito, for rounded friendliness [D: license must be checked at the time]). Tooltips are compact. Icons for items are composed procedurally: a base shape per slot plus a coloured gem and a rarity frame; Keepsake icons rendered from code to 256 x 256 PNG for Steam.

## 10.6 Particle effects [D]
Short 0.2 to 0.6 s bursts: sparks on hit (6 to 10 particles), loot sparkles, level-up ring, healing motes. Hard cap 60 particles on strip at once; none in Eco preset.

## 10.7 Procedural audio plan [D]
- Engine: `AudioStreamGenerator` with small synths (sine, triangle, square, noise) and an ADSR envelope per voice; sounds are pre-rendered at startup to cached `AudioStreamWAV` to save CPU. Alternatively CC0 packs where code cannot match; no paid assets.
- Music: opt-in generative loop per zone: 3 voices (pad, pluck, soft bass), D mixolydian or A minor pentatonic, 60 to 80 BPM, 8-bar phrases from a seeded generator, reverb via `AudioEffectReverb`. Silent when the strip is hidden.
- Ambient: low-pass noise "wind" 5% volume option.

## 10.8 Placeholder vs final
| Element | Placeholder (first playable) | Final (v1) |
|---|---|---|
| Wick | A coloured capsule with a lantern dot and squash | Full construction above, 8 expressions, scarf |
| Gel | Circle with wobble | Spring polygon, face, hats |
| Enemies | 3 colour blobs | 60 grammar-built variants and 20 bosses |
| Item icons | Rarity-coloured shapes | Procedural composed icons |
| UI | Godot default theme in palette colours | Custom theme, rounded panels |
| Audio | 8 beeps | Full SFX set, optional music |
| Steam art | n/a | Capsule art rendered from the engine; a human should hand-polish (see risk) |

---

# 11. Pricing and Steam page plan

## 11.1 Price recommendation: **$7.99 USD (assumption [D])**
Reasoning, with sources:
- Idle and companion titles mostly sit at $0 to $7. [F] Rusty's was $6.99, Tiny Pasture $5.99, Desktop Defender $4.99, Deskrawl about $4.89 at 30% off (which suggests about $6.99 list; not confirmed). [F]
- The Steam Page Analyzer note says the $10 to $14.99 band had the best share reaching 1,000 reviews (16.1% vs 2.5% under $5), small sample. [F, weak]
- A paid price raises the cost of bot farming and matches Option A's anti-farming rationale. [F: deep dive]
- $7.99 is slightly above peers to signal loot depth, below $10 to avoid scaring an impulse-buy audience. Alternative: $5.99 (peer pricing, higher volume), or free-to-play (TBH route; invites farming and wants a server, not recommended).
- This is a hypothesis to be revisited after demo feedback. No revenue forecast is given. The owner decides price.

## 11.2 Tags [D]
Idler / Incremental ("Clicker" was renamed "Incremental" [F]), Desktop Companion [F: official tag], Action RPG, Loot, Cute, Anime, Fantasy, Singleplayer, Casual, Relaxing, Indie, Atmospheric.

## 11.3 Store copy draft (short description) [D]
"A tiny lamplighter and a slime friend patrol a thin strip above your taskbar. They fight, loot and level while you work. Real ARPG loot with random affixes, sets and a skill tree; almost no CPU; click-through by default; hides when you play something fullscreen. Free timed collectibles (Keepsakes) can be traded on the Steam Community Market. No loot boxes."
Long description sections: Features, "What it will not do" (never steals focus, no loot boxes, no pay-to-win), Odds table (Keepsake odds shown), Performance promises (only once measured), and an FAQ.
- AI disclosure: all art and sound are code-generated, text is written by humans or tool-assisted; check the Valve disclosure form for any pre-generated text produced with AI before release. [F: January 2026 rewrite targets player-facing AI-generated content; tools exempt]

## 11.4 Capsule and trailer ideas [D]
- Capsule: Wick and Gel on a lit road under a purple dusk, lantern glow, "A tiny hero on your taskbar" tagline; rendered from the engine (screenshot with composite), hand-polished by a human; flagged as an art-risk.
- Trailer (45 to 60 s): a real desktop (a spreadsheet, a browser), the strip walking along the bottom, a Legendary beam, a boss; end card with the Steam Market line ("trade Keepsakes"). Show CPU meter at the end only if measured and true.
- GIFs: 3 looping strip GIFs (walk, loot beam, boss).

## 11.5 Demo and Next Fest plan [D / U]
- Demo "Gloamway: Prologue": zones 1 and 2, levels up to 12, all three classes' first skills, no Keepsake drops, saves carry over to the full game. [D]
- Next Fest: apply with the demo; dates and rules are not in our notes, so the owner must check the Steamworks calendar. The notes say idle demos at Next Fest are crowded (almost 500 demos in June 2026) and PC Gamer players keep few as desktop companions [F]; so the demo must make its first 3 minutes clean and light.
- Playtest: a small closed playtest for balance and multi-monitor.

## 11.6 Wishlist and community plan [D]
- Steam page live at least several weeks before launch (owner decides the timing; no figures assumed).
- Dev-log posts, a Discord or Steam community hub, short-form clips of strip moments, a "Desktop Setups" screenshot call.
- Honest messaging on trading: explain Keepsakes before launch to avoid TBH-style confusion.
- All publishing steps need the owner: Steamworks partner account, Steam Direct $100 [F], store page, any hosting. No agent publishes or spends.

---

# 12. Risks, open questions, owner decisions

## 12.1 Risk register
| Risk | Level | Mitigation |
|---|---|---|
| Crowded niche (1,566 Idler releases in 2026 [F]) | High | Charm, performance reputation, strong demo, differentiated theme |
| Code-drawn art under-delivers on charm and capsule | High | Invest early in Wick and Gel prototypes and a charm test with 5 outside players; budget a human art pass for the capsule only |
| Godot transparent-window quirks (polygon bugs, focus, fullscreen flip) [F] | High | Day-one spike; Interact-mode fallback; keep window smaller than the monitor |
| Fullscreen-app detection [U] | Medium | Spike; manual fallbacks |
| Multi-monitor and DPI | Medium | Owner or tester checklist (2 monitors; 100/150/200% scale; hot-plug) |
| Balance (all numbers are [H]) | High | Write a headless balance simulator; tune with data; playtest |
| Market economy (Keepsake values too low or inflated) | Medium | Weekly rotation, recipes, kill switch; no revenue forecast |
| Steamworks specifics unknown ([U]: field semantics, Market enablement, recipes with choice, rotation) | High | Read Steamworks docs on the owner's account; test with a private app |
| Bots and farms | Medium | See 8.3; paid base game |
| Legal/regional (loot-box rules, tax, Market availability) | Medium | No paid random boxes; ask the owner about geo-limiting and legal advice (outside our competence) [F] |
| Scope (95 sprites, 60 enemies, 40 uniques, 21 skills, tree of 90 nodes) | High | Cut list below |
| Name clash or trademark on "Gloamway" | Medium | Check before the store page [U] |
| Steam overlay and transparency | Low-Medium | Overlay is optional [F] |

## 12.2 Build effort table (Sage's estimates, hypotheses; Sage's blind spot is polish)
| System | Size | Cut-down version |
|---|---|---|
| Window stack (strip, passthrough, tray, hide-on-fullscreen) | M, risky | Ship docked only, tray toggle only |
| Combat sim + auto-skills | M | 12 skills not 21; two classes |
| Loot, affixes, filter, crafting | M | Drop Transmute and Echo; 20 uniques |
| Procedural art (Wick, Gel, 60 enemies, 10 bosses) | L | 6 enemy bases re-tinted; 5 bosses with palette swaps for the rest |
| Passive tree (90 nodes) | S to M | 45 nodes |
| 10 zones and content | M | 6 zones for v1.0, 10 by 1.1 |
| Keepsakes and Steam layer | S to M | 12 definitions; one rotation |
| UI (panel screens) | M | Merge Craft into Inventory |
| Audio | S | SFX only |
| Steam page and trailer | M | n/a |

## 12.3 Scope cut list (in order of first cut)
1. Seasonal festivals and Moth Night.
2. Fourth class and Glimmer Rifts.
3. Zones 7 to 10 (ship 6 zones plus Dusk Tier I).
4. Rotated enemy art and the second palette pass.
5. Music.
6. Rotating weekly Keepsake pool (use a fixed pool).

## 12.4 Open design questions (for playtest or data)
1. Is "no mana, cooldown-only" enough depth, or does the player feel the build is decided too passively?
2. Is a 20 kills/min cadence satisfying at 96 px height, or does Wick feel too busy?
3. Does the Legendary rate (one per 2.8 h) feel right? Too many cheapens, too few frustrates.
4. Are cosmetic-only Keepsakes valuable enough that anyone cares to trade? If not, A+ (tradable fixed uniques) would be the lever, at the cost of pay-for-power concerns.
5. Resting efficiency 0.60 versus Awake 1.00: does it nudge the player to keep the strip open, or feel punishing?
6. Does the Dusk Tier multiplier (x1.8 per tier) keep the endgame meaningful for 100+ hours?
7. How does `drop_window`/`drop_max_per_window` actually behave? Does a cap of 6 per day work? [U]
8. Is a human-polished capsule needed to compete?

## 12.5 What the owner must decide
1. **Market scope (request A8):** A (recommended), B, or C. A+ (tradable fixed uniques) is a sub-decision; default off.
2. **Theme and title:** confirm Gloamway (lamplighters at dusk) versus Slime Kingdom; confirm the name after a clash check.
3. **Price model:** $7.99 paid (recommended), $5.99, or free.
4. **Spend and identity:** Steamworks partner account, Steam Direct $100, tax and legal identity, any hosting for B. Agents cannot spend or publish.
5. **Risk appetite on Keepsake odds:** the 90 / 9.5 / 0.5 odds and the cap of 6 drops per day.
6. **Whether to ask Valve** about Market enablement before building the Steam layer. [F: unverified process]
7. **Testing:** who provides multi-monitor and varied Windows machines.
8. **Art pass:** whether a human may polish the capsule and trailer.

## 12.6 Multi-monitor and window test checklist (for owner or testers)
- Dock to monitor 1 and 2, swap primary, hot-unplug the strip's monitor, hot-plug it back.
- Mixed DPI (100% and 150%); taskbar auto-hide on and off.
- Fullscreen game on monitor 1 while the strip lives on monitor 2 (should the strip hide? default: hide only if the fullscreen app is on the same monitor [D]).
- Alt-tab, Win+D, lock/unlock, sleep/wake; confirm the strip never loses always-on-top and the passthrough polygon never hides Wick.
- Steam overlay on and off.

## 12.7 Sourced fact versus design choice: summary
- Sourced (from our notes, snippet-level): Godot window capabilities and pitfalls; Steam Inventory itemdefs, playtime generators, recipes, dynamic properties cleared on trade; fee levels 5% plus about 10%; the TBH and Deskrawl facts; price points of peers; official Desktop Companion tag; Steam Direct $100.
- Design choices: everything else, including all balance numbers, odds, the theme, characters, zones and the $7.99 price.
- Not available and not invented: sales or revenue forecasts, wishlist targets, Market payout per sale, CPU figures of competitors.
