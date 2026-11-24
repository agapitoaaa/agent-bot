# G1 Slime Strip: deep dive with Steam Market trading (research brief)

Author: Nova (researcher). Date: 2026-11-24. Requested by owner via approval A7 ("Give more context on Slime Strip. We want Steam Market trading.").
Evidence level: WebSearch result summaries only. I have no page-fetch tool, so NOTHING below is "opened-page level". Items marked [official snippet] are Valve/Steamworks pages whose text appeared in search summaries; [secondary] are news, guides, forums; [assumption] is my inference. Prior game-track notes are in `/home/user/agent-bot/ideas/backlog.md` (Game track section).

The owner wants Steam Market trading. This brief does not argue against it. It says how it works, what it needs, and what it costs.

---

## 1. Slime Strip in more detail

### Player fantasy
You are the keeper of a small slime hero that fights for you along a thin strip above your taskbar while you do other things. You glance down, see a rare drop, equip it, and the number goes up. With market trading the fantasy extends to "my slime's loot is worth something to someone".

### Core loop [assumption: design proposal, not sourced]
- **One minute:** the slime auto-walks and fights; enemies die; loot pops; a toast shows rarity. Optional click to grab loot or trigger one active skill.
- **One hour:** fill a few equipment slots, swap an item with better affixes, push to the next zone, craft or salvage junk into upgrade material. One tradable drop arrives on a timer (see section 2).
- **One week:** a weekly rotating "featured drop pool" (Deskrawl does a Monday rotation, see below), boss gates, build experiments (affix sets), and a trade/sell decision on surplus items. Prestige is optional: I recommend NO prestige in v1 because Desktop Defender reviews cite bugs in rebirth/prestige systems [secondary, VaporLens summary via backlog]; use zone depth and a mastery track instead.

### Systems
- **Combat on the strip:** auto-battle, one lane, 3 enemy archetypes for the first playable (melee, ranged, tank), a boss every N zones. Slime reacts with squash and stretch.
- **Loot and affixes:** 4 to 5 rarities; items have a base type plus 1 to 4 random affixes (flat and percent stats). Affix pools are data files, so agents can generate and balance-test them.
- **Equipment:** 6 slots (weapon, hat, body, trinket x2, "core"). Salvage and reroll as sinks.
- **Offline progress:** compute on launch from elapsed time with a cap (suggest 8 to 12 hours) and a simple expected-value model. A local-only model is easy; if tradable items exist, offline gains must NOT mint tradable items (see section 3).
- **Prestige:** none in v1 (see above).

### Desktop-companion window behaviour
Facts from the backlog notes [secondary, forum and repo evidence, unverified by us]: Godot 4.2+ supports transparent, borderless, always-on-top windows and `mouse_passthrough_polygon`. Known pitfalls: polygon made a sprite disappear in 4.6.1; window can drop behind others after a click; full-monitor-size transparent windows can flip to exclusive fullscreen (keep slightly smaller); Wayland drag problems. Unity alternative: UniWindowController (transparent, topmost, click-through). Valve's May 2026 tag overhaul made "Desktop Companion" an official tag (games that use only part of the screen).

Design intent [assumption]:
- Strip docks above the taskbar, resizable height, true transparency, click-through everywhere except the slime, loot toasts and a handle. Hotkey to toggle.
- **Hidden or fullscreen app running:** sleep. Godot offers `low_processor_usage_mode`, FPS cap and pausing the scene tree; one forum report claims about 1% CPU when unfocused with a 1 FPS cap and paused tree [secondary]. Detecting a fullscreen foreground app on Windows would need a native call (e.g. `SHQueryUserNotificationState`) through a GDExtension; I found no Godot example, so this is **unverified and a first-playable spike**. While asleep, simulate with the offline model rather than render.
- **Multi-monitor:** let the player pick the monitor and edge; one reviewer complaint on Tiny Pasture was second-monitor instability [secondary], so test a 2-monitor setup early. We cannot test real multi-monitor hardware in our sandbox [assumption]; this needs owner or tester machines.
- **Steam overlay vs transparent window:** unverified for Godot/Unity (one Construct post says it failed for a WebView2 case). Overlay is optional for us; note that Steam Inventory and Market do not need the overlay.

### Art and audio
Code-drawn: slime as a procedural blob (shader or `_draw()` with squash and stretch, metaball merge), enemies as generated geometric sprites, item icons composed from shapes and a rarity palette. Audio: synthesized blips and a few loops generated in code (no external assets). This sidesteps Valve's AI-disclosure form (Jan 2026 rewrite targets player-facing AI-generated content, tools exempt [secondary]). Honest risk: code-drawn art may under-deliver on charm and on Steam capsule art; market items also need icon images uploaded for item definitions (see section 2), which we can render from code.

### First playable (a few days) vs Steam-ready
| | First playable | Steam-ready |
|---|---|---|
| Window | transparent strip, click-through, always-on-top, sleep when hidden | multi-monitor selection, fullscreen-app detection, DPI handling, settings, tested on varied machines |
| Gameplay | 3 enemies, 4 rarities, random affixes, equip popup, offline calc, local save | 8 to 10 zones, bosses, crafting/salvage sinks, mastery track, balance pass over weeks of simulated play |
| Economy | local-only fake "tradable" flag and a mock market screen to test sinks and sources | real Steam Inventory item definitions, store page, market testing (needs Steamworks account, owner sign-off) |
| Platform | none | GodotSteam (GDExtension for 4.4+, version naming inconsistent), achievements, cloud saves, Steam Direct, store page, trailer |

### Differentiation (facts from backlog notes plus new search)
- **Task Bar Hero (TBH):** free, huge peak (about 526k concurrent mid-June 2026) but Mixed reviews: outages, lost loot, cheater crackdown, market strain. Reports describe a "Trade Ship" that moves items between the in-game inventory and the Steam inventory, and a "Cube" tool that strips decorations/engravings/inscriptions before listing [secondary guides]. So TBH keeps rich items in its own backend and bridges to Steam. 
- **Deskrawl:** Idle ARPG, Sep 2026, Very Positive, 43k+ concurrent in Oct. Its store page (search summary of the store page, [secondary but first-party text]) says the player receives one tradable "mob" Steam item every 60 minutes, rarity 95% common / 4.99% rare / 0.01% mythical, a weekly Monday rotation of 12 common, 6 rare, 3 mythical active drops, all mobs active at launch to seed the market. That is fixed definitions via timed drops, which is exactly Option A below. Reviews complained the strip is too large, blocks the taskbar, can't be resized or made transparent (VaporLens demo summary).
- **Desktop Defender:** auto-battler, $4.99, Very Positive; complaints about bugs in rebirth/prestige and shallow repetition.
- **Rusty's Retirement:** cozy, no loot economy, about 200k sales; shows the audience pays for charm, not trading.
- **Slime Strip angle:** deep loot (random affixes, equipment) like an ARPG, a genuinely small and transparent strip, near-zero CPU when idle, and a market lane that is deliberately bounded so it cannot be botted into the ground the way TBH was.

---

## 2. Steam Market trading: how it works for a developer

### Core building blocks (official snippets unless stated)
- **Steam Inventory Service** is free and can be used server-less or with a trusted server that knows game state [official snippet, Steamworks inventory docs]. It integrates with Community Market, Trading, Storefront and Workshop.
- **Item definitions (itemdefs):** a JSON schema (uploaded in Steamworks or via the `IGameInventory` Web API) with item types including `item`, `bundle`, `generator`, `playtimegenerator`, `tag_generator`. Each item def has `tradable` and `marketable` booleans. After changing those flags the developer should call `FlushAssetAppearanceCache` [official snippet].
- **Crafting/exchange:** `ExchangeItems` recipes; a crafted item inherits the latest trade restriction of any ingredient [official snippet].
- **How items are granted:**
  1. **Playtime drops (no server):** a `playtimegenerator` item def with `drop_interval` (minutes of playtime), `drop_limit`/`use_drop_limit` (per-user cap), `drop_window` and `drop_max_per_window` (cooldown/rate). The client calls `ISteamInventory::TriggerItemDrop`, but Steam servers track playtime and frequency per player [official snippet]. Valve's stance: the client can't be trusted and keys in a client can be extracted, so the client cannot ask for specific items; it can only trigger configured drops [official snippet].
  2. **Promo items:** `AddPromoItem` exists. The Web API version must be called from a secure server [official snippet]. Client grant functions are described as prototyping-only, can be disabled in Steamworks, and "hacked clients could grant arbitrary items" [Facepunch wiki, secondary]. I could not verify exact client-side promo rules.
  3. **Server-side `AddItem`** via `partner.steam-api.com/IInventoryService/AddItem/v1/` with a **publisher Web API key** (Economy permission) from a secure server. It fails for free-license owners who haven't played in the last 30 days [official snippet].
  4. **Exchange recipes** (client can call exchange; Steam checks the recipe) and `ConsumeItem` (client or server).
- **Dynamic item properties** [official snippet]: arbitrary string/int/bool/float properties on an item instance, readable on the client via `GetResultItemProperty(..., "dynamic_props")`. They can be written from the client (`StartUpdateProperties`, `SetProperty`, `RemoveProperty`, `SubmitUpdateProperties`, rate-limited per user, for properties you whitelist) or from a secure server via `IInventoryService/ModifyItems` with the publisher key. **Critical constraints from the same docs: dynamic properties are CLEARED when an item is traded, and are not currently visible when inspecting an item in the Steam inventory or on the Market.** This is the key technical constraint for random affixes (see below).
- **Item stores / purchases:** an item store exists (visible only to partner members by default). Not needed for drops-only trading.

### What this means for random affixes (the key constraint)
- A Steam item instance is an instance of a fixed **item definition**. Its identity on the Market is by definition (name/appearance), so Market listings group identical items. Random per-item stats must be stored as dynamic properties, but those are wiped on trade and not shown on the Market [official snippet]. So **per-item random affixes that survive a Market sale are not supported** by Steam Inventory as documented. [Inference: this is why TBH uses a separate in-game inventory and a bridge, and strips "decorations, engravings, inscriptions" before listing.]
- Workable patterns:
  - **Tradable = fixed definitions.** Affix-less "collectible" items (e.g. a "Forest Ember Slime Core") that are tradable and marketable; the rich, random-affix gear lives in our own save and is NOT tradable. Or tradable items are crates/keys/materials that convert into untradable gear in-game.
  - **Many definitions as affix baking.** Pre-define N item defs where the affix set is part of the definition (e.g. 200 named uniques). Random drop picks one of the defined items. This gives variety with trade identity, but definitions are finite and each needs a name, icon and description. Dynamic filters introduced in the May 2026 Market beta are built from existing item data [secondary], which may help browsing; unverified for our case.
  - **Bridge (TBH model):** own backend holds authoritative rich items; a "trade ship" mints a fixed-def Steam item from them and burns the in-game one, and the reverse. This needs a server and has all the duping and desync risk in section 3.

### Steam Community Market requirements and approval
- **Is it automatic?** I found NO documented approval process in search results. What I found: the item def's `marketable` flag controls Market eligibility [official snippet]; participation is up to the developer [Steam Support FAQ summary]; unreleased item stores are visible to partner members only [official snippet]. Whether Valve reviews or must enable something before items appear on the public Market is **unverified**. Assumption: it is largely self-serve via itemdefs, but Valve staff are reachable through the Steam Inventory discussions group in the Steamworks Developer group and the app's Steamworks contact. Needs confirmation by opening the Steamworks docs (owner's partner account).
- **Steam Economy page** states a game using its own asset back end needs a datacenter database plus the Steam Asset API Web APIs, with the Steam Inventory Service named as the available managed alternative [official snippet]. So for our purposes the Inventory Service is the path; running our own asset API is heavier and unnecessary.
- **Player-side requirements** [Steam Support FAQs, secondary snippets; details vary across sources]:
  - Account must not be limited: spent at least the equivalent of $5 USD on Steam (wallet funds, games or wallet codes count; gifts and retail keys do not). Our free-to-play or cheap game does not itself unlock this for a fresh player.
  - **Steam Guard Mobile Authenticator** for trading/market; a newly added device or newly enabled authenticator triggers holds (7-day device rule and up to 15 days reported in Steam Support snippets). Forum reports say items bought/acquired often carry a 7-day re-trade/re-market restriction. Treat exact day counts as **unverified and changeable**.
  - **Market hold:** items listed are held by Steam before becoming available on the Market (Steam Support).
  - **Wallet balance cap $2,000 and max single listing $1,800** (Steam Support FAQ snippet; Valve says it may change). Buyers/sellers in other currencies have equivalent limits.
  - Market sales pay out to Steam Wallet funds only; the player cannot cash out directly [secondary].

### Fees and what the developer earns
- Steam Support FAQ (snippet): **Steam Transaction Fee currently 5% with a $0.01 minimum**, plus a **game-specific fee, "determined and collected by the game publisher", currently set at 10%** in that FAQ; combined 15% is widely quoted for CS2 and Dota 2 [secondary]. Whether the developer can choose another percentage and how, I could not verify. Assume 5% + about 10% = 15% until confirmed.
- Developer earnings: the game fee portion of every Market sale. Example [illustrative arithmetic only, NOT a forecast]: a $1.00 sale to a buyer pays Steam about $0.05 and us about $0.10 if the 10% game fee applies; the seller nets the rest, in wallet credit. Valve takes its normal revenue share on item-store purchases (not relevant for drops-only). I did not find a statement of whether Valve's 30% revenue share applies to the game fee; treat our earnings as UNVERIFIED and likely modest.
- Valve's Market overhaul beta (May 12, 2026): more than 13,000 games have Steam Community items on the Market and more than 700 have in-game items; Inventory-based games get new item pages and dynamic filters without extra work [secondary: PC Gamer / GamesRadar / Neowin summaries].

### What needs NO server of ours vs what REQUIRES one
| Capability | Server we run? | Notes |
|---|---|---|
| Fixed tradable/marketable item defs granted by `playtimegenerator` + `TriggerItemDrop` | **No** | Steam enforces timing and drop caps. Cost: Steamworks account, itemdef art/text. Deskrawl's design looks like this. |
| Exchange recipes (e.g. 10 commons into 1 rare) | **No** | Client calls exchange; Steam validates recipe. Good sink. |
| Random affix drops that are tradable and keep their affixes | **Not possible as documented** | Dynamic props are cleared on trade. |
| Random affixes on untradable local gear | No | Pure local save; client trust issue only matters if gear is ever convertible to tradable value. |
| Specific item grants (boss kill gives item X, quantities, quest rewards) | **Yes** | `AddItem` / `AddPromoItem` with a publisher key must come from a secure server. |
| Dynamic properties set by our logic that clients can't forge | **Yes** | `ModifyItems` from a server. Client-writable properties are forgeable. |
| Anti-cheat (validate kills, offline gains, drop rates) | **Yes** | Needs an authoritative simulation or at least server-side plausibility checks. |
| A bridge between rich in-game items and Steam items | **Yes** | The TBH model. Highest risk. |

### Rough cost and effort [assumptions, not sourced]
- **No server (Option A):** effort about 3 to 6 days of agent work for itemdefs, drop config, GodotSteam integration, mock market UI; cost $0 to build, plus Steam Direct $100 at publishing. Ongoing: near zero.
- **Server-authoritative (Option B):** effort about 3 to 6 weeks (account/session auth via Steam tickets, a database, authoritative loot rolls, rate limiting, logs, admin tools, tests, monitoring), plus hosting cost. I will not invent a monthly figure: a small managed backend is plausibly low double digits of dollars per month at tiny scale, but hit-scale traffic (TBH reached 526k concurrent) would be a very different bill. **Hosting, domains, and anything recurring require owner sign-off; agents cannot spend money.**

---

## 3. Risks of a market-driven loot economy, and mitigations

### Evidence from Task Bar Hero and others
- **Bots and Market spam:** PC Gamer reported the second most-played Steam game was a "bot-filled marketplace that can get you banned"; Kotaku headline: bots selling in-game weapons for $1,000 or more (headline only; body not retrieved) [secondary].
- **Valve strain and rules:** GamesRadar headline: devs "apologize to Steam staff and all of our players" after the game drew 164,000 concurrent players "and starts breaking Valve's marketplace". Russian-language report: Valve told the studio it "did not properly adhere to server usage rules" with excessive requests, required item-system fixes, and asked the devs to tell players to remove listed items [secondary; page text not read]. A Swedish article argues the problem was how the game called the system, not general overload (minority view).
- **Developer response:** guides report market policy overhaul to reduce load, a pull-all-listings deadline before a June 1 patch, relaunch June 25 (v1.00.20), auction disabled for high-tier items over duplication exploits and fraudulent listings (July), permanent market restriction for players caught cheating twice, about 70 permanent market bans in launch week, and complaints of false positives and appeals [secondary guides; dates inconsistent].
- **Lost loot:** a Taiwanese outlet (4gamers) reports that on July 25 many players saw "server not responding" and, after relogging, gear/backpack/warehouse items were deleted because the server did not hold them; the studio said the items were not actually lost and data recovery followed; the developer name in the two articles conflicts (Tesseract vs Nugem) [secondary, unresolved]. Lesson [assumption]: a server-authoritative bridge with weak failure handling can wipe loot, and loot is the whole product.
- **TF2 2019 crate bug:** certain crates reliably dropped Unusual hats, flooding the Market; Valve paused crate opening, disabled Market access, marked items non-tradable, with a later fix allowing refunds; Unusual price fell from $17 to $35 to about $5 [secondary: PC Gamer / Game Developer]. Lesson: a source bug is an economy bug; build kill switches. Valve also hired an economist after inflation in TF2 (Gabe Newell remark) [secondary].
- **Dota 2 duplication exploit** reported as still used to dupe rare items (bo3.gg headline) [secondary].
- **Deskrawl's mitigations by design** (store page summary): one drop per 60 minutes, fixed odds, rotating weekly pool, a restock rule. It reads like supply control through time gating. Whether it avoided bot trouble: I found nothing either way.

### Risk list with mitigations
| Risk | Why | Mitigation |
|---|---|---|
| Bots and multi-account farming | Real money value attracts farms; free-to-play lowers cost | Playtime-based drops (Steam enforces per-player intervals); per-user `drop_limit`; price the game (not free) or require a base purchase so farm accounts cost money; rely on Steam's $5 spend rule for market access; server-side anomaly flags only if Option B |
| Duping / exploits | Any bridge or client-writable property | Prefer no bridge; no tradable items granted from client-trusted state; exchange recipes only; kill switch to flip `tradable`/`marketable` off |
| Cheating clients | Local game state is editable | Keep valuable output server-granted or Steam-timed; local power progression stays untradable |
| Inflation / oversupply | Unlimited sources, few sinks | Time-gated drops, weekly rotating pools, exchange recipes that consume items (sinks), per-user caps, scarce rare tiers; monitor listings and adjust definitions |
| Outages and lost loot | Backend failure (TBH) | Option A has no backend to fail (Steam holds inventory); for B use idempotent grants, journaling, and a recovery process |
| Steam load / policy | TBH broke Valve limits | Minimal API calls, batch dynamic property writes, respect rate limits, no polling |
| Gambling-like mechanics, loot boxes | New York AG sued Valve in Feb 2026 over CS2/Dota 2/TF2 loot boxes; Valve rejects the gambling claim and refuses to remove transferability; no US bills passed per one report [secondary, status unverified] | No paid random boxes, no keys. Only timed free drops; disclose odds on the store page (Deskrawl does); do not sell randomised items for real money. This keeps us far from the legal question. |
| Regional legal and tax | Cash-equivalent items; some countries restrict loot boxes or have tax duties | Only free timed drops; ask the owner whether to geo-limit; legal review is outside this team's competence. I found no authoritative country list for Market availability. Steam Support says Market covers taxes and a $2,000 wallet cap, not countries. |
| Account bans | Steam can limit accounts for abuse; developers can restrict player access to our market features (TBH did) | Document clear rules, appeals; do not ban based on guesses |
| Support burden | Real money plus "I lost my item" tickets | Few item types, Steam-held items, clear in-game status, a single support doc |
| Unknown: Valve's formal stance on idle games and the Market | I found no Valve policy change aimed at idle games or drops in 2026; only the TBH episode and the May 2026 Market beta | Contact Valve through Steamworks before launch; build the kill switch |

---

## 4. Scoping options for market trading

### Option A: tradable collectibles from fixed definitions, no server (recommended starting point)
- **What:** 12 to 24 tradable and marketable "core/relic" item definitions in 3 to 4 rarities; granted by a timed `playtimegenerator` (Deskrawl-style, for example one drop per N minutes of playtime); rotation weekly; exchange recipes combine duplicates into higher tiers. Rich random-affix gear is a local-only, untradable layer. Optional: a recipe where a tradable relic is consumed to unlock a cosmetic/gear boost in game (reads the Steam inventory; client-verifiable only by Steam's own state).
- **Effort:** S to M (about 1 week beyond the base game once the Steam account exists). **Cost to build/demo:** $0. **To release:** Steam Direct $100 (owner sign-off), nothing recurring.
- **Risk:** low to medium. Bots are only limited by Steam's drop timing and per-player caps; farms with many accounts could still exploit it. Market "value" may be tiny; the Market's economics are unproven for us. No random affix on traded items.
- **First playable:** mock the Steam layer: local `tradable` flags, a fake market screen, timed drops, recipes; verify sinks and sources by simulation. Real Steam testing requires the owner's partner account.
- **Release:** feasible as a v1.0 launch feature.

### Option B: server-authoritative loot with the bridge (TBH model)
- **What:** our backend owns random-affix items and quantities; a bridge mints and burns fixed-def Steam items; dynamic properties set server-side with `ModifyItems` (cleared on trade, so affixes must be re-attached from our database or baked into definitions).
- **Effort:** L (about 3 to 6 weeks plus ongoing ops, my estimate). **Cost:** hosting and monitoring, owner-approved only; unknown at hit scale.
- **Risk:** high: duping, desync, outages and lost loot (TBH), Valve rate-limit trouble (TBH), support burden, and attractiveness to botters. It is also the only option with true random-affix trading.
- **First playable:** a local fake server stub in the repo for design; no real hosting.
- **Release:** not before v1.x, and only after Option A has shown real market activity.

### Option C: no Market in v1; add later
- **What:** ship local-only loot; design the item data model so `tradable` can be added (stable ids, per-definition metadata).
- **Effort:** none extra. **Cost:** $0 beyond Direct. **Risk:** lowest operationally; weaker on the owner's wish and on differentiation versus TBH/Deskrawl; adding the Market later is possible but Steam item definitions for already-minted items are a migration job.
- **Release:** fastest.

### Effects on first playable and release
All options share the same first playable (strip window, combat, loot, equip, offline progress, save). Option A adds mock drops and recipes (+1 to 2 days). Option B adds a mock server and cannot be properly tested without hosting. **Building and demoing locally cost nothing. Steam Direct ($100 per app, recoupable at $1,000 revenue, per Steamworks fee page), any server hosting, any Steam publishing, and any store page need the owner's explicit sign-off. This team's agents cannot spend money.**

---

## 5. Owner decisions needed (max 4) and recommendation

1. **Market scope for v1:** A (fixed collectibles, no server), B (server bridge), or C (later)? 
2. **Price model:** free vs about $5 to $8 paid. A paid base raises the cost of bot farms and satisfies Steam's $5 spend rule for some players; free gets more installs but invites TBH-style farming. (Steam Page Analyzer's price notes are in the backlog and are only a small-sample heuristic.)
3. **Spend authorization:** approve Steam Direct $100 and a Steamworks partner account (and any hosting if B), and who holds the legal/tax identity needed for it (agents cannot). Also whether we should ask Valve about Market approval before building.
4. **Risk appetite:** is it acceptable that tradable value is low-power collectibles/relics and the random-affix gear stays untradable, with a kill switch and an explicit "no paid random boxes" rule?

**Recommendation (Nova, with my usual caution about hype):** Build G1 now with local loot, and give the owner the Market via **Option A** as the v1 target, designed so Option B can be added later if real market activity justifies it. Reasons: it honours "we want Steam Market trading" with the least operational risk; Deskrawl (Very Positive, 43k+ concurrent) appears to use essentially this pattern; Steam itself enforces timing and per-player caps without our server; and the one documented route to tradable random affixes (a bridge) is exactly where TBH's reported duping, outages and lost loot came from. Honest trade-offs: tradable items will be less "ARPG-deep" than owners may imagine (affixes don't survive trade), market income may be small, and I am a hype-prone researcher: TBH's peak is a bot-inflated outlier, and I have no data on how much a mid-size Market actually pays developers.

---

## What I could not verify
- Any page text was seen only through search summaries; I could not open partner.steamgames.com pages. Exact itemdef field names, limits, rate limits and per-user inventory caps (one 2019 forum answer says 1,000 items per game; unofficial) need checking in the Steamworks docs.
- Whether Valve approves or must enable Market listing for a new app's items, and any minimum conditions (min app age, review, partner standing).
- Whether the developer game fee (10%) can be set differently, and how fees split or get paid out; real developer earnings per sale.
- Exact trade-hold and Steam Guard day counts (sources conflict); Market country availability and legal status per region.
- Whether random per-item data can be shown on the Market (docs say dynamic props are not shown and are cleared on trade; may have changed).
- Task Bar Hero's architecture (own server vs Steam Inventory), its lost-loot details (outlet conflict on studio name), and what Valve actually told them; Kotaku's $1,000 weapon figure; Deskrawl's bot/market outcomes (nothing found).
- Any Valve statement or policy change specifically about idle games and the Market in 2026 (none found; only the May 2026 Market beta and the TBH episode).
- Godot fullscreen-app detection, multi-monitor behaviour, and Steam overlay compatibility with our transparent window; all need first-playable spikes.
- Cost of hosting at scale and legal/regional advice (outside our competence).
