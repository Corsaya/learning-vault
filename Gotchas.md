---
title: Gotchas
tags: [ai-improvement, memory]
created: 2026-07-06
---

# Gotchas

One line per entry — things that bit before, so they don't bite twice.
Idea adapted from obsidian-mind's `brain/Gotchas.md`. Append, don't prune;
if something stops being true, note the date it was superseded rather than
deleting the line.

- **2026-07-06** — `personal/` in the vault is the private wall (Journal,
  Health, Daily, Work, Inbox); the CLAUDE.md-described rename to
  `personal-private/` hasn't happened yet — don't assume the folder name
  matches the doc until that migration lands.
- **2026-07-06** — Health work under `personal/Health/` is a standing,
  explicitly scoped exception to the private-vault wall (not a general
  license for all of `personal/`). Enforced now by
  `~/.claude/hooks/private-vault-guard.py` + its allowlist, not just prose.
- **2026-07-06** — Each Obsidian sub-vault (`personal`, `learning`,
  `ai-improvement`, `finance`, `jarvis`, `card-flip`, etc.) has its own
  `.obsidian/` — a plugin installed in one vault is NOT available in
  another. The obsidian-claude-code sidebar plugin had to be built once
  then copied into each target vault's `.obsidian/plugins/`.
- **2026-07-08** — `uv tool install notebooklm-py --with rookiepy` fails on
  the default Python (rookiepy has no 3.14 wheel and its sdist pyproject is
  broken) — pin `--python 3.12`. And cookie import: Firefox profile had no
  Google cookies; `login --browser-cookies chromium` is the one that works
  on this machine.
- **2026-07-08** — The yt-analysis video backend 503'd on 4 attempts across
  3 sessions (nuwlyQXrADg, I-cvxBMue08) — treat it as unreliable; a video's
  yt-dlp description + chapters usually carries most of the signal.
- **2026-08-02** — Pytheas voice STT (`voice.py`, faster-whisper `"base"`
  model) mis-heard "khanacademy.org" as "conacademy.org" and opened the
  wrong URL without complaint — live-tested, not theoretical. Whisper's
  smallest model struggles with less-common brand/proper nouns spoken as
  URLs. Everything else in the same test (general knowledge Q&A, math,
  a homophone-prone book title) transcribed correctly, so this looks like
  a specific weak spot (compound brand names read aloud) rather than a
  broad accuracy problem. Fix candidates: bump to `"small"`/`"medium"`
  Whisper model, or add a confirm-before-open step for voice-triggered
  link/app opens so a mis-hear doesn't silently execute.
- **2026-08-02** — Pytheas voice chats can silently fail to save. The save
  path exists and normally works (`handle_voice_text` in `server.py`
  writes each turn to the same `chats.json` typed chat uses, via
  `chats.update_chat`), but it's entirely gated on a `chat_id` set by a
  prior `POST /api/voice_session {action:"start"}` call
  (`voice_session_start`, `server.py:112-124`). If audio ever reaches
  `/api/voice` without that session-start call having succeeded first,
  `handle_voice_text` falls back to a throwaway in-memory history list and
  never calls `chats.update_chat` — no error, no warning, just nothing
  written. Live-tested 2026-08-02: a voice conversation did not appear in
  chat history afterward, consistent with this failure mode. Not yet
  root-caused *why* the session-start call didn't stick that time (frontend
  race, a failed/slow `/api/voice_session` request, permissions) — next
  time this happens, check server logs around session start for that
  timestamp before assuming it's fixed.
