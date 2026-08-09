---
date: 2026-07-07
tags: [capability-scouting, fable-5, testing, ab-test-output]
---

# Side A output — real Fable 5, hiragana guide plan

Captured 2026-07-07 from a real `claude-fable-5` Claude Code session, responding
to the verbatim Main Task Prompt in [[2026-07-06-fable5-clone-test-prompt]].
Per that prompt's instruction, this is the planning stage only — no file was
written into `learning/Japanese/`. Compare against the Side B (Opus + clone
persona) run whenever it's done.

---

## The response

Here's the planned structure and the reasoning behind it. The whole design is
driven by one observation: **your hardest stated goal is #3 (sound → draw from
memory), and it's roughly 10× harder than the other two.** Recognition (#1, #2)
comes nearly free as a side effect of training production, but not the other
way around. So the file is built around forced blind production, with
recognition as the warm-up — not a reference chart with quizzes bolted on.

Second constraint that shapes everything: this is a **markdown file with no
audio and no images**. That means (a) "hear a sound" becomes "say the romaji
prompt aloud, then recall" — self-voicing is the closest a text file gets to
an audio quiz, and it works because hiragana sounds map 1:1 to romaji; and
(b) stroke order must be carried by numbered verbal descriptions plus the
small set of general CJK stroke rules, not diagrams. That's genuinely
workable for hiragana (max 4 strokes per character), but it's the riskiest
part of the design, so every description follows one fixed formula:
*stroke count → start position → direction → shape verb* (e.g. **あ**, 3
strokes: ① short horizontal, upper left → right; ② vertical cutting down
through it, curving left at the bottom; ③ big sweeping curve starting upper
right, looping down and around like a fish hook through the cross).

### Planned file: `learning/Japanese/Hiragana — Complete Study Guide.md`

**§0 — How to use this file (the protocol).** A 12-day plan: 10 content days
(one row of ~5 kana per day), 2 built-in consolidation days after day 5 and
day 10. Each day is a fixed 3-pass loop per row: (1) read the mnemonics once,
(2) trace each character 3× while saying its sound aloud, following the
stroke text, (3) close the section and blind-produce the whole row on paper
from romaji prompts, then check. Pass 3 is the one that counts; passes 1–2
exist to make pass 3 possible. Also states the materials assumption: paper
and pen, ~15 min/day.

**§1 — The gojūon map.** The full 46-character grid (5 vowels × rows a, ka,
sa, ta, na, ha, ma, ya, ra, wa/wo + ん) presented once up front as the mental
scaffold. Reasoning for row order over frequency order: the grid *is* the
retrieval structure — Japanese dictionaries, verb conjugation, and every
future lesson are organized by it, so encoding it now means every character
has a fixed "address" (e.g. ぬ = "na-row, u-column"), which is itself a
recall cue when a mnemonic fails.

**§2 — Row-by-row lessons (10 subsections).** Per character, always the same
five lines: the character large; romaji; **visual mnemonic** (a one-sentence
image linking shape → sound, Tofugu-style, e.g. く is a bird's beak going
"ku, ku"); **stroke order** in the fixed formula above; **pitfall** (which
lookalike it collides with, if any). Per row, a closing drill block: a
recognition line (the row's kana shuffled, name them aloud), a production
line (romaji shuffled, draw them blind), and 3–5 **real words** spellable
using only kana learned so far (あい, いえ, かき…), because words give the
characters somewhere to live and double as cumulative review.

**§3 — Lookalike disambiguation.** The confusion clusters get their own
section instead of being scattered: あ/お, ね/れ/わ, は/ほ/ま, さ/き,
ち/さ (mirror trap), ぬ/め, る/ろ, い/り, こ/て, し/つ (curve direction).
Each cluster gets a *contrast* mnemonic (what to look at to tell them apart),
not just individual mnemonics — because in month 2 the errors are almost
never "forgot ぬ", they're "wrote め". This section is scheduled for the two
consolidation days.

**§4 — Self-test kit.** Three quiz banks, each in a different shuffled order
so grid position never leaks the answer: (A) kana → sound (sight
recognition), (B) spoken romaji → point/say which kana (the audio-substitute
direction), (C) romaji → draw blind with stroke order (production). Answers
live at the very bottom of the file behind a "no peeking" gap, not inline —
the physical act of scrolling to check is what keeps it honest self-testing
instead of re-reading, and re-reading feels like learning but isn't.

**§5 — Spaced-repetition schedule.** A simple expanding-interval table
(learn day N → review days N+1, N+3, N+7, N+14) mapped concretely to
calendar checkboxes per row, plus a Leitner-lite rule: any character missed
twice in a review drops back to "daily" until it survives two clean tests.
Deliberately paper-and-checkbox, no plugin/Anki dependency — the file has to
work as your *only* material, per the brief.

**§6 — Progress tracker.** A 46-row checkbox table, three columns per
character (see→say / hear→identify / say→draw), matching your three stated
goals one-to-one, so "done" is defined as all 138 boxes checked rather than
a feeling.

### Judgment calls I made (flag if wrong)

- **Mnemonics for all 46**, even trivial ones — consistency beats cleverness;
  a character without a hook is the one you'll blank on in a test.
- **No dakuten/handakuten teasers** anywhere, per your scope line — not even
  a "coming next" note, to keep the test surface exactly 46.
- **Estimated length ~700–900 lines.** Long for one note, but the brief says
  single file and only-study-material, so completeness wins over tidiness.

That's the full plan. Want me to write it? If yes, say go — and tell me if
you want the 12-day pacing compressed (it can run as 6 days at 2 rows/day if
you're sprinting before a trip or a class).

---

## Notes for the A/B comparison (meta, not part of the response)

- Did ask before building: yes — held at planning stage per the prompt.
- Method picked: row-by-row + visual mnemonics + forced blind production +
  expanding-interval review; production treated as the driver, recognition
  as the side effect.
- Distinctive choices to compare against Side B: the no-audio/no-image
  constraint handled explicitly (self-voicing, fixed stroke-description
  formula), answers physically separated from quizzes, contrast-mnemonics
  for lookalike *pairs* as a separate concern from per-character mnemonics,
  progress defined as 46×3 checkboxes mapping to the three stated goals.
