---
date: 2026-07-07
tags: [capability-scouting, fable-5, system-prompt, claude-code]
---

# Fable 5's real Claude Code system prompt — capabilities observed from inside

Source: a live `claude-fable-5` Claude Code session (this one) reporting on
its own actual system prompt — not the claude.ai leak analyzed in
[[2026-07-06-fable5-clone-research]]. Paraphrased, not reproduced verbatim
(same reasoning as before: Anthropic's text isn't ours to duplicate). This is
the harness-side counterpart to that note, and it changes a few conclusions.

## Identity facts stated in the real prompt

- Fable 5 is **the first model in the Claude 5 family**, in a new
  **Mythos-class tier above Opus**. Fable 5 and **Claude Mythos 5 share the
  same underlying model**; Fable 5 adds safety measures for dual-use
  capabilities, Mythos 5 ships without them to approved orgs only.
  (Official page: anthropic.com/news/claude-fable-5-mythos-5)
- Knowledge cutoff: **January 2026**. Model id `claude-fable-5`.
- "Fast mode" in Claude Code is **Opus with faster output**, not a smaller
  model — worth knowing for the model-routing table.

## Capabilities the Claude Code harness gives Fable 5

- **Live token budget in-context.** The session sees a running
  `total_tokens left` figure (this session started at ~15,000,000). That's
  why "track your usage" is directly answerable — budget awareness is
  native, not estimated.
- **Context survival.** Long sessions auto-summarize and continue in the
  next window — the prompt explicitly says don't wrap up early; work
  continues across compactions.
- **Subagents (Agent tool):** typed agents (general-purpose, read-only
  Explore, Plan architect, etc.), background by default, **worktree
  isolation** (own git worktree per agent) and **remote cloud execution**,
  plus SendMessage to continue a previous agent with its context intact.
  Notably the prompt *discourages* casual spawning — subagents start cold
  and re-derive context; inline work is preferred unless the user asks.
  This matches Theo's "orchestration discipline" read almost exactly.
- **Self-scheduling:** ScheduleWakeup (self-paced loops) + cron tools. The
  prompt teaches **prompt-cache economics** explicitly — the 5-minute cache
  TTL, "don't pick 300s" (worst of both worlds), think in cache windows not
  round minutes. That's effort-discipline codified at the infrastructure
  level, not a personality trait.
- **Deferred tool loading (ToolSearch):** the harness holds a large tool
  space (Gmail, Calendar, Drive, GitHub MCP, yt-analysis, claude-mem, tasks,
  notifications, monitors) with schemas loaded on demand — tool count no
  longer bloats the prompt.
- **Artifacts:** publishes self-contained HTML pages to claude.ai (private
  by default), with design-skill gating before writing one.
- **/code-review ultra:** user-triggered multi-agent cloud review of a
  branch/PR — billed, and the model is explicitly forbidden from launching
  it itself.
- **Behavioral layer (the part the clone test cares about):** operate
  autonomously without permission-asking mid-task; act once you have enough
  information, don't re-derive established facts or re-litigate settled
  decisions; lead with the outcome; end the turn only when done or truly
  blocked; verify evidence before state-changing commands; report failures
  plainly. Parallel tool calls for independent operations are explicitly
  pushed.

## What this changes in the clone research

1. **The 2026-07-06 conclusion holds and strengthens:** the claude.ai leak
   was ~95% shared constitution because the claude.ai surface *is* mostly
   constitution. The Claude Code prompt is where the Fable-5-flavored
   discipline actually lives — and it's harness mechanics + autonomy/effort
   rules, still not personality.
2. **The clone persona prompt is missing three real ingredients.** To make
   Side B more faithful, append to the clone prompt:
   - "Act once you have enough information; never re-derive facts already
     established in the conversation or re-open decisions already made."
   - "Lead every report with the outcome in one sentence; supporting detail
     after."
   - "Do not end your turn on a plan, question, or promise — do the work
     first; end only when done or blocked on the user."
3. **Some Fable 5 'capabilities' are harness, not model** (wakeups, worktree
   agents, deferred tools, token budget). An Opus clone in the same Claude
   Code harness gets all of those for free — so the A/B tests correctly
   isolate the model + discipline layer, and any gap the tests find is real.

## Related

- [[2026-07-06-fable5-clone-research]] — the leak-based analysis
- [[2026-07-07-sideA-fable5-hiragana-plan]] — Side A output 1 (this session)
- [[2026-07-07-sideA-fable5-content-brand-plan]] — Side A output 2 (this session)
