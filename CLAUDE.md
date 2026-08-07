# Obsidian Second Brain — Claude Context

This directory holds Donovan's Obsidian vaults. Read this first every session
to understand the layout and how to work in it.

## Vault layout (restructured 2026-07-05, for OpenClaw access split)

The vault was split so an external agent (OpenClaw) can be pointed at
day-to-day reference vaults while journal/health/daily/identity-linked
content stays fully walled off in a private vault no AI ever touches.

- **`personal/`** (docs call it `personal-private/`; on-disk rename still
  pending) — Scope updated 2026-07-15 by Donovan: AI may **read** this vault
  EXCEPT `Journal/`, `Daily/`, `Work/`, `Private-Reference.md`, and anything
  identity-, location-, or social-life-related. Writes remain hook-blocked
  vault-wide (Health allowlist exception unchanged — see AI scope below).
  OpenClaw is still never pointed here.
- **`learning/`** (renamed from `personal/`) — School, Japanese, Entertainment
  (factual lookups only). AI-accessible. Its GitHub remote is still named
  `personal-vault` (private repo) — rename pending, ask before touching.
- **`ai-improvement/`** — Claude/Jarvis workflow notes, prompts, MCP/tool
  config, capability scouting across devices. AI-accessible.
- **`finance/`** — card-flip and trading cross-vault notes (ops vaults for
  card-flip live in their own separate repo). Exact dollar figures are kept
  in `personal-private/Private-Reference.md`, not here. AI-accessible.
- **`pytheas/`** — Notes for the Pytheas AI assistant project (retired the
  `jarvis/` vault 2026-07-29; Courses, Research, Briefings, and
  `pytheas-memory.md` all live here now). Source code lives at
  `~/code/pytheas`. Contains symlinks `code/` → `~/code` and
  `learning-vault/` → `../learning` (never symlinked to `personal-private/`).
  AI-accessible.
- **`agonizing-sentience/`** — Public, collaborative novel project with a
  friend. Donovan and his friend are the only voices here. Private scratchpad
  now lives in `personal-private/agonizing-sentience-scratchpad/`.
- **`card-flip/`** — Private (for now). TCG card-flipping business ops vault
  (SOPs, scanner, flip logs) — separate from `finance/card-flip/`'s
  cross-vault notes.
- **`minecraft-event/`** — Private. Donovan's **solo** vault for the custom
  Minecraft Java server event + YouTube project (1,000-player permadeath, nine
  fragments). It's a markdown-only **mirror** of the shared crew repo at
  `~/minecraft-event` (under `reference/`) plus his own `Inbox/`, `Log/`,
  `Research/`. The shared repo (with plugin code) is the source of truth; this
  vault is mirror + personal notes. AI scope: normal collaborative writing in
  the solo notes is fine; the `reference/` mirror is generated, not hand-edited
  here — change those docs in the shared repo and re-sync.

## Conventions

- **Daily-style notes use ISO dates: `YYYY-MM-DD.md`.**
- **Each major area has a `Home.md`** as its entry point.
- **AP Chem's unit structure is the template** for school subjects:
  `Unit N/Unit N Notes.md`, `Unit N Examples.md`, `Unit N Progress Check.md`,
  with images under `Images/Unit N/`. Don't replicate it preemptively into
  stub subjects — only when actively building them out.
- **Numbered prefixes** (`01 - Favorites/`, `02-strategy.md`) signal reading
  order. Preserve them.
- Don't invent new top-level vaults without asking.

## How to work here

- **Ask, don't assume (standing rule, 2026-07-28, until Donovan says stop):**
  whenever something in a request isn't entirely understood, or a judgment
  call comes up mid-work (naming, scope, defaults, trade-offs), ask Donovan
  to clarify before proceeding — batch questions where possible instead of
  interrupting repeatedly.
- **Manual approval for edits.** Donovan reviews changes before they land.
  Show diffs or drafts before saving non-trivial edits.
- **Add files freely. Remove empty folders freely. Editing or deleting files
  needs approval each time.**
- **Cross-vault context is the point.** Reference notes from any vault when
  relevant — that's why the mega-vault exists.
- **Don't fabricate.** If you don't know a card's price, an AP Chem formula,
  what happened on a specific date — say so.
- **Don't preemptively unify naming across vaults.** Each is internally
  consistent; that's enough.
- **`ai-improvement/North Star.md`, `Gotchas.md`, `Key Decisions.md`** —
  check these for current priorities, known pitfalls, and why past calls
  were made, before assuming or re-deriving.
- **Prompt logging (standing, 2026-08-02):** every substantive prompt gets
  saved as a file in the vault it relates to, under a `Prompts/` subfolder
  (e.g. `pytheas/Prompts/`, `learning/Prompts/` — never `personal-private/`
  beyond the existing Health exception). Each file includes the prompt
  itself, auto-generated tags, the AI model/tool used, and the result.
  Mega/vision-scale prompts (multi-workstream, roadmap-shaping) get tagged
  `mega-prompt` and cross-linked into the relevant roadmap doc.
- **Usage monitor (standing, 2026-08-02, tightened same day after it got
  missed once):** run `ccdash` (Bash) **every single response, no
  exceptions, before the final message is sent** — not "when relevant,"
  not "after every prompt" as a soft goal. Append the current 5h/7d
  percentages to the end of the response once either crosses a new 15%
  threshold since it was last reported (e.g. 60%→75%→90%), and always
  report immediately once either gauge is ≥85%, regardless of the 15%
  cadence. This already failed once (2026-08-02: 5h hit 92% before it was
  flagged) — treat that as the reason this is written this bluntly, not
  boilerplate. Real fix, not yet built: a Stop/PostToolUse hook in
  `settings.json` (see the `update-config` skill) that surfaces this
  automatically instead of relying on remembering a chat instruction —
  queued, build next time it comes up.
- **Check usage before/during long work too, not just per-response
  (added 2026-08-02):** before starting a long research pass or
  multi-step project, and again partway through if it's running long,
  run `ccdash` — don't wait until the end to discover it's already high.
- **Push cadence (standing, 2026-08-02):** once a session has added a
  meaningful amount of new content/changes to a vault repo (several new
  files or a substantial edit pass — use judgment, not a hard count),
  commit and push that vault without waiting to be asked. Exception: once
  usage (5h or 7d) is low, ask before pushing rather than doing it
  automatically — "low" here means the same territory where you'd
  otherwise be flagging a usage warning, so treat it as paired with the
  usage-monitor rule above, not a separate threshold to track. Note:
  `~/Documents/Obsidian` itself (this file's location) is NOT a git repo
  — there is nowhere to push CLAUDE.md changes to; only the sub-vaults
  (`pytheas`, `ai-improvement`, `learning`, `finance`, `card-flip`, etc.)
  have their own repos.
- **Each sub-vault has its own `.obsidian/`.** A plugin installed in one
  vault (e.g. `ai-improvement`) is not available in another — installing
  into multiple vaults means copying the built plugin into each one's
  `.obsidian/plugins/` and enabling it in `community-plugins.json`.

## AI scope per area (important)

- **`personal/`** (`personal-private/`) — **Read access granted 2026-07-15**
  except `Journal/`, `Daily/`, `Work/`, `Private-Reference.md`, and any
  identity/location/social-life content — treat those as walled off; when
  unsure whether a note is personal-life, don't open it. No AI writes
  anywhere in this vault.
  **Write block enforced, not just stated:** `~/.claude/hooks/private-vault-guard.py`
  (a PreToolUse hook on Write/Edit) hard-blocks writes into `personal/` or
  `personal-private/` except paths listed in
  `~/.claude/hooks/private-vault-allowlist.txt` (currently just `Health` —
  a standing, explicitly scoped exception, not a general license). Granting
  a new exception means editing that allowlist file, not just saying so in
  chat.
- **`agonizing-sentience/`** (public) and
  **`personal-private/agonizing-sentience-scratchpad/`** — Organize, edit,
  polish only. Do NOT write prose, plot, dialogue, or creative content unless
  explicitly asked. The writing is Donovan's and his friend's.
- **`learning/Entertainment/`** — Limited AI. Factual lookups (release
  dates, runtimes, cast) and organization fine. Don't write reviews or
  opinions in his voice.
- **`learning/School/`**, **`ai-improvement/`**, **`finance/`**, **`pytheas/`**,
  **`card-flip/`** — No restriction stated; normal collaborative writing is
  fine.

## Active context (as of 2026-07-05)

- Donovan is a **junior**, going into senior year 2026-2027.
- AP Chem prep is the highest-priority work in `learning/School/`.
- card-flip is an active operation — daily logs are real data.
- agonizing-sentience: Chapter 3 in progress. Brainstorming/plans expanding.
- OpenClaw is being wired up against `learning/`, `ai-improvement/`,
  `finance/`, `pytheas/` — never `personal-private/`.

## What this vault is for

A second brain. Daily life, school, hobbies, business, creative work — all
in one place so connections between them are visible. Help organize,
recall, and connect; don't replace Donovan's thinking.

## Session memory & sync

**At session end (automatic):** if meaningful work was done (any tool use,
edits, discoveries, or decisions), record it via claude-mem using
`observation_record_event`. Skip only if the session was trivially short
(e.g. a single question with no vault changes).

**On-demand sync keyword:** when Donovan says `sync mem [device]`, push
claude-mem to that device:

```
~/.claude/plugins/marketplaces/thedotmack/scripts/claude-mem-sync push <ip>
```

Known devices: see `personal-private/Private-Reference.md` for IPs.

If the push fails, report the error. Do not auto-sync on session end.

**Mirror sync keyword:** when Donovan says `sync mc-mirror`, refresh the
`minecraft-event` vault's `reference/` mirror from the shared crew repo:

```
~/Documents/Obsidian/minecraft-event/sync-reference.sh
```

Markdown-only, with `--delete` (tracks upstream deletions). Report the file
count it prints. Do not auto-sync.
