# Gloamway: the pitch in two pages

Status: PROPOSAL for the owner's review. Nothing is built. Not a commitment to spend money.
Full documents attached in the same request: the game design (Sage, ~12,600 words) and the production plan (Marlowe). Claims are labelled in the design as sourced from our notes, design choice, hypothesis, or unverified.

## The game in one paragraph
**Gloamway** is a desktop-companion idle ARPG for PC on Steam. A chibi lamplighter, Wick, and a slime familiar, Gel, patrol a dusk road on a thin transparent strip above your taskbar. They auto-fight and drop gear with random affixes, sets and uniques, like a proper loot ARPG. You choose skills, passives, gear and when to push a boss. The strip sleeps near 0% CPU, hides itself when a fullscreen app runs, and never steals focus. Slimes live on as the Jellyfolk faction (and Gel), so the anime-slime charm stays. Theme and name are proposals; the first alternative was a straight "Slime Kingdom".

## Why this could work (and why it might not)
- **Real demand:** Valve made "Desktop Companion" an official tag in May 2026; several desktop-strip idlers have very positive reviews, and one free one peaked around half a million players (with mixed reviews). Evidence is search snippets only.
- **Crowded and hit-driven:** about 1,566 idle games released in 2026 so far, and the median paid release reportedly earns very little (secondary source). Our edge has to be restraint and polish: low CPU, a truly transparent click-through strip, no buggy prestige resets, no paid random boxes.
- **Honest unknowns:** code-drawn art may not carry the store capsule; all balance numbers are hypotheses until a headless simulator and playtests; the Godot transparent-window technique is unproven on this team (that is the first spike).

## What v1.0 contains (the cut line)
6 zones; 2 classes (Lampwright, Hush Archer); 45 passive nodes; 20 uniques; one difficulty tier ("Dusk Tier I"); no music; Gel as a companion. Cut to v1.1: the Gel Tamer class, zones 7-10, Glimmer Rifts, festivals, music. Each cut lists what it costs to restore (production plan section 1.3).
Core numbers (all hypotheses): about 20 kills a minute, about 36 items an hour, a Legendary roughly every 2.8 hours; awake, resting and offline progress at 100%, 60%, 40%; offline capped at 8 hours; performance targets under 2% of a core active, under 0.3% resting, under 180 MB.

## Steam Market (your decision A8: not in v1)
v1.0 ships **without** Market trading. The item model is built Market-ready: randomly rolled gear is never tradable; fixed-definition "Keepsakes" (cosmetic collectibles granted by Steam playtime drops, no server of ours) are the only future-tradable kind and arrive as a clearly marked v1.x milestone (about 6-10 agent-days). Note: Sage's design document describes Keepsakes as launching in 1.0 (its default before your answer); the production plan moves them to v1.x per A8. Reported fees: Steam 5% plus a 10% game fee. No paid random boxes, ever.

## Effort, time and money (all estimates)
- M0 window spike 4-6 agent-days; vertical slice 16-22; alpha 26-36; demo (Prologue, zones 1-2) 10-16; 1.0 38-54. Total about 94-134 agent-days, realistically 6-8 months of calendar because runs go step by step and you review in loops.
- Money: $0 to build and demo. Steam Direct is reported at $100 per app (unverified) and only matters when you decide to publish. Optional paid polish (capsule art, trailer, music) default $0, revisit after the first outside charm check. Agents never spend or publish.
- Gates: G0 window spike works; G1 charm check with 5 outside viewers; G2 measured Windows performance; G3 your Steam spend and identity; G4 release; G5 Market go-live. Kill rule: if the Godot window spike fails (another Godot version, then a native extension, then ask you about Unity).

## What only you can do
A Windows machine to test on (ideally two monitors) is a hard stop for the first gate. Steam partner account, identity, tax and bank, store page, uploads and every publish button. Name and trademark clash check. Recruiting a few testers. Charm judgement.

## Your decisions (defaults in brackets)
1. Go with Gloamway (theme and name) or stay with the original Slime Strip plan (A9). [Gloamway]
2. Approve the v1.0 cut line as written. [yes]
3. Windows test access. [none yet: needed before the window spike]
4. Price placeholder $7.99. [decide later]
5. Steam spend and identity. [defer until the performance gate]
6. Authority for a Unity fallback. [ask first]
7. Art budget. [$0]
8. Market go-ahead and when to ask Valve. [after release]
Approving this request only means: plan accepted as direction; the next step is the engineering prerequisites and the M0 spike on your machine. Nothing is built or published.
