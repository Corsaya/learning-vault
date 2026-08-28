---
tags: [pytheas, sat, math, algebra, crash-course]
created: 2026-08-12
source: "Foundations Knowledge Check A1-A10"
related: ["[[../Foundations Knowledge Check]]", "[[../Diagnostic Gap Lessons (2026-08-07)]]"]
---

# Math — Algebra Crash Course

Algebra is the single biggest domain on the digital SAT math section — roughly
**35% of the test (13–15 questions)**, per
[[../Research/Official SAT Structure and Content Research (2026-08-07)]] — and this
doc covers all 10 skills (A1–A10) from the
[[../Foundations Knowledge Check]] in one pass.

---

### A1 — Solve a linear equation in one variable

**What this actually tests:** can you isolate a variable through a clean, ordered
sequence of inverse operations, including when there's distribution or
like-terms cleanup first. This is the single most repeated mechanical skill
underneath half the other Algebra skills (A3, A5, A6, A9 all end in "now solve
a linear equation").

**The core method:**
1. Distribute anything in parentheses.
2. Combine like terms on each side separately.
3. Move variable terms to one side, constants to the other (add/subtract).
4. Divide by the coefficient on the variable.
5. Check by plugging back into the *original* equation, not a middle step.

**Worked example:** Solve $3(x-2) + 5 = 2x + 7$.
$$3x - 6 + 5 = 2x + 7$$
$$3x - 1 = 2x + 7$$
$$x = 8$$
Check: $3(8-2)+5 = 3(6)+5 = 23$, and $2(8)+7 = 23$. Matches.

**Trips people up:** distributing a negative sign — $-2(x-4)$ becomes
$-2x+8$, not $-2x-8$. Do the distribution as its own written step instead of
in your head when there's a negative out front.

**Worked example 2:** Solve $5(x+3) - 2x = 4x - 9$.
$$5x + 15 - 2x = 4x - 9$$
$$3x + 15 = 4x - 9$$
$$x = 24$$
Check: $5(24+3) - 2(24) = 5(27) - 48 = 87$, and $4(24) - 9 = 87$. Matches.

**Trips people up:** combine like terms *within* each side first — here the
$5x$ and $-2x$ on the left simplify to $3x$ before you ever move anything
across the equals sign. Moving terms across too early, before simplifying
what's already on that side, is a common source of arithmetic slips.

**Worked example 3:** Solve $\dfrac{2x-1}{3} = x - 4$.
$$2x - 1 = 3(x-4)$$
$$2x - 1 = 3x - 12$$
$$x = 11$$
Check: $\dfrac{2(11)-1}{3} = \dfrac{21}{3} = 7$, and $11 - 4 = 7$. Matches.

**Trips people up:** when you clear a fraction by multiplying both sides by
the denominator, that multiplication has to hit the *entire* other side —
$x-4$ becomes $3(x-4) = 3x-12$, not just $3x-4$. Losing the distribution on
one side is the single most common error in this step.

---

### A2 — Solve a linear inequality in one variable

Same steps as A1, with one extra rule: dividing or multiplying both sides by a
**negative number flips the inequality sign**. This is already covered in full
(rule, worked example, and a 4-question drill) in
[[../Diagnostic Gap Lessons (2026-08-07)#Lesson 2 — Algebra: the inequality-flip rule]]
— go there for the complete lesson instead of a rewrite here.

**Worked example 2:** Solve $5 - 2x > 11$.
$$-2x > 6$$
$$x < -3$$
Check: $x=-4$ gives $5-2(-4)=13>11$ (true, and $-4<-3$). $x=-3$ gives
$5-2(-3)=11$, which is not $>11$, so $-3$ is correctly excluded.

**Trips people up:** the flip happens because of the *division by $-2$*, not
because of the subtraction step before it — subtracting doesn't flip
anything. Only multiplying or dividing by a negative number does.

**Worked example 3:** Solve $\dfrac{-3x}{4} \ge 9$.
$$-3x \ge 36$$
$$x \le -12$$
Check: $x=-12$ gives $\dfrac{-3(-12)}{4} = \dfrac{36}{4} = 9$ (equality
holds). $x=-13$ gives $\dfrac{39}{4}=9.75 \ge 9$, and $-13 \le -12$. Matches.

**Trips people up:** multiplying both sides by $4$ (positive) doesn't flip
the sign — only the later division by $-3$ does. Flipping at the wrong step,
or flipping twice and canceling the flip out, is the most common error here.

---

### A3 — Build a linear equation/inequality from a word problem

**What this actually tests:** translating English into algebra — identifying
the *fixed* part (a flat fee, a starting amount) versus the *variable* part
(a per-unit rate times a quantity), then setting up the equation before
solving anything.

**The core method:**
- Find the flat/starting value — it stands alone, no variable attached.
- Find the rate — it's always multiplied by the changing quantity.
- Assemble: **total = flat amount + (rate × quantity)**, or as an inequality
  if the problem says "at least," "at most," "no more than," etc.
- Only then solve using A1/A2 mechanics.

**Worked example:** A phone plan charges a flat fee of \$20 plus \$0.10 per
minute. A bill came to \$35.50. How many minutes were used?
$$20 + 0.10m = 35.50$$
$$0.10m = 15.50$$
$$m = 155 \text{ minutes}$$

**Trips people up:** watch for inequality keywords ("no more than" → $\le$,
"at least" → $\ge$, "more than"/"fewer than" → strict $<$/$>$) — the SAT tests
whether you know these translate to non-strict vs. strict inequalities, not
just that you can solve the equation.

**Worked example 2:** A rideshare company charges a \$4 base fee plus \$2.00
per mile. Sam has at most \$30 to spend on a ride. Write an inequality for
the number of miles $m$ he can travel, and find the maximum whole number of
miles.
$$4 + 2m \le 30$$
$$2m \le 26$$
$$m \le 13 \text{ miles}$$

**Trips people up:** "at most" means the total can equal the budget exactly,
so the inequality is non-strict ($\le$), not strict ($<$) — missing that
distinction costs the boundary value (here, exactly 13 miles).

**Worked example 3:** A gym membership costs \$200 up front, then charges
\$30 per month. After how many months will total payments reach \$470?
$$200 + 30m = 470$$
$$30m = 270$$
$$m = 9 \text{ months}$$

**Trips people up:** identify the flat amount and the rate correctly even
when the flat fee is the *larger* number — size alone doesn't tell you which
value is fixed and which is multiplied by the variable; only "up front"
(one-time) vs. "per month" (recurring) does.

---

### A4 — Interpret slope and y-intercept in context

**What this actually tests:** reading a linear model $y = mx + b$ (or any
letters standing in for $x$ and $y$) and stating what $m$ and $b$ *mean in the
real-world scenario*, not just naming them "slope" and "intercept."

**The core method:**
- $b$ (or whatever term stands alone, no variable) = the **starting value** —
  what's true at time zero / quantity zero.
- $m$ (the coefficient multiplying the variable) = the **rate of change** —
  how much $y$ changes per one unit of $x$. Sign matters: positive = increasing,
  negative = decreasing.
- Always attach units from the problem when stating the interpretation.

**Worked example:** A tank's water level (in gallons), $t$ minutes after a
drain valve opens, is modeled by $L = 50 - 2t$. Interpret the slope and the
$y$-intercept.
- $y$-intercept $50$: the tank starts with 50 gallons before draining begins.
- Slope $-2$: the water level decreases by 2 gallons every minute.

**Trips people up:** the sign of the slope is not optional in the answer —
"the level changes by 2 gallons per minute" is an incomplete/wrong answer on
a question where direction (draining vs. filling) is part of what's being
tested.

**Worked example 2:** A company's profit (in thousands of dollars), $x$
years after opening, is modeled by $P = -15 + 8x$. Interpret the slope and
the $y$-intercept.
- $y$-intercept $-15$: the company started \$15,000 *in the red* (a loss)
  in its opening year.
- Slope $8$: profit increases by \$8,000 per year.

**Trips people up:** a negative $y$-intercept is a valid, meaningful
starting value (debt or loss) — it's not a sign of a mistake, and it
shouldn't be reported as "no starting value" or skipped.

**Worked example 3:** A car's value (in dollars), $y$ years after purchase,
is modeled by $V = 24000 - 1800y$. Interpret the slope and $y$-intercept,
and find the car's value after 5 years.
- $y$-intercept $24000$: the purchase price of the car.
- Slope $-1800$: the car's value decreases by \$1,800 per year.
- $V(5) = 24000 - 1800(5) = 24000 - 9000 = 15000$, so the car is worth
  \$15,000 after 5 years.

**Trips people up:** always attach both the unit ("dollars") *and* the time
unit ("per year") to the slope — "decreases by 1800" without "per year" is
treated as an incomplete interpretation on this skill.

---

### A5 — Solve a system of two linear equations (substitution)

**What this actually tests:** using one equation (already solved, or easy to
solve, for one variable) to eliminate that variable from the other equation,
collapsing two unknowns into one.

**The core method:**
1. Solve one equation for one variable, if it isn't already.
2. Substitute that expression into the *other* equation everywhere that
   variable appears.
3. Solve the resulting one-variable equation (A1 mechanics).
4. Plug that value back into either original equation to get the second
   variable.

**Worked example:** Solve $y = 2x + 1$ and $3x + y = 16$.
$$3x + (2x+1) = 16$$
$$5x + 1 = 16$$
$$x = 3, \quad y = 2(3)+1 = 7$$
Check in the other equation: $3(3) + 7 = 16$. Matches.

**Trips people up:** substitute into the equation you *didn't* use to solve
for the variable — plugging back into the same equation you started from just
gives you a trivially true statement (like $0=0$), not an answer.

**Worked example 2:** Solve $x + 3y = 11$ and $2x - y = 1$ using substitution.
$$y = 2x - 1$$
$$x + 3(2x-1) = 11$$
$$x + 6x - 3 = 11$$
$$7x = 14 \Rightarrow x = 2, \quad y = 2(2) - 1 = 3$$
Check in the first equation: $2 + 3(3) = 11$. Matches.

**Trips people up:** when neither equation is pre-solved, isolate whichever
variable has a coefficient of $1$ or $-1$ (here, $y$ in the second equation)
— isolating a variable with any other coefficient introduces fractions you
don't need.

**Worked example 3:** Solve $3x - y = 7$ and $2x + 3y = 1$ using substitution.
$$y = 3x - 7$$
$$2x + 3(3x-7) = 1$$
$$2x + 9x - 21 = 1$$
$$11x = 22 \Rightarrow x = 2, \quad y = 3(2) - 7 = -1$$
Check in the second equation: $2(2) + 3(-1) = 4 - 3 = 1$. Matches.

**Trips people up:** a negative result for one variable isn't automatically a
sign of an error — don't discard it and restart. Verify with the check step
instead of assuming negative means wrong.

---

### A6 — Solve a system of two linear equations (elimination)

**What this actually tests:** the same underlying idea as substitution
(collapse two variables into one) but by adding or subtracting the two
equations directly, after scaling one or both so a variable's coefficients
cancel.

**The core method:**
1. Look for a variable whose coefficients are already equal, or opposite,
   in the two equations (or multiply one/both equations by a constant to
   make that true).
2. Add the equations (if coefficients are opposite) or subtract (if equal) —
   one variable cancels out.
3. Solve the resulting one-variable equation.
4. Substitute back into either original equation for the second variable.

**Worked example:** Solve $3x + 2y = 12$ and $3x - 2y = 0$.
$$\underline{+\; (3x+2y) + (3x-2y) = 12 + 0}$$
$$6x = 12 \Rightarrow x = 2$$
$$3(2) - 2y = 0 \Rightarrow 2y = 6 \Rightarrow y = 3$$
Check in the first equation: $3(2)+2(3) = 6+6 = 12$. Matches.

**Trips people up:** when you scale an equation to set up cancellation, scale
*every term on both sides* — a common error is multiplying only the
left-hand side and forgetting the constant on the right.

**Worked example 2:** Solve $x + 2y = 9$ and $3x - y = 6$ using elimination.
$$\text{Scale the second equation by 2: } 6x - 2y = 12$$
$$\underline{+\; (x+2y) + (6x-2y) = 9 + 12}$$
$$7x = 21 \Rightarrow x = 3$$
$$3(3) - y = 6 \Rightarrow y = 3$$
Check in the first equation: $3 + 2(3) = 9$. Matches.

**Trips people up:** decide *add* vs. *subtract* by checking the sign on the
target variable after scaling — here scaling made the $y$-coefficients
opposite ($+2$ and $-2$), so the equations get added, not subtracted.

**Worked example 3:** Solve $5x + 4y = 22$ and $5x - 3y = 1$ using
elimination.
$$\underline{(5x+4y) - (5x-3y) = 22 - 1}$$
$$7y = 21 \Rightarrow y = 3$$
$$5x + 4(3) = 22 \Rightarrow x = 2$$
Check in the second equation: $5(2) - 3(3) = 10 - 9 = 1$. Matches.

**Trips people up:** subtracting equations means subtracting *every* term,
including the right-hand side, and distributing the negative across the
entire second equation ($-(5x-3y) = -5x+3y$) — dropping that distribution on
just one term is the most common sign error in elimination.

---

### A7 — Determine when a linear system has no solution / infinite solutions

**What this actually tests:** recognizing that a system's solution count is
about how the two lines relate geometrically (crossing once, parallel, or
identical) — and that you can determine which case applies just from the
coefficients, without fully solving.

**The core rule:** write both equations in the same form (e.g. $Ax+By=C$).
Compare the ratios of corresponding coefficients:
- $\dfrac{A_1}{A_2} \ne \dfrac{B_1}{B_2}$ → lines cross once → **exactly one
  solution**.
- $\dfrac{A_1}{A_2} = \dfrac{B_1}{B_2} \ne \dfrac{C_1}{C_2}$ → same slope,
  different line → **no solution** (parallel).
- $\dfrac{A_1}{A_2} = \dfrac{B_1}{B_2} = \dfrac{C_1}{C_2}$ → literally the same
  line → **infinitely many solutions**.

**Worked example:** For what value of $k$ does this system have no solution?
$$kx + 6y = 12 \qquad 2x + 3y = 9$$
Set the variable-coefficient ratios equal: $\dfrac{k}{2} = \dfrac{6}{3} = 2
\Rightarrow k = 4$. Check the constant ratio doesn't also match:
$\dfrac{12}{9} = \dfrac{4}{3} \ne 2$ — confirmed, $k=4$ gives no solution
(parallel, non-identical lines).

**Trips people up:** these questions almost never ask you to actually solve
the system — they ask for the value of a constant that produces a *type* of
solution. Solving fully still works but wastes time; set up the ratio
comparison directly instead.

**Worked example 2:** For what value of $k$ does this system have infinitely
many solutions?
$$kx + 8y = 20 \qquad 3x + 4y = 10$$
Set the variable-coefficient ratios equal: $\dfrac{k}{3} = \dfrac{8}{4} = 2
\Rightarrow k = 6$. Check the constant ratio: $\dfrac{20}{10} = 2$ — it
*matches* too, so all three ratios are equal and $k=6$ gives infinitely many
solutions (the second equation, doubled, is literally the first).

**Trips people up:** no-solution and infinite-solutions cases start
identically (matching variable-coefficient ratios) — the constant ratio is
what tells them apart. Skipping that last check risks mixing the two cases up.

**Worked example 3:** How many solutions does this system have?
$$4x - 2y = 8 \qquad -6x + 3y = -12$$
Compare all three ratios: $\dfrac{4}{-6} = -\dfrac{2}{3}$,
$\dfrac{-2}{3} = -\dfrac{2}{3}$, and $\dfrac{8}{-12} = -\dfrac{2}{3}$ — all
three match, so this is the same line written two ways (the second equation
is the first multiplied by $-1.5$): **infinitely many solutions**.

**Trips people up:** recognize a scaled duplicate even when the scale factor
is negative or a fraction — an equation multiplied by $-1.5$ looks
unrelated at a glance, but the coefficient ratios reveal it's the same line.

---

### A8 — Graph interpretation: find slope/intercept from a line's graph

**What this actually tests:** reading two clear points off a graphed line
(or a labeled point plus the $y$-intercept) and converting that into slope and
equation form — same math as A4/A5 but starting from a picture instead of an
equation.

**The core method:**
1. Identify two points the line clearly passes through (grid intersections
   are chosen deliberately so this is exact, not estimated).
2. Slope: $m = \dfrac{y_2-y_1}{x_2-x_1}$.
3. $y$-intercept: read directly where the line crosses the $y$-axis, or
   solve for $b$ using $y=mx+b$ and one known point if the intercept isn't
   a clean grid point.

**Worked example:** A line passes through $(-2, 5)$ and $(4, -7)$. Find its
slope and $y$-intercept.
$$m = \frac{-7 - 5}{4 - (-2)} = \frac{-12}{6} = -2$$
$$y - 5 = -2(x-(-2)) \Rightarrow y = -2x - 4 + 5 = -2x + 1$$
$y$-intercept is $1$. Check with $(4,-7)$: $-2(4)+1 = -7$. Matches.

**Trips people up:** it's easy to swap the order and compute $\frac{y_1-y_2}{x_2-x_1}$
by accident — keep the same point as "point 1" in both the numerator and
denominator.

**Worked example 2:** A line passes through $(1, 2)$ and $(5, 14)$. Find its
slope and $y$-intercept.
$$m = \frac{14 - 2}{5 - 1} = \frac{12}{4} = 3$$
$$y - 2 = 3(x-1) \Rightarrow y = 3x - 3 + 2 = 3x - 1$$
$y$-intercept is $-1$. Check with $(5,14)$: $3(5)-1 = 14$. Matches.

**Trips people up:** when neither given point sits on the $y$-axis, don't
assume the first listed point *is* the intercept — you have to actually
solve for $b$ using point-slope form or substitution.

**Worked example 3:** A line crosses the $y$-axis at $(0, -3)$ and passes
through $(6, 9)$. Find its slope and equation.
$$m = \frac{9 - (-3)}{6 - 0} = \frac{12}{6} = 2$$
$$y = 2x - 3$$

**Trips people up:** when the $y$-intercept is visible directly on the graph
(a point with $x=0$), skip point-slope form entirely — just compute the
slope and read $b$ straight off the point. Grinding through point-slope form
when it isn't needed wastes time on the timed section.

---

### A9 — Linear function notation: evaluate f(x), interpret f(a)=b in context

**What this actually tests:** function notation is just a labeled equation —
$f(x)$ means "the output of the rule $f$ when the input is $x$." Evaluating
$f(4)$ means substitute $4$ for $x$; being told $f(a) = b$ means the *output*
is $b$ and you're solving for the input $a$.

**The core method:**
- $f(\text{number})$: substitute that number for $x$ everywhere, compute.
- $f(x) = \text{value}$: set the expression equal to that value, solve for
  $x$ (A1 mechanics) — this gives you the *input* that produces it.
- In a word problem, $f(\text{input})$ = output in the units given (cost,
  distance, height, etc.) — state both the number and what it means.

**Worked example:** A rental company charges $f(x) = 35x + 60$, where $x$ is
the number of days rented. Evaluate $f(5)$, then interpret what $f(x)=305$
means and solve for $x$.
$$f(5) = 35(5) + 60 = 235 \quad \text{(5 days costs \$235)}$$
$$35x + 60 = 305 \Rightarrow 35x = 245 \Rightarrow x = 7 \quad \text{(a \$305 bill means 7 days)}$$

**Trips people up:** $f(a) = b$ is frequently misread as "plug $b$ into $f$."
It's the reverse — $b$ is the *output*, $a$ is the *input* you're solving for.

**Worked example 2:** A cell phone plan's monthly cost is modeled by
$f(x) = 0.05x + 45$, where $x$ is the number of texts sent. Evaluate
$f(200)$, then find $x$ if $f(x) = 65$.
$$f(200) = 0.05(200) + 45 = 55 \quad \text{(200 texts costs \$55)}$$
$$0.05x + 45 = 65 \Rightarrow 0.05x = 20 \Rightarrow x = 400 \quad \text{(a \$65 bill means 400 texts)}$$

**Trips people up:** a decimal coefficient like $0.05$ doesn't change the
mechanics at all — substitute and solve exactly as with whole-number
coefficients. Treating it as a "special case" and second-guessing the
arithmetic is where students lose time here.

**Worked example 3:** A hot air balloon's height in feet is modeled by
$f(t) = 800 - 25t$, where $t$ is minutes after descent begins. Evaluate
$f(12)$, then interpret what $f(t) = 0$ means and solve for $t$.
$$f(12) = 800 - 25(12) = 500 \quad \text{(after 12 minutes, height is 500 ft)}$$
$$800 - 25t = 0 \Rightarrow t = 32 \quad \text{(the balloon lands — height 0 — after 32 minutes)}$$

**Trips people up:** $f(t) = 0$ asks for the *input* that produces an output
of zero — it's not an instruction to plug $0$ in for $t$. This input/output
reversal is especially easy to make when the target output itself is $0$.

---

### A10 — Absolute value equations — two-case solving

**What this actually tests:** absolute value strips a sign, so $|X| = n$
(for positive $n$) means the expression inside could have been $n$ *or*
$-n$ before the absolute value was applied. Both cases are real, separate
solutions unless one gets ruled out.

**The core method:**
1. Isolate the absolute value expression on one side, alone, first (if
   there's anything added/multiplied outside the bars).
2. Split into two equations: (inside) $= n$, and (inside) $= -n$.
3. Solve each normally (A1 mechanics).
4. Both answers are valid unless the problem gives an extra restriction that
   rules one out (e.g. "$x$ must be positive").

**Worked example:** Solve $|2x - 3| = 9$.
$$\text{Case 1: } 2x - 3 = 9 \Rightarrow x = 6$$
$$\text{Case 2: } 2x - 3 = -9 \Rightarrow x = -3$$
Check: $|2(6)-3| = |9| = 9$. $|2(-3)-3| = |-9| = 9$. Both valid.

**Trips people up:** if there's anything outside the bars (like
$|2x-3| + 4 = 13$), isolate the absolute value bars *first* ($|2x-3|=9$)
before splitting into two cases — splitting too early keeps the outside term
tangled into both branches incorrectly.

**Worked example 2:** Solve $|3x + 6| - 4 = 11$.
$$|3x+6| = 15$$
$$\text{Case 1: } 3x+6 = 15 \Rightarrow x = 3$$
$$\text{Case 2: } 3x+6 = -15 \Rightarrow x = -7$$
Check: $|3(3)+6|-4 = |15|-4 = 11$. $|3(-7)+6|-4 = |-15|-4 = 11$. Both valid.

**Trips people up:** add the $4$ back to both sides *before* splitting into
cases — writing $3x+6-4=15$ as one of the two cases (instead of isolating
first) leaves the outside term incorrectly stuck to only one branch.

**Worked example 3:** Solve $|x - 5| = 2x + 1$.
$$\text{Case 1: } x-5 = 2x+1 \Rightarrow x = -6$$
$$\text{Case 2: } x-5 = -(2x+1) \Rightarrow x-5 = -2x-1 \Rightarrow x = \tfrac{4}{3}$$
Check $x=-6$: right side $= 2(-6)+1 = -11$. An absolute value can never equal
a negative number, so $x=-6$ must be **rejected**.
Check $x=\tfrac{4}{3}$: left side $= |\tfrac{4}{3}-5| = \tfrac{11}{3}$, right
side $= 2(\tfrac{4}{3})+1 = \tfrac{11}{3}$. Matches — this is the only
valid solution.

**Trips people up:** when the "$n$" side of $|X|=n$ contains a variable
instead of a fixed number, both candidate solutions must be checked in the
*original* equation — since $|X|$ can never be negative, any solution that
makes the right side negative has to be thrown out, even though the algebra
looked fine.

---

## Mini-Diagnostic

One question per skill, A1–A10. Answer key with brief solution steps is at
the bottom — don't peek until you've attempted all 10.

**A1.** Solve for $x$: $4(x+3) - 5 = 2x + 9$

**A2.** Solve: $6 - 3x > 18$

**A3.** A gym charges a \$25 sign-up fee plus \$15 per month. Write an
equation for total cost $C$ after $m$ months, and find how many months until
the total reaches \$175.

**A4.** A candle's height (in cm), $t$ hours after being lit, is modeled by
$h = 24 - 2t$. What does the value $2$ represent in this context, and how
tall is the candle after 6 hours?

**A5.** Solve the system using substitution: $y = 4x - 1$, $\;2x + y = 11$

**A6.** Solve the system using elimination: $5x + 2y = 16$, $\;3x - 2y = 0$

**A7.** For what value of $k$ does this system have no solution?
$$kx + 6y = 12 \qquad 2x + 3y = 9$$

**A8.** A line on a graph passes through $(-2, 5)$ and $(4, -7)$. Find its
slope and $y$-intercept.

**A9.** A ride-share fare is modeled by $f(x) = 2.5x + 4$, where $x$ is
miles traveled. Evaluate $f(6)$, then find $x$ if $f(x) = 26.5$.

**A10.** Solve $|5x - 10| = 30$.

---

### Answer key

**A1.** $4x+12-5=2x+9 \Rightarrow 4x+7=2x+9 \Rightarrow 2x=2 \Rightarrow x=1$

**A2.** $6-3x>18 \Rightarrow -3x>12 \Rightarrow x<-4$ (flipped — divided by $-3$)

**A3.** $C = 25+15m$. Set $175=25+15m \Rightarrow 150=15m \Rightarrow m=10$ months.

**A4.** $2$ = the burn rate, 2 cm lost per hour. $h(6)=24-2(6)=12$ cm.

**A5.** $2x+(4x-1)=11 \Rightarrow 6x=12 \Rightarrow x=2$, then $y=4(2)-1=7$.

**A6.** Add the equations: $8x=16 \Rightarrow x=2$. Then $3(2)-2y=0 \Rightarrow y=3$.

**A7.** $\dfrac{k}{2}=\dfrac{6}{3}=2 \Rightarrow k=4$ (and $\dfrac{12}{9}\ne 2$, confirming no solution rather than infinite).

**A8.** $m=\dfrac{-7-5}{4-(-2)}=\dfrac{-12}{6}=-2$. Using $(4,-7)$: $-7=-2(4)+b \Rightarrow b=1$. Slope $-2$, $y$-intercept $1$.

**A9.** $f(6)=2.5(6)+4=19$. For $f(x)=26.5$: $2.5x+4=26.5 \Rightarrow 2.5x=22.5 \Rightarrow x=9$ miles.

**A10.** $5x-10=30 \Rightarrow x=8$; $5x-10=-30 \Rightarrow x=-4$. Both check: $|5(8)-10|=30$, $|5(-4)-10|=30$.
