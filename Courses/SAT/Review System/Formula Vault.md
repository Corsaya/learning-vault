---
tags: [sat, formulas, review]
created: 2026-08-19
related: ["[[Adaptive Review System]]", "[[English Rule Vault]]", "[[Claude Instructions]]"]
---

# Formula Vault

Use this vault for formulas uncovered through the [[Adaptive Review System]].

## Geometry

**SOH-CAH-TOA — map the side to the angle before picking the ratio.** *From
[[Bluebook Practice Test — 2026-08-20]], Math M1 Q20 (chose cos, answer was sin).*

Right angle at R, SR = 18, asked for the hypotenuse QS:
SR is **opposite** angle Q, so `sin Q = 18/QS` → `QS = 18/sin Q`.

Procedure: label **opposite / adjacent / hypotenuse relative to the named angle** first, then
choose the ratio. Choosing the ratio first is what produces the cos/sin swap.

**Angles formed by two intersecting lines.** *Math M2 Q17.*
Two lines crossing make two acute and two obtuse angles. Vertical angles are equal; adjacent
angles are supplementary (sum 180°). Any two of the four sum to either **180°** or **twice one
of them** — the "could NOT be" answer is the sum that fits neither.

## Algebra

**"At least one solution" includes infinitely many.** *From
[[Bluebook Practice Test — 2026-08-20]], Math M2 Q19.*

| Relationship | Solutions | Counts as "at least one"? |
|---|---|---|
| Different slopes | exactly one | ✅ |
| Same line (all coefficients proportional) | infinitely many | ✅ **don't exclude this** |
| Same slope, different intercept | none | ❌ |

`2x + 9y = 7` and `3x + 13.5y = 10.5` are the same line (×1.5). Check proportionality across
**all three** coefficients before calling a system parallel.

**Reading a value off an intercept.** *Math M1 Q19.* When a graph's intercept represents "all
of the quantity in one variable," the per-unit value is `total ÷ intercept`. Confirm **which
axis** the intercept is on before dividing — an x-intercept and a y-intercept give different
answers, and both are usually offered.

## Functions

**Rational function — the numerator's roots are the function's zeros.** *From
[[Bluebook Practice Test — 2026-08-20]], Math M2 Q16.*

For `g(x) = (x² − x − a)/(x³ − x − b)`:
- `g(k) = 0` ⟹ plug `k` into the **numerator** and set it to 0.
- `g(0)` = (constant term of numerator) / (constant term of denominator) = `−a/−b = a/b`.

Given `g(−22) = 0` → `484 + 22 − a = 0` → `a = 506`; given `g(0) = 22` → `b = a/22 = 23`.

**Factored form off a polynomial graph.** *Math M2 Q21.* Each x-intercept where the curve
**bounces** is a squared factor `(x − r)²`; each one it **crosses** is a single factor.
Read the roots off the graph, flip the signs, then match — including any horizontal shift
applied to the input (`g(x + 28)` shifts the roots by 28).

**Rational exponents.** *Math M2 Q15 — method was correct, the final division was not.*
`ⁿ√(aᵐ) = a^(m/n)`. Set the exponents equal, solve, and **re-check the last arithmetic step**;
this one was lost by dividing by 9 instead of 81.

## Statistics


## Probability

**Compound conditions — apply every restriction before counting.** *From
[[Bluebook Practice Test — 2026-08-20]], Math M2 Q12.*

Integers 1–160, "even **and** ≤ 50" → 25 favorable, not 50. `25/160 = 5/32`.
Underline each condition in the question and tick it off as you count; dropping one is what
produced `5/16` here.

**Chained percent relationships.** *Math M2 Q22.* "A is 468% of B" → `A = 4.68B`. "A is 0.780%
of C" → `A = 0.00780C`. Set the two expressions equal and solve for the relationship asked.
Convert every percent to a decimal multiplier **before** combining — and expect an answer that
looks absurd (60,000%) when the two percentages differ by orders of magnitude.


## Future Additions


For grammar rules, see [[English Rule Vault]]. [[Claude Instructions]] governs updates to this vault.

---

- Written by Codex (GPT-5), 2026-08-19.
