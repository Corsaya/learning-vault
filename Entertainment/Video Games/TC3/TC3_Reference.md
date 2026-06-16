# The Conquerors 3 (TC3) — Master Reference Document
> **Purpose:** This document gives any AI assistant full context to generate accurate TC3 strategy, stat analysis, and game advice without prior knowledge of the game. It contains verified unit/building stats, confirmed prices, game mechanics, meta analysis, and strategic frameworks derived from competitive play research. Treat all prices and stats as ground truth — the wiki has numerous errors documented at the bottom.

---

## WHAT IS TC3?

The Conquerors 3 (TC3) is a real-time strategy (RTS) game on Roblox created by BrokenBone. Players build bases, develop income, produce military units, and destroy all enemy buildings and units to win. It is played on a variety of maps with different terrain, water presence, and crystal layouts. The game has a competitive community with clan wars, tournaments, and ranked play through the TC3 Discord.

**Core loop:** Secure income (crystals/oil) → Build production → Research key units → Field army → Destroy enemy base.

**Win condition (Conquest):** Eliminate all enemy buildings and units. Last team/player standing wins, or the 240-minute timer expires.

---

## GAME MECHANICS

### Starting Conditions
- Base income: **$10 CPM** (Cash Per Minute)
- Income is paid out once per minute in a lump sum

**Naval maps:**
- Starting money: **~$350**
- Starting units: Command Center, Construction Soldier, 3 Light Soldiers, Scout

**Non-naval maps:**
- Starting money: **$410**
- Starting units: Command Center, 3 Light Soldiers, Scout

### FFA Pricing
**All unit and building prices are reduced by 25% in FFA (Free For All) and 1v1 modes.** When calculating FFA costs, multiply any listed price by 0.75. Research costs on the wiki likely reflect FFA pricing — treat research costs as unverified until tested in a standard game.

### Terrain & Elevation
- **Layer 1** (light green) — ground level, all units traverse freely
- **Layer 2** (dark green) — elevated terrain, planes CAN fly over
- **Layer 3** (darkest green) — highest elevation, planes CANNOT fly through or over. Only ground/naval units can attack or be placed here. Layer 3 creates natural fortresses that are air-immune.
- Walls block surface fire (ground and naval) but planes bypass them
- Higher elevation = significant defensive advantage for ground units

### Building Placement Rules
- All buildings must be placed **adjacent to an existing friendly building** — this creates a building chain that extends from your Command Center outward
- **Exception 1: Power Plants** — only require any friendly unit to be near a Power Crystal. No building chain needed. This is critical for early neutral island income grabs.
- **Exception 2: Oil Rigs** — placed by transforming an Oil Ship over an oil spot on water
- **Exception 3: Construction Yards** — placed by transforming a Construction Soldier anywhere accessible
- Buildings **cannot** be placed near enemy buildings
- Naval Shipyards must be built on coastal shoreline (sandy/beach tiles)
- Only one Power Plant per crystal (per player). If an enemy shares your crystal in FFA, both players get half income from it.

### Income System
- **Base:** $10 CPM always
- **Power Plant on regular crystal:** +$10 CPM ($65 cost, breaks even at 6:40)
- **Power Plant on supercrystal:** +$20 CPM (breaks even at 3:15)
- **Nuclear Plant on regular crystal:** +$15 CPM ($130 cost, breaks even at ~8:40)
- **Nuclear Plant on supercrystal:** +$30 CPM (breaks even at ~4:20)
- **Oil Rig:** +$10 CPM (free after Oil Ship transforms)
- **Supercrystals** produce 2x income compared to regular crystals for the same building
- Nuclear Plants are better long-term on contested or permanent crystals; Power Plants are better when capital is scarce or crystals may be lost

### Research Center Mechanics
- Required to unlock any research
- Each additional Research Center built adds **1x research speed multiplier** (2 RCs = 2x speed, 3 RCs = 3x speed, etc.)
- Building multiple RCs is a legitimate strategy to fast-track critical researches like Space Link

### Population Caps by Gamemode
| Type | 2v2/3v3 | 4v4/5v5 | Survival | KOTH | FFA | Territory |
|---|---|---|---|---|---|---|
| Soldiers | 10 | 9 | 9 | 10 | 10 | 10 |
| Tanks | 7 | 6 | 6 | 7 | 7 | 7 |
| Planes | 7 | 6 | 6 | 7 | 7 | 7 |
| Naval | 7 | 6 | 6 | 7 | 7 | 7 |
| Buildings | 25 | 25 | 25 | 25 | 40 | 55 |
| Mines | 18 | 18 | 20 | 18 | 40 | 18 |

### House Population Upgrades
Each house adds +1 to its unit type cap at base. Upgrades are researched at Research Center.
| House | Base | +2 Research | +3 Research | +4 Research |
|---|---|---|---|---|
| Soldier House | +1 | $7 | $15 | $30 |
| Naval House | +1 | $18 | $30 | — capped at +3 |
| Plane House | +1 | $18 | $30 | $75 |
| Tank House | +1 | $11 | $18 | $45 |

### Garrison Mechanics
- Units garrisoned inside vehicles/buildings are **protected from outside fire**
- Garrisoned soldiers in a Jeep can still shoot out
- Medi-Truck heals units garrisoned inside it
- Helicopter heals garrisoned units if a Medic is inside
- Bunker and HQ garrison units for protection but units cannot shoot from inside
- Command Center garrisons 6 units; HQ garrisons 8

### Construction Soldier Infiltration
- Construction Soldiers can build a Construction Yard anywhere they can physically reach, even inside an enemy base
- This creates a forward building chain deep in enemy territory
- Use other units to escort/protect the Construction Soldier during infiltration
- Always watch your base perimeter for enemy Construction Soldiers — they are the primary infiltration tool
- Counter: Scouts (fast, cheap) are excellent at hunting enemy Construction Soldiers before they can place

---

## UNITS — COMPLETE STATS

> All prices listed are **standard (non-FFA)**. Multiply by 0.75 for FFA prices.
> DPS = Damage Per Second. Negative DPS = healing rate.

### SOLDIERS — produced at Barracks (unless noted)

| Unit | Price | HP | DPS | Range | Speed | Prod Time | Notes |
|---|---|---|---|---|---|---|---|
| Light Soldier | $10 | 100 | 1 | 15 | 7 | 7s | Basic combat unit |
| Heavy Soldier | $20 | 100 | 2 | 15 | 6 | 8s | 2x DPS of Light Soldier for 2x cost |
| Scout | $12 | 70 | 0.7 | 12 | 10 | 5s | Fastest ground unit; best for map vision and hunting Construction Soldiers |
| Medic | $60 | 75 | -1.25 | 10 | 7 | 13s | Heals nearby soldiers passively |
| Repairman | $25 | 10 | -1.75 | 10 | 7 | 12s | Repairs buildings, naval units, and walls. Very low HP — protect it. |
| Construction Soldier | $25 | 10 | — | — | 7 | 10s | Transforms into Construction Yard. Core expansion tool. |
| Engineer | $50 | 50 | — | 6 (buff) | 7 | 18s | 25% production speed + build speed buff in aura range. Does NOT stack with multiple Engineers. |
| Anti-Air Soldier | $40 | 75 | 6.6 | 16 | 7 | 12s | Targets air units only. Essential defense vs planes/space. |
| Sniper | $70 | 40 | 7.5 | 23 | 5.5 | 10s | Longest range ground unit. Targets soldier-slot units **including Nuclear Missiles in flight**. Low HP. |
| Juggernaut | $50 | 190 | 3.5 | 15 | 5 | 15s | **Research required: 5:00 for $60** — Fort. High HP tank for frontline pushes. |
| Jeep | $55 | 150 | — | — | 10 | 10s | Fort. Garrisons 4 soldiers who can shoot while inside. Fast transport. |
| Humvee | $85 | 250 | — | — | 9 | 12s | **Research required: 3:00 for $30** — Fort. Garrisons 6 soldiers. Meta mid-game unit. |
| Medi-Truck | $90 | 200 | -2.5 | — | 11 | 20s | Fort. Garrisons 12 units and heals them. Fastest healing vehicle. |
| General | $135 | 200 | — | 9 (buff) | 8.5 | 9s | Fort. **+50% damage to attacking soldiers in range, +50% heal rate to Medics/Repairmen**. Game-changing buff unit. |
| Artillery | $115 | 40 | 6.2 | 32 | 5.5 | 15s | **Research required: 4:00 for $55** — Fort. Classified as Tank type. Longest range unit in the game. Cannot attack units — buildings and structures only. Extremely fragile. |

### TANKS — produced at Tank Factory (unless noted)

| Unit | Price | HP | DPS | Range | Speed | Prod Time | Notes |
|---|---|---|---|---|---|---|---|
| Light Tank | $60 | 275 | 2.6 | 16 | 6 | 15s | Budget tank, decent HP |
| Heavy Tank | $90 | 275 | 3.4 | 17 | 5.5 | 18s | Better DPS and range than Light Tank |
| Explosive Tank | $60 | 100 | 120 | Melee | 7 | 15s | Suicide unit — contact detonation, one-time use. 120 instant damage on contact. Countered by range. |
| Anti-Air Tank | $90 | 225 | 10 | 18 | 8 | 12s | Fastest tank, high AA DPS. Essential on maps with heavy air presence. |

### PLANES — produced at Airport or Aircraft Carrier

| Unit | Price | HP | DPS | Range | Speed | Prod Time | Notes |
|---|---|---|---|---|---|---|---|
| Light Plane | $60 | 125 | 1.8 | 15 | 12 | 15s | Cheapest air unit |
| Heavy Plane | $75 | 160 | 2.4 | 16 | 11 | 18s | More HP and DPS than Light Plane |
| Helicopter | $60 | 110 | 0.55 + 0.7/soldier inside | 14 | 12 | 16s | Carries 4 soldiers. Heals 1.2hp/s to garrisoned units if a Medic is inside. |
| Transport Plane | $90 | 185 | — | — | 11 | 25s | Carries 6 soldier/tank/vehicle units. Cannot carry Explosive Tanks. |
| Stealth Bomber | $140 | 32 | 9 | 13 | 16 | 23s | **Research required: 4:00 for $40**. Cannot be targeted by ground units or standard turrets — only AA units. Very low HP. Invisible on radar. |

### SPACE UNITS — produced at Space Link (and Mothership)

| Unit | Price | HP | DPS | Range | Speed | Prod Time | Notes |
|---|---|---|---|---|---|---|---|
| Space Fighter | $130 | 210 | 2.5 | 16 | 14 | 12s | Fast, durable air unit. Produced by both Space Link and Mothership. |
| Mothership | $420 | 425 | 7.058 | 18 | 11 | 60s | **Space Link only.** Carries 12 Space Fighters. Heals garrisoned units (-2.5 heal rate, like Medi-Truck). Counts as 2 plane slots. The premier late-game unit. |

### NAVAL — produced at Naval Shipyard

| Unit | Price | HP | DPS | Range | Speed | Prod Time | Notes |
|---|---|---|---|---|---|---|---|
| Oil Ship | $35 | 80 | — | — | 10 | 16s | Transforms into Oil Rig over an oil spot |
| Transport Ship | $60 | 215 | — | — | 10 | 15s | Carries 6 soldier/tank/vehicle units |
| Hovercraft | $90 | 180 | 1.6 | 15 | 9 | 20s | Amphibious — can cross land and water. Carries 2 soldiers. |
| Gunboat | $55 | 215 | 2.5 | 17.5 | 10 | 21s | Fast, cheap naval combat unit |
| Destroyer | $90 | 300 | 3 | 20 | 9 | 26s | Attacks submarines (only unit besides sub that can). Has dedicated AA turret: **5 DPS**. |
| Battleship | $150 | 400 | 5 | 25 | 8 | 40s | High HP, long range, high DPS naval unit |
| Aircraft Carrier | $425 | 475 | 8.5 | 27 | 7 | 40s | Highest DPS naval unit. Can produce planes at sea. Max pop cost is high. |
| Submarine | $110 | 175 | 3.4 | 16 | 12 | 30s | **Research required: 2:00 for $30.** Invisible to most units. Only Destroyers and other subs can detect/attack it. |

### MISSILES — produced at Nuclear Silo

| Unit | Price | HP | Speed | Prod Time | Notes |
|---|---|---|---|---|---|
| Nuclear Missile | $300 | 333 | 36 | 240s | 300 damage in explosion range 11. One-time use. Snipers can intercept in flight. Shield Generator blocks it. |
| Fire Missile | $300 | 200 | 36 | 240s | 90 total damage on impact + fire spread (7 dmg per tick, range 14, spreads to allies). Fire penetrates Shield Generator. One-time use. |

---

## BUILDINGS — COMPLETE STATS

> All prices listed are **standard (non-FFA)**. Multiply by 0.75 for FFA prices.

### INCOME BUILDINGS

| Building | Price | HP | Build Time | Income | Notes |
|---|---|---|---|---|---|
| Power Plant | $65 | 265 | 10s | +$10 CPM (regular) / +$20 CPM (super) | Break-even: 6:40 regular, 3:15 super |
| Nuclear Plant | $130 | 300 | 10s | +$15 CPM (regular) / +$30 CPM (super) | Break-even: ~8:40 regular, ~4:20 super |
| Oil Rig | Free | 325 | 18s | +$10 CPM | Transforms from Oil Ship over oil spot |
| Construction Yard | Free | 100 | 12s | — | Transforms from Construction Soldier. Can toggle back to soldier. |

### PRODUCTION BUILDINGS

| Building | Price | HP | Build Time | Notes |
|---|---|---|---|---|
| Barracks | $150 | 170 | 16s | Produces all soldier-type units |
| Fort | $200 | 350 | 16s | Produces Fort units. Also has DPS 7, Range 25 defensive fire. Garrisons 6 soldiers/tanks. |
| Tank Factory | $235 | 220 | 30s | Produces all tank-type units |
| Naval Shipyard | $80 | 325 | 30s | Produces all naval units. Must be placed on shoreline. |
| Airport | $200 | 265 | 25s | Produces all plane units |
| Space Link | $440 | 125 | 40s | **Research required: 12:00 for $100.** Produces Space Fighters and Mothership. |
| Nuclear Silo | $575 | 200 | 180s | **Research required: 15:00 for $100.** Max 1. Produces Nuclear and Fire Missiles. 3-minute build time. |

### DEFENSE BUILDINGS

| Building | Price | HP | DPS | Range | Build Time | Notes |
|---|---|---|---|---|---|---|
| Turret | $65 | 175 | 5.5 | 16 | 8s | Basic ground/naval defense |
| Anti-Air Turret | $35 | 160 | 10 | 20 | 8s | Air units only. High DPS for price. |
| Fort | $200 | 350 | 7 | 25 | 16s | See Production |
| Command Center | $400 | 450 | 10 | 27 | 32s | Starting building. Garrisons 6. Losing it removes ability to use ally production in team modes. |
| Headquarters | $300 | 520 | 14.5 | 27 | 30s | Max 1. Highest HP building. Garrisons 8. Strongest defensive building. |
| Shield Generator | $250 | 100 body / 500 shield | — | 30 | 25s | Max 1. Shield HP 500, regenerates at 3.5/s. Blocks Nuclear Missiles entirely. Fire Missile spread still penetrates. Combat cooldown 50s, destroyed cooldown 160s. |
| Walls | $30 | Col: 75 / Wall: 275 | — | — | 10s (col) / 5s (wall) | Gate upgrade $10. Columns auto-connect within 12 studs. Blocks ground/naval fire. Planes bypass. |
| Landmine | $20 | 145 | 120 | — | instant | Contact detonation vs ground units. One-time use. |
| Watermine | $20 | 145 | 80 | — | instant | Contact detonation vs naval units. One-time use. |
| Bunker | $75 | 400 | — | — | 32s | Garrisons 6 soldiers/tanks for protection |

### POPULATION BUILDINGS

| Building | Price | HP | Build Time | Notes |
|---|---|---|---|---|
| Soldier House | $40 | 300 | 10s | +1 soldier cap base. Upgradeable to +4 via research. |
| Tank House | $50 | 300 | 12s | +1 tank cap base. Upgradeable to +4 via research. |
| Naval House | $50 | 400 | 14s | +1 naval cap base. Capped at +3 (no +4 upgrade). |
| Plane House | $60 | 300 | 14s | +1 plane cap base. Upgradeable to +4 via research. |
| Skyscraper | $200 | 350 | 10s | **+8 building slots.** Max 1. Critical on high-building-count strategies. |

### SUPPORT BUILDINGS

| Building | Price | HP | DPS | Range | Build Time | Notes |
|---|---|---|---|---|---|---|
| Research Center | $75 | 240 | — | — | 20s | Enables research. Each additional RC multiplies research speed. |
| Hospital | $180 | 215 | -4 | 12 | 22s | Heals soldiers, tanks, planes at double Medic rate. Functions while damaged. |
| Bunker | $75 | 400 | — | — | 32s | See Defense |

---

## RESEARCH COSTS

> **Important:** These costs may reflect 25% FFA pricing from wiki sources. Verify in standard games.

| Item | Cost | Time | Unlocks |
|---|---|---|---|
| Humvee | $30 | 3:00 | Fort unit |
| Juggernaut | $60 | 5:00 | Fort unit |
| Artillery | $55 | 4:00 | Fort unit |
| Submarine | $30 | 2:00 | Naval unit |
| Stealth Bomber | $40 | 4:00 | Airport unit |
| Space Link building | $100 | 12:00 | Unlocks Space Link construction |
| Nuclear Silo building | $100 | 15:00 | Unlocks Nuclear Silo construction |
| Soldier House +2 | $7 | — | +1 soldier pop |
| Soldier House +3 | $15 | — | +1 soldier pop |
| Soldier House +4 | $30 | — | +1 soldier pop |
| Naval House +2 | $18 | — | +1 naval pop |
| Naval House +3 | $30 | — | +1 naval pop (max) |
| Plane House +2 | $18 | — | +1 plane pop |
| Plane House +3 | $30 | — | +1 plane pop |
| Plane House +4 | $75 | — | +1 plane pop |
| Tank House +2 | $11 | — | +1 tank pop |
| Tank House +3 | $18 | — | +1 tank pop |
| Tank House +4 | $45 | — | +1 tank pop |

---

## UNIT VALUE ANALYSIS (DPS per dollar — standard prices)

> Higher = more cost-efficient combat output. Use this to evaluate unit trades.

### SOLDIERS
| Unit | DPS/$  | Notes |
|---|---|---|
| Light Soldier | 0.100 | Baseline |
| Heavy Soldier | 0.100 | Same efficiency, more bulk production |
| Scout | 0.058 | Value is speed/vision, not DPS |
| Anti-Air Soldier | 0.165 | Best AA value in the game |
| Sniper | 0.107 | Value is range (23) not raw DPS |
| Juggernaut | 0.070 | Value is HP (190), not DPS efficiency |

### TANKS
| Unit | DPS/$ | Notes |
|---|---|---|
| Light Tank | 0.043 | HP-efficient, not DPS-efficient |
| Heavy Tank | 0.038 | Slightly worse efficiency but more range |
| Anti-Air Tank | 0.111 | Excellent AA vs planes/space |
| Explosive Tank | 2.000 | Highest burst in game but one-use; only viable with micro |

### PLANES
| Unit | DPS/$ | Notes |
|---|---|---|
| Light Plane | 0.030 | Weak value |
| Heavy Plane | 0.032 | Marginally better |
| Stealth Bomber | 0.064 | Value is immunity to ground targeting |
| Space Fighter | 0.019 | Value is speed (14) + durability (210 HP) |
| Mothership | 0.017 | Value is carrier utility + healing, not raw DPS |

### NAVAL
| Unit | DPS/$ | Notes |
|---|---|---|
| Gunboat | 0.045 | Best cheap naval option |
| Destroyer | 0.033 | Value is sub detection + AA turret |
| Battleship | 0.033 | Best DPS/HP ratio in naval |
| Aircraft Carrier | 0.020 | Value is plane production + range, not DPS/$ |
| Submarine | 0.031 | Value is invisibility, not DPS |

### BUILDINGS (DPS per dollar)
| Building | DPS/$ | Notes |
|---|---|---|
| Anti-Air Turret | 0.286 | Best defensive value in the game per dollar |
| HQ | 0.048 | Best HP/$ defense |
| Turret | 0.085 | Solid ground defense |
| Fort | 0.035 | Value is production + garrison, not just DPS |

---

## STRATEGIC FRAMEWORK

### The Three Game Phases

**Early Game (0–8 min): Income Race**
- Priority 1: Secure all crystals in your territory immediately
- Priority 2: Get Power Plants down — every minute without income is lost money
- Priority 3: Build toward your first Research Center
- Priority 4: Light combat presence to defend and contest neutral crystals
- Do NOT overinvest in units early at the cost of income — a 2-minute income advantage compounds the entire game

**Mid Game (8–20 min): Army Building + Research**
- Research your key units based on map type (see below)
- Upgrade House caps to increase unit ceiling
- Begin contested pushes and harassment — deny enemy income
- Build toward your strategic win condition (Space Link / Nuclear Silo)
- Multiple Research Centers dramatically speed up Space Link (12 min → 6 min with 2 RCs)

**Late Game (20+ min): Win Condition Execution**
- Space Fighter + Mothership is the universal late-game win condition on almost all maps
- Nuclear Silo + missile combo breaks Shield Generator turtles
- Politics matters in FFA — coordinate elimination order
- Mothership with Space Fighters inside is the strongest singular unit composition in the game

### Map Type Decision Tree

**Is there water? (Naval map)**
→ Naval Shipyard is mandatory Day 1
→ Oil Ships for oil spots = free income
→ Naval dominance = map control
→ Transport Ships for island invasions
→ Submarine research early if opponent going naval heavy
→ Aircraft Carrier = late-game naval + air dominance

**No water? (Land map)**
→ No Construction Soldier at start
→ Building chains are the only expansion method
→ Fort + Artillery is dominant on chokepoint maps
→ Layer 3 terrain = air-blocked zones, ground required
→ Walls + Turrets at chokepoints for defense

**Chokepoints present?**
→ Fort + Artillery + Turrets at the chokepoint = nearly impenetrable
→ Walls to funnel enemy into kill zones
→ Snipers behind Artillery for unit protection

**Open map (no chokepoints)?**
→ Mobile units dominate (Humvee, fast tanks, air)
→ Defense is spread thin — aggression rewarded
→ Naval maps with open water: naval control = win

### Unit Composition Meta

**Ground push (land maps):**
Juggernaut (frontline tank) + General (damage buff) + Sniper (AA/range) + Artillery (base damage) + Anti-Air Soldier (air defense) = core land army

**Naval maps:**
Battleship + Aircraft Carrier (control) + Submarine (harassment/stealth) + Destroyer (AA + sub counter) = naval dominance

**Air composition:**
Anti-Air Tank + Anti-Air Soldier + Anti-Air Turret = air defense stack
Space Fighters + Mothership = offensive air late game
Stealth Bomber + Space Fighter = air harassment combo (stealth to draw out AA, fighters to clean up)

**Humvee meta (FFA mid-game):**
Humvee is the dominant mid-game FFA unit. Load with 2 Snipers + 4 soldiers. Mirror matchups are decided by sniper count — having 1–2 more snipers than opponent usually wins. Use Sniper range to hit enemy Humvee before it can return fire.

**Nuke combo:**
Nuclear Missile (blocks with Shield Generator) + Fire Missile (penetrates shield via spread) = guaranteed base damage. Fire spreads to allies so target wisely. Coordinate with teammate in team modes for simultaneous missile strikes before enemy can repair.

### Aggressive vs Defensive Playstyles

**Aggressive:** Minimal income investment, rush units early, contest crystals, deny enemy income. High risk/high reward. Works best in team modes when a teammate can cover economy.

**Balanced:** Standard income development + proportional unit production. Most common competitive style.

**Defensive/Turtle:** Stack defenses at base, max income, wait for Space Link. Strong if executed perfectly but loses to coordinated rushes before Space Link is up. Never turtle without a Shield Generator.

### Key Timings to Know
- **3:00** — Humvee research completes (if started immediately)
- **4:00** — Artillery/Stealth Bomber research completes
- **5:00** — Juggernaut research completes
- **6:40** — Power Plant breaks even on regular crystal
- **12:00** — Space Link research completes (single RC)
- **6:00** — Space Link research completes (double RC)
- **15:00** — Nuclear Silo research completes (single RC)
- First income tick comes at 1:00 — the opening minute is purely build time

---

## FFA STRATEGY GUIDE

### Core Mindset
FFA is 50% military, 50% politics. Being the strongest player militarily does not guarantee a win if all three other players coordinate against you. The ideal FFA path: develop quietly → become second or third strongest → eliminate the weakest → coordinate with remaining player to eliminate the next → win the 1v1.

### FFA Early (0–15 min)
- Secure all crystals in your zone — neutral crystals go to whoever gets there first
- Nuclear Plants over Power Plants on safe crystals (better long-term income on permanent crystals)
- Power Plants on contested crystals (cheaper to lose)
- Research priority: **Humvee (3:00) → Juggernaut (5:00) → Space Link (start immediately)**
- Upgrade Soldier Houses to at least +3 before mid-game Humvee fights begin
- Build 2 Research Centers to halve Space Link research time

### FFA Mid (15–35 min)
- Humvee + Juggernaut is the dominant mid-game composition
- Humvee mirror fights won by sniper count — load 2 snipers + 4 heavy soldiers
- Micro tip: attack enemy Humvee with snipers from outside its garrison's effective range
- Destroy enemy Power Plants, not units — denying income is more valuable than winning fights
- 1–2 tanks for deterrence; save money for Space Link
- Artillery + escort can neutralize a base entirely if protected well
- Target whoever is weakest — avoid being first aggressor against the strongest

### FFA Late (35+ min)
- Space Fighters online = constant pressure on enemy Power Plants
- Space Fighter mirror fights decided by micro (unit control, focus fire, positioning)
- Nuke + Fire Missile combo to break Shield Generators
- Coordinate informally with another player to triple-nuke one target simultaneously
- Mothership is the win condition unit — get it, fill it with Space Fighters, clean up

---

## TEAM STRATEGY GUIDE

### Role Division (3v3 example)
- **Rusher (1 player):** Minimal income, rush units, apply early pressure to deny enemy income development. Does not need to win fights — just deny crystals and production time.
- **Econ (1 player):** Maxes all friendly crystals with Nuclear Plants, builds Skyscraper, funds the team's Space Link research, stays protected behind frontlines.
- **Fighter (1 player):** Balanced army + income, responds to threats, holds the line while rusher and econ do their jobs.

### Team Coordination Priorities
- Only **one player** needs to research Space Link — all teammates benefit from the unlocked building
- Do NOT duplicate research — if one teammate is researching Juggernaut, build something else
- Call out Construction Soldier infiltrations immediately — they're the #1 team-game threat
- Losing a Command Center in a team game doesn't eliminate you but removes ally production access
- Simultaneous pushes from two directions split enemy defensive response — coordinate timing

### Naval Team Rush (Ocean Maps)
One of the most effective team strategies on naval maps:
1. Everyone builds Naval Shipyard immediately
2. Pool money into one player to fast-build Aircraft Carrier
3. Rush enemy base, produce 1–3 planes, destroy their Power Plants
4. Build production from nearest crystal to enemy Command Center (Barracks first)
5. Push with Snipers vs enemy Barracks, Explosive Tanks vs Tank Factory
6. Sell Aircraft Carrier if needed to fund ground production

---

## MAP ANALYSIS FRAMEWORK

When given a map, evaluate these factors for strategy:

1. **Water present?** → Naval required or not
2. **Starting money** ($350 naval / $410 land)
3. **Crystal count and distribution** — are they contested or isolated?
4. **Supercrystal count** — prioritize these for Nuclear Plants
5. **Chokepoints?** → Artillery/Fort/Wall strategy viable
6. **Layer 3 terrain?** → Air blocked in those zones; ground only
7. **Island isolation** → Transport Ships/Planes required for invasion
8. **Oil spot locations** → Contested early game; free income for naval maps
9. **Starting position relative to others** → Who are your immediate neighbors vs distant threats
10. **Max income** — tells you how much total CPM is available to fight over

### Six Small Islands (Naval, FFA4)
- 4 corner islands, 1 player each, open water center
- 8 oil spots (some contested in open water), 16 crystals
- No layer 3 terrain (max layer 2) — all air units viable
- Naval dominance = map control since no land chokepoints
- Oil Ship power plant trick: send Oil Ship near neutral crystal, place Power Plant without building chain
- Island capture priority (from top-left start): Own island → Top-center → Left-center → Bottom-left
- Key units: Submarine (stealth harassment), Battleship (naval dominance), Aircraft Carrier (late control), Space Fighter/Mothership (end game)

### Monument Park (Land, FFA4)
- 4 mid-edge starting positions (not corners), open sand road network
- 20 regular crystals, 8 supercrystals (2x income), max income $580
- Heavy layer 2 AND layer 3 terrain — many air-blocked zones
- Sand roads = all ground combat funnels through predictable corridors
- Center node equidistant from all 4 players — contested killzone early
- Key units: Artillery (32 range down corridors), Juggernaut (frontline), General (50% damage buff), Anti-Air Tank, Sniper
- Layer 3 creates natural fortress zones — build base behind layer 3, defend sand path entrances
- Do NOT contest center early — let others fight over it

---

## KEYBINDS

| Key | Action |
|---|---|
| G | Select all nearby movable units |
| C | Deselect all units |
| M1 (left click) | Select unit / Place building / Move command |
| M2 (right click) | Context action (attack, garrison, transform) |
| Click unit in control panel | Select/deselect individual unit |

> Some keybinds are configurable in Settings.

---

## WIKI DISCREPANCIES (verified errors — do not trust wiki for these)

| Item | Correct Value | Wiki Says |
|---|---|---|
| Scout price | $12 | $17 |
| Light Plane price | $60 | $65 |
| Heavy Plane price | $75 | $85 |
| Transport Plane price | $90 | $125 |
| Stealth Bomber price | $140 | $110 |
| Gunboat price | $55 | $65 |
| Anti-Air Turret price | $35 | $85 |
| Anti-Air Turret damage | 5 (reload 0.5s) | 10 (reload 0.4s) |
| Walls price | $30 | $25 |
| All research costs | Unverified | Likely 25% FFA-discounted |

---

## DATA SOURCE NOTES

All stats in this document were verified through:
1. **In-game screenshots** of the buy menus (ground truth for prices)
2. **TC3 Discord bot** (`/info unit` command) for unit stats
3. **Cross-referencing wiki** and flagging all discrepancies found
4. **NamuWiki TC3 strategy page** for meta/strategic information

Do not use the TC3 Fandom wiki as a primary source — it contains numerous outdated or incorrect values. Use this document instead.
