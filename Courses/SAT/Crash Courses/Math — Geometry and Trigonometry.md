---
tags: [pytheas, sat, math, geometry, trigonometry, crash-course]
created: 2026-08-12
source: "Foundations Knowledge Check G1-G8"
related: ["[[../Foundations Knowledge Check]]", "[[../Research/Bluebook Tools and Pacing Reference (2026-08-12)]]"]
---

# Math — Geometry & Trigonometry Crash Course

This domain is ~15% of the Math section (5–7 questions per the existing
[[../Research/Official SAT Structure and Content Research (2026-08-07)|Official SAT Structure research]]) — the smallest of the three math
domains, but a good one to lock down fast since most of it is either given
to you outright or a short, memorizable rule. Covers G1–G8 from the
[[../Foundations Knowledge Check]].

**The reference-sheet split — know this before you study anything below.**
Per the [[../Research/Bluebook Tools and Pacing Reference (2026-08-12)|2026-08-12 research]], the digital SAT's
built-in reference sheet is **geometry-only** — about 15 formulas: area of a
rectangle/triangle/circle, circumference, volumes of a rectangular solid,
cylinder, sphere, cone, and pyramid, the Pythagorean theorem, both special
right triangle ratios (drawn out as diagrams), "a circle has 360° = 2π
radians," and "the angles of a triangle sum to 180°." That's it — nothing
about coordinate geometry, similarity, or trig is on it. Per skill:

| Skill | On the reference sheet? |
|---|---|
| G1 — area/volume formulas | **Yes, fully.** Every formula you need is given. |
| G2 — Pythagorean theorem + special right triangles | **Yes, fully.** Both the theorem and both triangle ratio diagrams are given. |
| G3 — arc length, sector area, central/inscribed angles | **Partially.** Circle area/circumference and "360° = 2π radians" are given; the arc-length/sector-area *proportion setup* and the central-inscribed angle relationship are **not** — you must know how to use the givens. |
| G4 — circle equation | **No.** Memorize $(x-h)^2+(y-k)^2=r^2$. |
| G5 — similar triangles | **No.** No proportion formula is given; know the method. |
| G6 — right-triangle trig (SOH-CAH-TOA) | **No.** Not on the sheet at all. |
| G7 — trig identities | **No.** Not on the sheet at all. |
| G8 — angle relationships | **Partially.** Triangle angle sum (180°) is given; parallel-line/transversal angle rules are **not**. |

So the real memorization load in this domain is G4, G5, G6, G7, and the
transversal half of G8 — five and a half items, not eight. The rest is
about recognizing *when* to reach for a formula that's already sitting in
front of you.

---

### G1 — Area/perimeter/volume formulas

**What this actually tests:** can you pick the right formula out of the
reference sheet and plug in correctly — including 3D shapes where it's easy
to mix up which dimension is which.

**Reference sheet:** ON it — rectangle, triangle, circle area/circumference,
and volumes of a rectangular solid, cylinder, sphere, cone, and pyramid are
all given formulas.

**Core rule:**
$$A_{\text{rect}} = lw \qquad A_{\text{triangle}} = \tfrac{1}{2}bh \qquad A_{\text{circle}} = \pi r^2 \qquad C = 2\pi r$$
$$V_{\text{rect. solid}} = lwh \qquad V_{\text{cylinder}} = \pi r^2 h \qquad V_{\text{sphere}} = \tfrac{4}{3}\pi r^3 \qquad V_{\text{cone}} = \tfrac{1}{3}\pi r^2 h$$

**Worked example:** A cylindrical water tank has radius 4 ft and height 9 ft.
Find its volume in terms of $\pi$.
$$V = \pi r^2 h = \pi (4)^2 (9) = \pi (16)(9) = 144\pi \text{ ft}^3$$

**Shortcut/trap:** the cone and pyramid volumes have an extra $\tfrac{1}{3}$
that the cylinder/rectangular-solid versions don't — it's easy to forget
that factor under time pressure even with the formula right in front of
you. Double-check you copied the whole formula, not just the shape part.

**Worked example 2:** A rectangular storage box has length 5 ft, width 4 ft,
and height 3 ft. Find its volume.
$$V = lwh = (5)(4)(3) = 60 \text{ ft}^3$$

**Shortcut/trap:** rectangular solid volume has no fraction in front — it's
just the product of all three dimensions. Don't second-guess yourself into
adding a $\tfrac{1}{3}$ or $\tfrac{4}{3}$ from the cone/sphere formulas;
those factors only belong to shapes that taper to a point or curve back on
themselves.

**Worked example 3:** A sphere has radius 6. Find its volume in terms of
$\pi$.
$$V = \tfrac{4}{3}\pi r^3 = \tfrac{4}{3}\pi (6)^3 = \tfrac{4}{3}\pi (216) = 288\pi$$

**Shortcut/trap:** cube the radius *before* multiplying by $\tfrac{4}{3}$ —
a common slip is squaring $r$ (copying the pattern from area/cylinder
formulas) instead of cubing it, which silently produces a much smaller,
wrong answer.

---

### G2 — Pythagorean theorem + special right triangles

**What this actually tests:** finding a missing side of a right triangle,
either generically or via the fixed ratios of 30-60-90 and 45-45-90
triangles (much faster than Pythagorean theorem when they apply).

**Reference sheet:** ON it — the theorem and both special-triangle diagrams
(with ratios labeled) are given.

**Core rule:**
$$a^2 + b^2 = c^2 \quad (c = \text{hypotenuse})$$
- **45-45-90:** legs are equal, ratio $x : x : x\sqrt{2}$ (leg : leg : hypotenuse).
- **30-60-90:** ratio $x : x\sqrt{3} : 2x$ (short leg opposite 30° : long leg opposite 60° : hypotenuse).

**Worked example:** A 30-60-90 triangle has a short leg of 5. Find the
hypotenuse and long leg.
Using $x : x\sqrt{3} : 2x$ with $x = 5$: hypotenuse $= 2(5) = 10$, long leg
$= 5\sqrt{3}$.

**Shortcut/trap:** recognizing a special triangle (angles given, or side
ratios that look like $1:\sqrt3:2$ or equal legs) saves a full Pythagorean
calculation — but if you're not sure it's actually 30-60-90 or 45-45-90,
Pythagorean theorem always works and never assumes an angle you haven't
confirmed.

**Worked example 2:** A right triangle has legs of length 9 and 12. Find
the hypotenuse.
$$a^2+b^2=c^2 \Rightarrow 9^2+12^2=c^2 \Rightarrow 81+144=225=c^2 \Rightarrow c=15$$

**Shortcut/trap:** notice $9:12:15$ reduces to $3:4:5$ — recognizing common
Pythagorean triples (3-4-5, 5-12-13, 8-15-17, and their multiples) lets you
skip the squaring/adding entirely once you spot the pattern.

**Worked example 3:** A 45-45-90 right triangle has a hypotenuse of
$8\sqrt{2}$. Find the length of one leg.
Using $x : x : x\sqrt2$ with $x\sqrt2 = 8\sqrt2$: $x = 8$, so each leg is 8.

**Shortcut/trap:** when the hypotenuse is given as "(number)$\sqrt2$," the
leg is just that number — you don't need to divide by $\sqrt2$ and rationalize
if the problem already handed you the hypotenuse in that exact form.

---

### G3 — Circle theorems: arc length, sector area, central/inscribed angles

**What this actually tests:** treating an arc or sector as a *fraction of
the whole circle*, and knowing the fixed 2:1 relationship between a central
angle and the inscribed angle that intercepts the same arc.

**Reference sheet:** PARTIAL — circle area/circumference and "a circle has
360° (or $2\pi$ radians) of arc" are given; the proportion setup itself and
the inscribed-angle rule are not spelled out — you have to know how to
build them from those givens.

**Core rule:**
$$\text{arc length} = \frac{\theta}{360^\circ} \times 2\pi r \qquad \text{sector area} = \frac{\theta}{360^\circ} \times \pi r^2$$
where $\theta$ is the central angle in degrees. **Inscribed angle theorem:**
an inscribed angle is always **half** the central angle that intercepts the
same arc.

**Worked example:** A circle has radius 9. A central angle of 60° cuts off
an arc. Find the arc length.
$$\text{arc length} = \frac{60}{360} \times 2\pi(9) = \frac{1}{6} \times 18\pi = 3\pi$$

**Shortcut/trap:** it's always "part over 360," never "part over the whole
circumference/area number directly" — write the fraction $\theta/360$ first,
then multiply by the *whole-circle* formula, so you don't accidentally use
the arc's own length as if it were the radius.

**Worked example 2:** A circle has radius 12. A central angle of 90° cuts
off a sector. Find the sector's area.
$$\text{sector area} = \frac{90}{360} \times \pi(12)^2 = \frac{1}{4} \times 144\pi = 36\pi$$

**Shortcut/trap:** a 90° central angle is always exactly one quarter of the
circle — recognizing "nice" fractions (90° = 1/4, 120° = 1/3, 180° = 1/2)
lets you skip writing out the full $\theta/360$ fraction and go straight to
the simplified multiplier.

**Worked example 3:** An inscribed angle intercepts an arc, and that same
arc is also intercepted by a central angle. If the inscribed angle measures
35°, find the central angle.
Since the inscribed angle is always half the central angle: central angle
$= 2 \times 35° = 70°$.

**Shortcut/trap:** this is the *reverse* direction of the inscribed angle
theorem — going from inscribed to central, you multiply by 2 instead of
dividing by 2. Reread the question to see which angle you're given before
picking the operation.

---

### G4 — Circle equation

**What this actually tests:** reading off (or reverse-engineering via
completing the square) a circle's center and radius from its equation.

**Reference sheet:** NOT on it — memorize the form.

**Core rule:**
$$(x-h)^2 + (y-k)^2 = r^2 \quad \Rightarrow \quad \text{center } (h,k), \text{ radius } r$$
If the equation is given in general form ($x^2+y^2+Dx+Ey+F=0$), complete
the square on the $x$-terms and $y$-terms separately to get it into
$(x-h)^2+(y-k)^2=r^2$ form.

**Worked example:** Find the center and radius of $(x-3)^2 + (y+2)^2 = 25$.
Rewrite $(y+2)^2$ as $(y-(-2))^2$: center $(3, -2)$, and $r^2 = 25$ so
$r = 5$.

**Shortcut/trap:** the signs inside the parentheses flip — $(x-3)^2$ means
the center's $x$-coordinate is $+3$, and $(y+2)^2$ means the center's
$y$-coordinate is $-2$. Read it as "$x$ minus $h$," not "$x$ plus whatever
number is written."

**Worked example 2:** Find the center and radius of the circle
$x^2 + y^2 - 6x + 4y - 3 = 0$.
Group and complete the square: $(x^2-6x) + (y^2+4y) = 3$
$\Rightarrow (x-3)^2 - 9 + (y+2)^2 - 4 = 3$
$\Rightarrow (x-3)^2 + (y+2)^2 = 16$. Center $(3, -2)$, radius $r = 4$.

**Shortcut/trap:** whatever you add inside the parentheses to complete the
square (here, $+9$ and $+4$) must also be added to the *other side* of the
equation — forgetting to balance both sides gives a wrong radius even when
the center comes out right.

**Worked example 3:** A circle has center $(-1, 5)$ and radius 7. Write its
equation.
$$(x-(-1))^2 + (y-5)^2 = 7^2 \Rightarrow (x+1)^2 + (y-5)^2 = 49$$

**Shortcut/trap:** this is the reverse direction — going from center/radius
to equation, a *negative* center coordinate becomes a *plus* sign inside
the parentheses ($x - (-1) = x+1$), which feels backwards if you're used to
always reading centers off of existing equations.

---

### G5 — Similar triangles

**What this actually tests:** matching up corresponding sides between two
similar triangles and solving a proportion — including "shadow"/real-world
setups where the triangles aren't drawn overlapping.

**Reference sheet:** NOT on it — no formula is given, but the method is
simple enough it shouldn't need one.

**Core rule:** if two triangles are similar (same angles, proportional
sides — often established via AA: two matching angles), then corresponding
sides are all in the same ratio:
$$\frac{AB}{DE} = \frac{BC}{EF} = \frac{AC}{DF}$$
Match vertices in the *order the similarity is stated* ($\triangle ABC \sim
\triangle DEF$ means $A \leftrightarrow D$, $B \leftrightarrow E$, $C
\leftrightarrow F$) — that tells you which sides correspond.

**Worked example:** $\triangle ABC \sim \triangle DEF$, with $AB = 6$,
$BC = 8$, $DE = 9$. Find $EF$.
$$\frac{AB}{DE} = \frac{BC}{EF} \Rightarrow \frac{6}{9} = \frac{8}{EF} \Rightarrow 6 \cdot EF = 72 \Rightarrow EF = 12$$

**Shortcut/trap:** cross-multiply, don't cross-cancel by eye under time
pressure — mismatching which side pairs with which is the single most
common error here, especially when the two triangles are drawn at
different orientations or aren't drawn touching at all.

**Worked example 2:** A 5-foot student casts a 3-foot shadow at the same
time a nearby flagpole casts a 21-foot shadow. How tall is the flagpole?
$$\frac{\text{student height}}{\text{student shadow}} = \frac{\text{pole height}}{\text{pole shadow}} \Rightarrow \frac{5}{3} = \frac{h}{21} \Rightarrow 3h = 105 \Rightarrow h = 35 \text{ ft}$$

**Shortcut/trap:** shadow problems are similar triangles even though no
triangle is drawn — the sun's rays hit both objects at the same angle, so
object height and shadow length form the two pairs of corresponding sides.
Keep "height over shadow" consistent on both sides of the proportion.

**Worked example 3:** $\triangle DEF \sim \triangle GHI$, with $DE = 10$,
$EF = 14$, $GH = 15$. Find $HI$.
$$\frac{DE}{GH} = \frac{EF}{HI} \Rightarrow \frac{10}{15} = \frac{14}{HI} \Rightarrow 10 \cdot HI = 210 \Rightarrow HI = 21$$

**Shortcut/trap:** the similarity ratio here is $10:15 = 2:3$ — once you
spot it, you can scale $EF=14$ by $\tfrac{3}{2}$ directly ($14 \times 1.5 =
21$) instead of setting up and cross-multiplying a full proportion.

---

### G6 — Right-triangle trig: sin/cos/tan (SOH-CAH-TOA)

**What this actually tests:** given a right triangle and an angle, finding
a trig ratio (or, in reverse, a side length given a ratio).

**Reference sheet:** NOT on it — memorize SOH-CAH-TOA.

**Core rule:** for an acute angle $\theta$ in a right triangle, relative to
$\theta$:
$$\sin\theta = \frac{\text{opposite}}{\text{hypotenuse}} \qquad \cos\theta = \frac{\text{adjacent}}{\text{hypotenuse}} \qquad \tan\theta = \frac{\text{opposite}}{\text{adjacent}}$$

**Worked example:** A right triangle has an angle $\theta$ with the side
opposite $\theta$ equal to 5 and hypotenuse 13. Find $\sin\theta$,
$\cos\theta$, $\tan\theta$.
First find the adjacent side: $\text{adj} = \sqrt{13^2 - 5^2} = \sqrt{169-25} = \sqrt{144} = 12$.
$$\sin\theta = \frac{5}{13} \qquad \cos\theta = \frac{12}{13} \qquad \tan\theta = \frac{5}{12}$$

**Shortcut/trap:** "opposite" and "adjacent" are defined *relative to
whichever angle you're evaluating* — the same triangle gives different
opposite/adjacent labels depending on which of the two acute angles you're
computing the ratio for. Always re-check which angle is $\theta$ before
labeling sides.

**Worked example 2:** A right triangle has an angle $\theta$ with the side
adjacent to $\theta$ equal to 9 and hypotenuse 15. Find $\sin\theta$,
$\cos\theta$, $\tan\theta$.
First find the opposite side: $\text{opp} = \sqrt{15^2-9^2} = \sqrt{225-81} = \sqrt{144} = 12$.
$$\sin\theta = \frac{12}{15} = \frac{4}{5} \qquad \cos\theta = \frac{9}{15} = \frac{3}{5} \qquad \tan\theta = \frac{12}{9} = \frac{4}{3}$$

**Shortcut/trap:** always simplify the final fractions — $9/15$ and
$12/15$ don't look like a familiar triple until you reduce them to $3/5$
and $4/5$, at which point you can recognize the underlying 3-4-5 triangle.

**Worked example 3:** In a right triangle, $\cos\theta = \tfrac{7}{25}$.
Find $\sin\theta$ and $\tan\theta$.
The hypotenuse is 25 and the adjacent side is 7, so the opposite side is
$\sqrt{25^2-7^2} = \sqrt{625-49} = \sqrt{576} = 24$.
$$\sin\theta = \frac{24}{25} \qquad \tan\theta = \frac{24}{7}$$

**Shortcut/trap:** given just one ratio, rebuild the whole right triangle
with the Pythagorean theorem before answering — don't try to guess the
missing ratio without finding the missing side first, since $\sin\theta$
and $\tan\theta$ depend on a side you weren't given directly.

---

### G7 — Trig identities: co-function relationship, Pythagorean identity

**What this actually tests:** using one trig value or ratio to get another
without a triangle drawn, via two fixed identities.

**Reference sheet:** NOT on it — memorize both identities.

**Core rule:**
$$\sin^2\theta + \cos^2\theta = 1 \quad \text{(Pythagorean identity)}$$
$$\sin(\theta) = \cos(90^\circ - \theta) \quad \text{(co-function identity — complementary angles)}$$
The co-function identity follows directly from SOH-CAH-TOA: in any right
triangle the two acute angles sum to 90°, and what's "opposite" one of them
is "adjacent" to the other — so sine of one angle always equals cosine of
its complement.

**Worked example:** If $\sin\theta = \tfrac{3}{5}$ and $\theta$ is acute,
find $\cos\theta$.
$$\sin^2\theta + \cos^2\theta = 1 \Rightarrow \cos^2\theta = 1 - \frac{9}{25} = \frac{16}{25} \Rightarrow \cos\theta = \frac{4}{5}$$
(positive root, since $\theta$ is acute — cosine of an acute angle is always positive.)

**Shortcut/trap:** the co-function identity is the fast way to solve "if
$\sin(x°) = \cos(y°)$, find $x$ in terms of $y$" questions — set
$x = 90 - y$ directly instead of trying to compute either value numerically.

**Worked example 2:** If $\cos(x°) = \sin(40°)$ and $0 < x < 90$, what is
$x$?
By the co-function identity, $\cos(x°) = \sin(90° - x°)$, so
$90 - x = 40 \Rightarrow x = 50$.

**Shortcut/trap:** watch which function is on which side — here it's
cosine equal to sine, the mirror image of the standard "$\sin = \cos$"
setup, but the same rule applies: the two angles must sum to 90°.

**Worked example 3:** If $\cos\theta = \tfrac{5}{13}$ and $\theta$ is
acute, find $\sin\theta$ using the Pythagorean identity.
$$\sin^2\theta + \cos^2\theta = 1 \Rightarrow \sin^2\theta = 1 - \frac{25}{169} = \frac{144}{169} \Rightarrow \sin\theta = \frac{12}{13}$$

**Shortcut/trap:** same identity as before, just solving for $\sin\theta$
instead of $\cos\theta$ — don't memorize it as "always solve for cosine";
memorize the identity itself and isolate whichever variable the question
asks for.

---

### G8 — Angle relationships (parallel lines + transversal, triangle angle sum)

**What this actually tests:** two separate, small rule sets — the fixed
angle relationships created when a transversal crosses parallel lines, and
the fact that a triangle's angles always sum to 180°.

**Reference sheet:** PARTIAL — triangle angle sum (180°) is given;
parallel-line/transversal rules are **not** on the sheet.

**Core rule:** when a transversal crosses two **parallel** lines, eight
angles are formed, but only two measures exist among them:
- **Equal:** corresponding angles, alternate interior angles, alternate
  exterior angles, vertical angles.
- **Supplementary (sum to 180°):** co-interior / same-side interior angles,
  and any linear pair.

Triangle angle sum: $A + B + C = 180°$ for any triangle.

**Worked example:** Two parallel lines are cut by a transversal. One angle
formed measures 118°. Find its alternate interior angle and its co-interior
(same-side interior) angle.
Alternate interior angles are equal: $118°$.
Co-interior angles are supplementary: $180° - 118° = 62°$.

**Shortcut/trap:** don't try to memorize which named pair ("alternate
exterior," "corresponding," etc.) goes with which picture under time
pressure — instead just sort every angle in the diagram into one of two
buckets, "same as the angle I'm given" or "supplementary to it." Only
same-side interior pairs (and linear pairs) are supplementary; everything
else that isn't literally the same angle is equal.

**Worked example 2:** Two parallel lines are cut by a transversal. One
angle formed measures 73°. Find its corresponding angle and the angle that
forms a linear pair with it.
Corresponding angles are equal: $73°$.
A linear pair is supplementary: $180° - 73° = 107°$.

**Shortcut/trap:** "corresponding" angles sit in the *same relative
position* at each intersection (e.g., both upper-right) — if you can't
picture the position, fall back on the two-bucket rule: same angle unless
it's a same-side-interior or linear pair, in which case it's supplementary.

**Worked example 3:** In $\triangle PQR$, the angles measure $x°$,
$(x+20)°$, and $(2x-20)°$. Find the measure of the largest angle.
$$x + (x+20) + (2x-20) = 180 \Rightarrow 4x = 180 \Rightarrow x = 45$$
The three angles are $45°$, $65°$, and $70°$ — the largest is $70°$.

**Shortcut/trap:** when a triangle's angles are given as algebraic
expressions, set their sum equal to 180° first and solve for the variable
before evaluating any individual angle — plugging in a guessed value for
$x$ before solving is how these go wrong.

---

## Mini-Diagnostic

One question per skill, no notes. Answer key with brief solution steps is
at the bottom — don't peek until you've attempted all 8.

**G1.** A cone has radius 6 and height 8. Find its volume in terms of $\pi$.

**G2.** A 45-45-90 right triangle has a hypotenuse of 12. Find the length of one leg.

**G3.** In a circle, a central angle measures 80°. What is the measure of the inscribed angle that intercepts the same arc?

**G4.** A circle is given by the equation $x^2 + y^2 + 8x - 2y + 8 = 0$. Find its center and radius.

**G5.** A 6-foot person casts a 4-foot shadow at the same time a nearby tree casts a 30-foot shadow. How tall is the tree?

**G6.** A right triangle has legs of length 8 and 15 (hypotenuse 17). For the acute angle $\theta$ opposite the side of length 8, find $\tan\theta$.

**G7.** If $\sin(x°) = \cos(50°)$ and $0 < x < 90$, what is $x$?

**G8.** In $\triangle PQR$, the angles measure $3x$, $5x$, and $4x$ degrees. Find the measure of $\angle R$ (the $4x$ angle).

---

### Answer key

**G1.** $V = \frac{1}{3}\pi r^2 h = \frac{1}{3}\pi(36)(8) = 96\pi$

**G2.** Leg $: $leg$\sqrt2 = $hyp, so leg $= 12/\sqrt2 = 6\sqrt2$

**G3.** Inscribed angle = half the central angle: $80° \div 2 = 40°$

**G4.** Complete the square: $x^2+8x=(x+4)^2-16$, $y^2-2y=(y-1)^2-1$. So $(x+4)^2+(y-1)^2-16-1+8=0 \Rightarrow (x+4)^2+(y-1)^2=9$. Center $(-4, 1)$, radius $3$.

**G5.** Proportion: $\frac{6}{4} = \frac{h}{30} \Rightarrow 4h = 180 \Rightarrow h = 45$ ft

**G6.** $\tan\theta = \frac{\text{opp}}{\text{adj}} = \frac{8}{15}$

**G7.** Co-function identity: $\sin(x°) = \cos(90°-x°)$, so $90 - x = 50 \Rightarrow x = 40$

**G8.** $3x + 5x + 4x = 180 \Rightarrow 12x = 180 \Rightarrow x = 15$, so $\angle R = 4(15) = 60°$
