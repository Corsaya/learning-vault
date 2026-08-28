---
tags: [pytheas, sat, bluebook, practice-test, tools]
created: 2026-08-21
---

# Practice 11 — Screenshots and Review Tools

Everything from the official College Board practice test taken 2026-08-20
(`mypractice.collegeboard.org`, SAT Practice 11 — 71/98).

## Contents

- **98 screenshots**, one per question, in question order (R&W M1 Q1–27, R&W M2 Q1–27,
  Math M1 Q1–22, Math M2 Q1–22). Ordering was established by file mtime and verified against
  27 independently known question numbers.
- **`question-only/`** — the same 98 cropped to the question panel, with the answer banner and
  rationale removed. Used by the tools' blind mode.
- **`manifest.json`** — per question: file, section, module, number, correct/incorrect, confidence.
- **`misses.json`** — the 27 misses with domain, question type, and diagnosis.

## Tools (open in a browser — plain static HTML, no server)

| File | What it does | Status |
|---|---|---|
| `confidence-rater.html` | 1–5 confidence on all 98, blind | **done** — 98/98 |
| `desmos-log.html` | Desmos use, method, and exact input per Math question | **done** — 44/44 |
| `miss-review.html` | Triage the 27 misses: got it / still lost / careless | in progress |

Each saves to browser localStorage and exports markdown. Exports live in
`Practice Tests/` as `Practice 11 — Raw *.md`.

Analysis: [[Bluebook Practice Test — 2026-08-20]].
