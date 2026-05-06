# AP Chem — Unit 5 Notes: Kinetics
**Exam Weight: 7–9% | Topics: 5.1–5.11**
**Krug Videos:** [5.1](https://youtu.be/FDV_qaFCARA) | [5.2](https://youtu.be/PWXJ7xxuhnw) | [5.3](https://youtu.be/Jln8OrpjEsA) | [5.4/5.5/5.6](https://youtu.be/AGte-WD8kdU) | [5.7/5.8/5.9/5.10](https://youtu.be/0goaDsXV56w) | [5.11](https://youtu.be/5zF6kurqvk4)

---

## Study Hub Quick Reference — Unit 5

> [!check] Q3 — Immediately After Adding a Reagent: Only Forward Rate Changes
> When a reactant is added to an equilibrium system, **only the forward reaction rate changes immediately** (more reactant present → more collisions). The **reverse rate is unchanged** at that instant (product concentrations haven't changed yet). Over time, both rates shift until a new equilibrium is reached. This is the most-tested MCQ trap in this unit.

> [!check] Q8 — Catalysts Lower Ea, Not ΔG or K
> A catalyst provides an alternative pathway with **lower activation energy (Ea)**. This increases rate constant k and speeds up the reaction. A catalyst does **NOT** change: ΔH, ΔG, ΔS, K, or the energies of reactants/products. Enzymes are biological catalysts — they lower Ea but do not change thermodynamic favorability.

> [!check] Q13 — Identifying Reaction Order from Linear Graphs
> If **[A] vs. time is linear** → 0th order (rate = k, constant). If **ln[A] vs. time is linear** → 1st order. If **1/[A] vs. time is linear** → 2nd order. Memory: **0-1-2 → [A]-ln[A]-1/[A]**. The slope of the ln[A] vs. t graph = −k.

> [!check] Q23 — First-Order Kinetics: k = 0.693 / t½
> For first-order reactions ONLY: $t_{1/2} = 0.693/k$ — **constant and independent of initial concentration**. Given a half-life, solve for k: $k = 0.693/t_{1/2}$. Then use integrated rate law: $\ln[A]_t = -kt + \ln[A]_0$.

> [!check] Q38 — Surface Area Increases Reaction Rate
> Increasing the surface area of a **solid reactant** exposes more collision sites → more effective collisions per unit time → faster rate. Powdered solid reacts faster than a single chunk of the same mass. Surface area does not appear in rate laws for homogeneous (solution) reactions.

> [!check] Q40 — Diamond → Graphite: Kinetic vs. Thermodynamic Control
> Diamond converting to graphite is thermodynamically **favorable** (ΔG < 0; graphite is the stable allotrope). But the reaction is **kinetically controlled** — the activation energy is enormous because converting diamond's 3D covalent network requires breaking millions of C–C bonds simultaneously. At room temperature, essentially zero rate. Thermodynamics says it should happen; kinetics says it won't.

> [!check] FRQ Q2B(ii) — Catalyst on Energy Diagram
> A catalyst **lowers the peak (Ea)** but does NOT change the energies of reactants or products. ΔH (height difference between start and end) is **unchanged**. The catalyzed diagram shows a different (lower) pathway, often more humps (more steps), but same starting and ending energy levels.

> [!check] FRQ Q2D — Rate Decreases as [Reactant] Decreases
> For any positive-order reaction, rate = k[A]ⁿ. As [A] decreases over time, the rate **continuously decreases**. A concentration-time graph shows the slope getting shallower — not constant. Only a zeroth-order reaction maintains a constant rate throughout.

> [!check] FRQ Q2E — Zeroth-Order: Rate is Constant Throughout
> For a zeroth-order reaction: rate = k (completely independent of concentration). Concentration decreases **linearly** with time. The rate is **constant** until the reactant is completely consumed. Graph: [A] vs. t is a straight line; slope = −k.

> [!warning] Trap — Reaction Order ≠ Stoichiometric Coefficient
> **NEVER** determine reaction order from coefficients in the balanced equation. Order is determined ONLY from experimental data (rate tables) or from the slow step of a mechanism. A coefficient of 2 does NOT mean second-order.

> [!warning] Trap — k Changes With Temperature Only, NOT Concentration
> The rate constant k depends only on **temperature**. When [A] changes and rate changes, k is unchanged. If two experiments at different concentrations show the same k, that confirms k is concentration-independent.

> [!danger] Catalyst: Changes ONLY Ea and Rate — NOT ΔH, ΔG, or K
> A catalyst does not change the equilibrium constant K, ΔH, ΔG, or the equilibrium position. It only provides a lower-Ea pathway, increasing k and therefore rate. **Both forward and reverse rates increase equally** → equilibrium position is unaffected.

---

## Topic 5.1: Reaction Rates

**Essential Knowledge (Krug 5.1, Farabaugh CED):**
- The **rate of a chemical reaction** is the change in concentration of a reactant or product per unit time.
- Rate is always expressed as a positive value — use a negative sign for reactants to account for their disappearance:

$$\text{Rate} = -\frac{1}{a}\frac{\Delta[\text{A}]}{\Delta t} = -\frac{1}{b}\frac{\Delta[\text{B}]}{\Delta t} = \frac{1}{c}\frac{\Delta[\text{C}]}{\Delta t} = \frac{1}{d}\frac{\Delta[\text{D}]}{\Delta t}$$

for the reaction $a\text{A} + b\text{B} \rightarrow c\text{C} + d\text{D}$.

- **Stoichiometric ratio rule:** Rate of disappearance of X = (stoichiometric coefficient of X / coefficient of product) × rate of appearance of product.
- Example: $2\text{X} + \text{Y}_2 \rightarrow \text{X}_2\text{Y}_2$. Rate of X disappearance = $2 \times$ rate of $\text{X}_2\text{Y}_2$ appearance.

**Factors that affect rate:**
- Concentration of reactants (increases collision frequency)
- Temperature (increases fraction of molecules with $E \geq E_a$)
- Surface area of solid reactants (more collision sites)
- Presence of a catalyst (lowers $E_a$ via alternative pathway)

---

## Topic 5.2: Introduction to Rate Laws

**Essential Knowledge (Krug 5.2, Farabaugh CED):**
- The **rate law** relates the rate of reaction to the concentrations of reactants:

$$\text{Rate} = k[\text{A}]^m[\text{B}]^n$$

- $k$ = rate constant (depends only on temperature; increases with $T$)
- $m$, $n$ = reaction orders with respect to each reactant — determined **experimentally only**, never from stoichiometric coefficients
- Overall reaction order = $m + n$

**Determining order from a data table:**
- Hold one concentration constant; vary the other. Compare the rate ratio to the concentration ratio:

$$\frac{\text{Rate}_2}{\text{Rate}_1} = \left(\frac{[\text{A}]_2}{[\text{A}]_1}\right)^m \Rightarrow \text{solve for } m$$

- If rate doubles when $[\text{A}]$ doubles → first order ($m = 1$)
- If rate quadruples when $[\text{A}]$ doubles → second order ($m = 2$)
- If rate unchanged when $[\text{A}]$ doubles → zeroth order ($m = 0$)

**MCQ pattern:** Stoichiometric coefficient of X is 2, but the reaction order in X may be 1, 2, or 0. Never assume the coefficient equals the order.

---

## Topic 5.3: Concentration Changes over Time (Integrated Rate Laws)

**Essential Knowledge (Krug 5.3, Farabaugh CED):**

![[integrated_rate_law_u5.svg|697]]
*Three linearization plots: which graph is linear identifies the reaction order. Memory rule: 0-1-2 → [A]-ln[A]-1/[A].*

**The integrated rate laws and their linear plots:**

| Order | Integrated Law | Linear Plot | Slope | Half-life ($t_{1/2}$) |
|---|---|---|---|---|
| 0th | $[\text{A}] = -kt + [\text{A}]_0$ | $[\text{A}]$ vs. $t$ | $-k$ | $[\text{A}]_0 / 2k$ |
| 1st | $\ln[\text{A}] = -kt + \ln[\text{A}]_0$ | $\ln[\text{A}]$ vs. $t$ | $-k$ | $0.693/k$ |
| 2nd | $1/[\text{A}] = kt + 1/[\text{A}]_0$ | $1/[\text{A}]$ vs. $t$ | $+k$ | $1/(k[\text{A}]_0)$ |

**Graphical test for reaction order:**
1. Plot $[\text{A}]$ vs. $t$ → if linear → zeroth order
2. Plot $\ln[\text{A}]$ vs. $t$ → if linear → first order
3. Plot $1/[\text{A}]$ vs. $t$ → if linear → second order

**First-order half-life:** For first-order reactions, $t_{1/2} = 0.693/k$ — **constant and independent of initial concentration**. Each successive half-life reduces the amount to half of the current amount.

**Radioactive decay:** Always first-order. Plot $\ln n_{\text{reactant}}$ vs. time gives a straight line.

---

## Topic 5.4: Elementary Reactions and Reaction Mechanisms

**Essential Knowledge (Krug 5.4/5.5/5.6, Farabaugh CED):**

![[mechanism_rules_u5.svg|697]]
*Intermediate vs. catalyst definitions, rate law from mechanism rules, collision theory requirements, and factors affecting rate.*

**Elementary reactions:**
- A single collision event; no intermediate steps. Written as one step.
- Molecularity = number of reactant particles in the elementary step (unimolecular, bimolecular, termolecular — last is rare).
- For elementary steps ONLY: rate law is written directly from stoichiometry of that step.
  - Unimolecular: Rate $= k[\text{A}]$
  - Bimolecular: Rate $= k[\text{A}][\text{B}]$ or Rate $= k[\text{A}]^2$

**Reaction mechanisms:**
- A proposed sequence of elementary steps whose sum equals the overall balanced equation.
- Validity check: (1) steps sum to the overall equation; (2) rate law predicted by mechanism matches experiment.

**Intermediate vs. Catalyst:**
| | Intermediate | Catalyst |
|---|---|---|
| Produced | In one step | Consumed in one step |
| Consumed | In a later step | Regenerated in a later step |
| Present before reaction? | No | Yes |
| In overall equation? | No (cancels) | No (cancels) |
| In rate law? | No | Yes (if in slow step) |

**Writing the overall equation from a mechanism:**
Add all elementary steps. Cancel species that appear on both sides (intermediates cancel; catalyst appears on both sides and also cancels).

---

## Topic 5.5: Collision Model

**Essential Knowledge (Krug 5.4/5.5/5.6, Farabaugh CED):**
- **Collision theory:** Reactant molecules must collide with (1) sufficient energy ($\geq E_a$) AND (2) correct orientation for a reaction to occur.
- **Activation energy ($E_a$):** The minimum energy required for the collision to result in product formation.
- **Effective collision:** One with both sufficient energy and proper orientation.
- **Transition state (activated complex):** The high-energy, unstable arrangement of atoms at the peak of the energy diagram.

**Orientation dependence:**
- Spherical atoms (e.g., O, noble gases): symmetrically distributed electron clouds → NO orientation requirement → every collision with sufficient energy is effective.
- Molecules with directional bonds: specific orbital geometry must align for bond formation → strong orientation requirement.
- $S_N2$ reactions (e.g., $\text{CH}_3\text{I} + \text{Br}^-$): nucleophile must attack from the back side → highly orientation-dependent.

**Temperature and rate:**
- Higher temperature → broader Maxwell–Boltzmann distribution → larger fraction of molecules with $E \geq E_a$ → faster rate.
- The rate constant $k$ increases exponentially with temperature (Arrhenius equation: $k = Ae^{-E_a/RT}$).
- $k$ is constant at a given temperature — it does NOT change with concentration.

---

## Topic 5.6: Reaction Energy Profiles

**Essential Knowledge (Krug 5.4/5.5/5.6, Farabaugh CED):**

![[energy_profile_u5.svg|697]]
*Catalyzed (blue, solid) vs. uncatalyzed (red, dashed) energy profiles. Lower Ea, multi-step path, same ΔE.*

**Energy diagram features:**
- **Reactants:** Starting energy level (left side of diagram)
- **Products:** Final energy level (right side)
- **Transition state (TS):** Peak of each energy hump; highest-energy species along the path
- **Activation energy ($E_a$):** Energy difference from reactants (or intermediate) to the next TS peak
- **$\Delta H$ (or $\Delta E$):** Energy difference from reactants to products; independent of pathway

**Catalyst effect on energy profile:**
- Provides a different reaction pathway with **lower $E_a$**
- Often introduces additional elementary steps → more humps on the energy diagram, but each hump is lower
- Catalyst does NOT change: $\Delta H$, $\Delta G$, the energies of reactants or products, or the equilibrium position
- Both catalyzed and uncatalyzed paths begin and end at the same energy levels

**Multi-step mechanism on energy diagram:**
- Each hump = one transition state
- Each valley between humps = one intermediate
- Number of humps = number of elementary steps in the mechanism

---

## Topic 5.7: Introduction to Reaction Mechanisms

**Essential Knowledge (Krug 5.7/5.8/5.9/5.10, Farabaugh CED):**

**Elementary reactions:**
- A single collision event with no intermediate steps; written as one step.
- Molecularity = number of reactant particles in the elementary step (unimolecular, bimolecular, termolecular — termolecular is rare).
- For elementary steps ONLY: rate law is written directly from stoichiometry of that step.

**Reaction mechanisms:**
- A proposed sequence of elementary steps whose sum equals the overall balanced equation.
- Validity check: (1) steps sum to the overall equation; (2) rate law predicted by mechanism matches experiment.

**Writing the overall equation from a mechanism:**
Add all elementary steps. Cancel species that appear on both sides — intermediates cancel completely; catalyst appears on both sides and also cancels.

**Intermediate vs. Catalyst:**
| | Intermediate | Catalyst |
|---|---|---|
| Produced | In one step | Consumed in one step |
| Consumed | In a later step | Regenerated in a later step |
| Present before reaction? | No | Yes |
| In overall equation? | No (cancels) | No (cancels) |
| In rate law? | No | Yes (if in slow step) |

---

## Topic 5.8: Reaction Mechanism and Rate Law

**Essential Knowledge (Krug 5.7/5.8/5.9/5.10, Farabaugh CED):**

**Rate-determining step (slow step):**
- The slowest elementary step controls the overall reaction rate.
- The rate law for the overall reaction = rate law for the rate-determining (slow) step.
- For elementary steps, the rate law is written directly from stoichiometry of that step.
- Write from the reactants of the slow step only — regardless of what comes after.

**Pre-equilibrium mechanism:**
When a fast equilibrium precedes the slow step and an intermediate appears in the slow step's rate law, that intermediate must be eliminated using the pre-equilibrium approximation:

Step 1 (fast eq): $a\text{A} \rightleftharpoons b\text{B}$ → $K_{eq} = \frac{[\text{B}]^b}{[\text{A}]^a}$ → $[\text{B}] = K_{eq}^{1/b}[\text{A}]^{a/b}$

Step 2 (slow): $\text{B} + \text{C} \rightarrow \text{products}$ → Rate $= k[\text{B}][\text{C}]$

**Substitute** $[\text{B}]$ from the equilibrium expression to eliminate the intermediate:
$$\text{Rate} = k \cdot K_{eq}[\text{A}][\text{C}] = k'[\text{A}][\text{C}]$$

**Critical rule:** Intermediates CANNOT appear in the final rate law — they cannot be experimentally controlled as initial concentrations. Always substitute equilibrium expressions to eliminate them. The result must contain only observable (original) reactant concentrations.

**Back-solving for a missing step:**
Given an overall equation and one known step, subtract to find the missing step:
$$\text{Missing step} = \text{Overall equation} - \text{Known step}$$
Check: the missing step must produce or consume the intermediate; all steps must sum to the overall equation.

---

## Topic 5.9: Steady-State Approximation

**Essential Knowledge (Krug 5.7/5.8/5.9/5.10, Farabaugh CED):**
- Assumes the rate of formation of an intermediate equals the rate of its consumption throughout the reaction: $d[\text{I}]/dt \approx 0$.
- Applied when no single step is clearly much slower than all others — unlike pre-equilibrium, which requires an explicit fast reversible step before the slow step.
- To apply: set rate of formation of intermediate = rate of consumption, solve for [intermediate], then substitute into the overall rate expression.

**Distinguishing from pre-equilibrium:**
- **Pre-equilibrium:** Step 1 is a fast reversible equilibrium → intermediate builds up quickly → use $K_{eq}$ to eliminate it.
- **Steady-state:** No such fast-equilibrium assumption → concentration of intermediate is simply held constant: $d[\text{I}]/dt = 0$.

**AP exam relevance:**
- Rarely tested directly on the AP exam; more likely to appear in FRQ context.
- MCQ signal: if a question states "the concentration of intermediate remains constant throughout the reaction," it is invoking the steady-state approximation — set rate of formation = rate of consumption of that intermediate.

---

## Topic 5.10: Multistep Reaction Energy Profile

**Essential Knowledge (Krug 5.7/5.8/5.9/5.10, Farabaugh CED):**

**Reading a multistep energy diagram:**
- Each hump = one transition state = one elementary step.
- Each valley between humps = one intermediate.
- Number of humps = number of elementary steps in the mechanism.
- Number of valleys between humps = number of intermediates.

**Identifying the rate-determining step:**
- The rate-determining step has the highest transition state measured from the preceding energy minimum (preceding valley or reactant level) — NOT necessarily the highest point from the reactant baseline.
- Compare each activation energy: Ea(step N) = [TS height of step N] − [energy of preceding minimum].
- The step with the largest individual Ea is the slow step.

**Reading rule table:**

| Feature of energy diagram | What it tells you |
|---|---|
| Number of humps | Number of elementary steps |
| Number of valleys between humps | Number of intermediates |
| Highest hump measured from preceding minimum | Rate-determining (slow) step |
| Energy of products − energy of reactants | Overall ΔH (negative = exothermic) |
| Height of any hump above starting energy | Activation energy for that step from the preceding minimum |

**For a two-step mechanism:**
- First hump = transition state of step 1; valley = intermediate; second hump = transition state of step 2.
- Compare Ea of step 1 (TS1 − reactant energy) and Ea of step 2 (TS2 − intermediate energy).
- The step with the larger Ea is rate-determining.

**Catalyst effect on multistep profile:**
- Introduces additional elementary steps (more humps) but each hump is lower.
- Overall ΔH is unchanged — reactant and product energy levels remain the same.
- The rate-determining step may change if the catalyst selectively lowers one barrier more than another.

---

## Topic 5.11: Catalysis and the Arrhenius Equation

**Essential Knowledge (Krug 5.11, Farabaugh CED):**
- A **catalyst** increases reaction rate by providing an alternative pathway with lower activation energy ($E_a$). It is consumed in one step and regenerated in a later step — not consumed overall.
- Catalysts do **not** change: $\Delta H$, $\Delta G$, $K$, or the energies of reactants or products. Only $E_a$ (and therefore $k$) changes.
- **Homogeneous catalyst:** Same phase as reactants (e.g., $\text{H}^+$ in aqueous acid catalysis, enzymes in solution).
- **Heterogeneous catalyst:** Different phase from reactants (e.g., Pt or Ni solid catalyst for gas-phase hydrogenation; catalytic converters).

**The Arrhenius Equation:**
$$\boxed{k = Ae^{-E_a/RT}}$$

- $k$ = rate constant (depends on temperature)
- $A$ = frequency factor (pre-exponential) — accounts for collision frequency and fraction with correct orientation
- $E_a$ = activation energy (J/mol)
- $R$ = 8.314 J/(mol·K) — always use this value here, never 0.08206
- $T$ = temperature in Kelvin

**Linearized (Arrhenius) Form:**
$$\ln k = -\frac{E_a}{R} \cdot \frac{1}{T} + \ln A$$

A plot of $\ln k$ vs. $1/T$ gives a straight line with:
- Slope $= -E_a/R$ → $E_a = -\text{slope} \times R$
- Steeper (more negative) slope = larger $E_a$
- $y$-intercept $= \ln A$

![[arrhenius_u5.svg|697]]
*Left: linear ln k vs. 1/T plot — slope = −Ea/R. Right: at fixed T, a catalyst lowers Ea → larger k.*

**Two-Temperature Form (AP FRQ — most common calculation):**
$$\ln\frac{k_2}{k_1} = -\frac{E_a}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)$$

Use when: given $k_1$ at $T_1$ and asked to find $k_2$ at $T_2$, or given two rate constants to find $E_a$.

**Why Temperature Increases Rate (Arrhenius connection to KMT):**
- Higher $T$ → Maxwell–Boltzmann curve shifts right → more molecules have $KE \geq E_a$.
- This directly increases $k$ via $e^{-E_a/RT}$: as $T$ increases, the exponent becomes less negative → $k$ increases exponentially.
- A larger $E_a$ means $k$ is more sensitive to temperature changes.

**Common Mistakes:**
- Using $R = 0.08206$ — wrong here. Arrhenius requires $R = 8.314\ \text{J/(mol·K)}$.
- Forgetting to convert temperature to Kelvin.
- Claiming a catalyst changes $K$ or $\Delta H$ — it changes only $E_a$ and the rate.

---

## MCQ Pattern Recognition — Unit 5

| If you see...                                            | It's testing...                                   | Key move                                                                                |
| -------------------------------------------------------- | ------------------------------------------------- | --------------------------------------------------------------------------------------- |
| Data table with initial rates and concentrations         | Determining rate law experimentally               | Hold one reactant constant; compare rate ratio = conc ratio^n                           |
| "Rate of disappearance of X"                             | Stoichiometric ratio of rates                     | Multiply rate of product appearance by (coeff of X / coeff of product)                  |
| "Concentration doubled, rate unchanged"                  | Zeroth-order kinetics                             | Rate = k; independent of concentration                                                  |
| Graph: $[\text{A}]$ vs. $t$ is linear                    | Zeroth order                                      | Rate = k                                                                                |
| Graph: $\ln[\text{A}]$ vs. $t$ is linear                 | First order                                       | $\ln[\text{A}] = -kt + \ln[\text{A}]_0$                                                 |
| Graph: $1/[\text{A}]$ vs. $t$ is linear                  | Second order                                      | $1/[\text{A}] = kt + 1/[\text{A}]_0$                                                    |
| "First-order radioactive decay"                          | $\ln n$ vs. time is linear                        | $t_{1/2} = 0.693/k$, constant                                                           |
| Species present before reaction, regenerated after       | Catalyst (not intermediate)                       | Catalyst: consumed then regenerated; intermediate: produced then consumed               |
| "What is the rate law?" — given mechanism                | Rate-determining step                             | Write rate from slow step reactants; substitute away intermediates                      |
| Slow step contains an intermediate                       | Pre-equilibrium substitution                      | Use $K_{eq}$ from fast equilibrium to eliminate intermediate                            |
| "Find missing step 1 given step 2 and overall"           | Mechanism back-solve                              | Subtract step 2 from overall; product of step 1 must feed step 2                        |
| Same T, same conc → faster rate                          | Catalyst effect                                   | Catalyst lowers $E_a$; rate constant $k$ increases; k doesn't change with conc          |
| Higher concentration → faster rate                       | Collision frequency                               | More particles per unit volume → more collisions per unit time                          |
| Powdered vs. chunk solid                                 | Surface area                                      | More surface area → more collision sites → faster heterogeneous rate                    |
| Maxwell–Boltzmann + $E_a$ dashed line                    | Temperature and fraction with $E \geq E_a$        | Higher T → curve shifts right → larger area beyond $E_a$ line → faster rate             |
| Energy diagram with one large hump vs. two smaller humps | Catalyzed pathway                                 | Two humps = two steps = one intermediate; same start/end energy; lower individual $E_a$ |
| Spherical atom reaction                                  | Orientation independence                          | Symmetric electron cloud → no preferred orientation → all directions equally effective  |
| "k is larger in trial 2 at same T"                       | Incorrect — $k$ doesn't change with concentration | $k$ depends only on $T$. Rate changes because concentration changes, not $k$.           |

---

## AP Answer Templates — Unit 5

> **Rate law from data:** "Comparing experiments X and Y, where $[\text{A}]$ is held constant, the rate doubles when $[\text{B}]$ doubles. This indicates first-order dependence on $[\text{B}]$ ($2^1 = 2$). The experimental rate law is Rate $= k[\text{A}]^m[\text{B}]^1$."

> **Rate of disappearance vs. appearance:** "For the reaction $a\text{A} \rightarrow c\text{C}$, the rate of disappearance of A is $(a/c)$ times the rate of appearance of C, by stoichiometry."

> **Catalyst claim:** "The higher rate is most likely due to the presence of a catalyst. A catalyst provides an alternative reaction pathway with lower activation energy. At the same temperature and concentration, a lower $E_a$ means a greater fraction of collisions have sufficient energy to react, increasing the rate constant $k$ and therefore the rate."

> **Rate law from mechanism:** "The slow step is Step [N], which involves [reactants]. For an elementary step, the rate law is written directly from the reactants: Rate $= k[\text{A}][\text{B}]$. The intermediate $[\text{X}]$ does not appear in the final rate law."

> **Pre-equilibrium substitution:** "Step 1 establishes a fast equilibrium: $K_{eq} = [\text{intermediate}]/[\text{reactant}]^n$, so $[\text{intermediate}] = K_{eq}[\text{reactant}]^n$. Substituting into the slow-step rate law eliminates the intermediate, giving Rate $= k'[\text{reactant}]^n[\text{other}]$."

> **Catalyst on energy diagram:** "Profile Y represents the catalyzed reaction because it shows a lower activation energy. A catalyst provides an alternative reaction pathway that requires less energy to proceed to the transition state. The overall energy change ($\Delta H$) is the same for both profiles, since the catalyst does not alter the energies of the reactants or products."

> **Rate-determining step from energy diagram:** "The rate-determining step is Step [N] because its transition state is the highest in energy relative to the preceding energy minimum. The activation energy for Step [N] is [TS energy] − [preceding minimum energy] = [value] kJ/mol, which is larger than the activation energy of any other step. The slowest step controls the overall rate."

> **Number of intermediates from energy diagram:** "There are [N] intermediates in this mechanism. Each valley between two transition state humps on the energy profile represents one intermediate — a species that is produced in one elementary step and consumed in a subsequent step. It has measurable stability (a local energy minimum) but is not present in the starting materials or final products."

> **Why a catalyst changes rate but not ΔH or K:** "A catalyst increases the reaction rate by providing an alternative reaction pathway with lower activation energy ($E_a$). However, a catalyst does not change the energies of the reactants or products — only the pathway between them. Because $\Delta H$ depends on the difference in energy between products and reactants (not on the path), $\Delta H$ is unchanged. Since $\Delta G = \Delta H - T\Delta S$ is also unchanged, the equilibrium constant $K$ (which depends on $\Delta G$) is likewise unaffected. A catalyst speeds up both the forward and reverse reactions equally."

---

## Critical Reminders — Unit 5

> [!danger] Reaction Orders Are NEVER From Stoichiometric Coefficients
> Always determined from experimental data (rate tables) or from the slow step of a mechanism. A coefficient of 2 in a balanced equation does NOT mean second-order.

> [!danger] Catalyst: Does NOT Change ΔH, ΔG, K, or Equilibrium Position
> Catalyst only lowers Ea and increases k. ΔH, ΔG, equilibrium constant K, and equilibrium position are ALL unchanged. Both forward and reverse rates increase equally.

> [!warning] k Depends ONLY on Temperature, Not Concentration
> k is constant at a given temperature. When concentration changes and rate changes, k is unchanged. Only temperature changes k.

> [!warning] Intermediates Cannot Appear in the Final Rate Law
> Intermediates are produced in one step and consumed in another — not experimentally controllable. Substitute away using the pre-equilibrium $K_{eq}$ expression.

> [!check] Rate-Determining Step = Slow Step
> Rate law for the overall reaction = rate law written from the **reactants of the slow step** only. For elementary steps, write rate law directly from stoichiometry of that step.

> [!warning] First-Order t½ is Constant; Second-Order t½ Depends on [A]₀
> First-order: $t_{1/2} = 0.693/k$ — **constant**, independent of $[A]_0$. Second-order: $t_{1/2} = 1/(k[A]_0)$ — increases as concentration decreases.

> [!check] Linearization Memory: 0-1-2 → [A]-ln[A]-1/[A]
> 0th order: [A] vs. t is linear (slope = −k). 1st order: ln[A] vs. t is linear (slope = −k). 2nd order: 1/[A] vs. t is linear (slope = +k).

> [!warning] Maxwell-Boltzmann + Ea: Higher T → More Molecules With E ≥ Ea
> Higher T shifts the curve right → larger area past the $E_a$ threshold → more effective collisions → faster rate. This is the molecular-level reason rate increases exponentially with temperature.

> [!check] Arrhenius Equation: Use R = 8.314 J/(mol·K)
> $k = Ae^{-E_a/RT}$. **NEVER use R = 0.08206 here.** Temperature must be in Kelvin. For two-temperature problems: $\ln(k_2/k_1) = -(E_a/R)(1/T_2 - 1/T_1)$.

> [!danger] Diamond → Graphite: Thermodynamically Favored, Kinetically Blocked
> ΔG < 0 (graphite is the stable allotrope), but the activation energy for breaking the 3D covalent network of diamond is enormous → essentially zero rate at room temperature. **Classic kinetic vs. thermodynamic control example.**

> [!check] Q3 Pattern: Immediately After Adding Reagent — Only Forward Rate Changes
> At the instant a reactant is added to an equilibrium system, only the **forward rate increases** (more reactant). The **reverse rate is unchanged** at that moment. Both rates equalize over time at a new equilibrium.

> [!check] Back-Solving for Missing Mechanism Step
> Missing step = Overall equation − Known steps. Cancel species on both sides. The missing step must produce or consume the intermediate that links the steps.

> [!warning] Rate-Determining Step from Energy Diagram
> The slowest step has the **highest Ea measured from the PRECEDING energy minimum** (preceding valley or reactant level), NOT necessarily the highest absolute energy. Always subtract the preceding minimum, not the reactant starting point.
