# AP Chem — Unit 7 Notes: Equilibrium
**Exam Weight: 7–9% | Topics: 7.1–7.12**
**Krug Videos:** [7.1 Intro to Equilibrium](https://youtu.be/Zmks1z6PT6U) | [7.2/7.3 Reversible Reactions & Kc](https://youtu.be/yf7ZD9bOQC0) | [7.4/7.5 Working With K](https://youtu.be/VkC0mQwKM1c) | [7.6 Properties of K](https://youtu.be/u4adSYN8tMM) | [7.7a ICE Tables](https://youtu.be/IxYfMZulypc) | [7.7b Small K](https://youtu.be/Dq4_DGACaDE) | [7.8 Representations](https://youtu.be/z40T4AN2veo) | [7.9 Le Chatelier's](https://youtu.be/5t0PRjJgNmc) | [7.10 Q and Le Chat.](https://youtu.be/u2L9l6J4s7E) | [7.11a Ksp Intro](https://youtu.be/1qqbnWTnZfQ) | [7.11b Ksp Practice](https://youtu.be/HI9y2l04aMY) | [7.12 Common-Ion](https://youtu.be/c3U_p7OjdAs)

---

## Study Hub Quick Reference — Unit 7

> [!check] Q7 — K Manipulation Rules
> **Reverse a reaction:** $K_{new} = 1/K$. **Multiply all coefficients by n:** $K_{new} = K^n$. **Add two reactions:** $K_{new} = K_1 \times K_2$. These rules apply to both $K_c$ and $K_p$. Example: if K = 4 for A ⇌ B, then K = 1/4 for B ⇌ A and K = 16 for 2A ⇌ 2B.

> [!check] Q34 — Ksp and Dynamic Equilibrium in a Saturated Solution
> A **saturated solution** is at equilibrium: solid ⇌ dissolved ions (dissolution rate = precipitation rate). Both processes occur simultaneously — it is **dynamic**, not static. Adding more solid to a saturated solution does NOT change ion concentrations; the extra solid simply sits undissolved. $K_{sp}$ depends only on temperature.

> [!check] Q47 — Reaction Quotient Q: Q < K → Forward Shift
> Q has the same algebraic form as K but uses non-equilibrium concentrations. **Q < K:** too few products → system shifts **forward** (→). **Q > K:** too many products → system shifts **reverse** (←). **Q = K:** already at equilibrium → **no shift**.

> [!check] Q49 — Ksp and the Common-Ion Effect
> Adding a solution containing an ion **already present** in the equilibrium suppresses dissolution (Le Chatelier: adding a product → reverse shift). $K_{sp}$ itself is **unchanged** — only the molar solubility decreases. Set up ICE table with **nonzero initial concentration** for the common ion.

> [!check] Q50 — Hess's Law for K + ΔG° Connection
> Adding two reactions → multiply their K values ($K_{total} = K_1 \times K_2$). **K >> 1 means ΔG° < 0** (thermodynamically favored) because $\Delta G° = -RT\ln K$. A large K (e.g., $K = 10^{30}$) means the forward reaction goes essentially to completion.

> [!check] FRQ Q1G — Le Chatelier's Principle: Temperature and Pressure
> For an **exothermic** reaction (ΔH < 0): **decreasing temperature** shifts equilibrium **forward** (system shifts in exothermic direction to replace heat). **Increasing pressure** (decreasing volume) shifts toward the side with **fewer moles of gas**. K changes with temperature; pressure changes do NOT change K.

> [!check] FRQ Q3D — Pressure-Time Graphs: Q > K → Reverse Shift
> On a pressure-time graph, equilibrium = flat line (pressure stops changing). Identify starting Q by comparing initial partial pressures to K. If Q > K at the start → **reverse shift** → pressure adjusts toward fewer gas moles on the product side. Read the equilibrium pressure from the flat region.

> [!check] FRQ Q3E — Kp Expression + ICE Table
> Write $K_p$ using **partial pressures (atm)** for all gaseous species only. Pure solids and liquids are **omitted**. ICE table: I = initial pressures, C = change in terms of x (with stoichiometric coefficients), E = equilibrium pressures. Substitute into $K_p$ expression and solve for x.

> [!warning] Trap — Equilibrium ≠ Equal Concentrations
> Equilibrium is when **rates are equal** (forward rate = reverse rate) and concentrations are **constant**. Concentrations do not need to be equal to each other. [A] = [B] is NOT a definition of equilibrium.

> [!warning] Trap — A Single Particle Diagram Cannot Confirm Equilibrium
> A single snapshot shows composition at one moment. To confirm equilibrium, you need to show that concentrations are **no longer changing** — you need at least two time points.

> [!danger] K Changes ONLY With Temperature
> Adding reactants, removing products, changing pressure, or adding a catalyst all change Q but **NOT K**. Only a **temperature change** changes K itself.

---

## Topic 7.1: Introduction to Equilibrium

**Essential Knowledge (Farabaugh CED):**
- **Dynamic equilibrium** is established when the forward and reverse reactions occur simultaneously at **equal rates**. Macroscopic properties (concentration, pressure, color) remain constant, but microscopic processes never stop.
- Equilibrium requires a **closed system** at constant temperature. An open system never reaches equilibrium because products escape.
- Equilibrium is reached when concentrations stop changing — not when they are equal. Equal concentrations are a coincidence of specific initial conditions, not a definition.
- The **vapor–liquid equilibrium** of a volatile liquid in a sealed container is a classic example: evaporation rate equals condensation rate; pressure reaches a constant value while liquid remains.
- A single-snapshot particle diagram cannot confirm equilibrium — it shows composition at one moment. You need at least two snapshots over time to confirm concentrations are no longer changing.

**Recognizing Equilibrium:**

| Observable | Interpretation |
|---|---|
| Concentrations constant over time | Equilibrium established |
| Color stops changing in sealed tube | Equilibrium established |
| Pressure stops changing (gas reaction, sealed) | Equilibrium established |
| Concentrations still changing | Not yet at equilibrium |
| $[\text{X}] = [\text{Y}]$ (equal concentrations) | Not sufficient — depends on $K$ |
| Mass constant in sealed container | Always true; does NOT indicate equilibrium |

---

## Topic 7.2: Direction of Reversible Reactions

**Essential Knowledge (Farabaugh CED):**
- A reversible reaction can proceed in either the forward (→) or reverse (←) direction. At equilibrium, both directions proceed at equal rates.
- Before equilibrium: if forward rate > reverse rate, net conversion of reactants to products occurs (and vice versa).
- The comparison of $Q$ to $K$ tells the direction the system must shift to reach equilibrium (Topic 7.10).

---

## Topic 7.3: Reaction Quotient and Equilibrium Constant

**Essential Knowledge (Farabaugh CED):**
- The **equilibrium constant expression** $K_c$ is written as products over reactants, with each concentration raised to its stoichiometric coefficient:
$$K_c = \frac{[\text{C}]^c[\text{D}]^d}{[\text{A}]^a[\text{B}]^b} \quad \text{for} \quad a\text{A} + b\text{B} \rightleftharpoons c\text{C} + d\text{D}$$
- **Pure solids and pure liquids are omitted** from the $K$ expression — their "concentration" is constant (absorbed into $K$). Aqueous ions and gases are included.
- **$K_p$** uses partial pressures (atm) instead of molarities. Used when all species are gases.
$$K_p = \frac{(P_C)^c(P_D)^d}{(P_A)^a(P_B)^b}$$
- Relationship between $K_c$ and $K_p$:
$$K_p = K_c(RT)^{\Delta n_{\text{gas}}}$$
where $\Delta n_{\text{gas}} = \text{mol gaseous products} - \text{mol gaseous reactants}$ and $R = 0.08206\ \text{L·atm/mol·K}$.
- The **reaction quotient $Q$** has the same algebraic form as $K$ but is evaluated at non-equilibrium conditions. It compares to $K$ to predict the direction of shift.

**$K$ Expression Rules Summary:**

| Species type | Included in $K$? |
|---|---|
| Gas ($g$) | Yes — use $[\text{M}]$ for $K_c$, partial pressure for $K_p$ |
| Aqueous ($aq$) | Yes — use $[\text{M}]$ |
| Pure liquid ($l$) | No — omit |
| Pure solid ($s$) | No — omit |

![[concentration_time_eq_u7.svg|697]]
*Concentration-time graph for $\text{N}_2\text{O}_4 \rightleftharpoons 2\text{NO}_2$: both curves flatten at the same time — equilibrium. The curves do not need to meet at equal concentrations; they simply stop changing.*

---

## Topic 7.4: Calculating the Equilibrium Constant

**Essential Knowledge (Farabaugh CED):**
- To find $K_c$ from experimental data: substitute equilibrium concentrations directly into the $K$ expression.
- To find equilibrium concentrations from initial conditions: use an **ICE table**.

**ICE Table Method:**

| | $\text{A}$ | $\rightleftharpoons$ | $\text{B}$ |
|---|---|---|---|
| **I**nitial | $[\text{A}]_0$ | | $[\text{B}]_0$ |
| **C**hange | $-ax$ | | $+bx$ |
| **E**quilibrium | $[\text{A}]_0 - ax$ | | $[\text{B}]_0 + bx$ |

- The **Change row** uses the stoichiometric coefficients from the balanced equation. If $x$ mol/L of reaction occurs, $a$ mol/L of A is consumed and $b$ mol/L of B is produced.
- Signs: species consumed have $-$; species produced have $+$.
- Check: equilibrium concentrations must be positive. If you get a negative concentration, the reaction shifted the wrong direction.

**Stoichiometric linking:** Species produced in equal molar ratio have equal equilibrium changes. For $\text{HI}(g) \rightleftharpoons \frac{1}{2}\text{H}_2(g) + \frac{1}{2}\text{I}_2(g)$: $[\text{H}_2]_{\text{eq}} = [\text{I}_2]_{\text{eq}}$ if both start at zero.

---

## Topic 7.5: Magnitude of the Equilibrium Constant

**Essential Knowledge (Farabaugh CED):**
- The **magnitude of $K$** tells where equilibrium lies — how much product vs. reactant is present at equilibrium.

| $K$ value | Equilibrium position | Practical meaning |
|---|---|---|
| $K \gg 1$ (e.g., $10^{10}$) | Strongly product-favored | Reaction goes nearly to completion |
| $K \approx 1$ | Neither side strongly favored | Significant amounts of both |
| $K \ll 1$ (e.g., $10^{-10}$) | Strongly reactant-favored | Very little product at equilibrium |

- For very large $K$: assume the reaction goes to completion and work backward (reverse ICE or stoichiometric completion approach).
- For very small $K$: use the approximation $[\text{reactant}]_{\text{eq}} \approx [\text{reactant}]_0$ (5% rule: approximation valid if $x/[\text{reactant}]_0 < 0.05$).

---

## Topic 7.6: Properties of the Equilibrium Constant

**Essential Knowledge (Farabaugh CED):**
- $K$ depends **only on temperature**. Changing concentration, pressure, or adding a catalyst does not change $K$.
- Three algebraic manipulation rules for combining equilibrium constants:

| Manipulation | Effect on $K$ |
|---|---|
| Reverse the reaction | $K_{\text{new}} = \dfrac{1}{K}$ |
| Multiply all coefficients by $n$ | $K_{\text{new}} = K^n$ |
| Add two reactions | $K_{\text{new}} = K_1 \times K_2$ |

**Examples:**
- Forward: $\text{A} \rightleftharpoons \text{B}$, $K = 5$. Reverse: $\text{B} \rightleftharpoons \text{A}$, $K = 1/5$.
- $\text{A} \rightleftharpoons \text{B}$, $K = 5$. Then $2\text{A} \rightleftharpoons 2\text{B}$ has $K = 5^2 = 25$.
- Rxn 1 + Rxn 2 = Rxn 3: $K_3 = K_1 \times K_2$.

---

## Topic 7.7: Calculating Equilibrium Concentrations

**Essential Knowledge (Farabaugh CED):**
- Given initial concentrations and $K$, solve the ICE table for $x$ (the change in concentration per mol of reaction).
- The general strategy:
  1. Write balanced equation and $K$ expression.
  2. Set up ICE table; express all equilibrium concentrations in terms of $x$.
  3. Substitute into $K$ expression; solve for $x$.
  4. Back-calculate equilibrium concentrations and verify they are positive.

**Small-$K$ Approximation (5% rule):**
When $K \ll 1$, the change $x$ is negligible compared to initial concentrations:
$$[\text{reactant}]_0 - x \approx [\text{reactant}]_0$$
This converts a quadratic into a simple expression. After solving, verify: $x/[\text{reactant}]_0 < 0.05$.

**Quadratic case:**
If the 5% approximation fails (or $K$ is not tiny), solve the full quadratic:
$$ax^2 + bx + c = 0 \implies x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}$$
Take only the physically meaningful root (positive $x$ that gives positive equilibrium concentrations).

![[ice_table_u7.svg|697]]
*ICE table setup for $\text{H}_2 + \text{I}_2 \rightleftharpoons 2\text{HI}$: Change row uses $-x, -x, +2x$ from the 1:1:2 stoichiometry. Equilibrium expressions substitute into $K_c = (2x)^2 / ([\text{H}_2]_0 - x)([\text{I}_2]_0 - x)$.*

---

## Topic 7.8: Representations of Equilibrium

**Essential Knowledge (Farabaugh CED):**
- **Concentration-time graphs**: equilibrium is identified by flat (horizontal) concentration curves. The exact time at which curves become flat is the equilibrium point.
- **Particle diagram interpretation**: count each particle type, then calculate $Q$ from the counts. If $Q = K$, the system is at equilibrium. A single snapshot cannot confirm equilibrium — must compare two time points.
- **Rate-time graphs**: at equilibrium, the forward rate equals the reverse rate (both nonzero, equal horizontal lines). Before equilibrium, the lines are not equal.
- Equilibrium is **dynamic**: both rates are nonzero but equal. It is never "stopped."

**Reading a Particle Diagram:**
1. Count particles of each species.
2. Write $Q$ expression using particle counts (treat each particle as proportional to concentration).
3. Compute $Q$. Compare to given $K$.
4. If $Q < K$: system must shift forward (more product needed). If $Q > K$: shift reverse.

---

## Topic 7.9: Introduction to Le Chatelier's Principle

**Essential Knowledge (Farabaugh CED):**
- **Le Chatelier's Principle**: when a system at equilibrium is subjected to a stress, the system shifts in the direction that partially relieves the stress and restores equilibrium.
- $K$ itself does not change from any stress except a **temperature change**.

**Stresses and Responses:**

| Stress | System Response |
|---|---|
| Add reactant | Shifts **forward** (toward products) |
| Remove reactant | Shifts **reverse** (toward reactants) |
| Add product | Shifts **reverse** |
| Remove product | Shifts **forward** |
| Decrease volume (increase pressure) | Shifts toward side with **fewer moles of gas** |
| Increase volume (decrease pressure) | Shifts toward side with **more moles of gas** |
| Increase temperature | Shifts in the **endothermic** direction |
| Decrease temperature | Shifts in the **exothermic** direction |
| Add inert gas at constant volume | **No shift** (partial pressures unchanged) |
| Add catalyst | **No shift** (equilibrium position unchanged; only rate of reaching equilibrium changes) |

![[le_chatelier_u7.svg|697]]
*Le Chatelier's principle: each stress (concentration, pressure, temperature) paired with the direction of equilibrium shift and resulting change in $Q$ relative to $K$. Temperature uniquely changes $K$ itself.*

**Temperature and $K$:**
- Exothermic forward reaction ($\Delta H < 0$): increasing $T$ shifts equilibrium left (reverse); $K$ decreases.
- Endothermic forward reaction ($\Delta H > 0$): increasing $T$ shifts equilibrium right (forward); $K$ increases.
- Think of heat as a reactant (endothermic) or product (exothermic): add/remove it like any other species.

---

## Topic 7.10: Reaction Quotient and Le Chatelier's Principle

**Essential Knowledge (Farabaugh CED):**
- After any stress other than temperature change, compare the new $Q$ to the unchanged $K$ to determine shift direction.
- **Adding a reactant** increases the numerator denominator... wait: $Q = [\text{products}]/[\text{reactants}]$. Adding reactant increases denominator → $Q$ **decreases** below $K$ → forward shift.
- **Adding a product** increases numerator → $Q$ **increases** above $K$ → reverse shift.
- **Decreasing volume** (at constant $T$): all concentrations increase proportionally. For a reaction with unequal gas moles, $Q \neq K$ after compression:
  - If more moles on product side: $Q > K$ → reverse shift (reduces total gas moles).
  - If more moles on reactant side: $Q < K$ → forward shift.
  - If equal moles on both sides: $Q = K$ — no shift.

**Q vs. K Decision Table:**

| Comparison | Shift | Reasoning |
|---|---|---|
| $Q < K$ | Forward (→) | Too few products; system makes more |
| $Q = K$ | No shift | Already at equilibrium |
| $Q > K$ | Reverse (←) | Too many products; system breaks them down |

---

## Topic 7.11: Introduction to Solubility Equilibria

**Essential Knowledge (Farabaugh CED):**
- The **solubility product constant $K_{sp}$** describes the equilibrium between an ionic solid and its dissolved ions in a saturated solution.
$$\text{M}_a\text{X}_b(s) \rightleftharpoons a\,\text{M}^{n+}(aq) + b\,\text{X}^{m-}(aq)$$
$$K_{sp} = [\text{M}^{n+}]^a[\text{X}^{m-}]^b$$
- The solid is omitted from $K_{sp}$ (pure solid). Only the aqueous ions appear.
- **Molar solubility ($s$)**: the number of moles of ionic compound that dissolve per liter of solution to reach saturation. $s$ and $K_{sp}$ are related through stoichiometry.

**Solubility ICE Table:**

| | $\text{Ag}^+$ | $\text{Cl}^-$ |
|---|---|---|
| **I** | 0 | 0 |
| **C** | $+s$ | $+s$ |
| **E** | $s$ | $s$ |

$K_{sp}(\text{AgCl}) = (s)(s) = s^2$ → $s = \sqrt{K_{sp}}$

**Common $K_{sp}$–Solubility Relationships:**

| Salt type | Example | Dissolution | $K_{sp}$ expression | $K_{sp}$ in terms of $s$ |
|---|---|---|---|---|
| 1:1 (AB) | AgCl | $\text{Ag}^+ + \text{Cl}^-$ | $[\text{Ag}^+][\text{Cl}^-]$ | $s^2$ |
| 1:2 (AB₂) | $\text{PbCl}_2$ | $\text{Pb}^{2+} + 2\text{Cl}^-$ | $[\text{Pb}^{2+}][\text{Cl}^-]^2$ | $(s)(2s)^2 = 4s^3$ |
| 2:1 (A₂B) | $\text{Ag}_2\text{SO}_4$ | $2\text{Ag}^+ + \text{SO}_4^{2-}$ | $[\text{Ag}^+]^2[\text{SO}_4^{2-}]$ | $(2s)^2(s) = 4s^3$ |
| 1:3 (AB₃) | $\text{AlF}_3$ | $\text{Al}^{3+} + 3\text{F}^-$ | $[\text{Al}^{3+}][\text{F}^-]^3$ | $(s)(3s)^3 = 27s^4$ |

![[ksp_solubility_u7.svg|697]]
*Ksp ICE table for $\text{Ag}_2\text{SO}_4$: each formula unit releases 2 Ag⁺ and 1 SO₄²⁻, giving $[\text{Ag}^+] = 2s$ and $[\text{SO}_4^{2-}] = s$. So $K_{sp} = (2s)^2(s) = 4s^3$. Solve: $s = (K_{sp}/4)^{1/3}$.*

**Comparing Solubilities:**
- To compare solubilities of compounds with the **same $K_{sp}$ form** (e.g., both AB type), compare $K_{sp}$ directly — higher $K_{sp}$ → higher solubility.
- For compounds with **different $K_{sp}$ forms** (AB vs. AB₂), convert each to $s$ before comparing.

---

## Topic 7.12: Common-Ion Effect

**Essential Knowledge (Farabaugh CED):**
- The **common-ion effect**: the solubility of an ionic compound decreases when a solution already contains one of its ions.
- Mechanism: the pre-existing ion raises the ion product $Q$ above $K_{sp}$, so the system shifts left (precipitation occurs) until $Q = K_{sp}$ again. Less solid dissolves.
- $K_{sp}$ itself is **unchanged** — only temperature changes $K_{sp}$. The common ion changes the molar solubility, not the equilibrium constant.

**ICE Table with Common Ion:**

Dissolving AgCl in $0.10\ \text{M}$ NaCl ($[\text{Cl}^-]_0 = 0.10\ \text{M}$):

| | $\text{Ag}^+$ | $\text{Cl}^-$ |
|---|---|---|
| **I** | 0 | 0.10 |
| **C** | $+s$ | $+s$ |
| **E** | $s$ | $0.10 + s$ |

$K_{sp} = s(0.10 + s) \approx 0.10s$ (since $s \ll 0.10$)
$s = K_{sp}/0.10$

This $s$ is much smaller than $\sqrt{K_{sp}}$ in pure water — the common ion dramatically reduces solubility.

**Practical Applications:**
- Adding AgNO₃ to a saturated AgCl solution precipitates more AgCl.
- Adding NaCl to a saturated AgCl solution also precipitates more AgCl.
- Both share the common-ion effect but from different ions.

---

## MCQ Pattern Recognition — Unit 7

| If you see... | It's testing... | Key move |
|---|---|---|
| "Liquid remains, pressure stopped rising" | Vapor–liquid equilibrium identification | Pressure plateau with liquid present = dynamic equilibrium; both evap. and condensation continue |
| Single particle diagram — is it equilibrium? | Snapshot limitation | A single snapshot **cannot** confirm equilibrium; need two time points |
| Concentration-time graph — when is equilibrium? | Reading flat-line region | Equilibrium = when curves become **horizontal and stay flat** |
| $[\text{A}] = [\text{B}]$ on a graph — is it equilibrium? | Equal concentration trap | Equal concentrations ≠ equilibrium; only equal rates (flat graph) confirms equilibrium |
| $K_{eq} \gg 1$ (e.g., $10^{37}$) with $Q = 0$ initially | Completing a nearly-complete reaction | $Q \ll K$ → forward reaction; $K \gg 1$ → essentially to completion |
| $K_{eq} \ll 1$ — compare equilibrium concentrations | Small K interpretation | Products scarce; $[\text{reactant}] \gg [\text{product}]$ at equilibrium |
| Reaction reversed — find new $K$ | Reversing rule | $K_{\text{new}} = 1/K_{\text{original}}$ |
| Two reactions added — find $K_3$ | Combining rule | Reverse → $1/K$; add → multiply $K$ values |
| ICE table with stoichiometric coefficient $\neq 1$ | Change row scaling | Change row: multiply $x$ by the stoichiometric coefficient |
| $[\text{I}_2]_{\text{eq}} = ?$ when only HI was present initially | Stoichiometric equimolar production | Species produced in 1:1 ratio have equal equilibrium concentrations |
| Q given; asked for shift direction | $Q$ vs. $K$ | $Q < K$ → forward; $Q > K$ → reverse; $Q = K$ → no shift |
| Cl₂ added to equilibrium — direction? | Q after stress | Adding product → $Q$ increases above $K$ → reverse shift |
| Volume halved — gas reaction — which way? | Pressure stress | Count gas moles on each side; shift toward fewer gas moles |
| Inert gas added at constant volume | No-shift trap | Inert gas doesn't change partial pressures → no shift |
| Endothermic reaction heated | Temperature effect on K | Heating endothermic: $K$ increases; shift right; more product |
| Cooling exothermic equilibrium | Temperature effect on K | Cooling exothermic: $K$ increases (reverse is endo); shift left |
| $K_{sp} = 4s^3$ — which formula? | Reading $K_{sp}$ form | $4s^3$ comes from 2:1 or 1:2 salt — two ions of one type |
| $[\text{I}^-] = 2 \times s$ (Hg₂I₂ type) | Stoichiometry in Ksp ICE | If coefficient is 2, ion concentration = $2s$; $s = [\text{ion}]/2$ |
| Dissolving salt in solution containing same ion | Common-ion effect | Solubility decreases; $K_{sp}$ unchanged; set up ICE with nonzero initial $[\text{ion}]$ |
| NaCN added to saturated AgCN solution | Common-ion with CN⁻ | CN⁻ is a product ion → equilibrium shifts left → more AgCN precipitates |

---

## AP Answer Templates — Unit 7

> **Equilibrium identification from observable:** "The system has reached equilibrium because [concentration / pressure / color] has stopped changing over time. At equilibrium, the forward and reverse reactions occur at equal rates, so macroscopic properties remain constant even though both reactions continue."

> **Dynamic vs. static equilibrium:** "The diagram does not represent dynamic equilibrium because it shows the system at only one point in time. Dynamic equilibrium requires that the rates of the forward and reverse reactions be equal and nonzero — a single snapshot cannot demonstrate that both processes are occurring simultaneously at equal rates."

> **Q vs. K shift prediction:** "The reaction quotient is $Q = [products]^{\text{coeff}}/[reactants]^{\text{coeff}} = [value]$. Since $Q [< / >] K = [value]$, the system will shift [forward / reverse] to [produce more products / consume products] until equilibrium is reestablished."

> **Le Chatelier — concentration stress:** "[Adding / removing] [species] [increases / decreases] $Q$ [above / below] $K$. The system responds by shifting [forward / reverse] to partially [reduce / restore] the concentration of [species] until $Q = K$ again."

> **Le Chatelier — pressure stress:** "Decreasing the volume increases the pressure. With [n₁] mol of gas on the reactant side and [n₂] mol on the product side, the system shifts toward the side with fewer gas moles ([reactants/products]) to reduce total pressure. This [increases / decreases] the yield of product."

> **Le Chatelier — temperature stress:** "The forward reaction is [exothermic / endothermic], so heat can be treated as a [product / reactant]. [Increasing / decreasing] temperature [adds / removes] heat, which [raises $Q$ above $K$ / lowers $Q$ below $K$], causing the equilibrium to shift [reverse / forward]. The value of $K$ itself [decreases / increases]."

> **Ksp → molar solubility:** "Let $s$ = molar solubility. The dissolution equation gives $[\text{M}^{n+}] = [a]s$ and $[\text{X}^{m-}] = [b]s$. Substituting into $K_{sp} = [\text{M}^{n+}]^a[\text{X}^{m-}]^b$ gives $K_{sp} = ([a]s)^a([b]s)^b$. Solving for $s$: $s = [expression]\ \text{mol/L}$."

> **Common-ion solubility:** "In the presence of $[M]$ M $[\text{ion}]$ (common ion), the ICE table gives $K_{sp} = (s)([\text{M}] + s) \approx [\text{M}] \cdot s$ (since $s \ll [\text{M}]$). Therefore $s = K_{sp}/[\text{M}]$, which is much smaller than the solubility in pure water. The common ion suppresses dissolution; $K_{sp}$ is unchanged because temperature did not change."

---

## Critical Reminders — Unit 7

> [!danger] K Changes ONLY With Temperature
> Adding reagents, changing pressure, or adding a catalyst all change Q but **NOT K**. Only a temperature change changes K itself.

> [!warning] Equilibrium = Equal Rates, NOT Equal Concentrations
> Flat concentration-time graph = equilibrium. Concentrations do not need to be equal to each other — only rates must be equal.

> [!warning] Single Snapshot Cannot Confirm Equilibrium
> A single particle diagram shows composition at one moment. You need at least two time points to confirm concentrations are no longer changing.

> [!check] Mass Is Always Conserved — Does NOT Indicate Equilibrium
> Constant mass in a sealed container is always true. Only constant concentrations/pressure/color confirm equilibrium. Never cite constant mass as evidence of equilibrium.

> [!danger] Pure Solids and Liquids Are Excluded From K Expressions
> Solid AgCl present does not mean [AgCl] appears in K_sp. Only aqueous ions and gases are included in K expressions.

> [!check] K Manipulation Rules (MCQ Q7 and Q50)
> Reverse → $K' = 1/K$. Multiply coefficients by n → $K' = K^n$. Add two reactions → $K' = K_1 \times K_2$.

> [!warning] ICE Table: Change Row Must Use Stoichiometric Coefficients
> For N₂ + 3H₂ ⇌ 2NH₃: changes are $-x$, $-3x$, $+2x$. The coefficient is the multiplier — don't write all changes as ±x.

> [!check] Large K (K >> 1): Nearly Goes to Completion
> K >> 1 → strongly product-favored → limiting reactant almost entirely consumed. Initial Q = 0 << K → strong forward drive.

> [!warning] Small K (K << 1): Use 5% Approximation
> $[reactant]_0 - x \approx [reactant]_0$ when x is small. Verify: $x/[reactant]_0 < 0.05$. If the 5% rule fails, solve the full quadratic.

> [!check] Q vs. K Decision Rule (MCQ Q47)
> Q < K → forward shift (more product needed). Q = K → no shift. Q > K → reverse shift (too many products).

> [!check] Common-Ion Effect: K_sp Unchanged, Molar Solubility Decreases
> Adding a common ion suppresses dissolution (Le Chatelier reverse shift). $K_{sp}$ is constant at constant temperature. Only molar solubility changes — set up ICE with nonzero initial [ion].

> [!warning] K_p = K_c(RT)^Δn
> If $\Delta n_{gas} = 0$, then $K_p = K_c$. If gas moles differ between sides, must use the $(RT)^{\Delta n}$ conversion factor.

> [!check] Inert Gas at Constant Volume: No Shift
> Inert gas does not change partial pressures of reactants or products → no shift in equilibrium. Affects only total pressure, not individual species.

> [!warning] K_sp ICE Table: Coefficient Creates BOTH Exponent AND Ion Concentration Factor
> For PbCl₂ → Pb²⁺ + 2Cl⁻: $[Cl^-] = 2s$ (from the coefficient 2), AND the exponent in $K_{sp} = [Pb^{2+}][Cl^-]^2$ is 2. Both effects must be applied.
