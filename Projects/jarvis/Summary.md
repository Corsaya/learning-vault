---
tags: [project, jarvis, summary]
updated: 2026-05-30
---

# Jarvis — Summary

A personal AI assistant: terminal CLI, persistent memory, usage-aware model
routing. Anthropic-only with a provider seam. **Fully architected but not yet
implemented** — the repo is design-only; no `.py` files exist yet.

## Key design facts

- **Python 3.11+**, on-demand CLI (not a daemon).
- **3 model tiers** — fast / standard / full — selected by a router.
- **Explicit-only memory** via `/remember`; facts stored in flat `memory/facts.md`,
  loaded unconditionally in v1.
- **Identity:** `memory/identity.md` is injected first every session — currently blank.
- **API keys** live in `~/.config/jarvis/secrets`, never in the project.
- Seven hard architectural invariants; every v2 feature attaches at a named seam
  without touching the v1 core.

## v2 roadmap (planned)

- **Obsidian retrieval** — read-only context injected into the Prompt Builder
  after memory content. **Jarvis will never write to Obsidian.**
- Semantic memory, persistent history, optional daemon mode.

## Suggested build order

1. Fill in `memory/identity.md` with real identity content.
2. Add CLI quality libs (rich, prompt_toolkit).
3. Set up the Obsidian plugin stack (Dataview, Templater, Periodic Notes, Tasks).
4. Integrate semantic memory (e.g. mem0 + a local vector DB) once `facts.md` grows.
5. Wire the Obsidian REST API into the Prompt Builder.

Source of truth: the jarvis repo's `ARCHITECTURE.md` and `DECISIONS.md`.
