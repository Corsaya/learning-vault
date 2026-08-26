# Memory Export — jarvis

Exported 2026-08-25 from claude-mem (`~/.claude-mem/claude-mem.db`) before the
Claude Code subscription ended. Machine-generated session records, preserved as
portable markdown. Not hand-written — treat as a log, not as authored notes.

## Observations

### 2026-07-03T18:16 · `discovery` — Jarvis Project Structure and Capabilities
The Jarvis project is a personal AI assistant terminal CLI at /home/donovan/code/jarvis. It uses the Anthropic API with a usage-aware model routing system that selects between fast/standard/full tiers or exact model IDs. Persistent memory is split between identity.md (injected into every session) and facts.md (user-saved facts). Configuration is local and gitignored. The project entry point is python -m jarvis and supports meta-commands for memory, usage tracking, and model switching.
