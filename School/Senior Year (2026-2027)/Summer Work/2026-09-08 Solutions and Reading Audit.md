---
date: 2026-09-08
tags: [school, summer-work, verification, corrections]
status: checked against supplied packets; limitations stated below
---

# Summer-work corrections

Read this alongside [Calculus solutions](AP%20Calculus/AP_Calculus_Summer_Packet_Solutions.md), [Physics solutions](AP%20Physics/AP_Physics_Summer_Work_Solutions.md), and [Reading analysis](Honors%20World%20Literature/Summer_Reading_Analysis.md). Original files are preserved. This is a review, not evidence that the assignments have been completed or submitted.

## Calculus: confirmed corrections

Source: [original assignment](AP%20Calculus/2026%20AP%20Calculus%20Summer%20Assignment.pdf), including direct inspection of PDF pages 1, 2 and 6. Calculations use radians where appropriate.

| Item | Problem in existing answer | Correct result and reasoning |
|---|---|---|
| A3a | Graph readings f(3)≈3 and h(3)≈0.5 are wrong | f(3)=2 and h(3)=3, so (f−h)(3)=−1. |
| A3b | Composition based on those wrong readings | f(h(3))=f(3)=2. The rising branch of f passes through (0,−1), not (0,0). |
| B13 | Horizontal asymptote reported as y=3 | Dashed horizontal line is y=2. Domain excludes x=−2; range is (−∞,2) ∪ (2,∞). |
| B14 | Upper range bound reported as 3 | The vertical scale reads 1 at the initial maximum, 0.5 at the next tick, and −0.5 at the lowest trough. Range is approximately [−0.5,1], assuming the intended damped curve starts at x=0 and continues right. Domain [0,∞) is a continuation interpretation: the drawing alone has no explicit right-hand arrow. |
| D7–12 | All drawings derive from an incorrectly transcribed base graph | Original base vertices are (−4,0), (0,2), (2,−2), (3,0), with straight segments. The x-axis was mistaken for additional horizontal function segments; peak height and left endpoint were also misread. Use the replacement vertex table below. |
| N2 | Only two roots listed | 2x²−1=2ˣ has three real solutions: x≈−0.878605, 1.323337, **6.285836**. The third lies outside a narrow default graph window. |

For N2 set F(x)=2x²−1−2ˣ. Sign changes occur in (−1,0), (1,2), and (6,7). Bisection and substitution give residual magnitudes below 2×10⁻¹⁴ at the reported unrounded roots. There cannot be a fourth root: F'''(x)=−(ln 2)³2ˣ<0, so four distinct zeros would contradict Rolle's theorem.

### Replacement vertices for D7–12

Connect each listed sequence by straight lines; do not extend along the x-axis outside the original domain. No open endpoints are marked in the supplied base graph.

| Item | Ordered vertices |
|---|---|
| D7: 2f(x) | (−4,0), (0,4), (2,−4), (3,0) |
| D8: −f(x) | (−4,0), (0,−2), (2,2), (3,0) |
| D9: f(x−1) | (−3,0), (1,2), (3,−2), (4,0) |
| D10: f(x)+2 | (−4,2), (0,4), (2,0), (3,2) |
| D11: absolute value of f(x) | (−4,0), (0,2), (1,0), (2,2), (3,0) |
| D12: f(absolute value of x) | (−3,0), (−2,−2), (0,2), (2,−2), (3,0) |

D11 needs the extra corner at x=1 because the segment crosses zero there. D12 copies the nonnegative-x half across the y-axis; its domain is [−3,3].

### Other checks and qualifications

The written algebra in A (apart from A3), B1–12, E–M, and the numerical results in N1 and N3–5 were reviewed. No other numerical error was identified. Independently recomputed values: N1 1.279166; N3 1.241962 and 5.564498; N4 x=0, 1.032832, 2, 3.262092; N5 critical points 0.530607 and 1.130851 with h≈−3.623075 and −4.076555. J16≈4.630930 and J18≈1.412489 are consistent with the existing rounding.

Preserve original domains when simplifying: A1c requires h≠0; A2c requires r≠0; negative-power expressions in I retain their original nonzero restrictions, even when the final expression looks polynomial. G8 lists the real solution 5; if complex solutions are requested, also include ±i√5. E4 factors over integer/rational coefficients as given; over real coefficients x²−5 can factor further.

H3 can explicitly state horizontal asymptote y=2, in addition to the hole (−8,2). C's written feature summaries were checked, but its embedded base64 graph panels have **not** each received a pixel-level audit. The phrase “accurate sketches” in the original should not be read as independent verification of every panel.

## Physics

Source: [original assignment](AP%20Physics/AP%20Physics%20Summer%20Work.pdf), including direct diagram inspection on PDF pages 15–16.

**Magnitude/trigonometry problem 5 is in quadrant IV, not III.** The arrow points down and right, at 80° below the positive horizontal. Correct components:

Ax=15cos80°≈+2.60; Ay=−15sin80°≈−14.77.

Thus A≈2.60i−14.77j, direction 80° South of East. The existing negative x-component and “South of West” are wrong.

Diagram 2's angle is from the vertical: its existing 20sin40° and 20cos40° assignment is correct. Diagrams 3 and 8 also agree with the supplied arrows. The component arithmetic, magnitudes and final multi-vector sums were reviewed and are consistent to stated rounding.

Completeness still matters:

- The graphical vector-addition and scalar-multiplication section gives a method, not the required individual completed drawings. Drawings remain work to do unless already completed on paper.
- The scale-drawing section also supplies numbers rather than finished scale drawings. Include a scale legend and arrowheads.
- Six component examples give resultant magnitudes but omit resultant directions. If reporting these resultants, add respectively: 26.6° N of W; 56.3° N of E; 76.0° S of E; 71.6° N of W; 63.4° S of W; 73.3° N of E.
- For zero resultant, direction is undefined. Do not assign a compass angle.
- The magnetic field itself is a vector; the explanation should not equate magnetic field with force. Both are vector quantities, but they are different physical quantities.

## Literature

The [requirements](Honors%20World%20Literature/Summer%20Reading%20Requirements.md) explicitly require reading the books, passage/page records, questions and personal reflections. A prepared analysis sheet does not satisfy those parts.

### Night: factual corrections

1. The sentence saying he never sees his mother **and sisters** again is wrong. His mother and youngest sister Tzipora were murdered; his older sisters Beatrice and Hilda survived and were reunited with him. This also contradicts the existing analysis's own later paragraph. [USHMM biography](https://encyclopedia.ushmm.org/content/en/article/elie-wiesel).
2. Replace “death march evacuating Buchenwald/Auschwitz” with the route **Buna/Monowitz in the Auschwitz complex → Gleiwitz → transport to Buchenwald**. Buchenwald was the destination of this January evacuation, not its starting point. [USHMM map](https://encyclopedia.ushmm.org/content/en/gallery/elie-wiesel-maps).
3. Avoid claiming the child's hanging happened at night without a passage supporting that timing. Night/darkness is a defensible motif; it does not establish the time of every atrocity.
4. “Death of his faith” is too absolute as a settled conclusion. Frame the reading around crisis, protest and struggle with faith, and support it with specific passages. Likewise, describe survival under coercion rather than treating loss of empathy as a simple personal moral flaw.
5. Do not claim a reunion is “briefly mentioned” in the assigned edition without checking that edition. Separate later biographical knowledge from events actually narrated in the memoir.

### The Kite Runner and A Raisin in the Sun

The supplied summaries are broadly coherent, but this pass did not compare every statement against a full local copy of either book. In The Kite Runner, describe Ali as Hassan's **social/raising father**, and Baba as his biological father; the current shorthand is confusing beside the parentage reveal. Avoid treating Amir's rescue as erasing Sohrab's trauma: the ending offers tentative hope, not complete recovery. In Raisin, retain the distinction between Willy stealing the entrusted funds and the family's refusal of Lindner's offer; the lost money is not recovered by the final moral choice.

For each theme, add one concrete event plus a passage locator from the actual edition. Keep personal reflections genuinely personal. No invented page numbers, feelings or claims of having read the books.

## Submission check

- [ ] Correct A3, B13–14, D7–12 and N2 on the calculus packet.
- [ ] Correct the sign/direction in Physics problem 5 and complete drawings.
- [ ] Replace the two contradictory/incorrect Night facts in study materials.
- [ ] Check original packet for every blank; mark written work separately from AI solution availability.
- [ ] Use actual teacher deadlines; the existing September 14 / September 20 schedule is a recorded plan, not newly verified teacher confirmation.
