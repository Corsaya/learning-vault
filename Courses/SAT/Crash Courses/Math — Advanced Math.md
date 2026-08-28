---
tags: [pytheas, sat, math, advanced-math, crash-course]
created: 2026-08-12
source: "Foundations Knowledge Check M1-M15"
related: ["[[../Foundations Knowledge Check]]", "[[../Diagnostic Gap Lessons (2026-08-07)]]"]
---

# Math — Advanced Math Crash Course

Advanced Math is weighted ~35% of the Math section (13–15 questions) — tied with Algebra as
the largest domain on the digital SAT, per
[[../Research/Official SAT Structure and Content Research (2026-08-07)]]. This
doc covers all 15 skills (M1–M15) from
[[../Foundations Knowledge Check]] in one pass, ordered the same way they're listed there.

---

### M1 — Factor a quadratic (simple trinomial)

**What this actually tests:** whether you can reverse FOIL for $x^2 + bx + c$ — find two numbers
that multiply to $c$ and add to $b$.

**The rule:**
$$x^2 + bx + c = (x + p)(x + q) \quad \text{where } p \cdot q = c \text{ and } p + q = b$$
If $c$ is positive, $p$ and $q$ have the same sign (matching the sign of $b$). If $c$ is
negative, $p$ and $q$ have opposite signs.

**Worked example:** Factor $x^2 + 7x + 12$.
Need two numbers multiplying to $12$, adding to $7$: $3$ and $4$ ($3 \times 4 = 12$,
$3+4=7$).
$$x^2 + 7x + 12 = (x+3)(x+4)$$

**Trips people up:** when $c$ is negative, don't just grab two factors of $|c|$ — you need the
*signed* pair that actually adds to $b$. Test a couple of pairs mentally before committing.

**Worked example 2:** Factor $x^2 - 8x + 15$.
Need two numbers multiplying to $15$, adding to $-8$: $-3$ and $-5$ ($-3\times-5=15$,
$-3+-5=-8$).
$$x^2-8x+15=(x-3)(x-5)$$

**Trips people up:** when $b$ is negative but $c$ is positive, both numbers must be *negative*
— their product still needs to come out positive, so don't grab a positive/negative pair just
because $b$ is negative.

**Worked example 3:** Factor $x^2 + 2x - 24$.
Need two numbers multiplying to $-24$, adding to $2$: $6$ and $-4$ ($6\times-4=-24$,
$6+-4=2$).
$$x^2+2x-24=(x+6)(x-4)$$

**Trips people up:** with a negative constant, the two numbers have opposite signs, and the one
with the larger absolute value carries the sign of $b$ — here $b$ is positive, so the $6$ (not
the $4$) is the positive one.

---

### M2 — Solve a quadratic via factoring

**What this actually tests:** using the zero-product property once you've factored — if a
product equals zero, at least one factor must be zero.

**The rule:**
1. Get the equation into the form $\text{(expression)} = 0$.
2. Factor the expression.
3. Set each factor equal to $0$ and solve.

**Worked example:** Solve $x^2 - 2x - 15 = 0$.
Need two numbers multiplying to $-15$, adding to $-2$: $-5$ and $3$.
$$(x-5)(x+3) = 0 \implies x = 5 \text{ or } x = -3$$
Check: $5^2 - 2(5) - 15 = 25-10-15=0$ ✓. $(-3)^2-2(-3)-15 = 9+6-15=0$ ✓.

**Trips people up:** the equation must equal $0$ *before* you factor — if it's
$x^2-2x = 15$, move the $15$ over first. Factoring a non-zero-equals expression and setting
each piece to the right-hand side is a common wrong move.

**Worked example 2:** Solve $x^2+5x+6=0$.
Need two numbers multiplying to $6$, adding to $5$: $2$ and $3$.
$$(x+2)(x+3)=0 \implies x=-2 \text{ or } x=-3$$
Check: $(-2)^2+5(-2)+6=4-10+6=0$ ✓. $(-3)^2+5(-3)+6=9-15+6=0$ ✓.

**Trips people up:** with all-positive coefficients ($b$ and $c$ both positive), both roots come
out negative — don't second-guess a "no positive answers" result; check by substitution instead
of assuming you made a sign error.

**Worked example 3:** Solve $x^2-9=0$.
There's no middle term, but this is a difference of squares: $x^2-9=(x-3)(x+3)$.
$$(x-3)(x+3)=0 \implies x=3 \text{ or } x=-3$$
Check: $3^2-9=0$ ✓. $(-3)^2-9=0$ ✓.

**Trips people up:** a missing $x$-term doesn't mean the equation can't be factored — recognize
the $a^2-b^2=(a-b)(a+b)$ pattern instead of jumping straight to the quadratic formula.

---

### M3 — Solve a quadratic via the quadratic formula

**What this actually tests:** using the formula when factoring isn't clean (ugly numbers, no
integer factor pair).

**The rule:** for $ax^2+bx+c=0$:
$$x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$
Identify $a$, $b$, $c$ carefully (with signs), compute the discriminant first, then split into
the $+$ and $-$ cases.

**Worked example:** Solve $2x^2 + 3x - 5 = 0$.
$a=2,\ b=3,\ c=-5$. Discriminant: $b^2-4ac = 9 - 4(2)(-5) = 9+40=49$. $\sqrt{49}=7$.
$$x = \frac{-3 \pm 7}{4} \implies x = \frac{4}{4}=1 \ \text{ or } \ x = \frac{-10}{4}=-2.5$$
Check: $2(1)^2+3(1)-5 = 0$ ✓. $2(-2.5)^2+3(-2.5)-5 = 12.5-7.5-5=0$ ✓.

**Trips people up:** dropping the $\pm$, or plugging in $c$ without its sign (a very common
slip when $c$ is already negative — write $-4ac$ out with parentheses around $c$ before
simplifying).

**Worked example 2:** Solve $x^2-4x-1=0$.
$a=1,\ b=-4,\ c=-1$. Discriminant: $(-4)^2-4(1)(-1)=16+4=20$. $\sqrt{20}=2\sqrt5$.
$$x=\frac{4\pm2\sqrt5}{2} = 2\pm\sqrt5$$
Check: these are irrational, so no clean decimal check — verify by confirming $\sqrt{20}$
reduces to $2\sqrt5$ ($20=4\times5$) and that the $2$ in the numerator and denominator cancels
correctly.

**Trips people up:** don't leave $\sqrt{20}$ unsimplified, and don't forget to reduce the whole
fraction by any factor common to *both* terms in the numerator and the denominator — here every
term shares a factor of $2$.

**Worked example 3:** Solve $3x^2+2x+5=0$.
$a=3,\ b=2,\ c=5$. Discriminant: $2^2-4(3)(5)=4-60=-56$.
Negative discriminant → **no real solutions** (the formula would require $\sqrt{-56}$, which
isn't a real number).

**Trips people up:** don't force a decimal answer out of a negative number under the square
root — compute the discriminant first, and if it's negative, stop: the equation simply has no
real solutions.

---

### M4 — Complete the square

**What this actually tests:** rewriting $x^2+bx+c$ as a perfect square plus a constant — the
technique behind both solving quadratics and deriving vertex form.

**The rule:** for $x^2 + bx = (\text{number})$:
1. Take half of $b$, square it: $\left(\frac{b}{2}\right)^2$.
2. Add that to both sides.
3. The left side is now a perfect square: $\left(x + \frac{b}{2}\right)^2$.

**Worked example:** Solve $x^2 + 6x + 5 = 0$ by completing the square.
$$x^2+6x = -5$$
Half of $6$ is $3$; $3^2=9$. Add $9$ to both sides:
$$x^2+6x+9 = -5+9 = 4 \implies (x+3)^2 = 4$$
$$x+3 = \pm 2 \implies x = -1 \text{ or } x = -5$$
Matches factoring: $x^2+6x+5=(x+1)(x+5)$.

**Trips people up:** forgetting to add the same number to *both* sides — it's not just
"complete the left side," the equation has to stay balanced.

**Worked example 2:** Solve $x^2-10x+21=0$ by completing the square.
$$x^2-10x=-21$$
Half of $-10$ is $-5$; $(-5)^2=25$. Add $25$ to both sides:
$$x^2-10x+25=-21+25=4 \implies (x-5)^2=4$$
$$x-5=\pm2 \implies x=7 \text{ or } x=3$$
Matches factoring: $x^2-10x+21=(x-7)(x-3)$.

**Trips people up:** when $b$ is negative, half of $b$ is also negative — the binomial becomes
$(x-5)^2$, not $(x+5)^2$. Carry the sign through every step, not just the squaring.

**Worked example 3:** Solve $x^2+4x-3=0$ by completing the square.
$$x^2+4x=3$$
Half of $4$ is $2$; $2^2=4$. Add $4$ to both sides:
$$x^2+4x+4=3+4=7 \implies (x+2)^2=7$$
$$x+2=\pm\sqrt7 \implies x=-2\pm\sqrt7$$

**Trips people up:** not every completed-square equation ends with a perfect-square constant —
when the right side isn't a perfect square, the answer stays in $\pm\sqrt{\ }$ form; don't
force it into integers that don't actually check.

---

### M5 — Vertex form of a parabola: read vertex/max/min directly

**What this actually tests:** reading a parabola's vertex straight from its equation without
graphing or doing any algebra.

**The rule:** for $y = a(x-h)^2 + k$:
- Vertex is $(h, k)$ — watch the sign flip: $x - h$ means the vertex $x$-coordinate is
  $+h$, not $-h$.
- If $a > 0$, the parabola opens up → vertex is a **minimum**.
- If $a < 0$, the parabola opens down → vertex is a **maximum**.

**Worked example:** $y = 2(x-3)^2 + 7$. Vertex is $(3, 7)$. Since $a=2>0$, this is a
**minimum**: the smallest value $y$ ever takes is $7$, at $x=3$.

**Trips people up:** $y=2(x+3)^2+7$ (with a $+$) has vertex $x$-coordinate $-3$, not $3$ —
always rewrite $x+h$ as $x-(-h)$ before reading it off.

**Worked example 2:** $y = -(x+4)^2 - 2$. Vertex is $(-4, -2)$ (rewrite $x+4$ as $x-(-4)$, so
$h=-4$). Since $a=-1<0$, this is a **maximum**: the largest value $y$ ever takes is $-2$, at
$x=-4$.

**Trips people up:** an implied coefficient of $-1$ (no visible number in front of the
parentheses) is easy to miss — it still flips the parabola downward, making the vertex a max,
not a min.

**Worked example 3:** $y = 4(x-1)^2$. There's no visible "$+k$" term, but that just means
$k=0$. Vertex is $(1, 0)$. Since $a=4>0$, this is a **minimum**: the smallest value $y$ ever
takes is $0$, at $x=1$.

**Trips people up:** when the $+k$ term is missing entirely, don't assume there's no vertex or
that the equation isn't in vertex form — treat the missing constant as $k=0$ and read the
vertex normally.

---

### M6 — Discriminant: determine number of real solutions without solving

**What this actually tests:** using $b^2-4ac$ alone, without solving the whole equation, to
know how many real solutions exist.

**The rule:** for $ax^2+bx+c=0$, look at $b^2-4ac$:
- **Positive** → two distinct real solutions.
- **Zero** → exactly one real solution (a repeated root).
- **Negative** → no real solutions (two complex ones instead).

**Worked example:** How many real solutions does $x^2+4x+7=0$ have?
$$b^2-4ac = 16 - 4(1)(7) = 16-28=-12$$
Negative → **no real solutions**.

**Trips people up:** don't confuse this with "no solutions at all" — it means no *real*
solutions; the SAT phrases this carefully ("how many real solutions"), so answer exactly what's
asked.

**Worked example 2:** How many real solutions does $x^2-6x+9=0$ have?
$$b^2-4ac = (-6)^2-4(1)(9) = 36-36=0$$
Zero → exactly **one** real solution (a repeated/double root).

**Trips people up:** a discriminant of exactly $0$ is *not* "no solutions" — it means there's
one real solution counted twice ($x^2-6x+9=(x-3)^2$, so $x=3$ is a double root). Don't lump
$0$ in with the negative case.

**Worked example 3:** How many real solutions does $2x^2+3x-2=0$ have?
$$b^2-4ac = 3^2-4(2)(-2) = 9+16=25$$
Positive → **two distinct** real solutions.

**Trips people up:** the question only asks *how many*, not *what* — don't waste time actually
solving for the roots (via factoring or the quadratic formula) when the discriminant alone
answers the question.

---

### M7 — Exponent rules (product, quotient, power, negative, fractional)

**What this actually tests:** combining exponent rules correctly in one simplification, not any
single rule in isolation.

**The rules:**
$$a^m \cdot a^n = a^{m+n} \qquad \frac{a^m}{a^n}=a^{m-n} \qquad (a^m)^n = a^{mn}$$
$$a^{-n} = \frac{1}{a^n} \qquad a^{1/n} = \sqrt[n]{a} \qquad a^{m/n} = \left(\sqrt[n]{a}\right)^m$$

**Worked example:** Simplify $(2x^3y^{-1})^2 \cdot (4x^{-2}y^3)$.
Power rule first: $(2x^3y^{-1})^2 = 4x^6y^{-2}$.
Multiply: $4x^6y^{-2} \cdot 4x^{-2}y^3 = (4\cdot4)\,x^{6+(-2)}\,y^{-2+3} = 16x^4y$.

**Trips people up:** exponent rules only combine terms with the **same base** — you can't
combine $x$ and $y$ exponents together, and $a^m + a^n$ does *not* simplify by adding exponents
(that rule is multiplication-only).

**Worked example 2:** Simplify $\dfrac{(3x^{-2}y^4)^3}{9x^5y^{-2}}$.
Power rule first: $(3x^{-2}y^4)^3 = 27x^{-6}y^{12}$.
Divide: $\dfrac{27x^{-6}y^{12}}{9x^5y^{-2}} = 3\,x^{-6-5}\,y^{12-(-2)} = 3x^{-11}y^{14}$, which
can be rewritten with a positive exponent as $\dfrac{3y^{14}}{x^{11}}$.

**Trips people up:** when dividing, the exponent in the denominator gets *subtracted*, in
order — $-6-5=-11$, not $-6+5$. A leftover negative exponent isn't wrong, but SAT answer
choices are often written with all-positive exponents, so know how to flip it into a fraction.

**Worked example 3:** Simplify $\sqrt[3]{x^6}\cdot\sqrt{x}$.
Convert to fractional exponents: $\sqrt[3]{x^6}=x^{6/3}=x^2$ and $\sqrt{x}=x^{1/2}$.
Multiply (same base, add exponents): $x^2\cdot x^{1/2} = x^{2+1/2}=x^{5/2}$, equivalently
$x^2\sqrt{x}$.

**Trips people up:** converting a radical to a fractional exponent — the *index* of the root
becomes the denominator and the power inside becomes the numerator ($\sqrt[n]{a^m}=a^{m/n}$).
Mixing those up (index on top) is a common error.

---

### M8 — Simplify/manipulate a rational expression (factor & cancel)

**What this actually tests:** treating the numerator and denominator as things to factor first,
never canceling terms that are added/subtracted.

**The rule:**
1. Factor numerator and denominator completely.
2. Cancel any factor that appears in both (not individual terms).
3. State the domain restriction: any $x$-value that made the *original* denominator zero is
   excluded, even after it cancels.

**Worked example:** Simplify $\dfrac{x^2-9}{x^2+x-6}$.
Numerator: $x^2-9=(x-3)(x+3)$. Denominator: $x^2+x-6=(x+3)(x-2)$.
$$\frac{(x-3)(x+3)}{(x+3)(x-2)} = \frac{x-3}{x-2}, \quad x \neq -3,\, 2$$

**Trips people up:** canceling an $x$ that's part of a sum (e.g. crossing out the $x$'s in
$\frac{x+3}{x+5}$) is not legal — only whole factors cancel, never individual terms.

**Worked example 2:** Simplify $\dfrac{x^2-5x+6}{x^2-4}$.
Numerator: $x^2-5x+6=(x-2)(x-3)$. Denominator: $x^2-4=(x-2)(x+2)$.
$$\frac{(x-2)(x-3)}{(x-2)(x+2)} = \frac{x-3}{x+2}, \quad x \neq 2,\, -2$$

**Trips people up:** a denominator with no middle term (like $x^2-4$) is still factorable — it's
a difference of squares. Don't skip factoring it just because it "looks done" already.

**Worked example 3:** Simplify $\dfrac{x^2-16}{x^2-3x-4}$.
Numerator: $x^2-16=(x-4)(x+4)$. Denominator: $x^2-3x-4=(x-4)(x+1)$.
$$\frac{(x-4)(x+4)}{(x-4)(x+1)} = \frac{x+4}{x+1}, \quad x \neq 4,\, -1$$

**Trips people up:** the domain restriction has to list *every* zero of the **original**
denominator, including the one that cancels out ($x=4$) — not just the value still visible in
the simplified denominator ($x=-1$).

---

### M9 — Solve a rational equation (incl. checking for extraneous solutions)

**What this actually tests:** clearing denominators correctly and then verifying the answer
doesn't make any original denominator zero.

**The rule:**
1. Multiply every term by the common denominator to clear fractions.
2. Solve the resulting (usually linear or quadratic) equation.
3. **Plug the solution back into the original denominators** — if any denominator becomes $0$,
   that solution is extraneous and must be thrown out.

**Worked example:** Solve $\dfrac{x}{x-2} = \dfrac{2}{x-2} + 3$.
Multiply both sides by $(x-2)$:
$$x = 2 + 3(x-2) = 2+3x-6 = 3x-4$$
$$x - 3x = -4 \implies -2x=-4 \implies x=2$$
Check: $x=2$ makes the original denominator $x-2=0$ — undefined. **$x=2$ is extraneous; this
equation has no solution.**

**Trips people up:** solving correctly and stopping there. The algebra can be perfect and the
answer still has to be thrown out — always check against the *original* equation's denominators,
not the cleared version.

**Worked example 2:** Solve $\dfrac{x}{x-3} + 1 = \dfrac{6}{x-3}$.
Multiply every term by $(x-3)$ — including the standalone $1$:
$$x + (x-3) = 6 \implies 2x-3=6 \implies 2x=9 \implies x=4.5$$
Check: $x-3=1.5\neq0$, so this is defined. $\frac{4.5}{1.5}+1 = 3+1=4$; $\frac{6}{1.5}=4$.
Both sides match — **$x=4.5$ is valid.**

**Trips people up:** the common denominator has to multiply *every* term, not just the terms
that already have a fraction — forgetting to distribute it across a standalone constant (the
"$+1$" here) is a common setup error.

**Worked example 3:** Solve $\dfrac{2}{x+1} = \dfrac{1}{x-1}$.
With exactly one fraction on each side, cross-multiply: $2(x-1) = 1(x+1)$.
$$2x-2 = x+1 \implies x=3$$
Check: $x+1=4\neq0$ and $x-1=2\neq0$ — both denominators are fine. **$x=3$ is valid.**

**Trips people up:** cross-multiplication only works cleanly when each side is a *single*
fraction — with more than one term on a side (like Example 2 above), use the full
common-denominator method instead, or you'll drop terms.

---

### M10 — Asymptotes of a rational function $y=\frac{a}{x-h}+k$

Vertical asymptote is $x=h$ (where the denominator hits zero); horizontal asymptote is $y=k$
(what the function approaches as $x \to \pm\infty$). This was a confirmed diagnostic gap and
already has a full lesson with worked examples and practice — see
[[../Diagnostic Gap Lessons (2026-08-07)#Lesson 1 — Advanced Math: asymptotes of rational functions]]
rather than duplicating it here. Three quick variants below (vertical only, horizontal only,
both) since the SAT asks for either one alone or both together.

**Worked example:** $y = \dfrac{3}{x-5} + 2$. Find the vertical asymptote.
The denominator is zero when $x-5=0$, i.e. $x=5$. **Vertical asymptote: $x=5$.**

**Trips people up:** reading $h$ straight off the equation without flipping the sign — in
$\frac{a}{x-h}+k$, the denominator $x-5$ means $h=5$ (not $-5$), since it's already in
$x-h$ form here.

**Worked example 2:** $y = \dfrac{-2}{x+1} - 7$. Find the horizontal asymptote.
Rewrite in $\frac{a}{x-h}+k$ form: $x+1 = x-(-1)$, so $h=-1$, and $k=-7$. As $x\to\pm\infty$,
the fraction term shrinks to $0$, leaving $y\to k$. **Horizontal asymptote: $y=-7$.**

**Trips people up:** the horizontal asymptote is just the constant $k$ being added at the end
— don't confuse it with $h$ (which comes from the denominator) or accidentally report the
numerator's sign instead of $k$'s.

**Worked example 3:** $y = \dfrac{5}{x+2} - 3$. Find both asymptotes.
Rewrite $x+2$ as $x-(-2)$: $h=-2$, and $k=-3$.
**Vertical asymptote: $x=-2$** (denominator zero there). **Horizontal asymptote: $y=-3$**
(constant term, what $y$ approaches as $x\to\pm\infty$).

**Trips people up:** when a question asks for "both," report them as two separate values/lines
($x=-2$ and $y=-3$) — don't merge them into a single coordinate point; the graph never actually
touches either asymptote.

---

### M11 — Exponential growth/decay: build and interpret $y=a(b)^x$

**What this actually tests:** setting up the right base from a percent rate, then evaluating
at a given $x$.

**The rule:** $y = a(b)^x$, where $a$ is the starting value and:
- **Growth** ($r\%$ increase per period): $b = 1+r$ (as a decimal), $b>1$.
- **Decay** ($r\%$ decrease per period): $b = 1-r$ (as a decimal), $0<b<1$.
$x$ counts the number of time periods elapsed.

**Worked example:** A population starts at $500$ and grows $8\%$ per year. What's the
population after $5$ years?
$$y = 500(1.08)^x \implies y = 500(1.08)^5$$
$1.08^5 = 1.4693280768$ (built up: $1.08^2=1.1664$, $1.08^3=1.259712$,
$1.08^4=1.36048896$, $1.08^5=1.4693280768$).
$$y = 500 \times 1.4693280768 \approx 734.66$$

**Trips people up:** using $r$ itself as the base instead of $1\pm r$ (e.g. writing $b=0.08$
for 8% growth instead of $b=1.08$) — the base has to represent the *whole* new amount each
period, not just the change.

**Worked example 2:** A car worth $\$22{,}000$ depreciates $15\%$ per year. What's it worth
after $3$ years?
$$y = 22000(0.85)^x \implies y = 22000(0.85)^3$$
$0.85^2=0.7225$, $0.85^3 = 0.85 \times 0.7225 = 0.614125$.
$$y = 22000 \times 0.614125 \approx \$13{,}510.75$$

**Trips people up:** for decay, $b=1-r$, not $-r$ — a $15\%$ decrease gives $b=0.85$, not
$b=-0.15$. The base still has to be a positive number between $0$ and $1$.

**Worked example 3:** A bacteria culture is modeled by $y=1200(0.6)^x$, with $x$ in hours.
What percent does the population decay each hour, and what is the population after $4$ hours?
Rate: $b=0.6=1-r \implies r=0.4$, i.e. a **$40\%$** decrease per hour.
Population: $0.6^2=0.36$, $0.6^3=0.216$, $0.6^4=0.1296$.
$$y = 1200 \times 0.1296 = 155.52$$

**Trips people up:** to recover the rate from a given base, subtract — $r=1-b$ for decay
(or $r=b-1$ for growth) — then convert the decimal to a percent; don't report the base itself
($0.6$, i.e. "$0.6\%$") as the rate.

---

### M12 — Radical equations: isolate and square both sides, check extraneous roots

**What this actually tests:** the same extraneous-solution discipline as M9, applied to
square roots — squaring can introduce solutions that don't actually satisfy the original
equation.

**The rule:**
1. Isolate the radical on one side.
2. Square both sides.
3. Solve the resulting equation.
4. **Check every solution in the original (unsquared) equation** — squaring can turn a false
   statement true, so this step is mandatory, not optional.

**Worked example:** Solve $\sqrt{2x+3} = x$.
Square both sides: $2x+3 = x^2$.
$$x^2-2x-3=0 \implies (x-3)(x+1)=0 \implies x=3 \text{ or } x=-1$$
Check $x=3$: $\sqrt{2(3)+3}=\sqrt{9}=3$. Matches — valid.
Check $x=-1$: $\sqrt{2(-1)+3}=\sqrt{1}=1$, but $x=-1$. $1 \neq -1$ — **extraneous**.
Final answer: $x=3$ only.

**Trips people up:** a square root's output is always $\geq 0$ by definition, so any solution
where the right side would need to be negative is automatically suspect — check those first.

**Worked example 2:** Solve $\sqrt{x+7} = x+1$.
Square both sides: $x+7 = (x+1)^2 = x^2+2x+1$.
$$x^2+x-6=0 \implies (x+3)(x-2)=0 \implies x=2 \text{ or } x=-3$$
Check $x=2$: $\sqrt{9}=3$, and $x+1=3$. Matches — valid.
Check $x=-3$: $\sqrt{4}=2$, but $x+1=-2$. $2 \neq -2$ — **extraneous**.
Final answer: $x=2$ only.

**Trips people up:** expanding $(x+1)^2$ as $x^2+1$ (dropping the middle term) is a very common
slip — always write it out as $(x+1)(x+1)$ if the shortcut isn't automatic.

**Worked example 3:** Solve $\sqrt{3x-2} - x = -2$.
Isolate the radical first: $\sqrt{3x-2} = x-2$.
Square both sides: $3x-2 = (x-2)^2 = x^2-4x+4$.
$$x^2-7x+6=0 \implies (x-6)(x-1)=0 \implies x=6 \text{ or } x=1$$
Check $x=6$: $\sqrt{16}=4$, and $x-2=4$. Matches — valid.
Check $x=1$: $\sqrt{1}=1$, but $x-2=-1$. $1 \neq -1$ — **extraneous**.
Final answer: $x=6$ only.

**Trips people up:** you must isolate the radical *before* squaring — squaring
$\sqrt{3x-2}-x=-2$ directly (with the $-x$ still attached) produces a completely different,
wrong equation.

---

### M13 — Function composition $f(g(x))$

**What this actually tests:** evaluating from the inside out — $g$ first, then feed that
result into $f$.

**The rule:** $f(g(x))$ means: evaluate $g(x)$ first, then plug *that output* in for $x$ in
$f$. Work inside-out, always.

**Worked example:** $f(x)=2x+1$, $g(x)=x^2-3$. Find $f(g(2))$.
Step 1 — evaluate the inside first: $g(2) = 2^2-3 = 1$.
Step 2 — feed that into $f$: $f(1) = 2(1)+1=3$.
$$f(g(2)) = 3$$
(General form, if asked symbolically: $f(g(x)) = 2(x^2-3)+1 = 2x^2-5$.)

**Trips people up:** $f(g(x))$ and $g(f(x))$ are generally *not* the same — order matters, and
the SAT will test both directions to see if you're actually reading which function is
"outside."

**Worked example 2:** Using the same $f(x)=2x+1$, $g(x)=x^2-3$ as above, find $g(f(2))$.
Step 1 — evaluate the inside first: $f(2) = 2(2)+1 = 5$.
Step 2 — feed that into $g$: $g(5) = 5^2-3 = 22$.
$$g(f(2)) = 22$$
Compare to Example 1: $f(g(2))=3$, but $g(f(2))=22$ — same functions, same input, very
different answers.

**Trips people up:** swapping which function is "outside" swaps the whole calculation, not just
the final step — reversing the order here changes the answer from $3$ to $22$, not by a small
amount.

**Worked example 3:** $f(x)=x^2+1$, $g(x)=2x-3$. Find $f(g(-1))$.
Step 1 — evaluate the inside first: $g(-1) = 2(-1)-3 = -5$.
Step 2 — feed that into $f$: $f(-5) = (-5)^2+1 = 26$.
$$f(g(-1)) = 26$$

**Trips people up:** when the inner output is negative, square it carefully — $(-5)^2=25$, not
$-25$; dropping or mishandling the negative sign before squaring is a frequent slip.

---

### M14 — Polynomial operations (add/subtract/multiply/divide)

**What this actually tests:** distributing carefully across every term and combining like
terms without dropping signs — mechanical, but error-prone under time pressure.

**The rule:**
- **Add/subtract:** combine like terms only (same variable, same exponent). Distribute a
  negative sign across an entire polynomial being subtracted.
- **Multiply:** distribute every term in the first polynomial across every term in the second
  (generalized FOIL), then combine like terms.
- **Divide:** factor and cancel (like M8) if it divides evenly, or use long/synthetic division
  otherwise.

**Worked example:** Multiply $(2x-3)(x^2+4x-1)$.
$$2x(x^2+4x-1) = 2x^3+8x^2-2x$$
$$-3(x^2+4x-1) = -3x^2-12x+3$$
Add the two results, combining like terms:
$$2x^3 + (8x^2-3x^2) + (-2x-12x) + 3 = 2x^3+5x^2-14x+3$$

**Trips people up:** losing a sign when distributing a subtraction, especially on the last
term — write out every product explicitly before combining rather than trying to do it in your
head.

**Worked example 2:** Subtract $(3x^2-5x+4) - (x^2+2x-7)$.
Distribute the negative sign across *every* term of the second polynomial:
$$3x^2-5x+4-x^2-2x+7$$
Combine like terms:
$$(3x^2-x^2) + (-5x-2x) + (4+7) = 2x^2-7x+11$$

**Trips people up:** only flipping the sign of the second polynomial's *first* term (getting
$3x^2-5x+4-x^2+2x-7$) instead of every term — the minus sign has to distribute across the
entire parenthesized expression, not just the leading term.

**Worked example 3:** Divide $(x^3-2x^2-5x+6) \div (x-3)$ using synthetic division.
Root for divisor $x-3$ is $3$. Coefficients: $1,\ -2,\ -5,\ 6$.
Bring down $1$. $1\times3=3$; $-2+3=1$. $1\times3=3$; $-5+3=-2$. $-2\times3=-6$; $6+(-6)=0$.
Remainder $0$ confirms it divides evenly. Quotient coefficients: $1,\ 1,\ -2$.
$$x^3-2x^2-5x+6 \;\div\; (x-3) = x^2+x-2$$

**Trips people up:** for a divisor of $(x-3)$, the synthetic-division root is $+3$, not $-3$ —
flip the sign of the constant in the divisor before setting up the division.

---

### M15 — Nonlinear systems (line + parabola, etc.)

**What this actually tests:** finding where a line and a curve intersect by substitution —
setting the two $y$-expressions equal to each other.

**The rule:**
1. If both equations are solved for $y$, set the right-hand sides equal to each other.
2. Solve the resulting equation (usually a quadratic) for $x$.
3. Plug each $x$-value back into the **simpler** equation (usually the line) to get the
   matching $y$-value.
4. Report each solution as an $(x,y)$ pair.

**Worked example:** Solve the system $y=x^2-2x-3$ and $y=x+1$.
Set equal: $x^2-2x-3 = x+1$.
$$x^2-3x-4=0 \implies (x-4)(x+1)=0 \implies x=4 \text{ or } x=-1$$
Plug into $y=x+1$: $x=4 \to y=5$; $x=-1 \to y=0$.
$$\text{Solutions: } (4,5) \text{ and } (-1,0)$$
Check in the parabola: $4^2-2(4)-3=16-8-3=5$ ✓. $(-1)^2-2(-1)-3=1+2-3=0$ ✓.

**Trips people up:** substituting back into the *quadratic* equation to find $y$ instead of the
line — both work, but the line is almost always less arithmetic and less error-prone.

**Worked example 2:** Solve the system $y=x^2-4x+1$ and $y=-x+5$.
Set equal: $x^2-4x+1 = -x+5$.
$$x^2-3x-4=0 \implies (x-4)(x+1)=0 \implies x=4 \text{ or } x=-1$$
Plug into $y=-x+5$: $x=4 \to y=1$; $x=-1 \to y=6$.
$$\text{Solutions: } (4,1) \text{ and } (-1,6)$$
Check in the parabola: $4^2-4(4)+1=16-16+1=1$ ✓. $(-1)^2-4(-1)+1=1+4+1=6$ ✓.

**Trips people up:** matching the wrong $y$-value to an $x$-value (e.g. swapping which $y$ goes
with $x=4$ vs. $x=-1$) — compute and record each pair together instead of listing all the
$x$'s then all the $y$'s separately.

**Worked example 3:** Solve the system $y=x^2-6x+9$ and $y=0$.
Set equal: $x^2-6x+9=0$.
$$(x-3)^2=0 \implies x=3 \text{ (a repeated root)}$$
Only one $x$-value, so only one intersection point: with $y=0$, that's $(3,0)$.
Check in the parabola: $3^2-6(3)+9=9-18+9=0$ ✓ — and this is the parabola's vertex, sitting
exactly on the line $y=0$.

**Trips people up:** a repeated root means the line is **tangent** to the parabola — there's
only one intersection point, not two. Don't report $(3,0)$ twice or assume a second solution
must exist just because it's a line-parabola system.

---

## Mini-Diagnostic

One question per skill, fifteen total. Work them cold, then check the answer key at the bottom.

**M1.** Factor $x^2 - 5x - 14$.

**M2.** Solve by factoring: $x^2 + x - 20 = 0$.

**M3.** Solve using the quadratic formula: $3x^2 - 5x - 2 = 0$.

**M4.** Solve $x^2 - 8x + 3 = 0$ by completing the square.

**M5.** $y = -3(x+2)^2 + 5$. State the vertex and whether it's a max or min.

**M6.** Without solving, how many real solutions does $4x^2 - 12x + 9 = 0$ have?

**M7.** Simplify $\dfrac{(3x^2y^3)^2}{9x^{-1}y^4}$.

**M8.** Simplify $\dfrac{x^2-4}{x^2-5x+6}$, and state the domain restriction.

**M9.** Solve $\dfrac{x+1}{x-4} = \dfrac{5}{x-4} + 2$, checking for extraneous solutions.

**M10.** $y = \dfrac{-4}{x+6} - 1$. Find the horizontal asymptote.

**M11.** A car worth \$18,000 depreciates 12% per year. What is it worth after 4 years (nearest
cent)?

**M12.** Solve $\sqrt{3x+1} = x-1$, checking for extraneous solutions.

**M13.** $f(x) = x^2+2$, $g(x)=3x-1$. Find $g(f(2))$.

**M14.** Multiply $(x-5)(2x^2+x-3)$.

**M15.** Solve the system $y = x^2+2x-1$ and $y=2x+3$.

---

### Answer key

**M1.** Need factors of $-14$ summing to $-5$: $-7$ and $2$. $(x-7)(x+2)$.

**M2.** Factors of $-20$ summing to $1$: $5, -4$. $(x+5)(x-4)=0 \implies x=-5$ or $x=4$.

**M3.** $a=3,b=-5,c=-2$. Disc $=25-4(3)(-2)=25+24=49$, $\sqrt{49}=7$.
$x=\frac{5\pm7}{6} \implies x=2$ or $x=-\frac13$.

**M4.** $x^2-8x=-3 \implies x^2-8x+16=13 \implies (x-4)^2=13 \implies x=4\pm\sqrt{13}$.

**M5.** Vertex $(-2, 5)$; $a=-3<0$ so it's a **maximum**.

**M6.** Disc $=(-12)^2-4(4)(9)=144-144=0$ → exactly **one** real solution.

**M7.** $(3x^2y^3)^2=9x^4y^6$; divide by $9x^{-1}y^4$: $x^{4-(-1)}y^{6-4} = x^5y^2$.

**M8.** $\frac{(x-2)(x+2)}{(x-2)(x-3)} = \frac{x+2}{x-3}$, $x \neq 2, 3$.

**M9.** Multiply by $(x-4)$: $x+1 = 5+2(x-4) = 2x-3 \implies x=4$. That makes the original
denominator zero — **extraneous; no solution**.

**M10.** $y=\frac{-4}{x+6}-1$ is in $\frac{a}{x-h}+k$ form with $k=-1$: horizontal asymptote
$y=-1$.

**M11.** $18000(0.88)^4$. $0.88^2=0.7744$, $0.88^3=0.681472$, $0.88^4=0.59969536$.
$18000 \times 0.59969536 \approx \$10{,}794.52$.

**M12.** Square: $3x+1=(x-1)^2=x^2-2x+1 \implies x^2-5x=0 \implies x(x-5)=0 \implies x=0,5$.
Check $x=0$: $\sqrt1=1 \neq -1$, extraneous. Check $x=5$: $\sqrt{16}=4=5-1$, valid. **$x=5$**.

**M13.** $f(2)=4+2=6$. $g(6)=3(6)-1=17$.

**M14.** $2x^3+x^2-3x-10x^2-5x+15 = 2x^3-9x^2-8x+15$.

**M15.** $x^2+2x-1=2x+3 \implies x^2-4=0 \implies x=\pm2$. $y=2x+3$: $(2,7)$ and $(-2,-1)$.
