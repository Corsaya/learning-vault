# AP Chem — Unit 5 Examples: Kinetics

---

## Topic 5.1: Reaction Rates

**Example 1 — Stoichiometric rate relationships (Progress Check Q2):**
Reaction: $2\text{X} + \text{Y}_2 \rightarrow \text{X}_2\text{Y}_2$. Rate of appearance of $\text{X}_2\text{Y}_2$ = 32 M/s in experiment 1.

Find rate of disappearance of X:

$$-\frac{\Delta[\text{X}]}{\Delta t} = \frac{2}{1} \times \frac{\Delta[\text{X}_2\text{Y}_2]}{\Delta t} = 2 \times 32\ \text{M/s} = 64\ \text{M/s}$$

The coefficient of X is 2; the coefficient of product is 1. Rate of X disappearance is twice the rate of product appearance.

*Key move: Multiply the rate of product appearance by the ratio (coefficient of reactant / coefficient of product). The ratio comes from the balanced equation, not from the rate law.*

---

## Topic 5.2: Rate Laws from Data

**Example 2 — Determine rate law from a three-experiment table (Progress Check Q1):**

| Exp | $[\text{X}]_i$ | $[\text{Y}_2]_i$ | Rate (M/s) |
|---|---|---|---|
| 1 | 0.15 | 0.10 | 32 |
| 2 | 0.15 | 0.20 | 64 |
| 3 | 0.30 | 0.20 | 128 |

Step 1 — Order in $\text{Y}_2$ (compare Exp 1 and 2, $[\text{X}]$ constant):
$$\frac{64}{32} = \left(\frac{0.20}{0.10}\right)^n \Rightarrow 2 = 2^n \Rightarrow n = 1$$

Step 2 — Order in X (compare Exp 2 and 3, $[\text{Y}_2]$ constant):
$$\frac{128}{64} = \left(\frac{0.30}{0.15}\right)^m \Rightarrow 2 = 2^m \Rightarrow m = 1$$

Rate law: Rate $= k[\text{X}][\text{Y}_2]$

*Key move: Always hold one concentration constant when comparing experiments. The rate ratio must equal the concentration ratio raised to the power of the order. Stoichiometric coefficients (X has coefficient 2) have no bearing on reaction orders.*

---

**Example 3 — Effect of doubling both concentrations (Progress Check Q7, Q22):**
Rate law: Rate $= k[\text{CH}_3\text{I}][\text{NaOH}]$

If both concentrations are doubled:
$$\text{Rate}' = k(2[\text{CH}_3\text{I}])(2[\text{NaOH}]) = 4 \times k[\text{CH}_3\text{I}][\text{NaOH}] = 4 \times \text{Rate}$$

4-fold increase. If only $[\text{CH}_3\text{I}]$ is doubled: Rate $' = 2 \times$ Rate (doubles, since first-order in it).

*Key move: Each concentration factor is independent — multiply them. For a rate law $k[\text{A}]^m[\text{B}]^n$, doubling both $[\text{A}]$ and $[\text{B}]$ gives $2^m \times 2^n$ factor change.*

---

## Topic 5.3: Integrated Rate Laws

![[integrated_rate_law_u5.svg|697]]
*Linear plot identifies order. Slope magnitude = k.*

**Example 4 — Identify order from three graphs (Progress Check Q8):**
Graphs of $[\text{N}_2\text{O}_5]$ vs. $t$ (curved, decreasing), $\ln[\text{N}_2\text{O}_5]$ vs. $t$ (straight line, negative slope), $1/[\text{N}_2\text{O}_5]$ vs. $t$ (curved, increasing).

The $\ln[\text{N}_2\text{O}_5]$ vs. $t$ graph is the straight line → **first order**.

Integrated rate law: $\ln[\text{N}_2\text{O}_5] = -kt + \ln[\text{N}_2\text{O}_5]_0$

*Key move: Match the linear plot to its order. Only one of the three diagnostic plots will be linear — that identifies the order. If $\ln[\text{A}]$ vs. $t$ is linear, the reaction is first order regardless of the equation's stoichiometry.*

---

**Example 5 — First-order radioactive decay, which plot is linear? (Progress Check Q9):**
$^{214}_{83}\text{Bi} \rightarrow ^{214}_{84}\text{Po} + ^0_{-1}e$ — stated first-order.

For first order: $\ln[\text{A}] = -kt + \ln[\text{A}]_0$. Since moles $\propto$ concentration (same volume), $\ln n_{\text{Bi}} = -kt + \ln n_{\text{Bi},0}$ is also linear.

Answer: $\ln(n_{\text{Bi}})$ vs. time gives a straight line.

| Plot | First-order? |
|---|---|
| $n_{\text{Bi}}$ vs. $t$ | Exponential decay — curved |
| $n_{\text{Po}}$ vs. $t$ | Exponential growth — curved |
| $\ln(n_{\text{Bi}})$ vs. $t$ | **Straight line** ✓ |
| $1/n_{\text{Bi}}$ vs. $t$ | Curved (only linear for 2nd order) |

*Key move: For any first-order process, the logarithm of the quantity (concentration, moles, counts) is linear with time. Always use the reactant's logarithm — not the product.*

---

**Example 6 — Zeroth-order kinetics from graph (Progress Check Q10):**
Two parallel straight lines of $[\text{NH}_3]$ vs. time, with different starting concentrations but same slope magnitude → zeroth order.

Rate $= k$ (constant). The slope of $[\text{A}]$ vs. $t$ is $-k$. The rate does not depend on $[\text{NH}_3]$ at all.

*Key move: Two initial concentrations giving parallel straight lines on a $[\text{A}]$ vs. $t$ plot confirms zeroth order — the rate (= absolute slope) is the same regardless of starting concentration. This is common for surface-catalyzed reactions where all catalyst sites are occupied.*

---

## Topic 5.4: Reaction Mechanisms

![[mechanism_rules_u5.svg|697]]
*Intermediate vs. catalyst, rate law rules, and pre-equilibrium technique.*

**Example 7 — Write overall equation and identify rate law from mechanism (Progress Check Q12):**

Step 1: $\text{N}_2\text{O}_5 \rightarrow \text{NO}_2 + \text{NO}_3$ (slow)
Step 2: $\text{NO}_2 + \text{NO}_3 \rightarrow \text{NO}_2 + \text{NO} + \text{O}_2$ (fast)
Step 3: $\text{NO} + \text{N}_2\text{O}_5 \rightarrow 3\text{NO}_2$ (fast)

Add all steps and cancel intermediates ($\text{NO}_3$, $\text{NO}$, extra $\text{NO}_2$):

$$2\text{N}_2\text{O}_5 \rightarrow 4\text{NO}_2 + \text{O}_2$$

Rate law = from slow step (step 1): Rate $= k[\text{N}_2\text{O}_5]$ (unimolecular, first order)

*Key move: Cancel every species that appears on both sides when all steps are added. Intermediates cancel completely. The slow step is unimolecular here → first order in $\text{N}_2\text{O}_5$ only. Do not be distracted by the 2 in the overall equation — the order comes from the slow step.*

---

**Example 8 — Back-solve for missing slow step (Progress Check Q13):**

Step 1: ? (slow)
Step 2: $\text{NO}_2(g) + \text{F}(g) \rightarrow \text{NO}_2\text{F}(g)$ (fast)
Overall: $2\text{NO}_2(g) + \text{F}_2(g) \rightarrow 2\text{NO}_2\text{F}(g)$

Step 1 = Overall − Step 2:

$$[2\text{NO}_2 + \text{F}_2 \rightarrow 2\text{NO}_2\text{F}] - [\text{NO}_2 + \text{F} \rightarrow \text{NO}_2\text{F}]$$
$$= \text{NO}_2 + \text{F}_2 \rightarrow \text{NO}_2\text{F} + \text{F}$$

Rate law (slow step): Rate $= k[\text{NO}_2][\text{F}_2]$

F is the intermediate: produced in step 1, consumed in step 2.

*Key move: Subtract the known step from the overall equation to find the unknown step. Verify: the intermediate produced in step 1 must be consumed in step 2.*

---

**Example 9 — Catalyst vs. intermediate identification (Progress Check Q26):**

Step 1: $\text{HCOOH} + \text{H}_2\text{SO}_4 \rightarrow \text{HCOOH}_2^+ + \text{HSO}_4^-$
Step 2: $\text{HCOOH}_2^+ \rightarrow \text{HCO}^+ + \text{H}_2\text{O}$
Step 3: $\text{HCO}^+ + \text{HSO}_4^- \rightarrow \text{CO} + \text{H}_2\text{SO}_4$

| Species | Role | Evidence |
|---|---|---|
| $\text{H}_2\text{SO}_4$ | Catalyst | Consumed (step 1), regenerated (step 3) |
| $\text{HCOOH}_2^+$ | Intermediate | Produced (step 1), consumed (step 2) |
| $\text{HCO}^+$ | Intermediate | Produced (step 2), consumed (step 3) |
| $\text{CO}$ | Product | Only appears in final step products |

*Key move: Track each species across ALL steps. Catalyst appears at the start (consumed) and at the end (regenerated) — it brackets the mechanism. Intermediates are born and die within the mechanism.*

---

## Topic 5.5: Collision Theory

**Example 10 — Orientation-independent reaction (Progress Check Q14):**
Four elementary reactions given. Reaction A: $\text{O} + \text{O} \rightarrow \text{O}_2$.

Oxygen atoms are spherical with symmetrically distributed electron clouds. A collision from any direction results in identical orbital overlap. There is no "correct" vs. "incorrect" orientation — every collision from any angle is geometrically effective.

Compare to Reaction D ($\text{CH}_3\text{I} + \text{Br}^-$): the $\text{Br}^-$ must approach the back of the C atom to perform $S_N2$ — strong orientation dependence.

*Key move: Spherical atoms have no orientation requirement because their electron density is uniform in all directions. Molecules with directional bonds (pi bonds, sigma bonds with specific geometry) require correct orientation.*

---

**Example 11 — Effective collision diagram (Progress Check Q15):**
$\text{CO} + \text{NO}_2 \rightarrow \text{CO}_2 + \text{NO}$. Products show C–O bond formation.

Diagram 1: C end of CO facing O of $\text{NO}_2$ → correct orientation. C can bond to O to form $\text{CO}_2$.
Diagram 2: O end of CO facing N of $\text{NO}_2$ → wrong orientation. The atoms that need to bond are not in contact.

Effective collision = Diagram 1 + sufficient energy ($\geq E_a$).

*Key move: For a reaction that forms a specific bond (C–O here), the atom that will form the new bond must face the correct atom on the other molecule. Identify the new bond from the products, then trace which atoms must collide.*

---

**Example 12 — Maxwell–Boltzmann and activation energy (Progress Check Q16):**
Four temperature curves $T_1 > T_2 > T_3 > T_4$ (wait — lower-index = higher peak = narrower = LOWER temperature). Dashed vertical line marks $E_a$.

$T_1$ has the tallest, narrowest peak (lowest temperature). $T_4$ has the lowest, broadest peak (highest temperature). The area to the RIGHT of the $E_a$ line is largest at $T_4$.

At $T_4$: greatest fraction of molecules with $E \geq E_a$ → fastest consumption of reactant.

*Key move: Higher temperature = peak shifts RIGHT + gets LOWER + gets BROADER. The key metric is the area under the curve to the right of $E_a$. Higher T → more area beyond $E_a$ → faster rate. Do NOT pick the highest peak — that is the LOWEST temperature.*

---

## Topic 5.6: Energy Profiles

![[energy_profile_u5.svg|697]]
*Catalyzed vs. uncatalyzed energy profiles.*

**Example 13 — Identify catalyzed profile (Progress Check Q27):**
Profile X: single large hump (one transition state, high $E_a$). Profile Y: two smaller humps with a valley between them (two transition states, lower $E_a$, one intermediate).

Catalyzed reaction: Profile Y. Lower individual $E_a$ humps; multi-step pathway introduced by catalyst; same overall $\Delta E$ as Profile X.

*Key move: A catalyst introduces additional steps with lower energy barriers. More humps = more steps = lower individual $E_a$ per step. Both profiles must start and end at the same energy — the catalyst does not change the thermodynamics.*

---

## Topic 5.7: Rate Laws from Mechanisms — Pre-equilibrium

**Example 14 — Pre-equilibrium: $2\text{NO} + \text{O}_2 \rightarrow 2\text{NO}_2$ (Progress Check Q23):**

Step 1: $2\text{NO} \rightleftharpoons (\text{NO})_2$ (fast equilibrium) → $K_{eq} = \frac{[(\text{NO})_2]}{[\text{NO}]^2}$

Step 2: $(\text{NO})_2 + \text{O}_2 \rightarrow 2\text{NO}_2$ (slow) → Rate $= k[(\text{NO})_2][\text{O}_2]$

Intermediate $(\text{NO})_2$ — eliminate using step 1 equilibrium:
$$[(\text{NO})_2] = K_{eq}[\text{NO}]^2$$
$$\text{Rate} = k \cdot K_{eq}[\text{NO}]^2[\text{O}_2] = k'[\text{NO}]^2[\text{O}_2]$$

*Key move: Write rate from slow step, then substitute the equilibrium expression for each intermediate. Combine $k \cdot K_{eq}$ into a single effective rate constant $k'$. The final rate law must contain only original reactant concentrations.*

---

**Example 15 — Pre-equilibrium: $\text{H}_2 + \text{I}_2 \rightarrow 2\text{HI}$ (Progress Check Q24):**

Step 1: $\text{I}_2 \rightleftharpoons 2\text{I}$ (fast eq) → $K_{eq} = \frac{[\text{I}]^2}{[\text{I}_2]}$ → $[\text{I}]^2 = K_{eq}[\text{I}_2]$

Step 2: $\text{H}_2 + 2\text{I} \rightarrow 2\text{HI}$ (slow) → Rate $= k[\text{H}_2][\text{I}]^2$

Substitute:
$$\text{Rate} = k \cdot K_{eq}[\text{H}_2][\text{I}_2] = k'[\text{H}_2][\text{I}_2]$$

*Key move: Even though the slow step contains $[\text{I}]^2$, the equilibrium substitution converts it to $[\text{I}_2]$ — a reactant. The final rate law ($k'[\text{H}_2][\text{I}_2]$) is first order in each reactant, matching the experimental observation for this reaction.*

---

**Example 16 — Pre-equilibrium: $2\text{X} + \text{Y} \rightarrow \text{X}_2\text{Y}$ (Progress Check Q25):**

Step 1: $2\text{X}(g) \rightleftharpoons \text{X}_2(g)$ (fast eq) → $K_{eq} = \frac{[\text{X}_2]}{[\text{X}]^2}$ → $[\text{X}_2] = K_{eq}[\text{X}]^2$

Step 2: $\text{X}_2(g) + \text{Y}(g) \rightarrow \text{X}_2\text{Y}(g)$ (slow) → Rate $= k[\text{X}_2][\text{Y}]$

Substitute:
$$\text{Rate} = k \cdot K_{eq}[\text{X}]^2[\text{Y}] = k'[\text{X}]^2[\text{Y}]$$

Correct answer: rate $= k[\text{X}]^2[\text{Y}]$ — second order in X, first order in Y.

*Key move: The coefficient in the fast equilibrium (2X → $\text{X}_2$) determines the exponent. When $[\text{X}_2] = K_{eq}[\text{X}]^2$, substituting puts $[\text{X}]^2$ in the rate law. This is a three-step problem type: (1) write slow-step rate, (2) set up equilibrium, (3) substitute and simplify.*

---

## Topic 5.11: Arrhenius Equation — Two-Temperature Calculation

**Example 17 — Two-temperature Arrhenius: find k at a new temperature (AP FRQ style, Farabaugh):**

A reaction has $E_a = 75.0\ \text{kJ/mol}$ and a rate constant $k_1 = 4.20 \times 10^{-3}\ \text{M}^{-1}\text{s}^{-1}$ at $T_1 = 298\ \text{K}$. Find $k_2$ at $T_2 = 328\ \text{K}$.

Use: $\ln(k_2/k_1) = -(E_a/R)(1/T_2 - 1/T_1)$. $R = 8.314\ \text{J/(mol·K)}$. Convert $E_a$ to J/mol: $75{,}000\ \text{J/mol}$.

**Step 1** — Compute $1/T_2 - 1/T_1$:
$$\frac{1}{328} - \frac{1}{298} = 3.049 \times 10^{-3} - 3.356 \times 10^{-3} = -3.07 \times 10^{-4}\ \text{K}^{-1}$$

**Step 2** — Compute the exponent:
$$-\frac{E_a}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right) = -\frac{75{,}000}{8.314} \times (-3.07 \times 10^{-4}) = 9023 \times 3.07 \times 10^{-4} = +2.770$$

**Step 3** — Solve for $k_2$:
$$\frac{k_2}{k_1} = e^{2.770} = 15.96$$
$$k_2 = 15.96 \times 4.20 \times 10^{-3} = 6.70 \times 10^{-2}\ \text{M}^{-1}\text{s}^{-1}$$

*Key move: Use $R = 8.314\ \text{J/(mol·K)}$ (not 0.08206). Convert $E_a$ to J/mol if given in kJ. The sign of $(1/T_2 - 1/T_1)$ matters: if $T_2 > T_1$, the term is negative, making the overall exponent positive, so $k_2 > k_1$ — rate increases with temperature.*

---

## Topic 5.9: Steady-State Approximation

**Example 21 — Steady-state vs. pre-equilibrium (AP MCQ distinction):**

A mechanism has:
- Step 1: $\text{A} \rightarrow \text{B}$ (slow formation of intermediate)
- Step 2: $\text{B} + \text{C} \rightarrow \text{D}$ (fast)

Under what conditions does pre-equilibrium apply vs. steady-state?

**Pre-equilibrium:** Step 1 is a fast equilibrium (fast forward and reverse) followed by a slow step. The intermediate B builds up quickly and equilibrates before being consumed. Use $K_{eq}$ to express [B] in terms of [A], then substitute.

**Steady-state:** No step is clearly fast reversible. Instead, the concentration of intermediate B is assumed constant throughout the reaction:

$$\frac{d[\text{B}]}{dt} = k_1[\text{A}] - k_2[\text{B}][\text{C}] = 0 \implies [\text{B}] = \frac{k_1[\text{A}]}{k_2[\text{C}]}$$

*Key move: Pre-equilibrium requires a fast reversible step BEFORE the slow step. Steady-state requires no such assumption — just that $d[\text{intermediate}]/dt = 0$. If a question states "the intermediate reaches a constant concentration," it is invoking steady-state, not pre-equilibrium.*

---

## Topic 5.10: Multistep Reaction Energy Profile

**Example 18 — Reading a two-step energy profile (AP FRQ style):**

An energy diagram shows: reactants at 20 kJ, first transition state at 80 kJ, intermediate at 45 kJ, second transition state at 95 kJ, products at 10 kJ.

**(a) $E_a$ for step 1:** $80 - 20 = 60\ \text{kJ}$ (from reactants to first TS)

**(b) $E_a$ for step 2:** $95 - 45 = 50\ \text{kJ}$ (from intermediate to second TS)

**(c) Rate-determining step:** Step 1 TS is at 80 kJ; Step 2 TS is at 95 kJ. Step 2's transition state is the highest overall point on the diagram (95 kJ) — its activation energy from the intermediate (50 kJ) is also larger than Step 1's Ea from the intermediate level. Step 2 is rate-determining.

**(d) ΔH of overall reaction:** products (10) − reactants (20) = $-10\ \text{kJ}$ (exothermic).

**(e) Number of intermediates:** 1 valley → 1 intermediate.

*Key move: Rate-determining step = the elementary step whose transition state is highest in energy measured from the preceding energy minimum. Always subtract the preceding valley or reactant energy — not the reactant baseline for later steps.*

---

**Example 19 — Catalyst effect on multistep profile:**

A catalyzed pathway for the same reaction (reactants at 20 kJ, products at 10 kJ) shows three humps at absolute energies of 55, 60, and 40 kJ, with valleys at 35 kJ (after hump 1) and 45 kJ (after hump 2).

What changed from the uncatalyzed reaction (which had transition states at 80 kJ and 95 kJ)?

| Feature | Uncatalyzed | Catalyzed |
|---|---|---|
| Number of steps | 2 | 3 |
| Highest TS energy | 95 kJ | 60 kJ |
| Overall ΔH | −10 kJ | −10 kJ (unchanged) |
| Reactant energy | 20 kJ | 20 kJ (unchanged) |
| Product energy | 10 kJ | 10 kJ (unchanged) |

The catalyst introduced a three-step pathway with lower individual humps. The highest individual $E_a$ in the catalyzed path: Step 2 TS at 60 kJ − valley at 35 kJ = 25 kJ — far lower than the 50 kJ or 60 kJ barriers in the uncatalyzed path.

*Key move: A catalyst always: (1) introduces a different pathway (more humps), (2) lowers individual $E_a$ values, (3) leaves $\Delta H$ and the reactant/product energy levels unchanged. The equilibrium constant $K$ is unchanged because $K$ depends on $\Delta G$, not $E_a$.*

---

**Example 20 — Identify intermediates and transition states from energy diagram (AP MCQ style):**

An energy diagram for a reaction shows humps at positions A (TS₁), C (TS₂), and E (TS₃), with valleys at B (between TS₁ and TS₂) and D (between TS₂ and TS₃).

| Question | Answer | Reasoning |
|---|---|---|
| How many transition states? | 3 (A, C, E) | Each hump peak = one transition state |
| How many intermediates? | 2 (B, D) | Each valley between humps = one intermediate |
| How many elementary steps? | 3 | One step per hump |
| Which species NOT present before reaction? | B and D | Intermediates — produced during mechanism, not present at start |
| Can B or D be isolated? | No (intermediates) | Local energy minimum, but not separated like reactants/products |

*Key move: Humps = transition states = elementary steps. Valleys between humps = intermediates. A species at the TOP of a hump (transition state/activated complex) cannot be isolated — it exists only for an instant at the energy peak.*
