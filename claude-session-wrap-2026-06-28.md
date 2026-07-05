---
date: 2026-06-28
tags: [claude, session-wrap, action-plan]
---

# Claude Session Wrap — 2026-06-28

## What happened

Analyzed 22 MP4 reels + 39 JPG screenshots saved from Instagram, all about improving Claude usage. The yt-analysis MCP only accepts YouTube URLs so pivoted to ffmpeg frame extraction + Claude multimodal image reading. Compiled everything into:

- [[claude-improvement-notes]] — master reference, 13 themed sections, TL;DR top 10, full source index

---

## Action plan (ranked by impact)

### Do immediately

**1. Add a `[Gotchas]` section to CLAUDE.md**
Log every behavior Claude repeats that's wrong for your workflow. Accuracy progression documented: 40% → 60% → 85% → 98% across 4 iterations. Each gotcha you add automatically improves the next run.

**2. Install Graphify in active code repos**
- Repo: `github.com/safishamsi/graphify` (YC S26)
- One-time: run in project root, then `graphify claude install`
- Claimed gains: 10x faster code search, 7–70x fewer tokens per query
- Best target right now: `~/minecraft-event`

**3. Turn any repeating Claude Code setup into a SKILL.md**
Structure:
```
.claude/commands/your-skill/
  SKILL.md        ← main prompt + gotchas for this skill
  scripts/        ← helpers Claude can call
  references/     ← docs, specs, API refs
```
Candidates: `sync mc-mirror`, card-flip logging, AP Chem note gen.

---

### Set up once, pays forever

**4. Create `personal/Projects/4-System/Claude.md`** (Obsidian OS context file)
A structured file Claude reads at session start. Separate from CLAUDE.md so it holds dynamic state (active projects, this week's priorities) without touching the instruction layer.

Template:
```
## ABOUT ME
Name: [Your name]
Role: Junior → Senior (2026–2027), crew rower, card flipper, novel collaborator

## ACTIVE PROJECTS
- agonizing-sentience: Chapter 3 in progress
- card-flip: Daily ops active
- minecraft-event: Shared repo, mirror via sync-reference.sh

## PRIORITIES THIS WEEK
- ...
```

**5. Add the 7-rule anti-sycophancy prompt to Claude.ai Projects**
In any project where you want honest critique (agonizing-sentience, card-flip decisions, minecraft-event design), paste the advisor system prompt from [[claude-improvement-notes#Anti-Sycophancy]]. Forces `[Certain]`/`[Likely]`/`[Guessing]` confidence tagging on every claim.

---

## Repos to follow / clone

| Repo | Purpose | Action |
|------|---------|--------|
| `github.com/safishamsi/graphify` | Codebase knowledge graph | Clone + install |
| `github.com/anthropics/claude-code` | Official Claude Code | Star, watch releases |
| `github.com/anthropics/model-context-protocol` | MCP spec + server examples | Reference for new integrations |

**MCP servers worth adding** (already have GitHub):
- Perplexity — web search from inside Claude Code
- PostgreSQL — if any project touches a DB

---

## Key prompts saved (verbatim, in notes)

- **Second Brain Prompt** — full 4-step interview-to-vault system → [[claude-improvement-notes#AI Second Brain Prompt (Full System)]]
- **Court of Claude** — gauntlet anti-validation prompt → [[claude-improvement-notes#Court of Claude — Anti-Validation System]]
- **Morning Briefing** — daily task brief from Claude.md → [[claude-improvement-notes#Morning Briefing Prompt (Obsidian OS)]]
- **4C Prompt Formula** — Context + Content + Constraints + Command + Examples → [[claude-improvement-notes#Perfect Prompt Formula (4Cs + Examples)]]
