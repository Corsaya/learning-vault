---
tags: [pytheas, sat, workflow, claude, bluebook, crash-course]
created: 2026-08-19
status: active operating instructions
related: ["[[Adaptive Review System]]", "[[Pattern Index]]", "[[Formula Vault]]", "[[English Rule Vault]]", "[[Test Day Execution]]", "[[Morning-of Review]]"]
---

# SAT Study System — Claude Bridge

> **Claude: read this note before creating, revising, or recommending any SAT course material.**

This is the operating bridge between a Bluebook practice test and the materials in `Courses/SAT`.
The aim is not broad re-teaching. The aim is to turn the student's actual mistakes, guesses, and
timing data into the smallest set of reusable lessons needed before Saturday.

## The student workflow

1. Take an official Bluebook practice SAT using [[Test Day Execution]].
2. Put a complete record of **every question**—right, wrong, and guessed—into `Courses/SAT`.
3. For each question, record the answer outcome, confidence, elapsed time, domain, subskill, and
   why it was missed or uncertain.
4. Use the record to create or revise crash-course material only for questions that were wrong,
   guessed, too slow, or show a recurring pattern.
5. Study the targeted material, then retest it until the process is reliable under SAT timing.
6. Build the single final packet in `Morning Of Review/` for the morning of the exam.

## Bluebook record format

Create one note per official practice test in `Practice Tests/`, named
`Bluebook Practice Test — YYYY-MM-DD.md`. Preserve the original question wording, source, and
student work when supplied. Do not turn blank or unattempted questions into incorrect-answer data.

For every question, record:

| Field | What to capture |
|---|---|
| Question | Section, module, question number, prompt, choices, correct answer, and selected answer |
| Result | Correct, Incorrect, Blank, or Not reached |
| Confidence | 🟢 Certain, 🟡 Unsure, or 🔴 Guess |
| Time spent | Best estimate in seconds or minutes |
| Domain and subskill | Official domain plus the most specific skill available |
| Pattern | Existing [[Pattern Index|pattern]] or a candidate new pattern |
| Reason | Didn't know concept, forgot formula, misread, careless, timing, vocabulary, or second-guessed |
| Tool | Whether Desmos was used, should have been used, or would not help |
| Next action | Review, make pattern, add formula/rule, drill, or no action |

Interpret outcomes through [[Adaptive Review System]]:

- Wrong + certain: a knowledge or reasoning gap.
- Wrong + unsure: repetition and a clearer decision rule are needed.
- Correct + guess: treat as unlearned; it was a lucky result, not mastery.
- Correct but slow: teach a faster method, including Desmos when appropriate.
- Blank or not reached: treat as execution/timing data, not as proof of a content gap.

## Claude's course-building rules

When the completed record is available:

1. Analyze before writing. Group misses by domain, subskill, pattern, reason, confidence, and time.
2. Name the pattern before explaining computation. Add a reusable note in [[Pattern Index|Pattern Library]] when it recurs or has a clear recognition cue.
3. Add a formula to [[Formula Vault]] only when it caused a miss or is required by a verified weak pattern.
4. Add the governing grammar rule to [[English Rule Vault]]; never save a grammar question as a fact to memorize.
5. Build a targeted crash-course addition only for supported gaps. Each addition should contain:
   - recognition cues;
   - a short algorithm or decision rule;
   - the student's error pattern and trap;
   - one representative worked example;
   - a short timed retest with a clear mastery criterion.
6. Prefer a new targeted lesson or a clearly labeled subsection over silently rewriting an existing broad crash course.
7. Do not infer a weakness from unanswered questions, incomplete sections, or one isolated guess without considering timing and confidence.
8. State what evidence supports each recommendation and what is still unknown.

## Mastery standard

A skill is not ready because the explanation made sense. It is ready when the student can:

- recognize the pattern quickly;
- choose the correct method without prompting;
- execute it accurately at a reasonable SAT pace; and
- repeat that performance on new questions.

Use timed retests. If a miss is conceptual, reteach briefly. If it is a recurring decision,
timing, or careless-error pattern, improve the execution rule instead of adding more theory.

## Morning-of review packet

The single morning-of folder is [[Morning-of Review]]. Claude should keep it concise and
actionable. After each completed practice-test review, update it to contain only:

1. the test-taking strategy from [[Test Day Execution]];
2. a Desmos list: every verified question type where Desmos is faster or safer, with exact input
   steps and the cue that should trigger its use;
3. the student's most inconsistent patterns, with one-line decision rules and traps;
4. the few formulas and English rules still worth reviewing; and
5. a short no-new-content checklist for the morning of the official SAT.

Do not fill the packet with every crash-course topic. It is a last-mile execution tool, not a
second textbook.

## Sources — Bluebook and the Question Bank only

As of 2026-08-20 the only question sources are **official Bluebook practice tests** and the
**College Board Student Question Bank**. All self-generated practice tests, the vault
full-length test, and the Chiron test/drill apps have been deleted. Do not write new practice
questions, and do not treat any non-official item as score evidence.

## Critique of the current SAT material

### What is already strong

- The eight crash courses cover all official SAT domains, have 65 subcategories, worked examples,
  and mini-diagnostics. This gives the system an unusually solid content base.
- [[SAT Diagnostic — Score History and Domain Analysis]] makes a useful distinction between stable
  weaknesses (Advanced Math and Standard English Conventions) and volatile domains that may be
  execution problems instead of knowledge gaps.
- [[Diagnostic Gap Lessons (2026-08-07)]] already models focused remediation: one defined gap,
  a short lesson, practice, and a retest.
- [[Quick Reference — Math Formulas and Grammar Rules]] is the scannable pre-test layer the
  crash courses were too long to serve as.

### What must improve

- The crash courses are organized by coverage, not yet by the student's next Bluebook evidence.
  They should stay a resource library; the Bluebook and Question Bank record decides what gets
  studied.
- There is no per-question dataset yet that combines result, confidence, time, mistake reason,
  and Desmos opportunity. Without it, Claude cannot reliably distinguish a knowledge gap from a
  lucky guess, a pacing problem, or a careless error.
- Much of the crash-course content is explanatory and comprehensive. For the final study window,
  each verified weak skill needs a shorter recognition cue, algorithm, trap, and timed retest
  built from real Question Bank items.
- There is not yet a durable, personalized list of when to reach for Desmos. Build it only from
  verified question types, and only from official items.
- [[Formula Vault]] and [[English Rule Vault]] are still empty. They fill from real misses, not
  in advance.

## Navigation

- Start here: [[Quick Reference — Math Formulas and Grammar Rules]]
- Record and diagnose: [[Adaptive Review System]]
- Build recognition: [[Pattern Index]]
- Store rules: [[Formula Vault]] and [[English Rule Vault]]
- Execute: [[Test Day Execution]]
- Final review: [[Morning-of Review]]

---

- Written by Codex (GPT-5), 2026-08-19.
