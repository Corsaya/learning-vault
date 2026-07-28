# Briefings Roadmap (bookmark — not built yet)

The Pytheas "Briefing" tab became **Briefings** (2026-07-24) and is meant
to hold multiple daily briefs. Only the AI brief exists today.

## Live
- **AI briefing** — last30days multi-source pull + Claude synthesis.
  Now includes: official lab X accounts (@AnthropicAI, @OpenAI,
  @GoogleDeepMind, …) and GitHub / Claude-plugin ecosystem discoveries.

## Planned (bookmarked, do not build until asked)
- **Channel briefing** — for the future YouTube channel: niche news,
  competitor uploads, trending formats/sounds, algo-scout output.
- **Finance briefing** — markets + card-flip relevant: TCG price moves,
  trading watchlist, relevant macro headlines.
- Ideas for later: School brief (assignment deadlines from calendar +
  Courses activity), Japanese immersion brief.

## Implementation note (for future session)
`briefing.py` is single-topic; the natural refactor is a `BRIEFS` dict
(name → topic, prompt, output dir `jarvis/Briefings/<name>/`) with the UI
tabs already stubbed in `sections.js` (`.brief-tabs`).
