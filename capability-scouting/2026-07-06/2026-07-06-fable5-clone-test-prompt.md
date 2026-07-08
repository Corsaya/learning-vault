---
date: 2026-07-06
tags: [capability-scouting, fable-5, jarvis, testing]
---

# Fable 5 vs. "Fable 5 clone" — hiragana lesson A/B test

Not executed yet — this is the prompt package for Donovan to run manually in
two separate sessions, per his instruction. See
[[2026-07-06-fable5-clone-research]] for how this was derived.

**Why a system-prompt clone alone can't be perfect:** the leaked Fable 5
system prompt is ~95% shared Claude constitution — Opus already runs on the
same base. Fable 5's actual edge (per the Theo video researched today) is an
**orchestration/effort-discipline layer**, not a personality difference. So
the "clone" below is Opus + the closest approximation of that discipline
layer, not a verbatim system-prompt swap. Comparing the two outputs should
surface exactly where the discipline layer helps (or doesn't) versus where
it's actually raw-capability that's doing the work — that gap is the thing
worth tweaking afterward.

---

## Side A — Real Fable 5

Switch model to Fable 5 (`/model claude-fable-5` in Claude Code, or pick it
in claude.ai), start a **fresh session**, and paste the Main Task Prompt
below with nothing else prepended.

## Side B — The clone (Opus + Fable 5 discipline layer)

Switch model to Opus 4.8, start a **fresh session**, paste the **Clone
Persona Prompt** first, then in the same session paste the identical **Main
Task Prompt**.

### Clone Persona Prompt (paste first, Side B only)

```
You are operating with Fable 5's orchestration discipline layer on top of
your normal Claude behavior. Specifically, before and while doing any task:

1. Decompose before executing. Break the task into an explicit small plan
   before producing the final artifact. Don't jump straight to output.
2. Verify before calling it done. After producing something, check it
   against the stated goal line by line before presenting it as finished.
3. Effort discipline: think as hard as the task actually needs, not harder.
   Don't loop, second-guess, or over-elaborate past the point of
   diminishing returns — that produces worse output at higher cost, not
   better output.
4. Judge the output, not the effort spent. The only thing that matters is
   whether the deliverable actually achieves the stated goal for the
   specific person asking, not how much reasoning went into it.
5. One clarifying question max, and only if the task is genuinely
   ambiguous — otherwise make a reasonable assumption, state it, and
   proceed.
6. Minimal formatting unless the content's complexity genuinely requires
   structure (this one's already standard Claude behavior, keep it).

Keep this discipline active for the rest of this session.
```

### Main Task Prompt (paste to both Side A and Side B, verbatim)

```
Build me a hiragana learning guide as a single markdown file for my Obsidian
vault (learning/Japanese/). Goal: after studying this file, I should be able
to (1) recall the sound of every basic hiragana character on sight, (2) hear
a sound and know which character it is, and (3) draw every character from
memory when given just its sound — stroke order included. Cover all 46 basic
hiragana (a-i-u-e-o through wa-wo-n), not dakuten/handakuten or combinations.

Design it for actual memorization, not just reference — assume I'll use this
file as my only study material and won't have you around to quiz me live.
Whatever structure gets a 46-character syllabary to actually stick (grouping,
mnemonics, stroke-order description, self-test method, spaced-repetition
notes, whatever you think works) — your call, that's the point of this test.

Do not create the file yet — first show me the full planned structure/outline
and reasoning for your approach, and wait for my go-ahead before writing it.
```

*(The "don't create the file yet" line is deliberate — it keeps both sides at
the planning stage so nothing gets written into `learning/Japanese/` until
Donovan picks a direction. Drop that line if/when the actual file should get
generated.)*

---

## What to bring back

Paste (or describe) both outputs side by side. Useful things to note per
side, even informally:
- Did it actually ask before building, or ignore the instruction?
- What memorization method did it pick (mnemonics? drawing drills? spaced
  repetition schedule? grouping by row?) — and does that match how you
  actually learn?
- Any looping/over-thinking/rambling on Side B (would indicate the
  discipline layer isn't holding), or under-thinking on Side A (would
  indicate the "just raw capability" theory is wrong).
- Which plan you'd actually pick, and why — that's the real signal for what
  to tweak in either the clone persona prompt above or in how we prompt
  Fable 5 in general.
