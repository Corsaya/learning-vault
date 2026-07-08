---
date: 2026-07-08
tags: [capability-scouting, jarvis, notebooklm, courses, research]
---

# Deep dive: Zubair's JARVIS V4 video + NotebookLM course-forge integration

Research target: [I Built JARVIS from Iron Man with Claude Fable 5](https://www.youtube.com/watch?v=I-cvxBMue08)
(Zubair Trabzada / AI Workshop, 2026-07-04, ~34k views). The video-analysis
backend 503'd again (4th failure across 3 sessions — it's chronically
overloaded, stop retrying), so findings come from the full description +
chapters, his public GitHub, and web research. That turned out to be enough.

## 1. What JARVIS V4 actually is (from description + chapters)

Claude Fable 5 + Claude Code, prompt-driven build ("no coding required"):

- **Voice**: wake word + barge-in, free TTS voice, everything drivable by speech
- **Talking second brain**: any folder of notes → spoken answers **with
  sources**, while a **3D "knowledge galaxy" flies to the exact note** it's
  answering from
- **Live web research by voice** ("Jarvis, research…")
- **Screen sharing + AI vision** (it can see your screen)
- **Morning briefing from real Gmail + Calendar**
- **Mac control by voice**
- **Brain hot-swap**: switch the LLM to Grok/GPT mid-conversation
- **Personality**: TARS-style humor dials, personas

Distribution: finished V4 is paid (skool.com/aiworkshop); a free "prompt
pack" that builds a mini version is behind a free signup at
skool.com/aiworkshop-lite — **worth grabbing** (free tier, real prompts).

**Key public find — [zubair-trabzada/brain-map](https://github.com/zubair-trabzada/brain-map):**
the free/open piece of the knowledge galaxy. Stdlib-only Python, runs on any
Obsidian vault, builds an interactive animated knowledge graph from
`[[wikilinks]]` at `localhost:4710`, 100% local. This would run on our vaults
today (sandbox-review first — its one-liner is a `curl | bash`, exactly what
our checklist exists for; clone and run `build.py` directly instead). The
fancier 3D+voice "Brain Studio" is his paid product.

## 2. Gap analysis vs our Jarvis

| V4 feature | Our state |
|---|---|
| Morning briefing | ✅ built 2026-07-08 (DEC-024) — ours does AI news; his reads Gmail/Calendar (we have those MCP connectors on claude.ai; a Jarvis version is a v2 DEC) |
| Second brain w/ sources | ✅ Obsidian vaults + claude-mem (text, not spoken) |
| Web research | ✅ briefing web tools + Claude Code |
| Brain hot-swap | ✅ better: tier router + subprocess/api clients behind one seam (DEC-011/023) |
| Personality/persona file | 🟡 identity.md still blank (your task) |
| Knowledge-graph visual | ❌ → brain-map is the free adoption candidate |
| Voice (wake word, barge-in, TTS) | ❌ deliberately deferred (DEC-005); local TTS/STT was already the plan for content-brand anyway |
| Screen vision | ❌ not planned |
| Mac/OS control | ❌ v1 non-goal; "authority limits" pattern parked |

Takeaway: **we're not behind on the substance — we're behind on the
presentation layer** (voice + galaxy). His demo wow-factor is voice + visuals
on top of the same architecture we already have, with less engineering rigor
(ours has tests, DECs, and a self-improvement loop).

## 3. NotebookLM integration — the course bonus (main event)

State of NotebookLM access, July 2026:

- **Official API exists but is Enterprise-only** (Google Cloud: notebook CRUD,
  source management, audio-overview generation, queries).
- **[teng-lin/notebooklm-py](https://github.com/teng-lin/notebooklm-py)**
  (5.6k★, MIT) — **the pick.** Unofficial Python API + CLI + MCP server +
  **ships as a Claude Code skill**. Generates and *bulk-downloads* every
  studio artifact: Audio Overviews (4 formats: deep-dive/brief/critique/
  debate, 3 lengths, 50+ languages), **cinematic Video Overviews**, slide
  decks, **quizzes, flashcards** (export JSON/Markdown/HTML → straight into
  Anki), infographics, mind maps (JSON), study guides, reports. Has an
  explicit **"Curriculum / study-set builder" recipe** (one notebook per
  topic → bulk podcasts + quizzes + flashcards) and an **Obsidian sync
  recipe** (run from vault root, artifacts land in the vault, community
  skills resolve citations into `[[wikilinks]]`).
- **[jacob-bd/notebooklm-mcp-cli](https://github.com/jacob-bd/notebooklm-mcp-cli)**
  — solid alternative (`nlm` CLI + MCP, tested on free/Pro accounts).
- **Native NotebookLM learning features (2026)**: flashcards with saved
  progress + difficulty + shareable sets, quizzes with "explain" backed by
  citations, cinematic Video Overviews, audio Brief/Critique/Debate formats,
  Mind Maps, and a "Learning Guide" personalized-tutor mode.
- **Risk (both community tools)**: undocumented Google endpoints — can break
  anytime, rate limits, unofficial. Fine for personal use; pace bulk
  generation; don't build anything income-critical on it.

## 4. The Course Forge pipeline (design)

"I ask for a course on X; the assistant + model build it — interactive,
visual, audio, not just words":

1. **Interview** (needs-wants kit, method 2): goal, level, deadline → the
   model plans a syllabus (units, sources, drill types).
2. **Source pass**: assistant writes/curates per-unit source docs into
   `learning/<subject>/Course/sources/` (this is where model quality matters
   — spend the good model here, like blueprints).
3. **notebooklm-py**: create one notebook per course → add sources →
   generate per unit: **podcast** (audio), **cinematic video**, **quiz**,
   **flashcards** → `download --all` into the vault next to the notes.
4. **Claude-native interactive layer** for what NotebookLM can't do:
   production drills. E.g. an HTML canvas app for hiragana stroke practice,
   typed-answer drills, spaced-rep scheduling — Claude Code builds these
   directly as local HTML (zero dependencies, works offline).
5. **Progress**: NotebookLM flashcards track got-it/missed-it across
   sessions; the vault keeps the 46×3-style checkbox tracker as the
   source-of-truth "done" definition.

**Hiragana test, retrofitted** (it was always meant as the pilot): the
planned guide becomes the notebook's source → audio overview gives real
pronunciation (fixes the "hear a sound → know the character" goal a document
physically can't deliver) → flashcards = sight-recognition drills → quiz =
self-test → a Claude-built canvas app = stroke-order drawing practice → the
markdown guide remains the reference spine, not the whole course.
**Verify first**: Japanese audio quality of an Audio Overview on kana
content (50+ languages claimed; kana pronunciation specifically untested).

## 5. Recommended adoption order

1. `repo-scout adopt teng-lin/notebooklm-py` → sandbox checklist (pip
   package, MIT; check auth flow — it uses your Google login).
2. Install its Claude Code skill; auth with the Google account; smoke test:
   one notebook, one source, one audio overview, one flashcard export.
3. Pilot = hiragana course (steps in §4). Success test: "can you drill kana
   from the phone/audio without the document open?"
4. Grab the free prompt pack (skool aiworkshop-lite signup) — mine it for
   the voice/persona prompts; ignore the paid V4.
5. `repo-scout adopt zubair-trabzada/brain-map` → sandbox review → run
   against `learning/` for the galaxy demo (also: instant content-brand
   material — "my second brain as a galaxy" is a strong short).

## Related

- [[2026-07-06-fable5-clone-test-prompt]] — the hiragana A/B test this supersedes-in-part
- [[2026-07-07-sideA-fable5-hiragana-plan]] — the guide that becomes the course spine
- `~/code/jarvis/SELF-IMPROVEMENT.md` — the loop this adoption runs through
