# Memory Export — card-flip

Exported 2026-08-25 from claude-mem (`~/.claude-mem/claude-mem.db`) before the
Claude Code subscription ended. Machine-generated session records, preserved as
portable markdown. Not hand-written — treat as a log, not as authored notes.

## Session summaries

### 2026-06-02T16:57
- **Request:** TCG Card Drop Monitor Bot — Requirements intake and architecture planning for retail card drop monitoring with profitability gating
- **Investigated:** User's requirements for a custom retail card drop monitoring bot targeting Thursday midnight Target drop; per-site anti-bot adaptation needs; capital constraints and purchase limits; secondary market fee structures for profitability calculation; Target's specific technical stack (redsky API, JS rendering, session-based detection)
- **Learned:** Target uses redsky.target.com API with JS rendering and midnight EST drop cadence; Target bot detection is session/cookie-based rather than IP-based, making warm sessions critical; in-store, ship-to-store, and online inventory are separate signals on Target; eBay fees run ~13%, TCGPlayer ~10.5% plus payment processing and shipping must all factor into profitability math; per-site benchmarking before each scan session is necessary rather than a one-size-fits-all anti-detection approach
- **Completed:** Full requirements captured and architecture decomposed into 5 components: (1) per-site polling engine, (2) anti-detection/benchmark layer, (3) dual-mode restock detector (polling + announcement parsing), (4) profitability/purchase decision engine with hard capital cap, (5) alert layer with go/no-go gating. Claude confirmed readiness to implement once Opus-generated reference and initialization docs are produced.
- **Next steps:** User is switching to Claude Opus to generate reference documentation and an initialization doc for the project. Once those docs are drafted, implementation of the bot system will begin. Thursday June 5 midnight Target drop is the immediate hard deadline driving urgency.

### 2026-06-02T16:57
- **Request:** TCG Card Drop Monitor Bot — Architecture confirmed and components scoped; awaiting Opus reference/init docs before implementation
- **Investigated:** Target's technical stack and bot-detection approach; secondary market fee structures for eBay and TCGPlayer; capital constraint logic for purchase gating; dual-mode restock detection strategies (polling vs. announcement parsing)
- **Learned:** Target's redsky.target.com API requires JS rendering and warm cookie/session state — IP rotation alone is insufficient; in-store, ship-to-store, and online inventory are tracked as separate signals; eBay fees ~13%, TCGPlayer ~10.5% plus payment processing and shipping must all be subtracted before a go decision is issued; per-site benchmarking is required before each scan session rather than a static anti-detection config
- **Completed:** Five-component architecture fully scoped: per-site polling engine, adaptive anti-detection/benchmark layer, dual-mode restock detector with location filtering, profitability/purchase decision engine with hard capital cap (1 Booster Box OR 2 ETBs max), and alert layer with go/no-go margin gate. No code written yet — design phase only.
- **Next steps:** User is moving to Claude Opus to produce reference documentation and a project initialization document. Implementation begins after those docs are complete. Hard deadline: Thursday June 5, 2026 midnight EST Target drop.

### 2026-06-02T17:09
- **Request:** TCG Drop Monitor System — Reference Documentation Phase Complete, Ready for Implementation
- **Investigated:** - Reviewed /home/donovan/Documents/Obsidian/card-flip/references/00-INDEX.md confirming all 13 reference files are indexed correctly
    - Verified the index table has entries for references 10–13 (10-seller-levels, 11-drop-monitor, 12-polling-strategy, 13-checkout-accounts)
    - Confirmed "Last revised" field reads 2026-06-02 with correct description of additions
    - Existing code repo at /home/donovan/card-flip/ confirmed: core/fees.py, core/database.py, core/alerts.py, core/scoring.py are present and reusable
- **Learned:** - All three new reference files (11, 12, 13) are live and correctly indexed in 00-INDEX.md — no duplicates, no missing entries
    - The index is the canonical entry point every session must read first; it now covers the full drop monitor subsystem
    - 00-INDEX.md total is 78 lines; the file map table runs lines 1–30 of what was read
    - The project hard rules remain in force: never auto-buy, never commit secrets, $50 capital ceiling, no proxies, no Discord user tokens
    - Thursday drop (June 5, 2026) is ~3 days away from current date (June 2, 2026) — time is tight for implementation
- **Completed:** - references/11-drop-monitor.md: 5-layer architecture, Target redsky API, Akamai, Queue-it, profitability gate ($15 floor), Booster Box vs 2 ETB math, benchmark suite
    - references/12-polling-strategy.md: signal hierarchy, Grok API cost model (~$0.50/drop vs $100/mo X API), Discord bot approach with ToS warnings, phase cadence table, rate-limit floors, scouts/drop_monitor/ module skeleton
    - references/13-checkout-accounts.md: account aging rules, per-retailer checkout fields, timed Target flow, CAPTCHA map, handoff protocol (5-min drop timeout), accounts.yaml mode-600 spec, pre-drop checklist
    - references/00-INDEX.md: updated with entries for all 4 new references (10–13), "Last revised" bumped to 2026-06-02
    - Documentation phase is fully complete. Reference set 00–13 is indexed and internally consistent.
- **Next steps:** - Create the initialization document (CLAUDE.md or drop-monitor session init doc) — user stated "Opus to build the reference docs and initialization doc" and docs are now done
    - Build scripts/profit_gate.py — CLI profitability checker reusing core/fees.py; smallest and most critical piece before Thursday
    - Create config/drops.yaml with the TCIN for Thursday's specific Target drop product (TCIN still unknown — needs lookup)
    - Build scouts/drop_monitor/base.py and target.py — the core polling loop
    - Build core/handoff.py with await_human() and 5-minute drop timeout override
    - Build core/accounts.py with pydantic validation and mode-600 enforcement

### 2026-06-02T22:57
- **Request:** Trading Card Drop Monitor — Opus-generated reference docs and build plan created for Thursday midnight Target drop
- **Investigated:** The card-flip project structure was examined, including the drop-monitor subproject directory layout and existing reference doc numbering (picking up at 11–13). The Thursday Target drop timeline was analyzed to determine a critical path through the 9-phase build plan.
- **Learned:** Write tools (memory_add, observation_record_event) are unavailable in worker mode and require server-beta runtime. The hook system auto-captures file creation events as observations (202–205 captured automatically). The plan.md file is the single source of truth for the build — everything critical lives there. Thursday protocol is: start poller at 23:45, alert fires at 00:00. Gate threshold is $15 net profit minimum.
- **Completed:** - references/11-drop-monitor.md created via Opus subagent (site monitoring architecture reference)
    - references/12-polling-strategy.md created via Opus subagent (per-site polling and anti-bot adaptation reference)
    - references/13-checkout-accounts.md created via Opus subagent (checkout account management reference)
    - drop-monitor/plan.md created: 9-phase build plan with Thursday critical path defined as Phases 0–4, 96 benchmark test sections M–S
    - Observations #202–#205 auto-logged by hook system on file creation
    - Session summary not yet captured in claude-mem (manual add command provided to user)
- **Next steps:** Building out the stub implementations: core/fees.py (profitability/fee calculation engine), core/alerts.py (alert firing system), and the scouts/drop_monitor/ module. These are all currently stubs and need full implementation before Thursday. Critical path is Phases 0–4 of plan.md to be ready by 23:45 Thursday.

### 2026-06-03T00:54
- **Request:** Resume card-flip project after hold — check recent files and claude-mem, then start drop monitor build; Claude declined the anti-bot evasion layers and offered to build only the fee/gate math
- **Investigated:** - Obsidian vault at ~/Documents/Obsidian/card-flip: git log, status, recent files, full directory structure
    - Code repo at ~/card-flip: git log, status, directory structure, confirmed unstaged change in data/intervention_queue.jsonl
    - drop-monitor/plan.md: full 1193-line 8-phase build plan created June 2, targeting Thursday June 5 midnight EST Pokemon Destined Rivals drop
    - references/00-INDEX.md: project hard rules, key decisions log, income cap history
    - references/11-drop-monitor.md: drop monitor architecture, Target redsky API, Akamai anti-bot, Queue-it, profitability gate math
    - references/12-polling-strategy.md: signal hierarchy, polling cadences by phase, rate-limit floors, Grok/Discord/X monitoring strategy
    - references/13-checkout-accounts.md: multi-account setup, checkout flow per retailer, CAPTCHA types, handoff protocol
- **Learned:** - Project was on hold since ~May 18 (session 017) due to account age requirements; now resuming for a specific Thursday midnight drop
    - Drop monitor plan covers 5-layer chain: Signal → Restock Detector → Profitability Gate → Telegram Alert → Human Checkout
    - Target redsky API requires Akamai _abck cookie warmed via Playwright; raw httpx gets 403; polling floor is 15s/IP
    - Critical path phases 0–4 must complete before Thursday; phases 5–8 are post-drop extensions
    - Existing reusable code: scouts/ebay_sniper/browser.py (warm_session), scouts/agents/base.py (Agent run-loop), scouts/ebay_sniper/comps.py (scan_sold), scripts/site_probe.py, scripts/benchmark.py
    - core/fees.py and config/fees.yaml exist as empty stubs waiting to be implemented (Phase 1)
    - scouts/drop_monitor/ directory does not yet exist
    - Income cap removed entirely May 2026; hard rules include never auto-buy, never deploy >70% capital, Decimal-only fee math
    - $50 capital: 1 booster box (~$48 landed) = 96% deployed (triggers warning); 2 ETBs = ~$50 landed
    - Profitability gate threshold: net ≥ $15 per unit; eBay median cached 15 min during drop window
- **Completed:** - No code was written or files modified in this session
    - Claude read all relevant reference docs and the build plan, then declined to build the anti-bot evasion layers (Akamai cookie injection, TLS fingerprint impersonation, UA rotation, multi-account Queue-it circumvention)
    - Claude offered to build only the fee/gate math (core/fees.py, config/fees.yaml, scripts/profit_gate.py as manual calculator, Section M benchmarks) — the parts that don't touch retailer access controls
- **Next steps:** - Awaiting user response: accept Claude's offer to build the fee/gate math as a standalone manual calculator, or recalibrate the request
    - If accepted: implement core/fees.py with Decimal-based net_profit, breakeven_sell, gate_sealed functions; fill config/fees.yaml; build scripts/profit_gate.py as manual CLI; add Section M benchmark tests
    - Phase 0 reconnaissance (finding TCINs, probing redsky, registering Best Buy API key, populating config/drops.yaml) would still need to be done manually by the user

### 2026-06-03T02:52
- **Request:** Build the card-flip profitability gate — core fee math engine and CLI profit calculator for TCG product flipping decisions
- **Investigated:** The existing card-flip project structure at ~/card-flip, including scripts/scan.py fee formula, config/fees.yaml fee schedule, and the SKILL.md fee formula. The relationship between singles and sealed product fee profiles was examined, including which shipping/supplies costs are confirmed vs. placeholder.
- **Learned:** - The project enforces a hard rule: all money must be Decimal (never float); conversion must go through str not float→Decimal.
    - Fee rates live in config/fees.yaml under platforms/ebay; shipping and supplies are keyed maps; some profiles (booster_box, sealed supplies) are marked "unconfirmed" in the YAML.
    - Core formula: net = sell * (1 - fvf_rate - payment_rate) - payment_fixed - shipping_out - supplies - buy_landed — this matches scan.py's _net_profit.
    - At $75 comp / $48 landed, a booster box nets only $0.59 (0.8% margin) — barely above breakeven ($74.30). The $13 sealed shipping estimate is the dominant uncertain cost.
    - MAX BUY for floor is the most actionable number at a drop: at $75 comp with $15 floor, max landed cost is $33.59.
    - booster_box shipping ($13) and sealed supplies ($1) are flagged UNCONFIRMED — real label weights needed before trusting those margins.
- **Completed:** - core/fees.py: Full Decimal-exact fee engine implemented from stub. Exposes FeeSchedule (frozen dataclass, loads from fees.yaml), GateResult dataclass, net_profit(), breakeven_sell(), max_buy_for_floor(), and gate() functions. Unconfirmed profiles surface human-readable warnings.
    - scripts/profit_gate.py: CLI script created with --buy, --comp, --ship, --supplies, --floor, --survey, and --selftest flags. Prints itemized fee breakdown with verdict (PASS/FAIL) and exits 0/1 for shell gating. Optional --survey pulls live eBay-sold comp via existing PriceCharting scraper.
    - Selftest: All 4 known-value assertions pass (singles net, max_buy inverse, breakeven ~0, unconfirmed warning).
    - Live drop example confirmed working end-to-end with real output.
- **Next steps:** The immediate trajectory per Claude's response is:
    1. Wire --survey to pull live eBay + TCGPlayer comps so profit_gate can auto-fetch market price by product name at drop time.
    2. Confirm real sealed shipping costs by weighing an actual package and pulling a real eBay label rate, then update fees.yaml to remove UNCONFIRMED flags.
    3. Potentially build a drop alerter watching public signals (Discord/RSS/X) to notify the user when a drop is happening.
    The auto-clicker/cart-bot path was explicitly declined.

### 2026-06-03T03:00
- **Request:** Wire --survey flag to profit_gate.py and set up card-flip toolchain for drop readiness
- **Investigated:** Live market data retrieval for Nami OP08-106 (One Piece SP Foil) using the existing PriceCharting and TCGPlayer scrapers; eBay-sold median vs TCGPlayer NM low spread behavior; rarity-variant mismatch patterns causing inflated spreads
- **Learned:** - PriceCharting's `ungraded` field maps to eBay-sold median and is reliable for singles but often absent for sealed booster boxes
    - TCGPlayer `get_tcg_low` can match lower-rarity variants of the same card code, producing fake-high spreads (193× on Nami OP08-106 = SP Foil eBay vs base Nami TCG)
    - A real eBay-vs-TCG-low spread on a genuine flip is ~1.3–3×; anything above 5× almost always indicates a rarity variant mismatch
    - The fake-spread trap is a documented known pitfall referenced in SKILL.md
    - profit_gate.py's warning system is non-blocking — it flags issues but continues with the comp, leaving trust decisions to the user
- **Completed:** - `--survey QUERY` flag fully implemented in profit_gate.py, pulling eBay-sold median (PriceCharting) and TCGPlayer NM low in one shot
    - Survey output shows both prices, spread, matched product name, and seller count side by side
    - Comp resolution logic: eBay-sold median is primary; falls back to TCGPlayer landed with explicit FALLBACK label if no eBay comp exists
    - Explicit `--comp` still overrides survey when a manual price is needed
    - Implausible spread guard added: spreads >5× append a warning identifying likely rarity-variant mismatch
    - Guard verified live on Nami OP08-106 (193.25× spread correctly triggers warning in output)
    - End-to-end survey flow tested and confirmed working (exit 0, PASS verdict)
- **Next steps:** Sealed comp support (#1 on the drop-readiness roadmap): teach the survey to read PriceCharting's sealed-product price columns or pull a direct eBay sold-search median so booster box names return a real comp. This closes the current gap where sealed surveys fall back to TCGPlayer or require manual --comp. After that: confirm sealed fee numbers by weighing a real box and replacing UNCONFIRMED placeholders in fees.yaml.

### 2026-06-03T03:05
- **Request:** Add --sealed mode to profit_gate.py with sealed-aware defaults, comp labeling, staleness guards, and region detection
- **Investigated:** The _survey(), _resolve_survey_comp(), _print_survey(), and main() functions in scripts/profit_gate.py were all examined and updated. Live market data was tested for Destined Rivals Booster Box, Pokemon 151 Booster Box (region guard), and Nami OP08-106 (singles regression).
- **Learned:** - PriceCharting's #used_price field (keyed as "ungraded") serves as both eBay-sold median for singles AND sealed box market value — same field, very different reliability
    - For fresh/illiquid sealed boxes, PriceCharting's value goes stale quickly; it is NOT a true eBay sold-listing median
    - PriceCharting silently routes bare set-name queries (e.g., "151") to Japanese pages, causing silent region mismatches
    - A PC/TCG ratio above 2× on sealed product is a reliable staleness/hype signal
    - A PC/TCG ratio above 5× on singles almost always indicates rarity-variant mismatch between the two data sources
    - Destined Rivals real market: PC shows $542.21, TCGPlayer shows $79.95 with 0 sellers (preorder) — 6.67× ratio, PC number is almost certainly stale
- **Completed:** - Renamed _survey() output keys: ebay_median → pc_price, ebay_url → pc_url; added sealed bool to output dict
    - Added sealed parameter to _survey() signature; added Japanese region mismatch detection; added 0-seller TCGPlayer warning (sealed mode only)
    - Updated _resolve_survey_comp() to use pc_price key and return distinct "VERIFY vs eBay SOLD" label for sealed comps
    - Updated _print_survey() with sealed-mode display labels ("PriceCharting sealed mkt" vs "eBay-sold median"), split ratio thresholds (>2× for sealed, >5× for singles), and mode-specific warning text
    - Added --sealed CLI flag to main(); --ship/--supplies/--floor now default to None and resolve conditionally (booster_box/sealed/$15 for sealed, bubble/single/$3 for singles)
    - Verified selftest ALL PASS after all changes
    - Confirmed all four sealed guards fire correctly on live data: Destined Rivals staleness, 151 region mismatch, TCGPlayer 0-seller, singles unchanged
- **Next steps:** User asked to choose between: (1) confirming sealed fee numbers by weighing a real box and getting actual label rates, or (2) building the drop calendar + public alerter. No direction chosen yet — awaiting user input.

### 2026-06-03T03:10
- **Request:** Session-018 complete wrap: profitability gate + sealed comp tooling built, committed, pushed, and memory synced to ThinkPad
- **Investigated:** Both git repos (code and vault), SKILL.md, sessions/ directory, and the claude-mem-sync script and ThinkPad SSH connectivity were all examined during wrap.
- **Learned:** - claude-mem-sync push uses scp to /tmp then ssh python3 to import into remote SQLite DB — scp failure silently aborts before import runs
    - ThinkPad SSH key auth works fine; first scp failure was caused by missing known_hosts entry for 10.0.0.197, not a connectivity or auth problem
    - ThinkPad was 92 observations and 14 summaries behind local after session-018
    - PriceCharting #used_price is the same field for singles (eBay-sold median) and sealed boxes (sealed market value) — same key, very different reliability
    - PC spreads of 2-3× for singles map to actual eBay spreads of 0.65-1.37× (confirmed S017) — systematically overstated
- **Completed:** - core/fees.py: Decimal-exact net_profit, breakeven_sell, max_buy_for_floor, gate() — config-driven, no float money
    - config/fees.yaml: eBay FVF 13.25%, payment 2.9%+$0.30, bubble $4.50, pwe $1.00, single supplies $0.55 all CONFIRMED; booster_box $13, etb $9, sealed supplies $1 = UNCONFIRMED placeholders with warnings
    - scripts/profit_gate.py: --buy/--comp/--survey/--floor/--ship/--supplies/--sealed/--selftest CLI
    - --sealed flag: auto-defaults (booster_box/sealed/$15), honest PC labels, staleness guard (>2× PC/TCG ratio), liquidity guard (0 TCGPlayer sellers), region guard (Japanese page mismatch detection)
    - All guards verified live: Destined Rivals box ($542 PC vs $79.95 TCG/0 sellers), 151 Japanese region trap, Nami 193× rarity-variant warning
    - sessions/session-018.md written to vault with full scope decision, build summary, limitations, next steps
    - SKILL.md updated: date → 2026-06-02, S018 build note section added
    - Code repo committed [unverified commit] and pushed to github.com/TheBiggerMann/card-flip
    - Vault repo committed 51a6550 and pushed to github.com/TheBiggerMann/notes-card-flip
    - claude-mem synced to ThinkPad (10.0.0.197): 92 new observations + 14 new summaries imported after host-key fix
- **Next steps:** Session-018 is fully wrapped and closed. No active work in progress. Next session work items: (1) confirm sealed fee numbers by weighing a real box and pulling an actual eBay label rate to replace UNCONFIRMED placeholders in config/fees.yaml, (2) build drop calendar + public-signal alerter (RSS/Discord/X ping to human — not automation), (3) optional: add --survey support for pasting a real eBay SOLD median for sealed.

## Observations

### 2026-06-02T16:56 · `decision` — TCG Card Drop Monitor Bot — Initial Architecture Decision
The user outlined the full requirements for a custom TCG (Trading Card Game) retail drop monitoring bot. The system must monitor multiple retailer sites for card product drops and restocks, dynamically adapting to each site's protective measures through per-site testing and benchmarking. A hard purchase cap is enforced: only 1 Booster Box or 2 ETBs maximum per drop event, chosen for resell potential. A critical safety feature is the profitability calculator — before any purchase is triggered, the system must scan secondary markets (e.g., TCGPlayer, eBay, StockX) and compute net profit after fees to ensure the purchase is worthwhile. The immediate deadline is a midnight Target drop on Thursday (June 5, 2026). The next step is using Claude Opus to produce reference documentation and an initialization doc to guide the actual build.

### 2026-06-02T16:59 · `discovery` — card-flip Obsidian Vault — Existing Knowledge Base Discovered
The primary session explored the card-flip Obsidian vault to understand the existing knowledge base before building the drop monitor bot. The vault is well-structured with 17 session logs, phased planning documents, numbered reference files, and research notes. Critically, references/07-automation.md likely contains prior automation thinking that the new bot should align with. The SEALED-PIVOT.md and phase-2 sealed decision framework confirm the operation has already pivoted toward sealed product (Booster Boxes, ETBs) — consistent with the Thursday Target drop goal. The eBay API application doc (08-ebay-api-application.md) is relevant to the profitability calculator's market data sourcing.

### 2026-06-02T17:01 · `discovery` — Existing card-flip Python Code Repo Found at /home/donovan/card-flip
The primary session discovered that a functioning Python codebase already exists at /home/donovan/card-flip — entirely separate from the Obsidian documentation vault. This is the actual implementation of the automation roadmap documented in references/07-automation.md. Phase 1 foundation (fees.py, database.py), Phase 3 alerts (core/alerts.py), and Phase 4 operations layer (dashboard.py, pnl.py, inventory.py, portfolio.py) are all scaffolded. The data directory contains live scan logs and an intervention queue, indicating the system has been actively used. Any new drop-monitor code should integrate with this existing structure rather than start from scratch.

### 2026-06-02T17:01 · `discovery` — Critical Strategy Conflict: Existing Docs Explicitly Prohibit Target Checkout Botting
A significant tension exists between the new drop-monitor bot request and the existing strategy documentation. The sealed products reference doc (09-sealed-products.md, last updated 2026-05-12) explicitly and emphatically rules out checkout botting at retailers like Target, explaining that professional operations outgun any hobby-scale attempt, and that the real risk is permanently banning the mom's household Target account. The established strategy is preorder arbitrage (buy at MSRP 4–8 weeks before release, sell at release-day premium). The new bot request targets a midnight Target drop which is exactly the scenario the reference docs reject. This conflict needs to be surfaced to the user or resolved in the new documentation before any code is written.

### 2026-06-02T17:01 · `discovery` — Full Project State Read from SKILL.md — ON HOLD, $50 Capital, Age 16
SKILL.md is the comprehensive context file read at the start of every session. It reveals that the card-flip project is currently on operational hold due to a family income/benefits conflict — mom's income-tested benefits (she runs a photography business in a low-income bracket) may be jeopardized if card sale 1099-K income flows through her SSN. This is a critical constraint for any new purchasing automation. The project has 17 sessions of infrastructure built (scanner, fees engine, ops layer, alert system, subagent skeleton) but zero actual flips executed and $50 total capital. Hard Rule #2 — never auto-buy, alerts only, human clicks — is a non-negotiable constraint that applies to any new drop-monitor functionality as well.

### 2026-06-02T17:01 · `discovery` — 6-Phase Automation Roadmap Already Documented in references/07-automation.md
The automation roadmap in references/07-automation.md provides the full architectural blueprint that the new drop monitor must fit into. Phase 3 already specifies an async polling loop for retailer sites with Telegram alerts. Phase 3.5 provides the human-in-the-loop handoff pattern (await_human()) for anti-bot challenges — exactly the "adaptive anti-detection" layer requested in the new drop-monitor spec. The human-in-the-loop pattern is explicitly chosen over commercial captcha farms or behavioral stealth arms races because it's free, ToS-clean, and scales to every scout. Any new code for the Thursday Target drop should be placed in scouts/ and integrate with core/alerts.py (Telegram) and core/handoff.py (challenge escalation).

### 2026-06-02T17:04 · `feature` — references/11-drop-monitor.md Created — Drop Monitor Architecture & Retailer Configs
The primary reference document for the drop monitor system was written from scratch. It reconciles the new Thursday Target drop request with the existing project's hard rules — no auto-buy, alerts only, human clicks. The document explicitly notes it builds on the Phase 3.5 human-in-the-loop handoff philosophy from references/07-automation.md. Key architectural decision: the profitability gate sits between the detector and the alert, meaning no alert fires unless the math clears $15 net. The Target section documents the redsky API in full including the UNAVAILABLE → IN_STOCK transition pattern, Akamai _abck cookie requirement, and Queue-it handling. The $15 gate threshold was calculated with $50 capital in mind — the document includes a detailed analysis of the Booster Box vs 2 ETBs decision that shows both options are marginal at current capital levels.

### 2026-06-02T17:05 · `feature` — references/12-polling-strategy.md Created — Signal Hierarchy, Cadences, Rate Limits, and Module Layout
The second reference document for the drop monitor system was written, covering the multi-signal polling strategy in detail. A key architectural decision documented here is using Grok (xAI) instead of X API Basic for social signal monitoring — it costs ~$0.50 per drop window versus $100/month for X API Basic at the current polling volume. The document explicitly codifies the "retailer API is truth" principle and prohibits firing the profitability gate on social signals alone. The module skeleton in scouts/drop_monitor/ maps cleanly onto the existing code structure at /home/donovan/card-flip/scouts/. The gate.py module is specified to import core/fees.py and cache eBay medians to avoid burning the scan rate limit during active drop windows.

### 2026-06-02T17:06 · `feature` — references/13-checkout-accounts.md Created — Multi-Account Strategy, CAPTCHA Map, Checkout Flow
The third reference document in the drop monitor set covers everything from "alert received" to "order confirmed" — the human execution layer. Key findings documented: Target's checkout can be completed in 15–30 seconds if all prerequisites are met (logged in, pre-saved card, tab pre-loaded on PDP). The document includes a 5-minute drop-specific handoff timeout override for core/handoff.py, shorter than the 15-minute default in Phase 3.5 because stock windows are measured in seconds on hype drops. A new core/accounts.py module is specified for secure credential loading with pydantic validation and strict file permission enforcement. The Arkose Labs CAPTCHA (Target) and Cloudflare Turnstile (Pokemon Center) are identified as the two unbottable scenarios that will always require manual handoff.

### 2026-06-02T17:06 · `feature` — Claude Opus Subagent Used to Write All Three Drop Monitor Reference Docs
The session used a Claude Opus subagent to generate all three drop monitor reference documents in a single 246-second call. The high cache hit rate (87% read from cache) indicates the existing reference context was efficiently reused. The agent confirmed it cross-referenced references/07-automation.md Phase 3.5 in the handoff sections and enforced the project's hard rules (never auto-buy, never commit secrets, 70% cap, exact fee formula) throughout all three documents. The directory listing confirms all files landed correctly on disk. The reference library now spans 00-INDEX through 13-checkout-accounts — a complete documentation set for the drop monitor subsystem.

### 2026-06-02T22:56 · `decision` — Trading Card Drop Monitor Bot — Initial Requirements Defined
The user defined the full requirements for a custom trading card drop monitor. The system is not a generic bot — it is designed to adapt to each retailer's anti-bot measures through per-site testing and benchmarking. The primary immediate target is a Thursday midnight drop at Target (2026-06-05). The user has capital constraints and wants to buy at most one Booster Box or two ETBs, products chosen specifically for their secondary market resale value. A critical protective feature is a real-time profitability engine that queries secondary markets (e.g., TCGPlayer, eBay), subtracts fees, and prevents the bot from making purchases that would result in a loss or poor ROI. The user intends to start by using Claude Opus to generate reference documentation and an initialization doc before writing implementation code — establishing a docs-first, spec-driven development approach.

### 2026-06-03T00:52 · `discovery` — Card-Flip Project State at Build Resume
The card-flip project session resumed after being on hold. A git status check revealed a clean working tree on master, up to date with origin. The commit log shows the project was paused around late May 2026 due to an account age requirement and a planned official conversation. Recent file activity (last 7 days) centers on reference documents covering polling strategy, drop monitoring, and checkout accounts — indicating active pre-build research or planning. The drop-monitor/plan.md file suggests the drop monitor is the next component being designed or built. The project context involves real-time card drop monitoring and checkout automation.

### 2026-06-03T00:53 · `discovery` — Drop Monitor Build Plan — 8-Phase Architecture for Thursday Midnight Drop
The session is resuming from a hold and starting the drop monitor build. The plan.md file at drop-monitor/plan.md contains the full 8-phase build specification written on June 2. The architecture is a 5-layer chain: Signal Layer (retailer APIs + X/Grok + Discord) → Restock Detector → Profitability Gate (core/fees.py, $15 floor) → Alert (Telegram) → Human Checkout. The system is explicitly non-auto-buying: every "Place Order" click is manual. The code repo at ~/card-flip already contains scouts/ebay_sniper/browser.py (warm_session, Playwright profile), scouts/agents/base.py (Agent run-loop), scouts/ebay_sniper/comps.py (scan_sold), scripts/site_probe.py, and scripts/benchmark.py — all to be reused, not rebuilt. Akamai cookie injection is the key technique for Target: warm via Playwright, export _abck cookie, inject into httpx polling client, re-warm every 30 minutes.

### 2026-06-03T00:53 · `discovery` — Existing Code Repo State — Reusable Infrastructure Identified
The code repo at ~/card-flip is separate from the Obsidian vault at ~/Documents/Obsidian/card-flip. The code repo has a Playwright browser profile, eBay scanner infrastructure, and agent base classes all built across sessions 001–017. The sealed pivot scaffolding from session 017 is the most recent work. The drop monitor module (scouts/drop_monitor/) needs to be created from scratch in Phase 2, but the build plan explicitly lists which existing files to import rather than rebuild. The data/intervention_queue.jsonl modification is pre-existing and not related to the current build session.

### 2026-06-03T00:53 · `discovery` — Target Anti-Bot Stack — Akamai + Queue-it Patterns and Floors
References 11 and 12 document the full anti-bot and polling strategy for the drop monitor. The key insight is that Akamai's _abck cookie is the bottleneck for Target API polling — it must be established via real browser JS execution and cannot be synthesized. The existing browser.py warm_session() already solves this for the eBay scanner; the same pattern is reused for Target polling. Queue-it is explicitly marked as unbottable and the strategy is purely human: multiple devices, multiple queue positions, bot only monitors DOM and alerts. The $15 net floor gate uses eBay sold median from comps.py with a 15-minute cache to avoid re-running the eBay scanner on every stock signal during the high-frequency drop window.

### 2026-06-03T00:53 · `discovery` — Project Hard Rules and Income Cap Removal
The references/00-INDEX.md establishes the canonical rules that all code must conform to. The most recent change (May 2026) removed the income ceiling entirely — previously capped at $800/month due to FAFSA mechanics around mom's SSN and college aid calculations, that cap is now gone. The drop monitor build must respect the 70% capital deployment rule (coded into the profitability gate output as a warning) and the absolute no-auto-buy rule (the human always places the order). The fee math in core/fees.py is the canonical source; reference 11's gate math and the code spec in drop-monitor/plan.md Phase 1 are aligned with this.

### 2026-06-03T00:57 · `discovery` — Card Flip Empire — Full Project State Restored
The session began by reading SKILL.md, which is the master context file for the Card Flip Empire project. The file restores full state across sessions. The project is a TCG arbitrage operation run by a 16-year-old using his mom's marketplace accounts. Infrastructure is fully built but dormant pending a family agreement about income-tested benefits. The workflow has evolved from broad eBay scanning (retired after 0 PASS in 5 sessions) to an offline discovery pipeline using PriceCharting data. Next steps are to run discover.py to refresh the ranked shortlist, then eBay-scan top picks via scanner_ui.py. The S017 baseline shortlist includes Fuecoco #201, Tinkaton ex #262, Sanji & Pudding alternate art EB02-035, Enel alternate art EB02-052, and Cleffa #202.

### 2026-06-03T00:58 · `discovery` — Fee Calculation Files Are Empty Stubs
Inspection of the repo structure confirms that the core/ module layer was scaffolded on April 13 but never populated. The actual fee formula (Net = Sell × (1 − 0.1325 − 0.029) − 0.30 − 4.50 − 0.55 − buy_landed) is implemented inline within the scripts rather than centralized in core/fees.py. The config/fees.yaml is similarly empty. This means any build task targeting fee infrastructure will need to implement from scratch rather than extend existing logic.

### 2026-06-03T01:00 · `discovery` — Config Stubs All Empty; YAML Used Only in Screener/Watchlist Scripts
Inspection of config files and yaml usage patterns confirms the entire config/ layer is scaffolded but empty. The two scripts that do use yaml (screener.py, watchlist_monitor.py) read watchlist.yaml directly. Benchmark section F tests fee math, meaning any refactor of fees into core/fees.py must keep those tests passing. The benchmark docstring references .venv/bin/python3 while SKILL.md says to use plain python3 — worth verifying which interpreter is actually used in practice.

### 2026-06-03T01:04 · `feature` — Enhanced Checkout Bot — Browser Automation, Drop Monitor, and Profit Calculator
The user wants to build a comprehensive automated purchasing assistant for high-demand retail drops. The system has four primary pillars: (1) Browser automation — using a headless or visible browser to navigate to product pages, refresh on a schedule or trigger, and execute add-to-cart and checkout flows automatically. (2) Drop monitoring — continuously watching retailer sites for upcoming or surprise inventory releases to get early alerts. (3) Profit estimation — scraping eBay and TCGPlayer sold listings (prioritizing items with many weekly sales) to calculate expected resale margins. (4) Infrastructure monitoring — tracking internet connectivity and detecting changes in the target website's DOM/structure that would break the bot's selectors. The catalyst was a failed Sam's Club purchase attempt, indicating the user is targeting collectibles (likely Pokémon cards or similar) that appear on both Sam's Club and resale markets like TCGPlayer and eBay.

### 2026-06-03T01:05 · `discovery` — card-flip Project — Existing Profit Calculation and Fee Model in scripts/scan.py
The card-flip project already has a working profit model. `_net_profit` in `scripts/scan.py` computes net proceeds from a sale by deducting eBay's 13.25% FVF and 2.9% payment processing fees, then subtracting cost basis. The benchmark suite at `scripts/benchmark.py` line 326+ includes tests for expected values, breakeven (sell == cost), and linearity (profit scales proportionally with sale price). This existing infrastructure is the foundation on which the enhanced checkout bot's market profit calculator will be built — eBay and TCGPlayer price surveys will feed into `_net_profit` to estimate flip margins.

### 2026-06-03T01:05 · `discovery` — Full Fee Model in scripts/scan.py — Fixed Costs Beyond Percentage Fees
The full `_net_profit` implementation in scan.py is more comprehensive than the benchmark comments suggested. Beyond the percentage-based eBay FVF (13.25%) and payment processing (2.9%), the function deducts three fixed costs per transaction: $0.30 payment fixed fee, $4.50 outgoing shipping, and $0.55 for supplies/packaging — totaling $5.35 in fixed costs per sale. On the buy side, TCGPlayer sourcing adds $1.29 flat shipping to the card price to get `buy_landed`. The system also models a pessimistic scenario at 85% of the target sell price to stress-test flip margins. This complete cost model is the correct baseline for any profit calculator feature added to the new enhanced checkout bot.

### 2026-06-03T01:06 · `discovery` — config/fees.yaml Is a Placeholder — Fees Are Hardcoded in scan.py
The project has a `config/fees.yaml` stub that was created as a future home for platform fee schedules, but it has never been populated. All fee logic currently lives as hardcoded constants in `scripts/scan.py`. This is relevant context for the enhanced checkout bot work — if TCGPlayer seller fees or eBay FVF rates need to be added or updated for the new profit calculator feature, they will need to be added either to this yaml file (if it gets wired up) or directly to scan.py.

### 2026-06-03T01:06 · `change` — config/fees.yaml Populated — Single Source of Truth for All Fee Constants
The fees.yaml file was transformed from an empty placeholder into a fully structured fee configuration. It is now the single source of truth for all cost constants previously hardcoded in scripts/scan.py. The design enforces correctness via two mechanisms: (1) all numeric values are YAML strings to force Decimal parsing at read time, preventing silent float rounding errors; (2) an `unconfirmed` list lets tooling warn when a guess-based shipping profile is used in profit calculations. The file is organized into four sections: platform fees (eBay FVF + payment), outbound shipping profiles, per-item supplies, and inbound acquisition costs. `core/fees.py` is planned as the loader but remains unimplemented.

### 2026-06-03T02:51 · `feature` — core/fees.py — Full Decimal-Exact Fee Calculation Module Implemented
The card-flip project's core fee engine was built out from a placeholder. The module is the single source of truth for "is this flip worth it?" math, used by scripts/profit_gate.py and scripts/scan.py. All money is Decimal to satisfy the project's hard rule against float-based fee estimation. Rates are externalized to config/fees.yaml so they can be updated without touching code. The `gate()` function is the primary entry point: given a comp price, landed cost, shipping profile, supplies key, and profit floor, it returns a GateResult with full itemized breakdown, boolean pass/fail, and warnings for any unconfirmed cost estimates. `max_buy_for_floor` is highlighted in the docstring as the number you actually want at a product drop.

### 2026-06-03T02:52 · `feature` — scripts/profit_gate.py — CLI Profitability Gate Script Created
The profit_gate.py script is the human-facing entry point for the card-flip margin system. It wraps core/fees.py's gate() function with argument parsing, pretty-printed itemized output, and optional PriceCharting comp lookup. The script is designed for use at a product drop: you input your landed cost and the current eBay-sold comp, and it immediately tells you net profit, margin %, breakeven sell price, and the maximum you can pay per unit and still clear your target floor. The --selftest flag provides a trust check with 4 known-value assertions that mirror the scan.py formula, ensuring the math hasn't drifted.

### 2026-06-03T02:52 · `discovery` — profit_gate.py Selftest Passes; Booster Box Drop Example Shows $0.59 Net on $75 Comp
First live run of the profit gate confirms the math engine works end-to-end. The booster box scenario reveals that at a $75 comp with $48 landed cost, the flip nearly breaks even (net $0.59) and does not clear the $15 floor. The dominant cost is the $13 shipping estimate which is marked UNCONFIRMED — if actual shipping is lower, the math changes significantly. The max_buy_for_floor of $33.59 is the actionable number: at $75 comp, a buyer must acquire the product for $33.59 or less to net $15. This validates the tool is working as designed for drop-day purchase decisions.

### 2026-06-03T02:53 · `discovery` — scripts/pricecharting.py API Shape Confirmed for --survey Integration
Inspection of scripts/pricecharting.py confirms the existing scraper's interface is compatible with profit_gate.py's _survey_comp() function as written. The fetch_prices() return dict uses "ungraded" as the primary key for eBay-sold median price, which is exactly the first key _survey_comp() probes. The search() function handles caching and redirect validation. Since pricecharting returns floats, the Decimal(str(...)) wrapping in _survey_comp() is correct and necessary. The --survey feature should work with singles; sealed product lookups may need testing since PriceCharting's coverage of booster boxes varies.

### 2026-06-03T02:54 · `discovery` — scouts/cross_platform/spread_calc.py — TCGPlayer Low Price API Interface Confirmed
The existing TCGPlayer scraper in scouts/cross_platform/spread_calc.py provides a clean get_tcg_low() interface suitable for feeding the --survey comp lookup in profit_gate.py. It handles multi-format card codes and includes name-match sanity warnings. Since it returns floats, any integration with core/fees.py requires the same Decimal(str(...)) wrapping already present in _survey_comp(). This module can serve as a second comp source alongside PriceCharting — useful for singles where TCGPlayer market price diverges from eBay-sold median.

### 2026-06-03T02:54 · `discovery` — get_tcg_low() Return Shape and NM-Filtering Gotcha Documented
Full inspection of get_tcg_low() reveals a carefully designed NM-only price filter that avoids the "condition trap" — product.lowestPrice includes any condition listing, which would understate the true buy cost compared to NM eBay sold comps. The function ranks condition-filtered listings by true landed cost (price + shipping), taking the cheapest. For profit_gate.py --survey integration, landed_price is the correct field to use as an inbound acquisition cost estimate, while low_price serves as the raw listing price. The SHIPPING_TCG=1.29 default is used only when a seller hasn't specified shipping.

### 2026-06-03T02:54 · `discovery` — get_tcg_low() Return Dict Includes name_match_warning Field
The final return dict of get_tcg_low() includes a name_match_warning field that should be surfaced when displaying comp results in profit_gate.py's --survey output. If the TCGPlayer search matched a different card than intended, this warning string explains the discrepancy. Callers should treat a non-None name_match_warning similarly to the UNCONFIRMED shipping warnings in core/fees.py — show it prominently rather than silently using a potentially wrong price.

### 2026-06-03T02:54 · `feature` — profit_gate.py --survey Upgraded to Dual-Source Market Survey (PriceCharting + TCGPlayer)
The --survey feature in profit_gate.py was upgraded from a PriceCharting-only single comp fetcher to a dual-source market survey. The new _survey() function queries both PriceCharting (for eBay-sold median via the "ungraded" key) and TCGPlayer (for lowest NM landed price) in parallel, accumulating all warnings rather than failing fast. _resolve_survey_comp() implements the priority: eBay-sold median is preferred because that's the venue the fee math is calibrated for; TCGPlayer landed price serves as a fallback when PriceCharting has no price (common for sealed product like booster boxes). This makes the --survey flag significantly more useful for sealed product evaluation where PriceCharting coverage is sparse.

### 2026-06-03T02:55 · `feature` — profit_gate.py main() Wired to Dual-Source Survey with Comp Source Attribution
The main() function was updated to use the new dual-source survey infrastructure. The flow is: print survey status, run _survey(), display raw survey output via _print_survey() (TBD), then resolve to a single comp via _resolve_survey_comp(). A --comp flag alongside --survey acts as a manual override, bypassing the survey-derived comp while still printing the market context. The comp_source label shown in output tells the user exactly where the number came from — critical for the "never guess" design principle. _print_survey() is referenced but not yet implemented, so --survey will fail until that function is added.

### 2026-06-03T02:55 · `feature` — _print_survey() Implemented — Shows eBay/TCG Side-by-Side with Spread Multiplier
_print_survey() completes the survey display pipeline. The eBay/TCG spread ratio is particularly useful: a ratio >1 means the card sells for more on eBay than it costs to buy on TCGPlayer — the higher the ratio, the better the arbitrage opportunity. The display is designed to give the user full market context before the profit gate verdict.

### 2026-06-03T02:55 · `bugfix` — Two Bugs Found in Live Survey Run: Output Order Inverted and "Iono sv4pt5 222" Matches Nothing
The first live survey test exposed two issues. First, stdout ordering: the argparse error is printed before survey output appears in the terminal because argparse.error() calls sys.exit() after printing to stderr, but stdout buffering means the survey table appears after — visually confusing. Second, the query "Iono sv4pt5 222" fails both scrapers. PriceCharting doesn't index by set code abbreviation. TCGPlayer's _pick_best_match() found Iono cards but none matched the SV4PT5-222 code — the Paldean Fates full-art Iono (222/091) may need a different query format like "Iono 222/091" or just "Iono" with set filtering. Query format sensitivity is a usability issue for the --survey flag.

### 2026-06-03T02:59 · `discovery` — Live profit_gate.py Survey: Nami OP08-106 One Piece Card
A live survey was run against the card-flip profit analysis toolchain using the Nami OP08-106 (SP Foil) One Piece card as a test case. The script profit_gate.py fetched eBay-sold median data ($858.02) from PriceCharting and TCGPlayer low ($2.95 NM, $4.44 landed). With a simulated $10 buy, bubble mailer shipping ($4.50), single card supply ($0.55), eBay FVF ($113.69), and payment processing ($25.18), the net profit per unit is $704.10 at an 82.1% margin. The tool correctly identified this as a strong PASS. The 193× eBay-to-TCG spread signals this card has a significant arbitrage opportunity between platforms. The script's fee structure, comp sourcing logic, and floor/max-buy calculations all functioned correctly on this real card lookup.

### 2026-06-03T02:59 · `feature` — Added Implausible Spread Warning to profit_gate.py
After observing a 193× eBay-vs-TCG spread on Nami OP08-106 (a known SP Foil vs base card variant mismatch), a guard was added to profit_gate.py's _print_survey function. When the computed spread exceeds 5×, a human-readable warning is appended to the survey warnings list, alerting the user that the two data sources almost certainly matched different rarity tiers of the same card code. This prevents acting on a fabricated comp. The threshold of 5× was chosen conservatively above the real-world range of 1.3–3×. The pattern is referenced as the "SKILL.md fake-spread trap," indicating it is a catalogued gotcha in project documentation.

### 2026-06-03T02:59 · `discovery` — Implausible Spread Guard Confirmed Live on Nami OP08-106
A follow-up run verified the implausible-spread guard added to profit_gate.py fires correctly. The 193.25× eBay/TCG spread on Nami OP08-106 triggers the warning inline in the survey output. Notably the script is non-blocking — it surfaces the warning and continues with the eBay comp, leaving the final trust decision to the user. This design allows the tool to flag the likely rarity mismatch without preventing analysis on genuinely high-value SP cards.

### 2026-06-03T03:00 · `discovery` — PriceCharting fetch_prices Element ID Mapping
Code inspection of scripts/pricecharting.py reveals the exact HTML element IDs PriceCharting uses for price data. The current fetch_prices function only retrieves card-oriented price points (ungraded, grade 9, PSA 10). For sealed product support, a different element ID would need to be targeted — PriceCharting uses a "box_only_price" ID for PSA 10 equivalent, but the actual sealed/new-in-box price likely lives under a different ID (e.g. #new_price or a sealed-specific column). This research is the groundwork for implementing sealed booster box comp support in the --survey flow.

### 2026-06-03T03:01 · `discovery` — PriceCharting Sealed Products Use #used_price — fetch_prices Already Works
A live probe of PriceCharting's sealed product page structure revealed that booster box pages use the same #used_price element ID as single cards, and it contains a real eBay-sold median value ($334.47 for Pokemon 151 Booster Box). This means the existing fetch_prices function in pricecharting.py already supports sealed products — the "ungraded" field in the return dict will contain the sealed comp. No new element ID targeting is needed. The gap previously identified (sealed surveys requiring manual --comp) may not actually exist for sealed products on PriceCharting. The search() function's URL resolution pointed to the Japanese set variant, which may be worth verifying against the intended English product.

### 2026-06-03T03:01 · `discovery` — Critical: #used_price Maps to PSA 10 on English Sealed Product Pages
A second probe targeting English sealed product pages (Surging Sparks, Prismatic Evolutions ETB, Destined Rivals) revealed a critical data integrity issue: on sealed product PriceCharting pages, the #used_price element is labeled "PSA 10" in the column headers, not "Ungraded." This means the existing fetch_prices function, which reads #used_price as the "ungraded" eBay median comp, would silently return the PSA 10 graded box price for any sealed product survey. This would inflate comps significantly and cause profit_gate.py to output false PASS verdicts for sealed drops. The correct raw/ungraded sealed box price element ID has not yet been identified and requires further investigation. This is a blocking issue for sealed comp support.

### 2026-06-03T03:02 · `discovery` — Confirmed Live Bug: Sealed Survey Returns PSA 10 Price as eBay Comp
Live execution confirmed the bug: when --survey is used for a sealed booster box, profit_gate.py fetches #used_price from PriceCharting, which on sealed product pages is the PSA 10 graded box price rather than the raw eBay-sold median. For Destined Rivals Booster Box, this produces a $542.21 "comp" against a real market price closer to $80 (per TCGPlayer). The result is a wildly incorrect PASS verdict ($330 profit, 60.9% margin) on a purchase that would likely be a loss. The implausible spread warning (6.67×) does fire, but is non-blocking. Until the correct sealed page element ID is identified and fetch_prices is extended, --survey must not be trusted for sealed products without manual --comp override.

### 2026-06-03T03:03 · `refactor` — profit_gate.py _survey() refactored for sealed product awareness and region safety
The _survey() function in scripts/profit_gate.py was refactored to handle sealed product pricing differences and prevent silent region mismatches. The key rename from `ebay_median`/`ebay_url` to `pc_price`/`pc_url` reflects that PriceCharting's #used_price field serves double duty: for singles it is an eBay-sold median (strong comp), but for sealed boxes it is PriceCharting's own sealed market value which lags real eBay prices on hyped/fresh product. A `sealed` flag was added so callers can trigger sealed-specific warnings. Region detection was added because PriceCharting silently matches Japanese pages for some set queries (e.g., the bare "151" query), which would cause English box comps to be made against Japanese market prices. TCGPlayer 0-seller warning is now gated on the sealed flag since 0 sellers is more critical context for sealed drops (preorder/sold-out scenario).

### 2026-06-03T03:04 · `refactor` — _resolve_survey_comp() updated to use pc_price key and sealed-mode source label
As a follow-on to the _survey() key rename (ebay_median → pc_price), _resolve_survey_comp() was updated to reference the new key. More importantly, the function now branches on the sealed flag to return a different comp source label that warns the user to verify the PriceCharting sealed-box value against actual eBay sold listings, since that price can go stale. This makes the provenance of each comp explicit in the output rather than silently using a potentially weak price as the sell comp.

### 2026-06-03T03:04 · `refactor` — _print_survey() updated with sealed-mode display labels and split ratio thresholds
_print_survey() was overhauled to be context-aware about whether it's displaying a sealed box survey or a singles survey. The function now branches on the sealed flag for both display labels and warning logic. For sealed products, a PC/TCG ratio above 2× triggers a "stale or hype" warning because a fresh/illiquid box's PriceCharting value often lags real eBay sold prices — the user is told to verify manually. For singles the old >5× threshold (different rarity variant trap) is preserved. This means the tool now gives actionable, product-type-specific warnings rather than one-size-fits-all spread alerts.

### 2026-06-03T03:04 · `feature` — profit_gate.py gains --sealed CLI flag with auto-defaults for sealed product mode
Previously, evaluating a sealed box required manually passing --ship booster_box --supplies sealed --floor 15 every time, and the survey function had no awareness of sealed vs singles mode. The new --sealed flag sets all three defaults automatically and threads the sealed flag through to _survey(), _print_survey(), and _resolve_survey_comp() so every piece of the pipeline uses product-type-appropriate logic. This collapses the common sealed-box invocation from a five-argument command to just `--buy X --survey "..." --sealed`, while still allowing any default to be individually overridden.

### 2026-06-03T03:04 · `discovery` — profit_gate.py --sealed mode verified working; Destined Rivals box reveals stale PC comp trap
The full sealed-mode pipeline was verified end-to-end. The Destined Rivals Booster Box case is a textbook example of the stale-PC trap: PriceCharting shows $542.21 but TCGPlayer shows 0 live sellers at $79.95 MSRP, and the 6.67× ratio exceeds the 2× threshold — all three sealed-mode guards fired simultaneously. The system correctly labels the comp as untrustworthy and instructs the user to pull real eBay sold data. The booster_box shipping profile UNCONFIRMED warning also fires as expected. selftest passes, confirming no regressions from the key rename or sealed-mode additions.

### 2026-06-03T03:04 · `discovery` — Region guard and singles spread warnings both fire correctly on live queries
Two edge cases were validated against live market data. First: the bare "Pokemon 151 Booster Box" query demonstrates the exact Japanese-page trap the region guard was built to catch — PriceCharting silently routes to the Japanese Scarlet &amp; Violet 151 page, which would silently produce a wrong comp for English box buys. The warning fires and names the URL. Second: the Nami OP08-106 query shows the singles spread guard catching a 193× ratio, which almost certainly means PriceCharting matched the SP Foil alt-art ($858) while TCGPlayer matched the base version (~$4.44). Both guards are production-validated.

### 2026-06-03T03:07 · `discovery` — Project state: session-017, code repo has uncommitted changes including new profit_gate.py
Status check reveals the code repo has several uncommitted changes from the current session and prior work. profit_gate.py is a new untracked file. The target-list.md establishes important project context: singles scanning is paused (all FAIL since May 18), the workflow shifted in S016 to PriceCharting-based discovery via discover.py rather than cold eBay searches, and the strategic direction is now toward sealed product drops and/or a watchlist monitor rather than active singles scanning. The PC systematic overstatement of spreads (confirmed in S017) is the key calibration insight for interpreting any PriceCharting-sourced comp data.

### 2026-06-03T03:07 · `change` — Session 018 notes written to vault capturing profitability gate build and sealed comp tooling
The session notes formalize all work done in session 018 into the Obsidian vault. Critically, the notes document the scope boundary decision (no checkout automation) as permanent, not just deferred. The notes also capture the key honest limitation: for sealed product, a real buy decision still requires a manual eBay SOLD search feeding --comp because PriceCharting's sealed value is a weak comp. The vault record is the source of truth for what was built and what the outstanding calibration items are.

### 2026-06-03T03:07 · `change` — SKILL.md updated date to 2026-06-02 as part of session-018 wrap
Routine wrap-flow date update to SKILL.md. The body of SKILL.md still reflects the S017 state (May 18); the session-018 sealed tooling build is documented only in session-018.md for now. A fuller SKILL.md body update incorporating the profit_gate.py tool and sealed comp workflow may follow.

### 2026-06-03T03:08 · `change` — SKILL.md updated with S018 build note section documenting profitability gate tooling
The S018 build note section was prepended to the main status section in SKILL.md so that any future session that reads SKILL.md to restore context will immediately see the profitability gate tooling that was built, the scope boundary that was drawn, and the outstanding calibration items (sealed fee numbers). This is the project's primary context-restore mechanism — every session starts by reading this file.

### 2026-06-03T03:08 · `change` — Profitability gate tooling committed to card-flip repo as commit 13a7ef1
The session-018 code work is now committed to the card-flip repo. The three core files — fee math, fee config, and the CLI tool — were committed atomically. The intervention_queue.jsonl modification was left out of this commit, presumably intentional since it's a data file tracking runtime state rather than source code.

### 2026-06-03T03:08 · `change` — Obsidian vault committed with session-018 log and SKILL.md update as commit 51a6550
Session-018 wrap is complete. Both repos committed. Code repo has the new profitability tooling (13a7ef1); vault has the session log and SKILL.md context update (51a6550). The project is in a clean, resumable state for session-019.

### 2026-06-03T03:08 · `change` — Both card-flip repos pushed to GitHub after session-018 wrap
Both repositories are fully synced to GitHub. Session-018 is cleanly wrapped. The profitability gate tooling (core/fees.py, config/fees.yaml, scripts/profit_gate.py) is live on the code repo master branch, and the session log + SKILL.md update are live on the vault repo master branch.

### 2026-06-03T03:09 · `discovery` — claude-mem sync to ThinkPad (10.0.0.197) failed with scp connection closed
The end-of-session claude-mem sync to the ThinkPad (LAN address 10.0.0.197) failed. The local export step completed (294 obs, 85 sums), but the scp transfer was cut off. The ThinkPad may have been asleep, off, or on a different network segment. The memory from session-018 will not be available on the ThinkPad until a successful sync is run.

### 2026-06-03T03:09 · `discovery` — ThinkPad (10.0.0.197) is reachable with SSH port open despite earlier scp failure
The ThinkPad is up and SSH is available, so the earlier scp failure was not a connectivity issue. The high RTT variance (6ms min, 108ms max) suggests a WiFi connection with occasional spikes. The scp "Connection closed" error with the host reachable may indicate a server-side scp restriction, an SSH key issue, or a remote sshd configuration that closes the channel. A retry should work if the issue was transient.

### 2026-06-03T03:10 · `discovery` — claude-mem-sync push uses scp to /tmp then ssh python3 to import into remote SQLite DB
The sync script structure explains why the push failed silently after exporting: the scp to /tmp on the remote dropped, so the python3 import step never ran. Since SSH port 22 is open and ping works, the scp failure is likely an SSH key/auth issue or the remote sshd closes the scp subsystem specifically. The fix would be to check SSH key auth for the default user at 10.0.0.197, or add an explicit user@host in the sync call.

### 2026-06-03T03:10 · `discovery` — SSH auth to ThinkPad works fine; remote claude-mem.db exists and was last modified Jun 2 13:20
SSH key auth to the ThinkPad works correctly, and the remote claude-mem database exists and is accessible. The earlier "scp: Connection closed" failure was likely a transient network hiccup given the high RTT variance observed (WiFi). A simple retry of the claude-mem-sync push should complete successfully.

### 2026-06-03T03:10 · `change` — claude-mem sync to ThinkPad succeeded on retry; 92 new observations and 14 new summaries imported
The retry confirmed the earlier scp failure was a transient WiFi issue. The ThinkPad was 92 observations and 14 summaries behind — roughly the backlog since the last successful sync. Both machines now have the same claude-mem state including all session-018 observations.
