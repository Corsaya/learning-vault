# AP Chem — Unit 5 Progress Check: MCQ Answers
*(Kinetics — Questions 1–27)*

> **Note:** These questions cover Unit 5 (Kinetics) content and are filed here as `Unit_5_Progress_Check.md`.

---

## Q1. Determine the experimental rate law from the data table

Reaction: $2\text{X} + \text{Y}_2 \rightarrow \text{X}_2\text{Y}_2$

| Exp | $[\text{X}]_i$ (M) | $[\text{Y}_2]_i$ (M) | Rate (M/s) |
|---|---|---|---|
| 1 | 0.15 | 0.10 | 32 |
| 2 | 0.15 | 0.20 | 64 |
| 3 | 0.30 | 0.20 | 128 |

**Order in $\text{Y}_2$** (Exp 1 vs. 2 — $[\text{X}]$ constant):
$$\frac{\text{Rate}_2}{\text{Rate}_1} = \frac{64}{32} = 2 \qquad \frac{[\text{Y}_2]_2}{[\text{Y}_2]_1} = \frac{0.20}{0.10} = 2$$
$$2 = 2^n \Rightarrow n = 1 \quad \text{(first order in } \text{Y}_2\text{)}$$

**Order in X** (Exp 2 vs. 3 — $[\text{Y}_2]$ constant):
$$\frac{\text{Rate}_3}{\text{Rate}_2} = \frac{128}{64} = 2 \qquad \frac{[\text{X}]_3}{[\text{X}]_2} = \frac{0.30}{0.15} = 2$$
$$2 = 2^m \Rightarrow m = 1 \quad \text{(first order in X)}$$

Rate law: $\text{Rate} = k[\text{X}][\text{Y}_2]$

**Answer: A — Rate = $k[\text{X}][\text{Y}_2]$**

The rate doubles when either $[\text{X}]$ or $[\text{Y}_2]$ doubles alone, indicating first-order dependence on each reactant. The experimental rate law is determined solely from initial rate data — never from stoichiometric coefficients.

> **Trap:** Choosing B ($k[\text{X}]^2[\text{Y}_2]$). The stoichiometric coefficient of X is 2, and students incorrectly assume this means second-order in X. Reaction orders must be determined experimentally from the data table — coefficients are irrelevant to the rate law.

---

## Q2. Rate of disappearance of X in experiment 1

From Q1: Rate law is $\text{Rate} = k[\text{X}][\text{Y}_2]$, and Rate (appearance of $\text{X}_2\text{Y}_2$) = 32 M/s in experiment 1.

Relate rates using stoichiometry:
$$\text{Rate} = -\frac{1}{2}\frac{\Delta[\text{X}]}{\Delta t} = \frac{\Delta[\text{X}_2\text{Y}_2]}{\Delta t}$$

So the rate of disappearance of X:
$$-\frac{\Delta[\text{X}]}{\Delta t} = 2 \times 32\ \text{M/s} = 64\ \text{M/s}$$

**Answer: C — 64 M/s**

The stoichiometric coefficient of X in the balanced equation is 2, while $\text{X}_2\text{Y}_2$ has a coefficient of 1. The rate of disappearance of X is twice the rate of appearance of product.

> **Trap:** Choosing B (32 M/s) — treating the rate of disappearance of X as equal to the rate given. The given rate is the rate of appearance of the product $\text{X}_2\text{Y}_2$. Must multiply by the stoichiometric ratio: coefficient of X (2) divided by coefficient of product (1).

---

## Q3. Claim and justification for higher rates measured by second chemist

Same concentrations and temperature, but faster rates. The question asks for the MOST likely cause. Same $T$ rules out temperature. Same concentrations rules out concentration. A catalyst provides a different reaction pathway with lower $E_a$.

**Answer: C — The second chemist must have added a catalyst for the reaction, thus providing a different reaction pathway for the reactant particles to react with an activation energy that was lower than that of the uncatalyzed reaction in the first chemist's experiments.**

A catalyst lowers $E_a$ by providing an alternative reaction pathway. At the same temperature, a greater fraction of collisions now have energy $\geq E_a$, increasing the rate. This explanation is consistent with all given constraints (same $T$, same concentrations).

> **Trap:** Choosing A or B (lower pressure). Lower gas pressure would reduce the frequency of collisions between reactant molecules, which would DECREASE the reaction rate — the opposite of what was observed. Answer D is wrong because a catalyst does not provide energy to particles; it lowers the activation energy barrier.

---

## Q4. Which condition increases the rate of sucrose hydrolysis?

Rate is directly proportional to $[\text{sucrose}]$. The reaction: $\text{C}_{12}\text{H}_{22}\text{O}_{11}(aq) + \text{H}_2\text{O}(l) \rightarrow 2\text{C}_6\text{H}_{12}\text{O}_6(aq)$

Evaluate each option:
- A: Increasing water — water is a pure liquid; its concentration does not appear in the rate law for a solution reaction. More water does not change the sucrose concentration.
- B: Decreasing temperature — decreases average $KE$, fewer collisions exceed $E_a$ → rate DECREASES.
- C: Increasing $[\text{sucrose}]$ — rate $\propto [\text{sucrose}]$; more sucrose → more frequent collisions with water → rate increases. ✓
- D: Decreasing $[\text{sucrose}]$ — reduces rate.

**Answer: C — Increasing the concentration of sucrose will increase the rate of hydrolysis by increasing the frequency of collisions between the sucrose and the water molecules.**

Since rate is directly proportional to $[\text{sucrose}]$, increasing sucrose concentration increases the frequency of effective collisions with water molecules, raising the reaction rate.

> **Trap:** Choosing A (increasing water). The concentration of a pure liquid (water as solvent) is constant and does not appear in the rate law. Adding more water to a solution of sucrose actually dilutes the sucrose, decreasing $[\text{sucrose}]$ and thus decreasing the rate.

---

## Q5. Why is the rate of formation of $\text{N}_2$ greater in trial 2 than trial 1?

$2\text{NO}(g) + 2\text{H}_2(g) \rightarrow \text{N}_2(g) + 2\text{H}_2\text{O}(g)$

| Trial | [NO] (M) | $[\text{H}_2]$ (M) | Rate of $\text{N}_2$ (M/s) |
|---|---|---|---|
| 1 | 0.10 | 0.10 | $1.2 \times 10^{-3}$ |
| 2 | 0.10 | 0.20 | $2.4 \times 10^{-3}$ |

Same temperature → same $k$, same $E_a$. $[\text{NO}]$ is constant. $[\text{H}_2]$ doubled → rate doubled. The rate constant does not change between trials at the same temperature.

**Answer: B — The frequency of collisions between reactant molecules is greater in trial 2 than it is in trial 1.**

Doubling $[\text{H}_2]$ at constant $[\text{NO}]$ increases the frequency of collisions between $\text{NO}$ and $\text{H}_2$ molecules. More collisions per unit time → more successful collisions per unit time → higher rate.

> **Trap:** Choosing C or D (rate constant changes). The rate constant $k$ depends only on temperature, not on concentration. Since temperature is constant in both trials, $k$ is identical in both. The change in rate is entirely due to the change in collision frequency from the higher $[\text{H}_2]$.

---

## Q6. Which trial has a faster initial rate — piece vs. powder of Zn(s)?

$\text{Zn}(s) + 2\text{HCl}(aq) \rightarrow \text{ZnCl}_2(aq) + \text{H}_2(g)$

Trial 1: 5.0 g piece of $\text{Zn}(s)$. Trial 2: 5.0 g powdered $\text{Zn}(s)$. Same mass, same $[\text{HCl}]$.

Powdered zinc has much greater surface area than a single piece. For a heterogeneous reaction (solid + liquid), only the surface of the solid is exposed to the reactant. More surface area → more collision sites → faster rate.

**Answer: D — Trial 2, because the sample of $\text{Zn}(s)$ has a greater surface area for the reaction to take place.**

Powdering a solid dramatically increases the surface area available for contact with $\text{HCl}(aq)$. More surface area means more $\text{Zn}$ atoms are accessible for reaction simultaneously, increasing the rate of $\text{H}_2$ production.

> **Trap:** Choosing A (higher concentration of Zn(s)). The "concentration" of a pure solid is not a variable in the rate law — solids have fixed density regardless of mass. The relevant factor for a solid reactant is surface area, not concentration.

---

## Q7. Which claim about $\text{rate} = k[\text{CH}_3\text{I}][\text{NaOH}]$ is correct?

$\text{CH}_3\text{I} + \text{NaOH} \rightarrow \text{CH}_3\text{OH} + \text{NaI}$

Evaluate each option:
- A: Slower rate with increasing temperature — FALSE. Higher $T$ → higher $k$ → faster rate.
- B: Rate doubles when BOTH $[\text{CH}_3\text{I}]$ and $[\text{NaOH}]$ are doubled — calculate: $\text{Rate}' = k(2[\text{CH}_3\text{I}])(2[\text{NaOH}]) = 4k[\text{CH}_3\text{I}][\text{NaOH}] = 4 \times \text{Rate}$ → 4-fold increase, NOT 2-fold. FALSE.
- C: Rate doubles when only $[\text{CH}_3\text{I}]$ is doubled — $\text{Rate}' = k(2[\text{CH}_3\text{I}])[\text{NaOH}] = 2 \times \text{Rate}$ ✓ TRUE.
- D: More $\text{CH}_3\text{OH}$ produced if concentrations are halved — FALSE; lower concentrations mean slower rate and less product formed.

**Answer: C — The rate of the reaction will double if the concentration of $\text{CH}_3\text{I}$ is doubled while keeping the concentration of $\text{NaOH}$ constant.**

The rate law shows first-order dependence on each reactant. Doubling only $[\text{CH}_3\text{I}]$ multiplies the rate by $2^1 = 2$. This is the defining property of a first-order dependence.

> **Trap:** Choosing B. When BOTH concentrations are doubled, the rate increases by $2 \times 2 = 4$-fold (not 2-fold), because the rate law includes both concentrations multiplicatively.

---

## Q8. What is the order of the reaction with respect to $\text{N}_2\text{O}_5$ based on the graphs?

$2\text{N}_2\text{O}_5(g) \rightarrow 4\text{NO}_2(g) + \text{O}_2(g)$

Three graphs shown: $[\text{N}_2\text{O}_5]$ vs. time (curved), $\ln[\text{N}_2\text{O}_5]$ vs. time (straight line), $1/[\text{N}_2\text{O}_5]$ vs. time (curved upward).

The linearization rules:
- Zeroth order: $[\text{A}]$ vs. $t$ is linear
- **First order:** $\ln[\text{A}]$ vs. $t$ is linear ← straight line here
- Second order: $1/[\text{A}]$ vs. $t$ is linear

The middle graph ($\ln[\text{N}_2\text{O}_5]$ vs. time) is the straight line.

**Answer: B — First order**

A linear $\ln[\text{A}]$ vs. time plot is the diagnostic signature of a first-order reaction ($\ln[\text{A}] = -kt + \ln[\text{A}]_0$). This is the integrated rate law test: determine which plot is linear to identify the reaction order.

> **Trap:** Choosing C (second order). Second order gives a linear $1/[\text{A}]$ vs. $t$ plot. The rightmost graph ($1/[\text{N}_2\text{O}_5]$ vs. $t$) is curved (not linear), ruling out second order.

---

## Q9. Which quantity plotted vs. time gives a straight line for first-order $^{214}_{83}\text{Bi}$ decay?

$^{214}_{83}\text{Bi} \rightarrow ^{214}_{84}\text{Po} + ^{0}_{-1}e$

This is stated to be a **first-order** reaction. First-order integrated rate law:
$$\ln[\text{A}] = -kt + \ln[\text{A}]_0$$

Since moles $n$ is directly proportional to concentration (same volume), $\ln n_{\text{Bi}}$ vs. time is also linear. The answer choices are $n_{\text{Bi}}$, $n_{\text{Po}}$, $\ln(n_{\text{Bi}})$, and $1/n_{\text{Bi}}$.

- $n_{\text{Bi}}$ vs. $t$: exponential decay curve — not linear
- $n_{\text{Po}}$ vs. $t$: exponential growth — not linear
- $\ln(n_{\text{Bi}})$ vs. $t$: linear ✓ (first-order integrated rate law)
- $1/n_{\text{Bi}}$ vs. $t$: linear only for second-order — not here

**Answer: C — $\ln(n_{\text{Bi}})$**

For a first-order reaction, $\ln[\text{A}]$ (or equivalently $\ln n_\text{A}$) decreases linearly with time. This is the graphical test for first-order kinetics.

> **Trap:** Choosing A ($n_{\text{Bi}}$ vs. $t$). This plot produces an exponential decay curve for a first-order reaction, not a straight line. Students confuse "the reactant decreases" with "a plot of reactant concentration is linear."

---

## Q10. Rate law for catalyzed decomposition of $\text{NH}_3(g)$ from graph

$2\text{NH}_3(g) \xrightarrow{\text{catalyst}} \text{N}_2(g) + 3\text{H}_2(g)$

Graph: $[\text{NH}_3]$ vs. time for two different initial concentrations — both give straight lines (parallel lines, different starting points, same slope magnitude).

Linearization rules: a straight line of $[\text{A}]$ vs. time → **zeroth order**.

Rate $= k$ (independent of $[\text{NH}_3]$). The slope of $[\text{NH}_3]$ vs. time equals $-k$.

**Answer: A — Rate = $k$**

The linear $[\text{NH}_3]$ vs. time plot is the diagnostic test for zeroth-order kinetics. In a zeroth-order reaction, the rate is constant and independent of reactant concentration — the rate is determined solely by the rate constant $k$.

> **Trap:** Choosing B (Rate $= k[\text{NH}_3]$, first order). A first-order reaction gives a straight line on $\ln[\text{NH}_3]$ vs. time, not on $[\text{NH}_3]$ vs. time. The $[\text{NH}_3]$ vs. time curve would be exponential for first order — not linear as shown.

---

## Q11. Which statement about the $\text{H}_2\text{O}_2$ mechanism is correct?

Step 1: $\text{H}_2\text{O}_2 + \text{I}^- \rightarrow \text{IO}^- + \text{H}_2\text{O}$
Step 2: $\text{H}_2\text{O}_2 + \text{IO}^- \rightarrow \text{H}_2\text{O} + \text{O}_2 + \text{I}^-$

**Overall equation:** Add steps, cancel intermediates ($\text{IO}^-$ made in step 1, consumed in step 2):
$$2\text{H}_2\text{O}_2 \rightarrow 2\text{H}_2\text{O} + \text{O}_2$$

**Rate law for elementary step 2:** Rate $= k[\text{H}_2\text{O}_2][\text{IO}^-]$ (bimolecular — write reactants of that elementary step directly).

Check the answer choices:
- A: Overall equation $2\text{H}_2\text{O}_2 + \text{I}^- \rightarrow 2\text{H}_2\text{O} + \text{O}_2 + \text{I}^-$, rate $= k[\text{H}_2\text{O}_2][\text{IO}^-]$ ✓ overall equation correct; rate law for step 2 correct ✓
- C: Overall $2\text{H}_2\text{O}_2 \rightarrow 2\text{H}_2\text{O} + \text{O}_2$ (also correct canceling $\text{I}^-$); rate for step 1 $= k[\text{H}_2\text{O}_2][\text{I}^-]$ ✓

Wait — A's overall equation includes $\text{I}^-$ on both sides (not fully cancelled), which is actually written as a spectator — technically both A and C have the same net chemistry. But C states the overall equation without the $\text{I}^-$ (correct net), and the rate law for elementary step 1 is $k[\text{H}_2\text{O}_2][\text{I}^-]$ ✓.

The fully cancelled overall reaction: $2\text{H}_2\text{O}_2 \rightarrow 2\text{H}_2\text{O} + \text{O}_2$. Options C and D both give this net equation. Step 1 rate law: $k[\text{H}_2\text{O}_2][\text{I}^-]$ (both reactants of step 1). Option C matches; D says $k[\text{H}_2\text{O}_2]^2$ (wrong).

**Answer: C — Overall: $2\text{H}_2\text{O}_2 \rightarrow 2\text{H}_2\text{O} + \text{O}_2$; rate for step 1 $= k[\text{H}_2\text{O}_2][\text{I}^-]$**

The overall equation is obtained by adding both steps and cancelling $\text{IO}^-$ (intermediate) and $\text{I}^-$ (catalyst — consumed in step 1, regenerated in step 2). For any elementary step, the rate law is written directly from its reactants: step 1 has $\text{H}_2\text{O}_2$ and $\text{I}^-$ → $\text{Rate} = k[\text{H}_2\text{O}_2][\text{I}^-]$.

> **Trap:** Choosing A. Option A's overall equation leaves $\text{I}^-$ on both sides (not cancelled), making it appear as a reactant/product rather than a catalyst. The $\text{I}^-$ is consumed in step 1 and regenerated in step 2 — it is a catalyst and must be fully cancelled in the net equation.

---

## Q12. Identify the overall equation and rate law from the $\text{N}_2\text{O}_5$ mechanism

Step 1: $\text{N}_2\text{O}_5 \rightarrow \text{NO}_2 + \text{NO}_3$ (slow)
Step 2: $\text{NO}_2 + \text{NO}_3 \rightarrow \text{NO}_2 + \text{NO} + \text{O}_2$ (fast)
Step 3: $\text{NO} + \text{N}_2\text{O}_5 \rightarrow 3\text{NO}_2$ (fast)

**Overall equation:** Add all three steps, cancel intermediates:
- Intermediates: $\text{NO}_3$ (made in 1, used in 2), $\text{NO}_2$ (appears in 2 products and 3; track carefully), $\text{NO}$ (made in 2, used in 3)

Adding: $\text{N}_2\text{O}_5 + \text{NO}_2 + \text{NO}_3 + \text{NO} + \text{N}_2\text{O}_5 \rightarrow \text{NO}_2 + \text{NO}_3 + \text{NO}_2 + \text{NO} + \text{O}_2 + 3\text{NO}_2$

Net: $2\text{N}_2\text{O}_5 \rightarrow 4\text{NO}_2 + \text{O}_2$

**Rate law:** Determined by the slow (rate-determining) step: Step 1 $\rightarrow \text{Rate} = k[\text{N}_2\text{O}_5]$

**Answer: B — $2\text{N}_2\text{O}_5(g) \rightarrow 4\text{NO}_2(g) + \text{O}_2(g)$; rate $= k[\text{N}_2\text{O}_5]$**

The rate-determining step is step 1 (slow), which involves only $\text{N}_2\text{O}_5$ as a reactant → rate law is first-order in $\text{N}_2\text{O}_5$. The overall equation comes from summing all steps and cancelling intermediates.

> **Trap:** Choosing C ($\text{rate} = k[\text{N}_2\text{O}_5]^2$). The slow step is unimolecular ($\text{N}_2\text{O}_5$ alone), giving first-order kinetics. Second order would require two $\text{N}_2\text{O}_5$ molecules in the slow step.

---

## Q13. Identify step 1 and the overall rate law given step 2 (fast) and the overall reaction

Step 1: ? (slow)
Step 2: $\text{NO}_2(g) + \text{F}(g) \rightarrow \text{NO}_2\text{F}(g)$ (fast)
Overall: $2\text{NO}_2(g) + \text{F}_2(g) \rightarrow 2\text{NO}_2\text{F}(g)$

**Find step 1:** Subtract step 2 from overall:
Overall uses $2\text{NO}_2 + \text{F}_2 \rightarrow 2\text{NO}_2\text{F}$
Step 2 uses $\text{NO}_2 + \text{F} \rightarrow \text{NO}_2\text{F}$
Step 1 must be: $\text{NO}_2 + \text{F}_2 \rightarrow \text{NO}_2\text{F} + \text{F}$ (produces intermediate F used in step 2)

**Rate law:** Slow step 1 involves $\text{NO}_2$ and $\text{F}_2$:
$$\text{Rate} = k[\text{NO}_2][\text{F}_2]$$

Check answer C: Step 1 is $2\text{NO}_2 + \text{F}_2 \rightarrow 2\text{NO}_2\text{F}$ — this would just be the overall reaction in one step, inconsistent.

Answer A: Step 1 = $\text{NO}_2 + \text{F}_2 \rightarrow \text{NO}_2\text{F} + \text{F}$; rate $= k[\text{NO}_2][\text{F}_2]$ ✓

**Answer: A — Step 1: $\text{NO}_2(g) + \text{F}_2(g) \rightarrow \text{NO}_2\text{F}(g) + \text{F}(g)$; rate $= k[\text{NO}_2][\text{F}_2]$**

Step 1 must produce the intermediate F (consumed in step 2) and its reactants must sum with step 2 to give the overall equation. The slow step directly gives the rate law: bimolecular with $\text{NO}_2$ and $\text{F}_2$.

> **Trap:** Choosing C (step 1 = entire overall reaction with rate $= k[\text{NO}_2][\text{F}]$). The intermediate F must be produced in step 1 and consumed in step 2 — it cannot appear in the overall equation. Option C uses F (an intermediate) in the rate law, which is not allowed.

---

## Q14. Which elementary reaction is orientation-independent, and why?

Reaction A: $\text{O} + \text{O} \rightarrow \text{O}_2$ — both reactants are individual oxygen atoms (spherically symmetric electron clouds)
Reaction B: $\text{C}_2\text{H}_4 + \text{C}_2\text{H}_4 \rightarrow \text{C}_4\text{H}_8$ — double bond formation; specific pi-orbital overlap needed
Reaction C: $\text{CO} + \text{O}_2 \rightarrow \text{CO}_2 + \text{O}$ — C must approach O to form the new bond; orientation matters
Reaction D: $\text{CH}_3\text{I} + \text{Br}^- \rightarrow \text{CH}_3\text{Br} + \text{I}^-$ — $S_N2$; Br must attack from the back side of C; highly orientation-dependent

**Answer: A — Reaction A, because the electron clouds of the O atoms are distributed symmetrically.**

Oxygen atoms are spherical with symmetrically distributed electron clouds. A collision from any direction results in the same orbital overlap and the same potential for bond formation. No preferred orientation exists because the atom looks the same from all angles.

> **Trap:** Choosing C (both CO and $\text{O}_2$ are linear). Linear geometry does not mean orientation-independence for reactions — in fact, CO must approach $\text{O}_2$ with the correct end (the C end) to form the new C–O bond. Linearity of a molecule does not eliminate orientation requirements.

---

## Q15. Which collision diagram represents an effective collision for CO + $\text{NO}_2$ → $\text{CO}_2$ + NO?

Products: $\text{CO}_2$ and $\text{NO}$. This means a C–O bond must form between C (from CO) and O (from $\text{NO}_2$).

Diagram 1: CO molecule approaching $\text{NO}_2$ with the C atom facing the O of $\text{NO}_2$ — this positions C to bond to O, forming $\text{CO}_2$. Correct orientation. ✓
Diagram 2: CO molecule approaching $\text{NO}_2$ with the O of CO facing the N of $\text{NO}_2$ — incorrect bonding geometry; the C does not contact O.

An effective collision requires both sufficient energy ($\geq E_a$) AND correct orientation.

**Answer: B — Diagram 1 represents an effective collision because the two molecules have the proper orientation to form a new C–O bond as long as they possess enough energy to overcome the activation energy barrier.**

Effective collisions require correct orientation AND sufficient energy. Diagram 1 shows the C end of CO approaching the O of $\text{NO}_2$, which is the necessary geometry to form the new C–O bond in $\text{CO}_2$.

> **Trap:** Choosing A (molecules have same size and energy → larger rate constant $k$). The rate constant is not determined by whether molecules have the same size. $k$ depends on temperature and $E_a$ — not on molecular size similarity.

---

## Q16. At which temperature is the reactant consumed fastest (Maxwell–Boltzmann distribution)?

The diagram shows four curves $T_1 > T_2 > T_3 > T_4$: at $T_1$ the peak is highest (lower speed peak, narrow), at $T_4$ the peak is lowest (broad, flattened, most area to the right of $E_a$).

The fastest rate requires the greatest fraction of molecules with energy $\geq E_a$ (marked by the dashed line). At higher temperature, the distribution broadens, shifts right, and MORE molecules exceed the activation energy threshold.

$T_4$ has the broadest, most right-shifted distribution → largest fraction with $E \geq E_a$ → fastest rate.

**Answer: D — At $T_4$, because a larger fraction of the molecules have an energy that is equal to or greater than the activation energy.**

At higher temperature, the Maxwell–Boltzmann distribution broadens and shifts to higher energies. The area to the right of the $E_a$ line (fraction of molecules with sufficient energy to react) is greatest at $T_4$.

> **Trap:** Choosing A ($T_1$ — highest peak). The highest peak means most molecules cluster around a lower speed — $T_1$ is the LOWEST temperature. Students confuse "tallest peak = most energy" when in fact a taller, narrower peak means the distribution is more concentrated at lower speeds. Higher temperature = broader, lower, right-shifted curve.

---

## Q17. Which mechanism matches the particle diagram (X = open circle, Y = filled circle)?

Before: many X and some Y particles separately. During: fewer X, intermediate XY and $\text{X}_2$ visible. After: product $\text{X}_2\text{Y}$, fewer particles.

Diagram shows: before → X and Y atoms; during → some XY intermediate forms; after → $\text{X}_2\text{Y}$ product. This implies:
Step 1: $\text{X}(g) + \text{Y}(g) \rightarrow \text{XY}(g)$
Step 2: $\text{X}(g) + \text{XY}(g) \rightarrow \text{X}_2\text{Y}(g)$

This matches option C (two steps; XY is the intermediate produced in step 1 and consumed in step 2).

**Answer: C — Two steps: Step 1: $\text{X}(g) + \text{Y}(g) \rightarrow \text{XY}(g)$; Step 2: $\text{X}(g) + \text{XY}(g) \rightarrow \text{X}_2\text{Y}(g)$**

The particle diagram shows XY appearing during the reaction but not present before or after — the definition of a reaction intermediate. The overall reaction consumes 2 X and 1 Y to produce 1 $\text{X}_2\text{Y}$, which is reproduced by adding steps 1 and 2.

> **Trap:** Choosing D (two steps: $2\text{X} \rightarrow \text{X}_2$, then $\text{X}_2 + \text{Y} \rightarrow \text{X}_2\text{Y}$). This would show $\text{X}_2$ as the intermediate during the reaction, but the particle diagram shows an X–Y bonded intermediate, not an X–X intermediate.

---

## Q18. What is the role of Ru in the synthesis of ammonia?

Diagram: $\text{N}_2$ molecules adsorb onto Ru surface, weakening the N≡N triple bond. N atoms then react with H atoms (also adsorbed) to form $\text{NH}_3$. The Ru surface is present before and after the reaction.

A catalyst is consumed and regenerated — it provides an alternative pathway but is not used up. Ru appears in the diagram as the surface throughout, unchanged by the overall reaction. An intermediate is produced in one step and consumed in a later step — Ru is never consumed. A reactant would be used up.

**Answer: A — Ru is a catalyst.**

Ruthenium provides an alternative reaction pathway (surface adsorption weakens the N≡N bond, lowering $E_a$), but is regenerated after the reaction. Ru appears before the reaction and remains after — the defining characteristic of a catalyst.

> **Trap:** Choosing D (Ru is an intermediate). An intermediate is produced in one step and consumed in a later step — it does not appear in the overall equation as a reactant or product. Ru is present before the reaction starts and is not consumed, ruling out intermediate status.

---

## Q19. Which particle model represents a reaction intermediate?

Three-step mechanism shown with N (grey), O (black), H (open circle) particles.

Step 1: $\text{N}_2 + \text{O}_2 \rightleftharpoons \text{N}_2\text{O}_2$ (reversible)
Step 2: $\text{N}_2\text{O}_2 + \text{O}_2 \rightarrow \text{N}_2\text{O}_3 + \text{O}$ (approximate based on diagram)
Step 3: involves further reaction.

An **intermediate** is produced in one step and consumed in a later step; it does not appear in the overall reactants or products.

The intermediate is produced in Step 1 (the reversible step) and consumed in Step 2; it does not appear in the overall reaction. From the particle diagram, the cluster produced in Step 1 (the $\text{N}_2\text{O}_2$-type species shown as grey N particles bonded to a black O particle) reappears as a reactant in Step 2 and is absent from the final products.

**Answer: D — Three grey particles with one black particle ($\text{N}_2\text{O}$ or $\text{N}_3\text{O}$ cluster)**

The intermediate is produced in step 1 (the reversible step) and consumed in step 2. It does not appear in the final products.

> **Trap:** Choosing B (two open circles = H₂). H₂ is a reactant given at the start, not an intermediate. Intermediates are produced during the reaction, not present at the beginning.

---

## Q20. Rate law for $\text{O}_3$ decomposition with NO catalyst

$\text{O}_3(g) + \text{O}(g) \rightarrow 2\text{O}_2(g)$

Mechanism:
Step 1: $\text{O}_3 + \text{NO} \rightarrow \text{NO}_2 + \text{O}_2$ (slow)
Step 2: $\text{NO}_2 + \text{O} \rightarrow \text{NO} + \text{O}_2$ (fast)

Rate-determining step = Step 1 (slow). Rate law written directly from step 1 reactants:
$$\text{Rate} = k[\text{O}_3][\text{NO}]$$

Only original reactant species may appear in the rate law (no intermediates). $\text{NO}$ is a catalyst (consumed in step 1, regenerated in step 2) — it IS present at the start and can appear in the rate law.

**Answer: A — Rate $= k[\text{O}_3][\text{NO}]$**

The slow step (step 1) is the rate-determining step. For elementary reactions, the rate law is written directly from the stoichiometry of that step's reactants: $\text{O}_3$ and $\text{NO}$ → rate $= k[\text{O}_3][\text{NO}]$.

> **Trap:** Choosing C or D (includes O or NO appears wrong). O is a reactant of step 2 (the fast step) — the fast step does not determine the rate. The rate law must reflect the slow step. NO is a catalyst, not an intermediate, so it may legitimately appear in the rate law.

---

## Q21. Which rate law is consistent with the $\text{NO}_2 + \text{CO}$ mechanism?

$\text{NO}_2(g) + \text{CO}(g) \rightarrow \text{NO}(g) + \text{CO}_2(g)$

Step 1: $2\text{NO}_2(g) \rightarrow \text{NO}_3(g) + \text{NO}(g)$ (slow)
Step 2: $\text{NO}_3(g) + \text{CO}(g) \rightarrow \text{NO}_2(g) + \text{CO}_2(g)$ (fast)

Rate-determining step = Step 1 (slow). Step 1 reactants: $2\text{NO}_2$:
$$\text{Rate} = k[\text{NO}_2]^2$$

$\text{NO}_3$ is an intermediate (produced in step 1, consumed in step 2) — cannot appear in the rate law.

**Answer: B — Rate $= k[\text{NO}_2]^2$**

The slow step involves two $\text{NO}_2$ molecules colliding → second-order in $\text{NO}_2$, zero-order in $\text{CO}$. The fast step does not influence the rate law. The intermediate $\text{NO}_3$ cannot appear in the rate law.

> **Trap:** Choosing D (rate $= k[\text{NO}_2][\text{CO}]$). CO only appears in step 2 (the fast step), so it does not appear in the rate law. The overall balanced equation suggests both $\text{NO}_2$ and CO should appear, but the rate law is determined by the slow step — not the stoichiometry of the overall reaction.

---

## Q22. Rate prediction when $[\text{H}_2]$ and $[\text{IBr}]$ concentrations are both doubled

$\text{H}_2 + 2\text{IBr} \rightarrow \text{I}_2 + 2\text{HBr}$

Step 1: $\text{H}_2 + \text{IBr} \rightarrow \text{HI} + \text{HBr}$ (slow)
Step 2: $\text{HI} + \text{IBr} \rightarrow \text{I}_2 + \text{HBr}$ (fast)

Rate law from slow step (step 1): Rate $= k[\text{H}_2][\text{IBr}]$

If both $[\text{H}_2]$ and $[\text{IBr}]$ are doubled:
$$\text{Rate}' = k(2[\text{H}_2])(2[\text{IBr}]) = 4k[\text{H}_2][\text{IBr}] = 4 \times \text{Rate}$$

**Answer: C — The rate will undergo a 4-fold increase when both $[\text{H}_2]$ and $[\text{IBr}]$ are doubled.**

The rate law $k[\text{H}_2][\text{IBr}]$ is second-order overall. Doubling each concentration multiplies the rate by $2 \times 2 = 4$. Answer choices A and B involve HI and IBr — HI is an intermediate and cannot appear in the rate law.

> **Trap:** Choosing A (4-fold increase when HI and IBr doubled). HI is a reaction intermediate — produced in step 1, consumed in step 2. Intermediates do not appear in the observable rate law and cannot be manipulated as initial reactants.

---

## Q23. Rate law for $2\text{NO}(g) + \text{O}_2(g) \rightarrow 2\text{NO}_2(g)$ with pre-equilibrium

Step 1: $2\text{NO} \rightleftharpoons (\text{NO})_2$ (fast equilibrium)
Step 2: $(\text{NO})_2 + \text{O}_2 \rightleftharpoons 2\text{NO}_2$ (slow)

Rate-determining step = step 2: Rate $= k[\text{(NO)}_2][\text{O}_2]$

But $(\text{NO})_2$ is an intermediate — must eliminate it using the pre-equilibrium from step 1:
$$K_{eq} = \frac{[(\text{NO})_2]}{[\text{NO}]^2} \Rightarrow [(\text{NO})_2] = K_{eq}[\text{NO}]^2$$

Substitute:
$$\text{Rate} = k \cdot K_{eq}[\text{NO}]^2[\text{O}_2] = k'[\text{NO}]^2[\text{O}_2]$$

**Answer: C — rate $= k[\text{NO}]^2[\text{O}_2]$**

The slow step's rate depends on the intermediate $(\text{NO})_2$. Using the fast equilibrium expression to substitute for $[\text{(NO)}_2]$, the rate law in terms of original reactants is second-order in $[\text{NO}]$ and first-order in $[\text{O}_2]$.

> **Trap:** Choosing A (rate $= k[\text{NO}]^2$). This omits $[\text{O}_2]$, which appears as a reactant in the slow step. Both species in the slow step must appear in the rate law (after substituting away intermediates).

---

## Q24. Rate law for $\text{H}_2 + \text{I}_2 \rightarrow 2\text{HI}$ with fast equilibrium pre-step

Step 1: $\text{I}_2 \rightleftharpoons 2\text{I}$ (fast equilibrium)
Step 2: $\text{H}_2 + 2\text{I} \rightarrow 2\text{HI}$ (slow)

Rate from slow step: Rate $= k[\text{H}_2][\text{I}]^2$

I is an intermediate — eliminate using fast equilibrium step 1:
$$K_{eq} = \frac{[\text{I}]^2}{[\text{I}_2]} \Rightarrow [\text{I}]^2 = K_{eq}[\text{I}_2]$$

Substitute:
$$\text{Rate} = k \cdot K_{eq}[\text{H}_2][\text{I}_2] = k'[\text{H}_2][\text{I}_2]$$

**Answer: C — Rate $= k[\text{H}_2][\text{I}_2]$**

After substituting $[\text{I}]^2 = K_{eq}[\text{I}_2]$ from the fast equilibrium, the overall rate law is first-order in each original reactant.

> **Trap:** Choosing D (Rate $= k[\text{I}_2][\text{I}]^2$). This retains I (an intermediate) in the rate law — intermediates cannot appear in the final rate law because they cannot be experimentally controlled as initial concentrations.

---

## Q25. Rate law for $2\text{X}(g) + \text{Y}(g) \rightarrow \text{X}_2\text{Y}(g)$ with fast equilibrium

Step 1: $2\text{X}(g) \rightleftharpoons \text{X}_2(g)$ (fast equilibrium)
Step 2: $\text{X}_2(g) + \text{Y}(g) \rightarrow \text{X}_2\text{Y}(g)$ (slow)

Rate from slow step: Rate $= k[\text{X}_2][\text{Y}]$

$\text{X}_2$ is intermediate — eliminate using step 1 equilibrium:
$$K_{eq} = \frac{[\text{X}_2]}{[\text{X}]^2} \Rightarrow [\text{X}_2] = K_{eq}[\text{X}]^2$$

Substitute:
$$\text{Rate} = k \cdot K_{eq}[\text{X}]^2[\text{Y}] = k'[\text{X}]^2[\text{Y}]$$

**Answer: C — rate $= k[\text{X}]^2[\text{Y}]$**

The intermediate $\text{X}_2$ is eliminated using the equilibrium constant expression for step 1, yielding second-order in X and first-order in Y.

> **Trap:** Choosing B (rate $= k[\text{X}_2][\text{Y}]$). $\text{X}_2$ is a reaction intermediate — it cannot appear in the observable rate law. Always substitute the equilibrium expression to eliminate intermediates and express the rate law in terms of initial reactants only.

---

## Q26. Identify the catalyst in the HCOOH decomposition mechanism

Step 1: $\text{HCOOH} + \text{H}_2\text{SO}_4 \rightarrow \text{HCOOH}_2^+ + \text{HSO}_4^-$
Step 2: $\text{HCOOH}_2^+ \rightarrow \text{HCO}^+ + \text{H}_2\text{O}$
Step 3: $\text{HCO}^+ + \text{HSO}_4^- \rightarrow \text{CO} + \text{H}_2\text{SO}_4$

$\text{H}_2\text{SO}_4$: consumed in step 1, regenerated in step 3 → **catalyst** ✓
$\text{HCOOH}_2^+$: produced in step 1, consumed in step 2 → intermediate
$\text{HCO}^+$: produced in step 2, consumed in step 3 → intermediate
$\text{CO}$: appears in step 3 products only → product of overall reaction

**Answer: A — $\text{H}_2\text{SO}_4$, because it is consumed in the first step of the mechanism and regenerated in a later step.**

A catalyst is defined as a species that is consumed in one step and regenerated in a later step — it does not appear in the net equation as a reactant or product. $\text{H}_2\text{SO}_4$ satisfies this definition exactly.

> **Trap:** Choosing C ($\text{HCOOH}_2^+$ as catalyst). $\text{HCOOH}_2^+$ is produced (step 1) then consumed (step 2) — this defines it as a reaction intermediate, not a catalyst. An intermediate is not present before the reaction begins; a catalyst is.

---

## Q27. Which profile represents the catalyzed reaction?

Diagram: Profile X has one large hump (single high energy barrier). Profile Y has two smaller humps (two transition states, lower overall barrier, with an intermediate valley between them).

A catalyst provides an alternative reaction pathway with **lower activation energy** — it typically introduces additional elementary steps (more transition states) but each individual barrier is lower. Profile Y shows lower individual peaks and an intermediate, consistent with a multi-step catalyzed pathway.

**Answer: D — Profile Y, because it introduces a different reaction path that reduces the activation energy.**

A catalyst lowers $E_a$ by providing an alternative reaction mechanism, often with multiple steps. Profile Y shows a different pathway with lower activation energy peaks compared to Profile X. The overall $\Delta E$ (energy of products minus reactants) is the same for both — catalysts affect the rate, not the thermodynamics.

> **Trap:** Choosing A or B (Profile X = catalyzed). Profile X has a single, higher energy barrier — this represents the uncatalyzed reaction. A catalyst cannot increase the activation energy; it must lower it.

---

## Summary of Key Patterns — Unit 5 Kinetics MCQ

| Pattern | Rule | Questions |
|---|---|---|
| Determine order from rate table | Compare pairs of experiments where one concentration is constant; $\text{rate ratio} = (\text{conc ratio})^n$ | Q1 |
| Rate of disappearance vs. appearance | Multiply rate of appearance of product by stoichiometric coefficient ratio | Q2 |
| Higher rate — same conc, same T | Must be a catalyst (lower $E_a$) | Q3 |
| Concentration effect on rate | Rate $\propto$ [reactant]$^{n}$; higher conc → more collisions → faster rate | Q4, Q5 |
| Surface area of solids | More surface area → more collision sites → faster heterogeneous reaction | Q6 |
| Rate law algebra — doubling both concentrations | Each doubles independently; multiply rate factors: $2 \times 2 = 4$-fold increase | Q7, Q22 |
| Integrated rate law — linearization test | $[\text{A}]$ linear → 0th order; $\ln[\text{A}]$ linear → 1st order; $1/[\text{A}]$ linear → 2nd order | Q8, Q9, Q10 |
| Overall equation from mechanism | Add all steps; cancel species appearing on both sides (intermediates and catalysts cancel) | Q11, Q12, Q13 |
| Rate law from mechanism (simple slow step) | Write rate law from reactants of slow (rate-determining) step only | Q12, Q13, Q20, Q21 |
| Orientation and collision geometry | Spherical atoms have no orientation requirement; molecules with specific bonding geometry DO | Q14, Q15 |
| Maxwell–Boltzmann and activation energy | Higher T → distribution shifts right → more molecules exceed $E_a$ → faster rate | Q16 |
| Identifying intermediates from particle diagrams | Intermediate appears during reaction but not before or after; produced in one step, consumed in next | Q17, Q19 |
| Catalyst identification in mechanism | Consumed in one step, regenerated in a later step; not a net reactant or product | Q18, Q26 |
| Rate law from pre-equilibrium mechanism | Write rate from slow step; substitute fast-equilibrium expression to eliminate intermediates | Q23, Q24, Q25 |
| Energy profile — catalyzed vs. uncatalyzed | Catalyzed: lower $E_a$, often multiple humps (multi-step path), same overall $\Delta E$ | Q27 |
