---
tags: [pytheas, sat, quick-reference, formulas, grammar, test-day]
created: 2026-08-20
status: pre-test cheat sheet
related: ["[[Formula Vault]]", "[[English Rule Vault]]", "[[R&W — SAT Grammar Rules Reference]]", "[[Test Day Execution]]", "[[Morning-of Review]]"]
---

# Quick Reference — Math Formulas & Grammar Rules

Scan-before-the-test sheet. Not a lesson. Recognition cue → rule → trap.
Deeper versions live in [[R&W — SAT Grammar Rules Reference]] and the Crash Courses.

**Legend:** 📄 = printed on the Bluebook reference sheet (don't waste memory on it) · 🧠 = you must know it cold · ⚠️ = known trap.

---

# PART 1 — MATH

## 1.1 Given to you on the reference sheet 📄

Circle area `A = πr²` · circumference `C = 2πr`
Rectangle `A = ℓw` · Triangle `A = ½bh` · Pythagorean `a² + b² = c²`
Special right triangles: **30-60-90** → `x, x√3, 2x` · **45-45-90** → `s, s, s√2`
Rectangular solid `V = ℓwh` · Cylinder `V = πr²h` · Sphere `V = (4/3)πr³`
Cone `V = (1/3)πr²h` · Pyramid `V = (1/3)ℓwh`
Degrees in a circle = 360 · Radians in a circle = 2π · Angles in a triangle = 180

**⚠️ You still have to know what to plug in.** Half of geometry misses are setup, not formula.

## 1.2 Linear 🧠

| Form            | Equation                  | Use it when                               |
| --------------- | ------------------------- | ----------------------------------------- |
| Slope-intercept | `y = mx + b`              | you have/need slope + y-intercept         |
| Point-slope     | `y − y₁ = m(x − x₁)`      | given a point and a slope                 |
| Standard        | `Ax + By = C`             | intercepts fast: x-int = C/A, y-int = C/B |
| Slope           | `m = (y₂ − y₁)/(x₂ − x₁)` | two points                                |

- Parallel → **same slope**. Perpendicular → **negative reciprocal** (`m₁m₂ = −1`).
- Systems: **1 solution** = different slopes · **infinite** = same line (all coefficients proportional) · **none** = same slope, different intercept.
- ⚠️ "No solution" and "infinitely many" questions are slope-comparison questions, not solving questions.

## 1.3 Quadratics & parabolas 🧠

| Form | Equation | Reads off instantly |
|---|---|---|
| **Standard** | `y = ax² + bx + c` | y-intercept = `c` |
| **Vertex** | `y = a(x − h)² + k` | vertex `(h, k)` |
| **Factored** | `y = a(x − r₁)(x − r₂)` | x-intercepts `r₁, r₂` |

- Axis of symmetry / vertex x: `x = −b/(2a)` (then plug in for y).
- Vertex from roots: `x = (r₁ + r₂)/2` — faster when it's already factored.
- Quadratic formula: `x = (−b ± √(b² − 4ac)) / (2a)`
- **Discriminant** `b² − 4ac`: `> 0` two real roots · `= 0` one (tangent/double root) · `< 0` none.
- `a > 0` opens up (min) · `a < 0` opens down (max).
- ⚠️ **Vertex form ⇒ sign flip.** `y = (x − 3)² + 5` has vertex `(3, 5)`; `y = (x + 3)² − 5` has vertex `(−3, −5)`.
- ⚠️ "Minimum value of the function" = the **k**, not the h. "Value of x where minimum occurs" = **h**.

## 1.4 Circles 🧠

**Standard form:** `(x − h)² + (y − k)² = r²` → center `(h, k)`, radius `r`.

- ⚠️ **Sign flips again**: `(x + 4)² + (y − 1)² = 25` → center `(−4, 1)`, `r = 5` (not 25).
- General form `x² + y² + Dx + Ey + F = 0` → **complete the square** on x and y:
  take half the x-coefficient, square it, add to both sides. Repeat for y.
- Arc length `= (θ/360)·2πr` · Sector area `= (θ/360)·πr²` · Radians: `s = rθ`, `A = ½r²θ`
- Degrees ↔ radians: `× π/180` and `× 180/π`.
- Central angle = arc measure. **Inscribed angle = half** the arc.

## 1.5 Exponents, radicals, polynomials 🧠

`xᵃ·xᵇ = xᵃ⁺ᵇ` · `xᵃ/xᵇ = xᵃ⁻ᵇ` · `(xᵃ)ᵇ = xᵃᵇ` · `x⁻ᵃ = 1/xᵃ` · `x⁰ = 1`
`x^(a/b) = ᵇ√(xᵃ)` · `√x = x^(1/2)` · `ᶜ√x = x^(1/3)`

Factoring you should see instantly:
- Difference of squares `a² − b² = (a+b)(a−b)`
- `a² + 2ab + b² = (a+b)²` · `a² − 2ab + b² = (a−b)²`
- **Zero ⇒ flip ⇒ factor**: root `2` → `(x − 2)`; root `−1` → `(x + 1)`. See [[001 Polynomial Tables]].
- Factor/Remainder theorem: `p(a) = 0` ⟺ `(x − a)` is a factor.

## 1.6 Exponential growth/decay & functions 🧠

- `y = a·bˣ` — `a` = initial, `b` = growth factor. `b > 1` growth, `0 < b < 1` decay.
- Percent change: `y = a(1 + r)ᵗ` (growth) · `y = a(1 − r)ᵗ` (decay).
- Compounded n times/yr: `y = a(1 + r/n)^(nt)`.
- ⚠️ **Linear = constant amount added; exponential = constant percent/factor multiplied.** That's the whole "which model" question.
- Transformations: `f(x) + k` up · `f(x + k)` **left** · `−f(x)` flip over x-axis · `f(−x)` flip over y-axis · `a·f(x)` vertical stretch.
- ⚠️ Horizontal shifts go the **opposite** direction of the sign.
- Asymptotes (your flagged gap): vertical where **denominator = 0** (and doesn't cancel); horizontal by comparing degrees — bottom-heavy → `y = 0`; equal degrees → `y = ` ratio of leading coefficients; top-heavy → none.

## 1.7 Statistics & data 🧠

- Mean `= sum/count` · Median = middle when ordered · Mode = most frequent · Range = max − min.
- ⚠️ **Sum = mean × count** — this solves most "what's the missing value" questions.
- Outlier pulls the **mean**, not the median. Skewed right → mean > median. Skewed left → mean < median.
- Standard deviation = spread only. More clustered → smaller SD. **Never compute it; compare it.**
- Percent change `= (new − old)/old × 100`. Percent of `=` part/whole.
- ⚠️ Increase by 20% then decrease by 20% ≠ original (`×1.2×0.8 = 0.96`).
- Probability `= favorable/total`; from a two-way table, the denominator is whatever group the question restricts to.
- Margin of error / confidence: bigger **random** sample → narrower interval. Conclusions generalize only to the **population sampled**, and causation only from **random assignment**.

## 1.8 Geometry & trig extras 🧠

- **SOH-CAH-TOA**; `sin θ = cos(90° − θ)` (complementary).
- Similar triangles → sides proportional; **area scales by k², volume by k³**.
- Angles: vertical = equal · parallel lines cut by transversal → corresponding/alternate equal, same-side interior = 180.
- Polygon interior angle sum `= (n − 2)·180`.
- Distance `= √((x₂−x₁)² + (y₂−y₁)²)` · Midpoint `= ((x₁+x₂)/2, (y₁+y₂)/2)`.

## 1.9 Desmos triggers ⚡
Type it into Desmos instead of solving when you see: **systems of equations** (graph both, read intersection), **any "for what value of x" with ugly numbers**, **vertex/max/min**, **x-intercepts/roots**, **circle center-radius**, **quadratic with non-integer answers**, **table-of-values matching**. Type the equation exactly as printed; click the gray dots for exact points.

---

# PART 2 — GRAMMAR

## 2.0 The one question that solves punctuation
**Left of the blank: independent clause or not? Right of the blank: independent clause or not?**
Answer that before looking at the choices.

- **IC** = could stand alone as a sentence.
- **DC** = has subject+verb but starts with *because, although, since, while, when, if, unless, until, after, before, which, who, that…*

## 2.1 Joining two independent clauses (IC + IC) — only 4 legal ways
1. `IC. IC.` (period)
2. `IC; IC.` (semicolon)
3. `IC, FANBOYS IC.` (**F**or **A**nd **N**or **B**ut **O**r **Y**et **S**o)
4. `IC: IC.` (colon — only if the second explains the first)

> ⚠️ **Two-identical-answers trick:** period and semicolon do the *same* job. If both appear as choices for the same blank, **cross out both instantly** — neither can be the single correct answer.

## 2.2 Semicolon — the short version
- **Semicolon = period.** Full sentence on **both** sides. Nothing less.
- ✅ *The trail was steep; we climbed it anyway.*
- ❌ *The trail was steep; climbing it anyway.* (right side isn't a sentence)
- Second legal use: separating **list items that already contain commas**.
- ⚠️ *however, therefore, moreover, nevertheless, consequently, thus, furthermore, instead, for example* are **NOT** FANBOYS. A comma before them between two ICs is a splice.
  - ❌ *The data was incomplete, however, the team published.*
  - ✅ *The data was incomplete; however, the team published.*

## 2.3 Colon
- **Everything before the colon must be a complete sentence.** After it: anything (list, word, phrase, clause).
- ✅ *She packed three things: a passport, a map, and sunscreen.*
- ❌ *She packed: a passport, a map, and sunscreen.*
- **Never a colon after** *such as, including, like, for example, are, was, consists of*.
- ⚠️ **Always look LEFT of the colon. Never right.** The pretty list is bait.

## 2.4 Comma — the only jobs it has
1. `IC, FANBOYS IC`
2. After an **introductory** element (*After the storm, / Because it rained, / Running quickly,*)
3. **Both sides** of a nonessential interrupter
4. Between items in a list of 3+
5. Before a DC only when needed for clarity

**Never:**
- ⚠️ Between **subject and verb** (*The scientists who ran the trial, published…* ❌) — a long subject does **not** license a "breathing" comma.
- ⚠️ Between verb and its object; almost never before **that**.
- ⚠️ A comma alone between two ICs = **comma splice**. It *sounds fine out loud* — never check this rule by ear.

## 2.5 Dashes
- A **pair** of dashes = a pair of commas (interrupter).
- A **single** dash before an end-of-sentence break = a colon there.
- ⚠️ **Matched pair rule:** dash…dash or comma…comma. **Never dash…comma.** The opening mark is usually *outside the underline* — look for it.

## 2.6 Essential vs. nonessential (the comma test)
Cover the phrase. Does the sentence still tell you **which one**?
- Still clear → extra → **commas both sides**.
- Now vague → essential → **no commas**.

| | Essential (no commas) | Nonessential (commas) |
|---|---|---|
| Things | **that** | **, which,** |
| People | **who** | **, who,** |
| Names | *The novelist Zadie Smith spoke.* | *My oldest sister, Dana, spoke.* |

- ⚠️ **Bare "which" with no comma is essentially always wrong.**
- ⚠️ **One comma around an interrupter is wrong.** Both or neither.

## 2.7 Apostrophes
| Case | Form |
|---|---|
| One owner | `student's` |
| Many owners (plural ends in s) | `students'` |
| Irregular plural | `children's`, `women's`, `men's` |
| Plain plural, no ownership | **no apostrophe** |
| Possessive pronouns | **never**: *its, hers, theirs, ours, yours, whose* |
| Contractions | *it's = it is* · *who's = who is* · *they're = they are* |

⚠️ The real tested question is usually **singular vs. plural possessive of the same noun** (*the scientist's findings* vs. *the scientists' findings*) — decide from the passage how many there are.

## 2.8 Quotation marks
- **Periods and commas go INSIDE** the closing quotation mark. Always, in US usage.
  - ✅ *She called it "a triumph."* ❌ *…"a triumph".*
- **Colons and semicolons go OUTSIDE.**
  - ✅ *He called it "a triumph"; critics disagreed.*
- **Question marks / exclamation points**: inside if the **quote** is the question, outside if the **sentence** is.
  - *She asked, "Are we late?"* vs. *Did she really call it "a triumph"?*
- Introducing a quotation:
  - Short quote after *said/argued/noted* → **comma**: *Smith noted, "The data was thin."*
  - Full sentence before it → **colon**: *Smith's conclusion was blunt: "The data was thin."*
  - Quote woven into your own grammar → **no punctuation**: *Smith called the data "thin and unconvincing."*
- ⚠️ Punctuation still has to work **outside** the quote too — the sentence containing the quotation needs to be grammatical on its own.

## 2.9 Subject-verb agreement (your known gap — read twice)
**Find the real subject, ignore everything between it and the verb.**
- ⚠️ Prepositional phrases never contain the subject: *The **box** of old letters **is** heavy.*
- ⚠️ **Inverted order**: *There **are** several **reasons**…* / *Near the shore **stand** three **towers**.*
- ⚠️ Compounds: *A and B* → plural. *A, along with / as well as / in addition to B* → **singular** (A alone).
- ⚠️ *Each, every, either, neither, one, none, anyone, everybody, nobody* → **singular**.
- ⚠️ *Neither X nor Y* → verb matches the **nearer** noun.
- Collective nouns (*team, committee, jury*) → singular on the SAT.
- Pronouns follow the same rule: *Each student turned in **their** essay* → SAT wants **his or her**/rewrite; watch for a singular antecedent with a plural pronoun.

## 2.10 Verbs, modifiers, parallelism
- **Tense:** match the surrounding passage; don't switch without a time cue. Consistency > sophistication.
- **Dangling/misplaced modifier:** the noun right after an opening modifier phrase must be the thing doing it.
  - ❌ *Running late, the bus was missed.* ✅ *Running late, she missed the bus.*
  - ⚠️ On any question starting with an *-ing* or *-ed* phrase, check the **first noun after the comma** before anything else.
- **Parallelism:** items in a list / after *both…and, either…or, not only…but also, than, as* must share the same grammatical form.
  - ❌ *hiking, swimming, and to fish* ✅ *hiking, swimming, and fishing*
- **Comparison:** compare like to like. *Her scores are higher than **those of** her classmates* (not "than her classmates"). Use *fewer* for count, *less* for amount.

## 2.11 Transitions — pick by relationship, not by sound
| Relationship | Words |
|---|---|
| Add | moreover, furthermore, in addition, also |
| Contrast | however, nevertheless, on the other hand, conversely, still, yet |
| Cause → effect | therefore, thus, consequently, as a result, hence |
| Example | for example, for instance, specifically |
| Sequence | first, then, subsequently, finally |
| Concede | admittedly, granted, of course |
| Restate | in other words, that is |
| Compare | similarly, likewise |

⚠️ **Method:** cover the choices. Read the sentence before and the sentence after. Say the relationship in your own words ("this contradicts that"). *Then* pick. Never plug in choices one by one.

## 2.12 Rules the SAT does NOT test
Split infinitives · ending a sentence with a preposition · starting with *And*/*But* · *who* vs. *whom* in most cases · Oxford comma preference · spelling · vocabulary trivia.
⚠️ **Shortest grammatical answer usually wins** when meaning is identical — but grammar beats brevity every time.

---

## 60-Second Pre-Test Scan
1. Vertex form flips the sign; circle form flips the sign.
2. Semicolon = period. Full sentence both sides.
3. Look **left** of the colon.
4. Two answers doing the same job → both wrong.
5. Ignore everything between subject and verb.
6. First noun after an opening modifier must be the doer.
7. Periods and commas go **inside** quotes.
8. Sum = mean × count.
9. Slopes decide "no solution" vs. "infinitely many."
10. Desmos it before you solve it.

---

Log every miss into [[Formula Vault]] / [[English Rule Vault]] per [[Adaptive Review System]] after the test.
