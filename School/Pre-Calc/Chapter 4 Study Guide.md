# Unit 4 — Trigonometric Functions Study Guide

> **Test review** | All problems worked with full steps

---

## Reference: Key Angle Values

| Degrees | Radians | sin | cos | tan |
|---------|---------|-----|-----|-----|
| 0° | 0 | 0 | 1 | 0 |
| 30° | π/6 | 1/2 | √3/2 | √3/3 |
| 45° | π/4 | √2/2 | √2/2 | 1 |
| 60° | π/3 | √3/2 | 1/2 | √3 |
| 90° | π/2 | 1 | 0 | undef |
| 120° | 2π/3 | √3/2 | −1/2 | −√3 |
| 150° | 5π/6 | 1/2 | −√3/2 | −√3/3 |
| 180° | π | 0 | −1 | 0 |
| 270° | 3π/2 | −1 | 0 | undef |
| 300° | 5π/3 | −√3/2 | 1/2 | −√3 |
| 330° | 11π/6 | −1/2 | √3/2 | −√3/3 |

**ASTC (quadrant signs):** All positive | Sin+ | Tan+ | Cos+ → QI, QII, QIII, QIV

**Reciprocal identities:** $\csc\theta = 1/\sin\theta$ | $\sec\theta = 1/\cos\theta$ | $\cot\theta = 1/\tan\theta$

**Even/odd:** $\cos(-\theta) = \cos\theta$ (even) | $\sin(-\theta) = -\sin\theta$ (odd)

---

## Problem 1 — Terminal Side Angle from a Point

**Given:** Point $(-1, \sqrt{3})$. Find the smallest positive angle in degrees and radians.

**Step 1 — Find r:**
$$r = \sqrt{(-1)^2 + (\sqrt{3})^2} = \sqrt{1+3} = 2$$

**Step 2 — Reference angle:**
$$\cos\theta_{ref} = \frac{|x|}{r} = \frac{1}{2} \Rightarrow \theta_{ref} = 60°$$

**Step 3 — Quadrant:** $x<0, y>0$ → **QII** → $\theta = 180° - 60°$

$$\boxed{120° = \frac{2\pi}{3}}$$

---

## Problem 2 — Evaluate Without a Calculator

### A) $\sec(-\pi/3)$
Cosine is even, so $\cos(-\pi/3) = \cos(\pi/3) = 1/2$:
$$\sec(-\pi/3) = \frac{1}{1/2} = \boxed{2}$$

### B) $\sin(5\pi/6)$
QII, ref $= \pi - 5\pi/6 = \pi/6$, sin positive:
$$\sin(5\pi/6) = \sin(\pi/6) = \boxed{1/2}$$

### C) $\cos(17\pi/3)$
Subtract $2\pi$ twice: $17\pi/3 - 6\pi/3 - 6\pi/3 = 5\pi/3$
QIV, ref $= 2\pi - 5\pi/3 = \pi/3$, cos positive:
$$\cos(5\pi/3) = \cos(\pi/3) = \boxed{1/2}$$

### D) $\tan(4\pi/3)$
QIII, ref $= 4\pi/3 - \pi = \pi/3$, tan **positive** in QIII:
$$\tan(4\pi/3) = +\tan(\pi/3) = \boxed{\sqrt{3}}$$

### E) $\csc(7\pi/6)$
QIII, ref $= \pi/6$, sin **negative**:
$$\sin(7\pi/6) = -1/2 \Rightarrow \csc = \frac{1}{-1/2} = \boxed{-2}$$

### F) $\cot(-\pi/2)$
$$\cot(-\pi/2) = \frac{\cos(-\pi/2)}{\sin(-\pi/2)} = \frac{0}{-1} = \boxed{0}$$

---

## Problem 3 — All Six Trig Functions in △ABC

Right angle at C. Legs: opposite $\alpha$ = 5, adjacent $\alpha$ = 12.

$$c = \sqrt{5^2 + 12^2} = \sqrt{169} = 13$$

| Function | Value | Reciprocal | Value |
|----------|-------|------------|-------|
| $\sin\alpha$ | $5/13$ | $\csc\alpha$ | $13/5$ |
| $\cos\alpha$ | $12/13$ | $\sec\alpha$ | $13/12$ |
| $\tan\alpha$ | $5/12$ | $\cot\alpha$ | $12/5$ |

---

## Problem 4 — Solve Right Triangle: $B=72°,\ b=24$ cm

$$A = 180° - 90° - 72° = \boxed{18°}$$

$$c = \frac{24}{\sin 72°} = \frac{24}{0.9511} \approx \boxed{25.24 \text{ cm}}$$

$$a = \frac{24}{\tan 72°} = \frac{24}{3.0777} \approx \boxed{7.80 \text{ cm}}$$

---

## Problem 7 — Domain & Range of $y = -3\cos(x + \pi/2) + 2$

- $A = -3,\ B = 1,\ C = \pi/2,\ D = 2$
- **Amplitude** $= 3$
- **Period** $= 2\pi$
- **Midline** $y = 2$
- **Range** $= [2-3,\ 2+3] = \boxed{[-1,\ 5]}$
- **Domain of one period:** Phase shift $= -\pi/2$ (left), so one period runs $\boxed{[-\pi/2,\ 3\pi/2]}$

---

## Problem 8 — Write a Cosine Equation

**Given:** Amplitude $= 6$, Period $= \pi$, Phase shift $= \pi/2$ left

$$B = \frac{2\pi}{\pi} = 2 \qquad C = B \cdot \frac{\pi}{2} = \pi$$

$$\boxed{y = 6\cos(2x + \pi)}$$

---

## Problem 9 — Six Trig Functions from Point $(-5, -3)$

$$r = \sqrt{25+9} = \sqrt{34}$$

QIII → sin, cos, csc, sec negative; tan, cot positive.

| Function | Value |
|----------|-------|
| $\sin\theta$ | $-3\sqrt{34}/34$ |
| $\cos\theta$ | $-5\sqrt{34}/34$ |
| $\tan\theta$ | $3/5$ |
| $\csc\theta$ | $-\sqrt{34}/3$ |
| $\sec\theta$ | $-\sqrt{34}/5$ |
| $\cot\theta$ | $5/3$ |

---

## Problem 10 — Find x: $\tan x = -1,\ 0 \le x \le \pi$

Reference angle $= \pi/4$. On $[0,\pi]$, tan is negative only in QII:
$$x = \pi - \pi/4 = \boxed{3\pi/4}$$

---

## Problem 12 — Inverse Trig Values

> Range restrictions: $\sin^{-1} \to [-\pi/2, \pi/2]$ | $\cos^{-1} \to [0, \pi]$ | $\tan^{-1} \to (-\pi/2, \pi/2)$

| Part | Expression | Answer |
|------|-----------|--------|
| A | $\cos^{-1}(\sin 5\pi/3)$ | $5\pi/6$ |
| B | $\sin^{-1}(-\sqrt{3}/2)$ | $-\pi/3$ |
| C | undefined input | undefined |
| D | $\cos^{-1}(\sqrt{2}/2)$ | $\pi/4$ |
| E | $\sin^{-1}(-1/2)$ | $-\pi/6$ |
| F | $\tan^{-1}(-\sqrt{3}/3)$ | $-\pi/6$ |
| G | $\cos^{-1}(\sqrt{3}/2)$ | $\pi/6$ |
| H | $\tan^{-1}(-\sqrt{3})$ | $-\pi/3$ |
| I | $\cos^{-1}(-\sqrt{2}/2)$ | $3\pi/4$ |

**Worked example for A:**
$\sin(5\pi/3)$: QIV, ref $= \pi/3$, negative $\Rightarrow -\sqrt{3}/2$.
$\cos^{-1}(-\sqrt{3}/2)$: range $[0,\pi]$, in QII $\Rightarrow \pi - \pi/6 = 5\pi/6$

---

## Problems 13–18 — Graphs

> Formula sheet: $y = A\sin(Bx+C)+D$ | **Amplitude** $=|A|$ | **Period** $=2\pi/B$ | **Phase shift** $=-C/B$ | **Midline** $=D$

---

### #13 — $y = \sin(x + \pi/2)$
**Amplitude:** 1 | **Period:** $2\pi$ | **Phase shift:** $\pi/2$ left | **Equivalent to** $\cos x$

![[graph13_sin_phase.svg]]

---

### #14 — $y = -\frac{1}{2}\cos x$
**Amplitude:** $1/2$ | **Period:** $2\pi$ | **Reflected** (trough at $x=0$, peaks at $x=\pm\pi$)

![[graph14_neg_half_cos.svg]]

---

### #15 — $y = \sin(2x) + 1$
**Amplitude:** 1 | **Period:** $\pi$ | **Midline:** $y=1$ | Oscillates between 0 and 2

![[graph15_sin2x_plus1.svg]]

---

### #16 — $y = \csc x$
**Period:** $2\pi$ | **Unbounded** | **Asymptotes:** $x = n\pi$ | Sketch sine first, then draw U-branches

![[graph16_csc.svg]]

---

### #17 — $y = -2\cos(x + \pi)$
**Amplitude:** 2 | **Period:** $2\pi$ | Note: $-\cos(x+\pi) = \cos x$, so this **equals $2\cos x$**

![[graph17_neg2cos_phase.svg]]

---

### #18 — $y = -\sec(x - \pi)$
**Period:** $2\pi$ | **Asymptotes:** $x = \pi/2 + n\pi$ | Note: $-\sec(x-\pi) = \sec x$

![[graph18_neg_sec.svg]]

---

## Common Mistakes

1. **Even vs. odd:** $\cos(-\theta)=\cos\theta$ but $\sin(-\theta)=-\sin\theta$
2. **Reduce large angles** before finding reference angle (subtract $2\pi$ repeatedly)
3. **Period formula:** $2\pi/B$, not $2\pi \cdot B$
4. **QIII tan is positive** — both sin and cos are negative, so they cancel
5. **csc/sec graphs:** draw the parent sin/cos guide first, then branch from each peak/trough
6. **$\cos^{-1}$ never outputs negatives** — its range is $[0,\pi]$ only
