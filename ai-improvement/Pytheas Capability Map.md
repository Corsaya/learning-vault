# Pytheas Capability Map (updated 2026-08-27)

What the desktop app can do and where each capability plugs into the
vaults. Full change detail: [[Pytheas 2.0 Changelog]] (jarvis vault).

## Engines
| Engine id | What | Cost |
|---|---|---|
| `claude` / `claude:fable\|opus\|sonnet\|haiku` | claude CLI, per-tier | subscription / usage credits |
| `api:<provider>:<model>` | direct HTTP (OpenAI, Gemini, Anthropic API, OpenAI-compatible) | pay-per-use, BYO key |
| `ollama:<model>` | local, private | free |

Instant regex router still answers commands in 0 tokens before any model.

## Vault integration points
> [!note] Paths corrected 2026-08-25 — the 2026-08-12 restructure moved these.
- **pytheas/** (was `jarvis/`) — project architecture and roadmaps,
  `Generated/Briefings/`, and operating history under `Operations/`.
- **learning/Courses/** — canonical course folders managed by the Pytheas
  Courses section and displayed by Chiron; NotebookLM artifacts live under
  each course's `_artifacts/`.
- **learning/ai-improvement/** (now nested under `learning/`) — this map,
  [[Briefings Roadmap]], capability scouting, `Memory-Export/`.
- **life/personal-private/** (was `personal/`) — **full read/write, same as
  everywhere else.** The wall and its enforcing hook were both retired
  2026-08-12.

## Voice
Conversation sessions (ctrl+space ⇢ ctrl+alt+space), hands-free VAD,
saved to Chats→Voice with action context. STT: faster-whisper (local).
TTS: piper local (working); ElevenLabs optional via key.

## Safety posture (unchanged principles)
- Every capability behind a server-enforced switch; dangerous ones
  default off (shell, send-email, edit-anything, agent mode).
- Model can *draft* email but the send path requires a human click.
- ~~Private-vault wall has no switch.~~ **Retired 2026-08-12** — access is open
  by default across all vaults; the one override is a doc marked **"locked"**.

## Next (agreed direction)
- Agent/company tree — Donovan will supply the structure; chats layer
  already dispatches per-chat engines, the natural hook for named agents
  with own prompts/models/permissions.
- Realtime speech API (OpenAI Realtime / Gemini Live) as optional voice
  backend once a provider key exists — bookmark, not built.
