# Claude Improvement Master Notes

> Compiled from 22 video reels + 39 screenshots, all saved from Instagram.
> Sources noted as `[filename]` or `[@handle]`. Where multiple sources say the same thing, it's flagged.

---

## TL;DR — Top High-Impact, Actionable Tips

1. **Build a CLAUDE.md Gotcha Section**: Log every annoying behavior Claude repeats (creates files instead of editing, wraps in try/catch, uses deprecated APIs). Skill accuracy goes from 40% → 98% as you add gotchas. `[7618652355948465438]`
2. **Don't railroad Claude**: Give context + constraints, let Claude decide *how*. Tight micro-management degrades output. `[7618652355948465438]`
3. **Load context on demand**: Upfront context loading uses 80% of the window; progressive/on-demand loading uses 35%. More context *available* = better output — but don't dump it all at once. `[7618652355948465438]`
4. **Use the "Second Brain Prompt"** to have Claude build a personal context vault in Obsidian — interview-style, with an INDEX routing file. Then on every future task, Claude reads index first, loads only relevant files. `[DZnBNLSzatH]`
5. **Anti-sycophancy system prompt**: Use a 7-rule advisor prompt with `[Certain]`/`[Likely]`/`[Guessing]` confidence tags to get honest, pushback-enabled responses. `[DZFZovEma9h]`
6. **The perfect prompt formula**: Context + Content + Constraints + Command (+ examples). `[DYCROzYExar]`
7. **Graphify**: Install `graphify claude install` in your codebase to pre-build a knowledge graph. Claims 10x faster code search and 7x fewer tokens. `[DYnPUfru7aw, DYzrTT7u5TN]`
8. **Claude Code 10-level skill tree**: Terminal → CLAUDE.md → Commands → Custom Commands → Skills → MCP → Subagents → Hooks → Headless → Routines. Know which level you're on. `[DZ_RLROIFoq]`
9. **Claude + Obsidian OS**: Build an 8-folder Obsidian vault (Capture / Active / Resources / System / Generated / Queue / Calendar / Archive). Put your context in `4-System/Claude.md`, outputs go to `5-Generated/`. Use Cowork scheduled tasks for weekly reviews. `[DZJdPGmvmWl]`
10. **Skills with gotchas are self-improving**: SKILL.md contains main prompt + scripts/ + references/ folders. Each run that hits a new gotcha improves the next run automatically. `[7618652355948465438]`

---

## 1. Claude Code Configuration & CLAUDE.md

### 10 Levels of Claude Code Mastery
**Source**: `[DZ_RLROIFoq]` (@itsnextwork)

Progression from beginner to expert:
1. **Terminal** — Basic CLI usage
2. **CLAUDE.md** — Project instruction file that Claude reads at session start
3. **Commands** — Built-in slash commands: `/clear`, `/compact`, `/context`
4. **Custom Commands** — User-defined slash commands stored in the project
5. **Skills** — Reusable prompt modules with their own file structure
6. **MCP** — Model Context Protocol servers for external integrations
7. **Subagents** — Spawning parallel Claude instances for subtasks
8. **Hooks** — Shell commands that run on events (pre/post tool use, etc.)
9. **Headless** — Running Claude Code without interactive UI (scripted/automated)
10. **Routines** — Scheduled or chained automation sequences

### Build a Gotcha Section in CLAUDE.md
**Source**: `[7618652355948465438]`

One of the highest-leverage Claude Code improvements. Create a `gotchas.md` file (or section in CLAUDE.md) listing behaviors Claude repeatedly gets wrong on your project:
- Creates new files instead of editing existing ones
- Wraps everything in try/catch
- Uses deprecated APIs
- Over-comments code
- Breaks naming conventions

**Why it works**: Each time you add a gotcha, skill accuracy improves on subsequent runs:
- v1: 40% accuracy, 8 errors
- v2: 60% accuracy, 5 errors
- v3: 85% accuracy, 2 errors
- v4: 98% accuracy, 0 errors

"Add gotchas → skill improves automatically."

### SKILL.md File Structure
**Source**: `[7618652355948465438]`, `[DYsW6ZNDQdq]` (@charliehills)

Each skill has a directory containing:
- `SKILL.md` — Main prompt / instructions
- `scripts/` — Automation scripts Claude can call
- `references/` — Docs, specs, API references

The "caveman" skill mentioned by @charliehills cuts token usage by 65%.

### Don't Railroad Claude
**Source**: `[7618652355948465438]`

There's a spectrum from **Rigid** (micromanage every step) → **Balanced** → **Loose** (let Claude decide everything).

Best practice: **Give context + constraints. Let Claude decide how.**

Overly prescriptive prompts limit Claude's ability to find the best solution. Define the *what* and *why*, not the *how*.

### Load Context On Demand, Not All Upfront
**Source**: `[7618652355948465438]`

- Loading everything at context start: **80% of window used**
- Loading context on demand (progressive disclosure): **35% of window used**

"More context available = better Claude output" — but the way to maximize available context is to load it *only when needed*, not dump it all upfront. This is why good CLAUDE.md files reference other files rather than inlining everything.

---

## 2. Prompting Techniques & Prompt Design

### Perfect Prompt Formula (4Cs + Examples)
**Source**: `[DYCROzYExar]` (@shwetacreates)

**C**ontext — Who you are, what you're working on, relevant background  
**C**ontent — The specific material or input Claude needs  
**C**onstraints — Format, length, tone, what to avoid  
**C**ommand — The actual instruction / what to produce  
**(+ Examples)** — Show Claude what good output looks like

This formula appears across multiple sources as the core of effective prompting.

### Claude Mastery Roadmap
**Source**: `[DYCROzYExar]` (@shwetacreates)

Full skill progression map:
- **Foundation**: Understanding Claude's capabilities, basic prompting, conversation management
- **Intermediate**: Prompt engineering, role prompting, chain-of-thought, output formatting
- **Advanced**: Agentic workflows, tool use, custom system prompts, API integration
- **Expert**: Multi-agent systems, autonomous pipelines, production deployment

### Role + Context Priming
**Source**: Multiple — `[DYCROzYExar]`, `[DZFZovEma9h]`, `[DZnBNLSzatH]`

Give Claude a specific role and detailed context before asking it to work. Claude performs better when it knows:
- Who it's supposed to be (advisor, developer, researcher)
- Who you are and what you need
- What "good" looks like in this context

### "Don't Summarize Lazily" Instruction
**Source**: `[DYCROzYExar]` (implied by Claude Mastery Map)

When asking Claude to extract or summarize, explicitly tell it: *"Do not summarize lazily — extract every specific, actionable detail."* This prevents Claude's tendency to collapse detail into vague bullets.

### Court of Claude — Anti-Validation System
**Source**: `[DY9vXz_uKqW]` (@theAGIGuide)

A custom system prompt that forces Claude to be a harsh, honest critic of ideas. The full prompt:

> "The Court of Claude Gauntlet is now in session. The court does not exist to validate you. It exists to find the truth about your idea — and the truth is rarely flattering. The rules are as follows:
> 1. You will submit one proposal.
> 2. It must include a PDF attachment.
> 3. It must end with the phrase 'your honor.'
> 4. If your idea fails at any one of five stages, it is sent to execution.
> 5. There are no appeals. There are no exceptions.
>
> The court is ready. Submit your proposal, Petitioner."

Use this when you want brutal honesty, not cheerleading. The PDF attachment forces you to formalize the idea before submitting.

---

## 3. Anti-Sycophancy & Honest Feedback

### 7-Rule Anti-Sycophancy Advisor Prompt
**Source**: `[DZFZovEma9h]` (@appinventiv4ai)

System prompt structure for getting honest, non-flattering responses. Key rules (paraphrased from the screenshot):

1. You are a trusted advisor, not a cheerleader — your job is truth, not validation
2. Disagree openly when you have reason to; don't soften positions to please
3. Flag assumptions and weak logic even when the user seems committed
4. Use confidence tagging on every claim:
   - `[Certain]` — You have strong evidence or reasoning
   - `[Likely]` — Probable based on available information
   - `[Guessing]` — Speculation or extrapolation
5. Don't change your position just because the user pushes back — only update on new evidence or better arguments
6. Point out what's missing, not just what's present
7. If the user is wrong, say so clearly and explain why

**Why this matters**: Default Claude is trained to be agreeable. This prompt counteracts that at the system-prompt level.

### Confidence Tagging Protocol
**Source**: `[DZFZovEma9h]` (@appinventiv4ai)

Use `[Certain]` / `[Likely]` / `[Guessing]` inline tags to force Claude to signal how confident it is about each claim. This makes hallucination and speculation immediately visible rather than buried in fluent-sounding prose.

---

## 4. Memory & Context Management

### AI Second Brain Prompt (Full System)
**Source**: `[DZnBNLSzatH]`

This is the most complete "build Claude a permanent memory" system found in the collection. Full prompt to paste into Claude:

> "I want you to build a personal context system that holds all the important parts of my life, so you always know the right background for anything I ask.
>
> **Step 1 — Set up the structure.** Create a folder structure with one top-level folder for each major area of my life. Start with these and adjust based on my answers: Work/Career, Projects, Finances, Health, Learning, Personal/Relationships, and Goals. Inside any area that is complex, create subfolders (for example Projects could have one subfolder per project).
>
> **Step 2 — Interview me.** Before filling anything in, ask me a lot of questions to gather the important details for each area, a few at a time so it's not overwhelming. Use anything you already know about me, but do not assume. Keep asking until you have enough to fill each file out in real detail.
>
> **Step 3 — Build the files.** Turn my answers into clean, organized markdown files, one topic per file, written so a future version of you could read them and instantly understand my situation. As you write each file, finish it with a short "Related" section that links to its related notes using Obsidian wiki links like `[[note-name]]` (the exact file name, without .md). Add these links the moment you create each file, not as a separate pass at the end, so the vault is connected from the start.
>
> **Step 4 — Create an index.** Create an INDEX file at the top that is a routing table: for any type of question I might ask, it says exactly which file(s) you should open. Read this index first on every task, then load only the relevant files."

Used via Claude.ai Cowork. Results in an Obsidian vault with a graph-linked second brain.

### Obsidian OS Vault Structure for Claude
**Source**: `[DZJdPGmvmWl]`

8-folder Obsidian vault designed to work as a personal OS with Claude:

| Folder | Purpose |
|--------|---------|
| `1-Capture` | Raw dump — no organizing, no decision-making. Just get it in. |
| `2-Active` | In-progress tasks and projects |
| `3-Resources` | Reference material |
| `4-System` | Claude context files + system instructions |
| `5-Generated` | Claude output files (Morning-Briefing.md, Weekly-Review.md, etc.) |
| `6-Queue` | Backlog / things to process |
| `7-Calendar` | Time-based notes |
| `8-Archive` | Done/inactive material |

**Key file**: `4-System/Claude.md` — structured as:
```
ABOUT ME
Name: [your name]
Role: [your role]

ACTIVE PROJECTS
- [Project name]: [status] | Last Updated: [day]

PRIORITIES THIS WEEK
- [Priority 1]
- [Priority 2]
```

This file "tells Claude everything about your life" and gets read at the start of every Cowork session.

### Morning Briefing Prompt (Obsidian OS)
**Source**: `[DZJdPGmvmWl]`

```
Read my Claude.md file in the 4-System folder. Write a morning briefing with the single most important task for today and my top 3 priorities in order. Keep it under 100 words. Save the output as a new file called Morning-Briefing.md inside the 5-Generated folder.
```

**Priority check variant**:
```
Read my Claude.md file in the 4-System folder. Based only on what is inside that file, tell me the single most important thing I should work on right now.
```

### Claude + Obsidian Knowledge Base (Knowledge Vault Workflow)
**Source**: `[DXBCWkwj8vG]`

Build a searchable, AI-queryable knowledge base from all your saved content:

1. Create project directory with:
   - `raw-sources/` — Drop everything here: book notes, articles, podcasts, meeting transcripts, research papers. Don't organize, just dump.
   - `wiki/` — Claude writes organized, linked notes here
   - `assets/` — Images, attachments
2. Write a `CLAUDE.md` describing the structure
3. Give Claude this command: *"Read everything in raw-sources/ and write an organised wiki. Group by theme. Link related notes. Don't lose any ideas — just structure them."*
4. Claude reads all 11+ files, extracts themes, and builds linked wiki pages
5. Then ask: *"Write a briefing on [topic] — pull from everything in my vault"* → get answers **with citations** from specific source files

**Key insight**: "Articles saved that you never reopen" become queryable knowledge. Your second brain grows every time you use it. Build once, use forever.

**Context stat shown**: Vault with 8 wiki pages + 16 raw sources + 8 pages — all connected, all searchable.

### Claude x Obsidian = Unlimited Memory
**Source**: `[DYpsvyDu2by]`

General concept (less detailed than others): Use Obsidian as Claude's external memory by pointing it to specific files. Key mechanics:
- Give Claude the "correct file" as context for each task
- Obsidian wiki links (`[[note-name]]`) let Claude navigate between notes
- The vault acts as persistent memory across conversations

---

## 5. Skills, Subagents & Claude Code Workflows

### Parallel Subagents
**Source**: `[DVUJeahgMMe]`

Claude Code can spawn multiple subagents running simultaneously on independent subtasks. Example shown: `backend-architect` and `frontend-developer` agents running in parallel, each handling their domain, with results merged.

This dramatically speeds up complex multi-part work — instead of serial "do A, then do B", you get concurrent execution.

### Subagent Architecture (Fable 5 OS)
**Source**: `[DZiQ7GZnjR7]` (@chase.h.ai)

5-step system for a personal AI operating system using Claude Fable 5:
1. **Skill architecture** — Define modular, reusable skills
2. **Obsidian Vault memory** — Persistent memory via vault (see above)
3. **Local voice** — Voice interface layer
4. **V.A.U.L.T. HUD** — Visual interface/dashboard
5. **Bundle/ship/reskin** — Package and distribute the system

### Claude Code's "Bypass Permissions" Mode
**Source**: `[DZI1_0xgtQI]`

Visible in Claude Code UI: a "Bypass permissions" toggle. When enabled, Claude Code doesn't ask for approval before running commands. Used in the stock trading automation demo with Opus 4.7 on Max plan.

**Use case shown**: Claude autonomously used PowerShell to access the Alpaca paper trading API, placed orders, set up a monitoring pipeline, and scheduled a recurring daily task — all without step-by-step approval.

### Weekly Review Auto-Run (Cowork Scheduled Tasks)
**Source**: `[DZJdPGmvmWl]`

Claude.ai Cowork supports **Dispatch** (scheduled tasks). Set up a weekly review that runs automatically:
- Reads your `4-System/Claude.md` and active notes
- Generates "3 Things Accomplished This Week" + "3 Things to Focus on Next Week"
- Saves output to `5-Generated/Weekly-Review.md`
- "Runs by itself every week"

---

## 6. MCP Servers & External Integrations

### MCP Servers List
**Source**: `[DYsW6ZNDQdq]` (@charliehills), `[DZ_RLROIFoq]` (@itsnextwork)

MCP (Model Context Protocol) servers extend Claude Code with external tool access:
- **GitHub** — Repository operations, PRs, issues
- **Slack** — Messaging and channel integration
- **Notion** — Database and page management
- **PostgreSQL** — Direct database queries
- **Google Drive** — File access and editing
- **Figma** — Design file access
- **Linear** — Project management
- **Stripe** — Payment and subscription data
- **Perplexity** — Web search
- **Zapier** — Workflow automation

### Hooks (Claude Code)
**Source**: `[DZ_RLROIFoq]` (@itsnextwork)

Hooks are shell commands that Claude Code runs automatically in response to events:
- Pre-tool use (before Claude takes an action)
- Post-tool use (after an action completes)
- Session start/end
- Custom triggers

Use hooks to: auto-format code, run tests after edits, log activity, enforce safety checks.

---

## 7. Research & Writing Workflows

### NotebookLM + Claude Research Workflow
**Source**: `[DZ7UZVlifpX]` (@techwith.ram)

4-step workflow for grounded, hallucination-resistant research writing:
1. **Gather sources** in NotebookLM (upload PDFs, articles, etc.)
2. **Extract key findings** from NotebookLM's AI-generated summary
3. **Pass findings to Claude** with explicit source citations
4. **Have Claude write** — but grounded in NotebookLM's verified extractions, not its own training data

This hybrid approach combines NotebookLM's source-anchoring with Claude's superior writing output.

### Knowledge Base Query Workflow
**Source**: `[DXBCWkwj8vG]`

Once your knowledge vault is built:
- Ask open questions: *"What does my vault say I'm missing about [topic]?"* — Claude identifies knowledge gaps
- Get cross-note synthesis: *"Write a briefing on [topic] — pull from everything in my vault"* — outputs with citations showing exactly which source files were used
- Identified gaps example from video: energy management, context switching cost quantification, systems for capture

---

## 8. Tools & Third-Party Extensions

### Graphify
**Source**: `[DYnPUfru7aw]`, `[DYzrTT7u5TN]`

A codebase knowledge graph tool that pre-indexes your code so Claude doesn't need to re-read everything on each prompt.

**Install**: Run once in your project, then run `graphify claude install`

**Supported AI assistants**: Claude Code, Codex, OpenCode, GitHub Copilot CLI, VS Code Copilot, Aider, OpenClaw, Factory Droid, Trae, Trae CN, Cursor, Gemini CLI

**Claimed performance gains**:
- 10x faster code search
- 7.0x fewer tokens used
- "Searching 10x faster, 70x less token usage"

**How it works**: Reads your whole codebase once, builds a dependency and relationship graph. Subsequent AI queries navigate the graph instead of scanning files.

**GitHub**: github.com/safishamsi/graphify | Y Combinator S26 | 1M+ downloads

### Odysseus
**Source**: `[7647133916331052304]`

Local-first, privacy-first self-hosted AI workspace. Alternative to cloud-based Claude.ai. Features:
- Chat
- Agent
- Cookbook (saved prompts/workflows)
- Deep Research
- Compare (model comparison)
- Documents
- Notes

Relevant for users who want local AI with Claude-quality output without sending data to Anthropic.

---

## 9. Model Selection & Plans

### Claude Model IDs (Current)
**Source**: `[DZ5XRhMCn7F]`

Official model string identifiers:
- `claude-fable-5` — Claude Fable 5 (latest flagship)
- `claude-opus-4-8` — Opus 4.8
- `claude-sonnet-4-6` — Sonnet 4.6
- `claude-haiku-4-5-20251001` — Haiku 4.5

### Claude Max Plan
**Source**: `[DYnPUfru7aw]`

- **Price**: From $100/month (billed monthly)
- **Usage**: Up to 20x more than Pro
- **Best for**: Claude Code & Cowork power users
- **Perks**: Early access to advanced Claude features, higher output limits for all tasks, priority access at high traffic times

### When to Use Which Model
**Source**: `[DZ5XRhMCn7F]`, `[DZI1_0xgtQI]`

- Opus 4.7/4.8 — Used for autonomous long-running tasks (stock trading automation demo used Opus 4.7 on Max)
- Sonnet 4.6 — Balance of speed and capability for everyday Claude Code work
- Haiku 4.5 — Fast, cheap, for high-volume or simple tasks

---

## 10. Privacy & Digital Footprint Removal

### 6-Step Digital Footprint Removal Workflow
**Source**: `[DYXfI89GTDp]` (@airesearches), `[DZiHGBEQKYl]` etc. (@RAYCFU)

Mentioned across multiple sources — data broker removal was a common use case:

1. **Audit**: Prompt Claude — *"Search my name [Name] + [City, State] and list every data broker, people-search site, and public record database likely to have my info."*
2. **Build tracking spreadsheet**: Have Claude create an opt-out tracking sheet with columns for site name, opt-out URL, method, date submitted, confirmation
3. **Write opt-out emails**: Claude drafts CCPA opt-out requests, GDPR data deletion requests, KVKK (Turkish data law) requests for international sites
4. **Find direct opt-out pages**: *"Find the direct opt-out page or privacy request form for [site name]"*
5. **Dead account deletion**: Have Claude draft deletion request emails for old accounts
6. **Social media privacy audit**: Claude reviews each platform's privacy settings and flags what's exposed

**Claimed result**: 80% of digital footprint scrubbed in under 90 minutes using reusable prompts.

**Legal frameworks Claude can draft for**:
- CCPA (California Consumer Privacy Act)
- GDPR (EU General Data Protection Regulation)
- KVKK (Turkish data protection law)

---

## 11. Real-World Use Case Demonstrations

### Stock Trading Automation
**Source**: `[DZI1_0xgtQI]`

Claude Code + Alpaca paper trading API + Bypass permissions mode:
- Used Google Search AI to research political trading patterns
- Chose to mirror Jerry Moran's disclosed portfolio: GOOG + BRK.B ($10k each, $20k of $50k budget)
- Claude used PowerShell to access Alpaca paper trading API
- Placed paper orders, confirmed they queued for next market open
- Built daily monitoring pipeline that emails summaries of new STOCK Act filings
- Scheduled recurring task at correct timezone-adjusted time
- Full autonomous workflow — Claude caught its own timezone error and corrected it

**Model used**: Opus 4.7 on Max plan

### Life Audit Prompt (via Notion + Claude)
**Source**: `[DXBCWkwj8vG]` (brief glimpse)

Shown as an article titled "How to Fix Your Life in 1 Prompt" — a comprehensive psychological self-audit prompt covering identity, habits, career, health, relationships, daily routine. Paste it into Claude and answer every question.

---

## 12. Claude.ai Interface Tips

### Cowork (Projects + Tasks in Claude.ai)
**Source**: `[DZnBNLSzatH]`, `[DZJdPGmvmWl]`

Claude.ai Cowork is the project management view visible in several videos:
- Left sidebar: New task, Projects, Scheduled, Live artifacts, Dispatch (Beta), Customize
- Progress panel on right shows task steps as checkboxes
- Context panel shows which files/tools Claude used
- "Dispatch" enables scheduled/recurring tasks that run automatically
- Supports multiple concurrent tasks
- Task names visible in sidebar (e.g. "Personal context system", "Life context system setup", "Folder creation", "Customize Claude to your role")

### Cloud Environment vs Local Worktree
**Source**: `[DYnPUfru7aw]`

In Claude.ai's code interface, there's an environment selector:
- **Local worktree** — Uses your local filesystem
- **Cloud Environment** — Runs code in an isolated cloud container

Also shows quick-start prompts: "Create or update my Claude.MD file", "Search for a TODO comment and fix it", "Recommend areas to improve our tests"

---

## 13. Miscellaneous Observations

### Andrej Karpathy Joined Anthropic
**Source**: `[DYzrTT7u5TN]`

As of May 19, 2026 — Andrej Karpathy (formerly OpenAI, Tesla) announced joining Anthropic. Tweet had 27M views, 149K likes. Relevant context for why Claude's capabilities are accelerating.

### Language Learning via AI (Tangential)
**Source**: `[DYiV_ohMdx3]`

Not directly about Claude — about comprehensible input as a language learning method (how intelligence agencies train agents to learn Japanese fast). Fringe relevance: same principle applies to learning Claude — immerse in usage, don't study theory.

---

## Source Index

| File | Creator / Handle | Topic |
|------|-----------------|-------|
| `DZ_RLROIFoq.jpg` | @itsnextwork | 10 Levels of Claude Code |
| `DZFZovEma9h.jpg` | @appinventiv4ai | Anti-sycophancy 7-rule prompt |
| `DYCROzYExar.jpg` | @shwetacreates | Claude Mastery Map + 4C prompt formula |
| `DYXfI89GTDp.jpg` | @airesearches | Digital footprint removal workflow |
| `DYsW6ZNDQdq.jpg` | @charliehills | Claude Code plugins + skills + MCP |
| `DZiQ7GZnjR7.jpg` | @chase.h.ai | Fable 5 OS 5-step architecture |
| `DZ7UZVlifpX.jpg` | @techwith.ram | NotebookLM + Claude research workflow |
| `DZiH*.mp4` | @RAYCFU | Digital footprint removal prompts (series) |
| `7647133916331052304.mp4` | Unknown | Odysseus local AI workspace |
| `DVUJeahgMMe.mp4` | Unknown | Parallel subagents demo |
| `DZ5XRhMCn7F.mp4` | Unknown | Claude Fable 5 model strings |
| `7618652355948465438.mp4` | Unknown | CLAUDE.md gotchas, skills, context management |
| `DXBCWkwj8vG.mp4` | Yellow shirt guy | Knowledge base vault with Claude Code |
| `DYiV_ohMdx3.mp4` | Curly hair guy | Language learning (off-topic) |
| `DYnPUfru7aw.mp4` | @Charlieautomates (?) | Graphify + Claude Max + Cloud Environment |
| `DYpsvyDu2by.mp4` | Unknown teen | Claude x Obsidian unlimited memory |
| `DYzrTT7u5TN.mp4` | @Charlieautomates (?) | Graphify deep dive + Karpathy news |
| `DZI1_0xgtQI.mp4` | Unknown | Stock trading automation with Claude Code |
| `DZnBNLSzatH.mp4` | Unknown (glasses teen) | Full Second Brain Prompt + Claude.ai Cowork |
| `DY9vXz_uKqW.mp4` | @theAGIGuide | Court of Claude idea-validation system |
| `DZJdPGmvmWl.mp4` | Ray (obey shirt) | Obsidian OS: 8-folder system + daily/weekly automation |
| *(remaining screenshots)* | Various | See individual entries above |

---

*Last compiled: 2026-06-28*
