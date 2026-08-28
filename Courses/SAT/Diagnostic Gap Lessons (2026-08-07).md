---
tags: [pytheas, sat, math, english, course, lesson]
created: 2026-08-07
status: lessons written — retest pending
source: confirmed gaps from SAT Diagnostic Test (2026-08-07) error log
---

# Diagnostic Gap Lessons — 2026-08-07

Four targeted lessons, one per confirmed gap from the 28/32 diagnostic attempt (see
`SAT Diagnostic Test (2026-08-07).md` → Error log). Not a full unit — each is short on purpose,
since three of these are narrow rules, not broad topics. A 12-question retest is at the bottom;
take it cold once you've read through all four.

Priority order (per `Ultimate Workspace Roadmap.md` workstream 19 and the revised priority in
the diagnostic doc): **Advanced Math asymptotes** and **Conventions subject-verb agreement**
are confirmed real gaps (both the Dec/Mar official reports and this fresh sitting agree) —
work through those two first if you're short on time. The inequality rule and percentages are
smaller, faster fixes.

---

## Lesson 1 — Advanced Math: asymptotes of rational functions

**What you missed:** Q12, "The graph of $y = \frac{3}{x-5} + 2$ has a horizontal asymptote at
$y = $" — you answered 5 (the vertical asymptote) instead of 2 (the horizontal one). You said
you "had no idea what to do" — this is a real gap, not a slip, so start from the definitions.

### The two asymptotes, and why they're different things

A rational function written in this shifted form:
$$y = \frac{a}{x - h} + k$$

has two asymptotes — invisible lines the graph approaches but never touches:

- **Vertical asymptote: $x = h$.** This is where the *denominator* would be zero — the function
  is undefined there, so the graph shoots up or down toward that $x$-value and never crosses it.
- **Horizontal asymptote: $y = k$.** This is what the function approaches as $x \to \pm\infty$.
  As $x$ gets very large, $\frac{a}{x-h} \to 0$, so $y \to k$. $k$ is just added on the outside —
  it's the "floor/ceiling" the whole fraction shifts toward but never reaches.

**The shortcut that would've caught this fast:** the number *subtracted from $x$ inside the
denominator* is the vertical asymptote. The number *added outside the fraction* is the
horizontal asymptote. They're never the same number, and the question is always asking about
one or the other — read which one it's asking for before you answer.

### Worked examples

1. $y = \frac{4}{x+2} - 1$. Rewrite as $\frac{4}{x-(-2)} + (-1)$: vertical asymptote $x = -2$,
   horizontal asymptote $y = -1$.
2. $y = \frac{-7}{x-9}$. No visible "$+k$" means $k = 0$: vertical asymptote $x = 9$, horizontal
   asymptote $y = 0$.
3. $y = \frac{2}{x} + 6$: this is $h = 0$, $k = 6$: vertical asymptote $x = 0$ (the $y$-axis),
   horizontal asymptote $y = 6$.

### Practice (answers below the line)

a. $y = \frac{5}{x-3} + 4$ — find both asymptotes.
b. $y = \frac{-2}{x+1} - 6$ — find both asymptotes.
c. A rational function has a vertical asymptote at $x = 8$ and a horizontal asymptote at
   $y = -3$. Write a possible equation in the form $y = \frac{a}{x-h}+k$ (any nonzero $a$ works).

---

## Lesson 2 — Algebra: the inequality-flip rule

**What you missed:** Q6, "$-2x + 7 \le 15$" — you answered $x \le -4$ instead of $x \ge -4$. You
said you "forgot the rule entirely." This is one specific, narrow rule — not a sign you're weak
at algebra generally, since everything else in Algebra except Q1 (a timing slip) was correct.

### The rule

When you multiply **or** divide both sides of an inequality by a **negative number**, the
inequality sign flips direction. This is the *only* time it flips — adding, subtracting, or
multiplying/dividing by a positive never flips it.

**Why:** think of a simple case — $2 < 5$ is true. Multiply both sides by $-1$: $-2$ vs. $-5$.
Is $-2 < -5$? No — $-2$ is bigger. The sign has to flip to $-2 > -5$ to stay true. Any time you
flip a number line's direction (multiplying by a negative does exactly that), "less than"
and "greater than" swap.

### Worked example (your exact missed question)

$$-2x + 7 \le 15$$
$$-2x \le 8 \quad \text{(subtracted 7 — no flip, this step is positive-only)}$$
$$x \ge -4 \quad \text{(divided by } -2 \text{ — FLIP the sign here)}$$

The flip happens on the *last* step, dividing by $-2$. It's easy to do all the algebra
correctly and just forget the flip on that one step — that's almost certainly what happened
here, not a deeper misunderstanding.

**Drill habit:** every time you divide or multiply an inequality by anything, say out loud (or
mentally flag) "is this negative?" before writing the next line. Make it a checkpoint, not
something you trust yourself to remember automatically under time pressure.

### Practice (answers below the line)

a. $-3x - 4 > 11$
b. $5 - x \ge 12$
c. $\frac{-x}{4} < 6$
d. $-6x + 2 \le -4x + 10$ (variables on both sides — isolate $x$ first, then check whether the
   final divide step is by a negative)

---

## Lesson 3 — Standard English Conventions: subject-verb agreement with interrupting phrases

**What you missed:** "The committee, along with its three subcommittees, ____ meeting every
Thursday..." — you were split between "are" and "have been," and didn't consider "is" (the
correct answer) at all. You said you weren't sure of the rule itself — this is a real gap in
the rule, not just a pattern-recognition trap, so it's worth learning the underlying principle,
not just memorizing this one example.

### The rule

The verb must agree with the **true subject** of the sentence — not with whatever noun happens
to sit closest to the verb. Certain phrases can sit between the subject and the verb without
changing the subject's number (singular/plural) at all. The most common ones:

- along with
- as well as
- together with
- in addition to
- accompanied by

These are called **non-essential interrupting phrases** — they add information but are not
part of the grammatical subject. Mentally delete the whole phrase (including the commas around
it) and check what's left:

> "The committee, ~~along with its three subcommittees,~~ **is** meeting every Thursday..."

With the phrase deleted, it's obviously "the committee is," singular — one committee, one verb
choice. The phrase "along with its three subcommittees" never changes that, no matter how many
subcommittees are named inside it.

**Why this trips people up:** "subcommittees" is plural and sits right before the blank, so
your ear wants to agree with it (this is called a "buried subject" or "distractor noun" trap).
The fix is mechanical, not intuitive: delete the interrupting phrase on paper/in your head, then
check agreement on what's left.

**Contrast — what actually *does* make a subject plural:** the word "and" joining two subjects.
"The committee and its three subcommittees are meeting..." — here they genuinely are joined as
one combined subject, so "are" would be correct. The difference between "and" (joins,
makes plural) and "along with/as well as/etc." (interrupts, doesn't change number) is the whole
rule.

### Worked example (your exact missed question)

"The committee, along with its three subcommittees, ____ meeting every Thursday to review
pending applications." Delete "along with its three subcommittees": "The committee ____ meeting
every Thursday" → singular subject → **is**.

### Practice (answers below the line)

a. The coach, as well as all of the players, (is/are) excited about the new season.
b. My grandmother, together with her two sisters, (has/have) always cooked Thanksgiving dinner.
c. The report, in addition to the appendices, (was/were) submitted on time.
d. The manager and the entire sales team (was/were) present at the meeting. (Note: this one
   uses "and" — different rule than a–c.)

---

## Lesson 4 — Problem-Solving & Data Analysis: percent-of-a-number refresher

**What you flagged:** Q13 (the discounted-then-taxed jacket) — you got it right but said you
didn't immediately recall how to compute a percentage of a number. Quick refresher since this
didn't cost you a point but clearly cost you time/confidence.

### The core move

"X% of a number" means: convert the percent to a decimal (divide by 100), then multiply.

$$25\% \text{ of } 80 = 0.25 \times 80 = 20$$

**Discount:** subtract that amount, or — faster — multiply by (1 − the decimal):
$$80 - 20 = 60 \quad \text{or equivalently} \quad 80 \times 0.75 = 60$$

**Increase (tax, markup, growth):** multiply by (1 + the decimal):
$$60 \times 1.08 = 64.80 \quad \text{(8% tax on \$60)}$$

**The trap to watch for (this is the actual SAT trap, not just the base skill):** in a
multi-step problem, each percentage applies to the **current** value, not always the original.
$80 \to 25\%$ off $\to \$60$, and *then* $8\%$ tax applies to $\$60$, not the original $\$80$.
Applying 8% to \$80 instead gives \$66.40 — a real answer choice designed to catch exactly this
mistake.

### Worked example (your exact question)

$$80 \times 0.75 = 60 \qquad 60 \times 1.08 = 64.80$$

### Practice (answers below the line)

a. What is 15% of 60?
b. A \$45 item is discounted 20%. What's the sale price?
c. A \$200 item is marked up 30%, then discounted 10% off the marked-up price. Final price?
d. "Increased by 150%" — what percent of the original does the new value represent? (Trap from
   the earlier YouTube research: this is a common headline-trap phrasing.)

---
---

# Answers

**Lesson 1 (asymptotes):**
a. vertical $x=3$, horizontal $y=4$
b. vertical $x=-1$, horizontal $y=-6$
c. $y = \frac{a}{x-8} - 3$ for any nonzero $a$ (e.g. $y=\frac{1}{x-8}-3$)

**Lesson 2 (inequality flip):**
a. $-3x - 4 > 11 \Rightarrow -3x > 15 \Rightarrow x < -5$ (flipped — divided by $-3$)
b. $5 - x \ge 12 \Rightarrow -x \ge 7 \Rightarrow x \le -7$ (flipped — divided/multiplied by $-1$)
c. $\frac{-x}{4} < 6 \Rightarrow -x < 24 \Rightarrow x > -24$ (flipped)
d. $-6x+2 \le -4x+10 \Rightarrow -2x \le 8 \Rightarrow x \ge -4$ (flipped — divided by $-2$)

**Lesson 3 (subject-verb agreement):**
a. is (subject: "the coach," singular; "as well as..." is an interrupting phrase)
b. has (subject: "my grandmother," singular)
c. was (subject: "the report," singular)
d. were (subject: "the manager and the entire sales team" — joined by "and," genuinely plural)

**Lesson 4 (percentages):**
a. $0.15 \times 60 = 9$
b. $45 \times 0.80 = 36$
c. $200 \times 1.30 = 260$; $260 \times 0.90 = 234$
d. 250% of the original (100% + 150% increase = 250% of the original value) — the "headline
   trap" is answering 150%, which is only the *increase*, not the new total.

---

## Retest — 12 questions, untimed, cold

Same rules, new numbers — not the same questions as above, so you can't just remember the
answer instead of applying the rule.

**R1.** (asymptotes) $y = \frac{6}{x+4} - 2$. Horizontal asymptote?
**R2.** (asymptotes) $y = \frac{-3}{x-7} + 5$. Vertical asymptote?
**R3.** (asymptotes) A function has vertical asymptote $x=-1$ and horizontal asymptote $y=0$. Write a possible equation.
**R4.** (inequality) $-5x + 3 < 18$
**R5.** (inequality) $12 - 2x \ge 4$
**R6.** (inequality) $\frac{-3x}{5} > 9$
**R7.** (agreement) The teacher, along with her students, (is/are) preparing for the field trip.
**R8.** (agreement) The boxes, as well as the crate, (was/were) shipped yesterday. *(Careful — check which noun is actually the subject here.)*
**R9.** (agreement) The captain and the first mate (is/are) responsible for the ship's log.
**R10.** (percent) What is 40% of 90?
**R11.** (percent) A \$120 jacket is discounted 30%, then taxed 5%. Final price?
**R12.** (percent) "Decreased by 40%" — the new value is what percent of the original?

### Retest answers

R1. $y=-2$
R2. $x=7$
R3. $y=\frac{a}{x+1}$ for any nonzero $a$ (e.g. $y=\frac{1}{x+1}$)
R4. $x > -3$ (flipped — divided by $-5$)
R5. $x \le 4$ (flipped — divided by $-2$)
R6. $x < -15$ (flipped — divided by $-3/5$, still negative)
R7. is (subject: "the teacher," singular)
R8. were — this one's the trap in reverse: "the boxes" is the true subject here (plural), and
    "as well as the crate" is the interrupting phrase, so it agrees with "boxes," not "crate."
R9. are (joined by "and" — genuinely plural)
R10. 36
R11. $120 \times 0.70 = 84$; $84 \times 1.05 = 88.20$
R12. 60% of the original
