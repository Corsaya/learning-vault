# AP Chem — Unit 9 Notes: Applications of Thermodynamics
**Exam Weight: 7–9% | Topics: 9.1–9.11**
**Hub:** [[../../Study Hub/AP Chem Master Overview]] | **Memorize:** [[../../Study Hub/Memorization/Must Memorize]] (thermodynamics spontaneity, electrochemistry, oxidation number rules)
**Krug Videos:** *(fetch from jeremykrug.com/ap-chem-videos/ — Unit 9 has ~10 videos covering Topics 9.1–9.11)*

---

## Study Hub Quick Reference — Unit 9

> [!check] Q11 — Electrochemistry: E°cell = E°cathode − E°anode
> $E°_{cell} = E°_{cathode} - E°_{anode}$. The electrode with the **higher** standard reduction potential is the cathode (reduction). The electrode with the **lower** standard reduction potential is the anode (oxidation). **Never flip the sign** of a given E° when plugging in — the formula already accounts for the sign difference.

> [!check] Q20 — Gibbs Free Energy: Entropy-Driven Spontaneous Dissolution
> Some ionic compounds dissolve even though ΔH > 0 (endothermic) because ΔS is large and positive (ions become dispersed in solution). From $\Delta G = \Delta H - T\Delta S$: if $T\Delta S > \Delta H$, then ΔG < 0 → spontaneous. This is **entropy-driven dissolution** — thermodynamically favored despite endothermic enthalpy.

> [!check] Q33 — Inferring ΔH° and ΔS° from K vs. Temperature
> Use $\Delta G° = \Delta H° - T\Delta S°$ and $\Delta G° = -RT\ln K$. If K > 1 **only at high T** → ΔH > 0 (endothermic) and ΔS > 0 (entropy-driven). If K > 1 **only at low T** → ΔH < 0 (exothermic) and ΔS < 0. K > 1 means $\Delta G° < 0$, so infer signs of ΔH and ΔS from the temperature behavior.

> [!check] Q36/Q37 — Quantitative Analysis: Calibration Curve → Concentration → Stoichiometry
> **Q36:** Measure absorbance of unknown → read concentration from calibration curve → use mass percent formula: mass% = (mass of target / total mass) × 100. **Q37:** From calibration curve get [target ion] → use stoichiometry (mole ratio from balanced equation) → convert to molarity or mass of another species. The calibration curve always gives you concentration first; then apply stoichiometry.

> [!check] FRQ Q1A — Redox: Determining Oxidized/Reduced Species via Oxidation Numbers
> Assign oxidation numbers to each element in reactants and products. **Increase in ON = oxidized** (loses electrons = reducing agent). **Decrease in ON = reduced** (gains electrons = oxidizing agent). Rules: O = −2, H = +1, monoatomic ion = charge, F = −1 always, sum = 0 for neutral compound or = charge for polyatomic ion.

> [!check] FRQ Q3C — ΔH > 0 and ΔS > 0: Spontaneous Only at High T
> From the four-quadrant table: **+ΔH and +ΔS → favored only at HIGH temperature** where the $-T\Delta S$ term (negative, large) overcomes the positive ΔH. At low T, ΔG > 0 (not favored). At high T, ΔG < 0 (favored). Threshold temperature: $T = \Delta H/\Delta S$ (with ΔS converted to kJ/mol·K).

> [!check] FRQ Q5A — Electrochemistry: Electrons Transferred per O₂
> Write and balance the half-reactions. Count the electrons transferred in the balanced cell reaction — this is n. For O₂ reduction: $O_2 + 4H^+ + 4e^- \rightarrow 2H_2O$ → **n = 4** electrons per O₂. This n value is used in $\Delta G° = -nFE°_{cell}$ and Faraday's Law.

> [!check] FRQ Q5B — E°cell Calculation
> $E°_{cell} = E°_{cathode} - E°_{anode}$. Identify cathode (higher E°) and anode (lower E°) from given standard reduction potentials. Show the subtraction explicitly. Result must be **positive** for a spontaneous (galvanic) cell.

> [!check] FRQ Q5C — ΔG° = −nFE°cell
> $\Delta G° = -nFE°_{cell}$. n = moles of electrons from balanced half-reactions (not from formula). F = 96,485 C/mol. E° in volts (V = J/C). Answer in **joules**; convert to kJ by ÷ 1000. Positive E° → negative ΔG° → spontaneous.

> [!check] FRQ Q5D — Nernst Equation: Q and Cell Potential
> $E_{cell} = E°_{cell} - \frac{RT}{nF}\ln Q$. At 25°C: $E_{cell} = E°_{cell} - \frac{0.0592}{n}\log Q$. If Q > 1 (product-favored concentrations) → $E_{cell} < E°_{cell}$. If Q < 1 → $E_{cell} > E°_{cell}$. At equilibrium: $E_{cell} = 0$ (dead battery).

> [!warning] Trap — Never Multiply E° by a Stoichiometric Coefficient
> E° is an **intensive property** — it does NOT scale with the number of moles. Never multiply E° by 2 even if you double the reaction. Only n (moles of electrons) changes with scaling.

> [!warning] Trap — S° Is Never Zero for Any Substance
> Unlike $\Delta H°_f$ and $\Delta G°_f$ (which are zero for elements in standard state), $S°$ is **always positive and nonzero** for every substance. Elements in standard state have $S° > 0$.

> [!danger] Unit Conversion: ΔS Must Be in kJ for T_threshold
> $T_{threshold} = \Delta H/\Delta S$ requires **matching units**. ΔH is typically in kJ/mol; ΔS is in J/mol·K. **Divide ΔS by 1000** to convert to kJ/mol·K before calculating T. Missing this step gives an answer off by a factor of 1000.

---

## Topic 9.1: Introduction to Entropy (S)

**Essential Knowledge (Farabaugh CED):**
- Entropy (S°) represents the number of accessible microstates — the dispersal of energy among particles; higher disorder = more microstates = higher S°.
- **Phase hierarchy:** Gas > Aqueous > Liquid > Solid (most to least entropy).
- Increasing temperature increases the entropy of any substance.
- For substances in the same phase at the same temperature, more particles → higher entropy.
- Unlike $\Delta H°_f$ and $\Delta G°_f$, **S° is never zero** for any substance — elements in standard state have positive, non-zero standard entropies.

---

## Topic 9.2: Calculating Entropy Change (ΔS°)

**Essential Knowledge (Farabaugh CED):**
- For a reaction $aA + bB \rightarrow cC + dD$:
$$\Delta S^\circ_{rxn} = [c \cdot S^\circ(C) + d \cdot S^\circ(D)] - [a \cdot S^\circ(A) + b \cdot S^\circ(B)]$$
- If $\Delta S^\circ_{rxn}$ and all but one $S°$ value are given, set the unknown as $x$ and solve algebraically.

**Key Entropy Patterns:**
- **Large Positive ΔS:** Reactions producing gas from solids or liquids (e.g., $\ce{CaCO3(s) -> CaO(s) + CO2(g)}$).
- **Negative ΔS:** Reactions decreasing total moles of gas (e.g., $\ce{2SO2(g) + O2(g) -> 2SO3(g)}$ goes from 3 moles of gas to 2).
- **Phase Change Reminder:** Solid → Liquid → Gas each step significantly increases entropy, often by 50–150 J/mol·K or more.

**Common Mistake:** Forgetting that elements have a non-zero entropy value ($S°$). Unlike $\Delta H°_f$ and $\Delta G°_f$, which are zero for elements in standard state, everything has disorder — $S°$ is never zero.

---

## Topic 9.2b: Calculating Enthalpy from Bond Enthalpies (FRQ crossover from Unit 6)

**Essential Knowledge (Farabaugh CED):**
- Bond enthalpies can be used to estimate $\Delta H°_{rxn}$:
$$\Delta H°_{rxn} = \sum (\text{bonds broken, reactants}) - \sum (\text{bonds formed, products})$$
- Only works for **gas-phase reactions** where all reactants and products have well-defined covalent bonds.
- **Critical Rule:** Count every bond in every molecule. For NH₃, there are **3** N−H bonds per molecule, so 2 NH₃ = 6 N−H bonds total.
- **Sign convention:** Bonds broken → endothermic (+); bonds formed → exothermic (−). The formula handles signs automatically.

---

## Topic 9.3: Gibbs Free Energy (ΔG) and Favorability

**Essential Knowledge (Farabaugh CED):**
- **The Gibbs Equation:** $\Delta G = \Delta H - T\Delta S$
- A process is **thermodynamically favored** (TFP) when $\Delta G < 0$.
- $T$ must be in Kelvin; $\Delta H$ and $\Delta G$ in kJ/mol; $\Delta S$ in kJ/mol·K (convert from J/mol·K by ÷ 1000).

**The Four-Quadrant Favorability Table**

| ΔH (Enthalpy) | ΔS (Entropy) | Favorability (ΔG < 0) | Temperature Behavior |
|---|---|---|---|
| **Negative (Exo)** | **Positive** | **Always Favored** | Favored at all temperatures |
| **Positive (Endo)** | **Negative** | **Never Favored** | Unfavored at all temperatures |
| **Positive (Endo)** | **Positive** | **Favored at High T** | Entropy-driven: $-T\Delta S$ dominates at high T |
| **Negative (Exo)** | **Negative** | **Favored at Low T** | Enthalpy-driven: $\Delta H$ dominates at low T |

- **Threshold Temperature Calculation ($T_{threshold}$):** Set $\Delta G = 0$:
$$T = \frac{\Delta H}{\Delta S}$$
- **CRITICAL UNIT CONVERSION:** ΔS is usually in J/mol·K; ΔH is in kJ/mol. Divide ΔS by 1,000 before solving for T.

- **Inferring ΔS° from K and temperature behavior:** If K > 1 only above a certain temperature → +ΔH, +ΔS. If K > 1 only below a threshold T → −ΔH, −ΔS. Bridge: K > 1 ↔ ΔG° < 0.

---

## Topic 9.4–9.5: Equilibrium and Kinetic Control

**Essential Knowledge (Farabaugh CED):**
- **Equilibrium Connection:**
$$\Delta G° = -RT\ln K$$
  - $\Delta G° < 0$ → $K > 1$ (products favored at equilibrium)
  - $\Delta G° > 0$ → $K < 1$ (reactants favored at equilibrium)
  - **Units:** R = 8.314 J/(mol·K), so ΔG° must be in **J/mol** (not kJ/mol) when plugging in.
  - **Wrong R warning:** R = 0.08206 L·atm/(mol·K) is for PV = nRT only — never use it in $\Delta G° = -RT\ln K$.

- **Kinetic Control:** A reaction is under kinetic control if it is thermodynamically favored ($\Delta G < 0$) but no measurable reaction is observed.
  - **Reasons:** High activation energy ($E_a$), low collision frequency, or poor molecular orientation.
  - **The Distinction:** Thermodynamics tells you the **endpoint** (WHERE); kinetics tells you the **speed** of reaching it (HOW FAST).
  - **Catalyst effect:** Lowers $E_a$ and increases rate but has **no effect** on $\Delta G°$, $\Delta H°$, $\Delta S°$, or $K$.

- **Q vs K and Le Chatelier Shifts:**
  - $Q < K$ → forward reaction favored
  - $Q > K$ → reverse reaction favored
  - $Q = K$ → at equilibrium
  - **Volume change:** Halving volume doubles partial pressures → recalculate Q → compare to K → determine shift. K itself does NOT change unless T changes.

- **Combining equilibria (Hess's Law for K):**
  - Reverse a reaction → K becomes $\frac{1}{K}$
  - Add two reactions → multiply their K values
  - Multiply a reaction by $n$ → raise K to the $n$th power

**Key Insight:** A large K ($K > 1$) means the reaction is favored, but it does **not** guarantee the reaction will happen quickly.

---

## Topic 9.6: Free Energy of Dissolution

**Essential Knowledge (Farabaugh CED):**
- A substance is soluble if its dissolution is thermodynamically favored ($\Delta G < 0$).
- **The Dissolution Energy Balance:** $\Delta H_{solution} = \Delta H_{lattice} + \Delta H_{hydration}$
  - **Step 1:** Breaking the solid lattice is **endothermic** (unfavorable enthalpy).
  - **Step 2:** Hydrating the ions is **exothermic** (favorable enthalpy).

**Entropy Trade-off:**
- Breaking the solid into ions **increases entropy** (disordering the salt).
- Water molecules organizing around ions **decreases entropy** (ordering the solvent).

**Driving Forces:**
- **Case 1 (KCl):** +ΔH, but a large increase in entropy makes it favored.
- **Case 2 (CaCl₂):** −ΔS, but large exothermic enthalpy makes it favored.
- **Case 3 (Ag₂CrO₄):** +ΔH AND −ΔS → insoluble (never favored).

**What particle diagrams CAN and CANNOT show:**
- ✅ CAN show: ion dispersal (illustrates ΔS > 0), solvation of ions by water (illustrates ΔH < 0)
- ❌ CANNOT show: the magnitude of energy released/absorbed (ΔH cannot be read from a diagram)

---

## Topic 9.7: Coupled Reactions

**Essential Knowledge (Farabaugh CED):**
- A process with $\Delta G° > 0$ will not occur spontaneously. There are two ways to drive it: supply external energy (sunlight, electrical power), or **couple** it to another reaction.
- **Coupled reactions** share a **common intermediate** — a product of one reaction that is a reactant in the other. When the unfavorable reaction is linked to a sufficiently favorable one, the overall $\Delta G°$ becomes negative.

$$\Delta G°_{overall} = \Delta G°_1 + \Delta G°_2 \quad \text{(after scaling to cancel the common intermediate)}$$

**Conditions for successful coupling:**
- The two reactions must share a **common intermediate** (it cancels when equations are added)
- The **sum of $\Delta G°$ values must be negative** for the overall process to be favorable
- Hess's Law applies to $\Delta G°$ exactly as it does to $\Delta H°$

**Recognizing the Common Intermediate:** It appears as a product in one equation and a reactant in the other. When you add the equations, it cancels. Scale one equation if needed, then scale its $\Delta G°$ by the same factor.

| Pair | Common Intermediate |
|---|---|
| Fe₂O₃ decomposition + CO combustion | O₂ |
| ZnS decomposition + S combustion | S(s) |
| Any ore decomposition + carbon combustion | O₂ (usually) |

---

## Topic 9.8: Galvanic (Voltaic) and Electrolytic Cells

**Essential Knowledge (Farabaugh CED):**
- An **electrochemical cell** links an oxidation and a reduction half-reaction, either harvesting or consuming electrical energy. **Oxidation always occurs at the anode** and **reduction always occurs at the cathode** — for both galvanic and electrolytic cells, without exception.
- **Galvanic (voltaic) cell:** Runs on a thermodynamically favorable (spontaneous) redox reaction. Chemical energy → electrical energy. $\Delta G° < 0$, $E°_{cell} > 0$.
- **Electrolytic cell:** Forces a non-spontaneous reaction using an external power source. $\Delta G° > 0$. Coupled reactions use chemistry; electrolysis uses electricity.

$$\boxed{E°_{cell} = E°_{cathode} - E°_{anode}}$$

**AP rules — absolute:**
- **Never flip the sign** of a standard reduction potential when plugging into the formula
- **Never multiply $E°$** by a stoichiometric coefficient ($E°$ is an intensive property)

![[galvanic_cell_u9.svg|697]]
*Labeled galvanic cell: anode (oxidation, mass decreases) on left; cathode (reduction, mass increases) on right. Salt bridge maintains electrical neutrality. Electrons flow through the external circuit from anode to cathode.*

**Galvanic Cell Components:**

| Component | What happens | Mass change |
|---|---|---|
| Anode (oxidation) | Metal oxidized → ions enter solution; electrons flow OUT | Decreases |
| Cathode (reduction) | Ions reduced → deposit as solid metal; electrons flow IN | Increases |
| Salt bridge | Inert electrolyte (KNO₃, NaCl); cations → cathode, anions → anode; maintains charge neutrality | — |

Use an **inert electrode** (Pt or graphite) if the reactant/product is a gas or dissolved in solution — not a solid metal.

**Galvanic vs. Electrolytic — Full Comparison**

| Feature | Galvanic | Electrolytic |
|---|---|---|
| Thermodynamics | Spontaneous ($\Delta G° < 0$) | Non-spontaneous ($\Delta G° > 0$) |
| $E°_{cell}$ | Positive | Negative |
| Energy direction | Produces electrical energy | Consumes electrical energy |
| Chambers | Separate half-cells | Often same chamber |
| Salt bridge | Required | Not needed |
| Power source | None | Required |
| Examples | Battery, fuel cell | Electroplating, water splitting, recharging |

**True for BOTH:** Oxidation at anode; reduction at cathode. Cations → cathode; anions → anode.

---

## Topic 9.9: Cell Potential and Free Energy

**Essential Knowledge (Farabaugh CED):**
- $E°_{cell}$ and $\Delta G°$ describe the same thermodynamic reality using different units. They are linked by:

$$\boxed{\Delta G° = -nFE°_{cell}}$$

where $n$ = moles of electrons transferred and $F$ = Faraday's constant = **96,485 C/mol**.

**The Thermodynamic Triangle — all three describe the same equilibrium position:**

$$\Delta G° = -nFE°_{cell} = -RT\ln K$$

Therefore: $nFE°_{cell} = RT\ln K$

![[thermodynamic_triangle_u9.svg|697]]
*The three quantities ΔG°, K, and E°cell are interconvertible. Spontaneous: E° > 0, ΔG° < 0, K > 1. At equilibrium (dead battery): E° = 0, ΔG° = 0, K = 1.*

| Condition | $E°_{cell}$ | $\Delta G°$ | $K$ |
|---|---|---|---|
| Spontaneous (galvanic) | > 0 | < 0 | > 1 |
| Non-spontaneous (electrolytic) | < 0 | > 0 | < 1 |
| Equilibrium (dead battery) | = 0 | = 0 | = 1 |

**Units check:** $n$ is dimensionless (mol e⁻), $F$ = C/mol, $E°$ = V = J/C → $nFE°$ gives **J/mol**. Convert to kJ by dividing by 1,000.

**Finding n:** $n$ is the number of electrons transferred in the balanced overall cell reaction — determined from the half-reactions, NOT from the formula. Always write and balance both half-reactions first.

**Common Mistake:** Forgetting that $n$ depends on the balanced cell reaction. For Zn/Cu: Zn → Zn²⁺ + 2e⁻ and Cu²⁺ + 2e⁻ → Cu, so $n = 2$.

---

## Topic 9.10: Cell Potential Under Nonstandard Conditions (Nernst Equation)

**Essential Knowledge (Farabaugh CED):**
- Standard conditions are 1 M, 25°C, 1 atm. When concentrations differ, the actual cell potential $E_{cell}$ deviates from $E°_{cell}$ according to the **Nernst equation:**

$$\boxed{E_{cell} = E°_{cell} - \frac{RT}{nF}\ln Q}$$

At 25°C this simplifies to:

$$E_{cell} = E°_{cell} - \frac{0.0592}{n}\log Q$$

**Key relationships:**

| Q relative to K | $\ln Q$ | Effect on $E_{cell}$ | Meaning |
|---|---|---|---|
| $Q < K$ (excess reactants) | Negative | $E_{cell} > E°_{cell}$ | More spontaneous than standard |
| $Q = 1$ (standard conditions) | 0 | $E_{cell} = E°_{cell}$ | Standard cell |
| $Q > K$ (excess products) | Positive | $E_{cell} < E°_{cell}$ | Less spontaneous |
| $Q = K$ (equilibrium) | — | $E_{cell} = 0$ | Dead battery |

**Qualitative reasoning (AP MCQ shortcut):** As a galvanic cell operates, products accumulate → Q increases → $E_{cell}$ decreases → approaches zero at equilibrium. You do not need to calculate for MCQ sign questions.

**Concentration cell:** A special case where both half-cells use the same metal/ion pair but at different concentrations. $E° = 0$ because the two half-reactions are identical. Spontaneity comes entirely from the concentration difference. The cell drives toward equalizing concentrations: the dilute side is the anode (oxidation increases ion concentration there), the concentrated side is the cathode (reduction decreases ion concentration there).

**0.0592 form vs. RT/nF form:**
- Use **0.0592/n · log Q** only at exactly 25°C
- Use **RT/nF · ln Q** for any other temperature (and AP FRQs that specify a different T)

---

## Topic 9.11: Electrolysis and Faraday's Law

**Essential Knowledge (Farabaugh CED):**
- Faraday's Law links electrical quantities (current, time, charge) to chemical change (moles of substance produced or consumed) in an electrolytic cell.
- The same electrode rules apply: oxidation at anode, reduction at cathode.
- In electrolysis of water, H₂ is produced at the cathode and O₂ at the anode in a 2:1 mole ratio.

**The Three-Step Equation Chain:**

$$\text{Step 1: } q = It \quad \text{(charge = current × time)}$$
$$\text{Step 2: } n_e = \frac{q}{F} \quad \text{(moles of electrons = charge ÷ Faraday's constant)}$$
$$\text{Step 3: } n_{substance} = n_e \times \frac{1}{\text{electrons per ion}} \quad \text{(stoichiometry from half-reaction)}$$
$$\text{Step 4: } m = n_{substance} \times M \quad \text{(mass = moles × molar mass)}$$

**Constants and units:**
- $I$ = current in **amperes (A)**
- $t$ = time in **seconds (s)**
- $q$ = charge in **coulombs (C)**
- $F$ = 96,485 C/mol e⁻ (use 96,500 on AP if not given)
- $n_e$ = moles of electrons transferred

**Electrons per ion from the half-reaction:**
- Cu²⁺ + 2e⁻ → Cu: 2 electrons per Cu atom
- Al³⁺ + 3e⁻ → Al: 3 electrons per Al atom
- Ag⁺ + e⁻ → Ag: 1 electron per Ag atom

**Reverse problem (find time or current):** Rearrange the chain backward — calculate moles of substance needed → moles of electrons → coulombs → solve for $I$ or $t$.

**Electrolysis of water (standard AP example):**
$$\text{Cathode: } 2H_2O + 2e^- \rightarrow H_2(g) + 2OH^-$$
$$\text{Anode: } 2H_2O \rightarrow O_2(g) + 4H^+ + 4e^-$$

Note the 2:1 mole ratio of H₂ to O₂ produced — a common MCQ trap.

---

## Problem-Solving Frameworks

### 1. 'Predict and Justify Entropy Changes' Framework
1. Identify Phase Changes: solid → liquid → gas? (Entropy increases each step)
2. Apply Entropy Hierarchy: Gas > Aq > Liquid > Solid
3. Count Moles of Gas: same phases? → count gas particles on each side
4. State Prediction: "ΔS is positive because the reaction produces more moles of gas, increasing possible energy states."

### 2. 'Entropy/Enthalpy Calculation' Checklist
- [ ] **Check Units:** Convert ΔS from J to kJ if using with ΔH
- [ ] **Write Formula:** $\Delta S°_{rxn} = \sum S°_{prod} - \sum S°_{react}$
- [ ] **Multiply by Coefficients:** Did you multiply each $S°$ value by its stoichiometric coefficient?
- [ ] **Show Units:** Final answer in J/mol·K for ΔS, kJ/mol for ΔG/ΔH

### 3. 'Thermodynamic Favorability Analysis' Procedure
1. Determine signs of ΔH and ΔS
2. Consult Four-Quadrant Table
3. If T-dependent: calculate $T_{threshold} = \Delta H / \Delta S$ (with unit conversion)
4. Justify: "The reaction is favored at high T because the $-T\Delta S$ term overcomes the positive ΔH."

### 4. 'Bond Enthalpy Calculation' Procedure
1. Draw/visualize Lewis structures of reactants and products — count every bond
2. List bonds broken (reactant-side) and bonds formed (product-side)
3. Multiply by coefficients AND by bonds per molecule (e.g., 2 NH₃ → 6 N−H)
4. Apply: $\Delta H° = \sum(\text{broken}) - \sum(\text{formed})$
5. If solving for unknown bond: set as $x$ and use algebra

### 5. 'Q vs K Shift Analysis' Framework
1. Identify what changed (concentration, pressure, volume, product removal)
2. Reason about new Q relative to K
3. State direction: $Q < K$ → forward; $Q > K$ → reverse
4. Connect to question: e.g., "Removing NH₃ keeps $Q_p < K_p$, so the forward reaction continues."

### 6. 'ΔG° from ΔG°f' Procedure
$$\Delta G°_{rxn} = \sum \Delta G°_f(\text{products}) - \sum \Delta G°_f(\text{reactants})$$
- Multiply each $\Delta G°_f$ by its stoichiometric coefficient
- Elements in standard state: $\Delta G°_f = 0$
- Back-calculate ΔS° if ΔH° also given: $\Delta S° = \frac{\Delta H° - \Delta G°}{T}$

### 7. 'Coupled Reactions' Procedure
1. Identify the common intermediate (product of one, reactant of the other)
2. Scale one or both equations so the intermediate cancels (Hess's Law)
3. Scale $\Delta G°$ by the same factor as its equation
4. Add $\Delta G°$ values: if sum < 0, overall process is favorable
5. FRQ answer must name the intermediate AND state $\Delta G°_{overall} < 0$

### 8. 'Cell Potential and ΔG°' Procedure
1. Write both half-reactions; identify cathode (higher $E°$) and anode (lower $E°$)
2. Balance electrons — determine $n$
3. Calculate $E°_{cell} = E°_{cathode} - E°_{anode}$
4. Calculate $\Delta G° = -nFE°_{cell}$ (answer in J; convert to kJ)
5. State spontaneity: $E°_{cell} > 0$ → $\Delta G° < 0$ → spontaneous

### 9. 'Faraday's Law Calculation' Procedure
1. Convert time to seconds if needed
2. $q = It$ (coulombs)
3. $n_e = q / F$ (moles of electrons)
4. Use half-reaction stoichiometry: $n_{substance} = n_e \div (\text{electrons per ion})$
5. $m = n_{substance} \times M$ (grams)
6. For reverse: start from grams → moles → moles e⁻ → coulombs → solve for I or t

---

## MCQ Pattern Recognition — Full Unit 9

| If you see... | It's testing... | Key move |
|---|---|---|
| State change in a reaction | Entropy sign | Apply hierarchy: Gas > Aq > Liq > Solid |
| Moles of gas change | Entropy sign | Count gas particles; more gas = positive ΔS |
| ΔH and ΔS both given | Four-quadrant favorability | Check signs; if mixed signs, find $T_{threshold}$ |
| K > 1 only at high T | Sign of ΔH, ΔS | +ΔH, +ΔS (entropy-driven) |
| ΔG < 0 but no reaction observed | Kinetic control | High $E_a$; thermodynamics ≠ kinetics |
| Catalyst added | Effect on K and ΔG° | No effect; only lowers $E_a$ and speeds rate |
| Two reactions sharing a species | Coupled reactions | Find intermediate; sum ΔG° values |
| "Is coupling suitable?" | ΔG° sum < 0 AND common intermediate | Must state both for full credit |
| "Which electrode increases in mass?" | Cathode gains mass | Reduction = deposit; cathode mass up |
| "Calculate $E°_{cell}$" | $E°_{cathode} - E°_{anode}$ | Show subtraction; keep signs as given |
| ΔG° is negative | Spontaneous → galvanic | $E°_{cell} > 0$ |
| External power source required | Electrolytic cell | $E°_{cell} < 0$ for that reaction |
| "[Ion] concentration decreases" | Nernst / Q increases | Q↑ → $E_{cell}$ drops toward 0 |
| Q < K in electrochemical context | More spontaneous than standard | $E_{cell} > E°_{cell}$ |
| At equilibrium, what is $E_{cell}$? | Dead battery | $E_{cell} = 0$ always |
| Current × time given | Faraday's Law | $q = It$ → $n_e = q/F$ → stoichiometry |
| "Twice the current, same time" | Double the charge | Double moles electrons → double product |
| $n$ in $\Delta G° = -nFE°$ | Electrons transferred | Count from balanced half-reactions, not formula |
| Particle diagram of ion dissolution | What ΔS can be inferred | Dispersal shown → ΔS > 0; water reorganization NOT shown → cannot infer magnitude |
| Salt bridge composition changed (KNO₃ → NaNO₃) | Does $E°_{cell}$ change? | No — bridge ions are spectators, never oxidized or reduced |
| "[Reactant ion] precipitates out of solution" | Nernst effect on $E_{cell}$ | Q decreases → $E_{cell}$ increases above $E°_{cell}$ |
| "[Reactant] concentration increased above 1 M" | Nernst: Q vs. $E_{cell}$ | Q = [products]/[reactants] decreases → $E_{cell} > E°_{cell}$ |
| Concentration-time graph: products dominate | K and $\Delta G°$ sign | K >> 1 → $\Delta G° < 0$ → thermodynamically favored |
| K value given numerically (e.g., K = 10⁻³⁰) | Is $\Delta G°$ positive or negative? | K << 1 → $\Delta G° = -RT\ln K > 0$ → not favored |
| T given vs ΔH/ΔS ratio | Does phase change / melting occur? | T > ΔH/ΔS → ΔG < 0 → favorable; T < ΔH/ΔS → unfavorable |
| Two competing reactions, different $E_a$ | Which product forms at low T? | Kinetics: lower $E_a$ pathway wins at low T; thermodynamics takes over at high T |
| "Which cell modification gives greatest $E°_{cell}$?" | Compare each option's net $E°$ | Calculate $E°_{cathode} - E°_{anode}$ for each; $E°$ is intensive — no multiplying |
| Particle diagram asked for coupled reaction favorability | Can it represent energy coupling? | No — diagrams show matter/particles, not $\Delta G°$ values or energy changes |
| Electrolysis cell + external power source shown | Is process spontaneous? | No — external voltage required means $\Delta G > 0$ → electrolytic |
| Same moles of two metals deposited, different $n$ | Which needs more current? | More electrons per ion (larger $n$) → more charge → more current at same time |
| Same current/time, two metals with different $n$ | Which deposits more mass? | Smaller $n$ → more moles per coulomb → potentially more mass (check molar mass too) |

---

## FRQ Pattern Recognition — Full Unit 9

| Part says... | It's asking for... | Key move |
|---|---|---|
| "Predict the sign of ΔS°, justify" | Entropy reasoning | Name phase change or moles of gas change |
| "Calculate ΔS° for the reaction" | Products minus reactants with coefficients | Show setup with all values and stoichiometry |
| "Determine ΔH° using bond enthalpies" | Bonds broken − bonds formed | Count ALL bonds; multiply by coefficient AND bonds/molecule |
| "Is the reaction favored at 298 K?" | Calculate ΔG° = ΔH − TΔS | Show calculation; state sign and conclusion |
| "At what temperature does favorability switch?" | $T_{threshold} = \Delta H / \Delta S$ | Convert ΔS to kJ; show algebra |
| "Calculate K from ΔG°" | $K = e^{-\Delta G°/RT}$ | Convert ΔG° to J/mol; use R = 8.314 |
| "Why is reaction kinetically controlled?" | High $E_a$, no reaction despite ΔG < 0 | Name the strong bond (e.g., N≡N) as source of high $E_a$ |
| "Determine ΔG° for Equation 3" | Hess's Law summation for ΔG° | Scale equations; scale ΔG°; add |
| "Explain why suitable for coupling" | Common intermediate + ΔG°overall < 0 | **Must name the intermediate AND state the sign** |
| "Identify anode and cathode" | Higher E° = cathode | State both E° values; compare explicitly |
| "Calculate $E°_{cell}$" | $E°_{cathode} - E°_{anode}$ | Show subtraction with signs |
| "Is this spontaneous?" | $E°_{cell} > 0$ check | State value and conclude |
| "Purpose of salt bridge" | Electrical neutrality | Name ion directions; state what happens without it |
| "Calculate ΔG° from $E°_{cell}$" | $\Delta G° = -nFE°_{cell}$ | Determine n from half-reactions; show units |
| "Predict effect of decreasing [reactant]" | Nernst / Q reasoning | Q increases → $E_{cell}$ decreases |
| "Predict effect of product precipitating" | Nernst / Q reasoning | Q decreases → $E_{cell}$ increases above $E°$ |
| "Calculate mass deposited by electrolysis" | Faraday's Law chain | $q = It$ → $n_e = q/F$ → stoichiometry → $m = nM$ |
| "How long to deposit X grams?" | Reverse Faraday | $n \rightarrow n_e \rightarrow q \rightarrow t = q/I$ |
| "Which electroplating setup requires more current?" | Faraday's Law comparison | q = (mol metal)(n)(F); I = q/t; larger n and/or shorter t = more current |
| "Why does thermodynamically favored reaction not occur?" | Kinetic control | High $E_a$ from strong bond; name the bond; catalyst can help |

---

## AP Answer Templates — Full Unit 9

> **Entropy sign justification:** "ΔS° is positive because the reaction produces [more moles of gas / converts a solid to a gas], increasing the number of possible energy states and the disorder of the system."

> **ΔG° at a given temperature:** "ΔG° = ΔH° − TΔS° = (\_\_\_ kJ/mol) − (\_\_\_ K)(\_\_\_ kJ/mol·K) = \_\_\_ kJ/mol. Because ΔG° is [negative/positive], the reaction is [favored/not favored] at this temperature."

> **Threshold temperature:** "Setting ΔG° = 0: T = ΔH°/ΔS° = (\_\_\_ kJ/mol)/(\_\_\_ kJ/mol·K) = \_\_\_ K. Above this temperature, the reaction becomes [favored/unfavored]."

> **Kinetic control:** "Although the reaction is thermodynamically favored (ΔG° < 0), it is under kinetic control because the [N≡N / other] bond has a very high bond enthalpy (~\_\_\_ kJ/mol), resulting in a large activation energy. Very few collisions at this temperature have sufficient kinetic energy to break this bond."

> **Coupled reactions — suitability:** "These two reactions share a common intermediate ([name it]), and when coupled, yield an overall reaction with a negative free energy change (ΔG°overall < 0), making the process thermodynamically favorable."

> **Identifying anode/cathode:** "[Metal A] is the anode because it has the lower standard reduction potential (\_\_\_ V), so it undergoes oxidation. [Metal B] is the cathode because it has the higher standard reduction potential (\_\_\_ V), so it undergoes reduction."

> **Calculating $E°_{cell}$:** "$E°_{cell} = E°_{cathode} − E°_{anode} = (\_\_\_ V) − (\_\_\_ V) = \_\_\_ V$"

> **Spontaneity from $E°_{cell}$:** "$E°_{cell} = \_\_\_ V > 0$, therefore ΔG° < 0 and the reaction is thermodynamically spontaneous."

> **Salt bridge purpose:** "The salt bridge allows ions to flow between the two half-cells, maintaining electrical neutrality in each solution. Without it, charge would accumulate and the reaction would stop."

> **ΔG° from $E°_{cell}$:** "$\Delta G° = -nFE°_{cell} = -(\_\_\_ mol\ e^-)(96{,}485\ \text{C/mol})(\_\_\_ \text{V}) = \_\_\_ \text{J/mol} = \_\_\_ \text{kJ/mol}$"

> **Nernst qualitative — Q increases:** "Because [products accumulate / reactant concentration decreases], Q increases relative to standard conditions. According to the Nernst equation ($E_{cell} = E°_{cell} - \frac{RT}{nF}\ln Q$), a larger Q results in a smaller $E_{cell}$, reducing the spontaneity of the reaction."

> **Nernst qualitative — Q decreases:** "Because [product ion precipitates / reactant concentration increases], Q decreases below standard conditions. According to the Nernst equation, a smaller Q makes $E_{cell} > E°_{cell}$, increasing the spontaneity beyond the standard value."

> **Faraday's Law — mass deposited:** "$q = It = (\_\_\_ \text{A})(\_\_\_ \text{s}) = \_\_\_ \text{C}$; $n_e = q/F = \_\_\_ \text{mol}\ e^-$; $n_{metal} = n_e / \_\_\_$ (from half-reaction); $m = n_{metal} \times M = \_\_\_ \text{g}$"

> **Faraday's Law — comparing two metals:** "For the same charge $q = It$: moles of Metal A = $n_e / n_A$ and moles of Metal B = $n_e / n_B$. The metal requiring fewer electrons per ion ($n$ smaller) deposits more moles and typically more mass. To deposit equal moles in equal time, the metal with larger $n$ requires proportionally more current."

> **Particle diagram and entropy:** "The particle diagram shows [ions / molecules] becoming more dispersed in solution, indicating that the entropy change for this process is positive (ΔS > 0). However, the diagram cannot show the magnitude of ΔS° or the decrease in entropy due to water molecule reorganization around the dissolved ions."

> **Threshold temperature conclusion:** "At T = \_\_\_ K: $T_{threshold} = \Delta H° / \Delta S° = $ \_\_\_ K. Since T [>/<] $T_{threshold}$, $\Delta G$ = $\Delta H - T\Delta S$ = \_\_\_ [<0 → favored / >0 → not favored]."

---

## Critical Reminders — Full Unit 9

> [!danger] S° Is Never Zero
> Do not treat standard entropy like $\Delta H°_f$. Elements in standard state have $\Delta H°_f = 0$, but $S° > 0$ always. Using zero for $S°$ of an element destroys the entire calculation.

> [!danger] Catalyst Does Not Change Thermodynamics
> A catalyst lowers $E_a$ and speeds rate — it does **not** change $\Delta G°$, $\Delta H°$, $\Delta S°$, or K. The equilibrium position is identical with or without a catalyst.

> [!danger] E° Is Intensive — Never Multiply by n
> Standard reduction potentials are intensive properties. Doubling the half-reaction does **not** double $E°$. Only $\Delta G° = -nFE°$ scales with $n$.

> [!danger] H₂:O₂ = 2:1 in Electrolysis of Water
> At the cathode: $2\text{H}_2\text{O} + 2e^- \to \text{H}_2 + 2\text{OH}^-$; at the anode: $2\text{H}_2\text{O} \to \text{O}_2 + 4\text{H}^+ + 4e^-$. Two moles of H₂ per one mole of O₂ — a repeated MCQ trap.

> [!warning] Unit Matching for $T_{threshold}$
> $T_{threshold} = \Delta H / \Delta S$ requires **matching units**. Convert $\Delta S$ from J/mol·K to kJ/mol·K before dividing if $\Delta H$ is in kJ/mol. A factor-of-1000 error gives a nonsense temperature.

> [!warning] Use R = 8.314 (Not 0.08206) for ΔG° and K
> R = 8.314 J/(mol·K) in $\Delta G° = -RT\ln K$. Also convert $\Delta G°$ to J/mol (not kJ/mol) before computing $\ln K = -\Delta G°/RT$. Using 0.08206 or leaving ΔG° in kJ gives the wrong K.

> [!warning] $E°_{cell}$ Signs: Never Flip Given Values
> $E°_{cell} = E°_{cathode} - E°_{anode}$. Use the standard reduction potential values exactly as given in the table — do **not** flip the sign of the anode's $E°$. The subtraction handles directionality.

> [!warning] $n$ Comes from the Balanced Cell Reaction
> In $\Delta G° = -nFE°_{cell}$, $n$ = moles of electrons transferred in the **balanced** overall equation, not the charge on the ion and not the stoichiometric coefficient in the formula.

> [!warning] Nernst Equation Temperature Restriction
> Use $E_{cell} = E°_{cell} - \frac{0.0592}{n}\log Q$ only at exactly 25°C. At any other temperature, use $E_{cell} = E°_{cell} - \frac{RT}{nF}\ln Q$.

> [!warning] Faraday's Law: Time Must Be in Seconds
> Always convert time to seconds before computing $q = It$. Amperes are coulombs **per second** — using minutes or hours without conversion gives a wrong charge and wrong mass.

> [!check] The Three-Way Equivalence
> $E°_{cell} > 0 \Leftrightarrow \Delta G° < 0 \Leftrightarrow K > 1$ — these are always equivalent. A positive cell potential, a negative free energy change, and K > 1 all say the same thing: the forward reaction is thermodynamically favored.

> [!check] $E_{cell} = 0$ at Equilibrium
> A dead battery is always at equilibrium. No calculation needed — whenever Q = K, $E_{cell} = 0$ exactly.

> [!check] Coupled Reactions FRQ: Two Required Elements
> Must state **both**: (1) name the common intermediate shared by the two reactions, and (2) state that $\Delta G°_{overall} < 0$. Omitting either earns no credit for the coupling justification.

> [!check] Nernst Qualitative Reasoning
> Product precipitates → $[\text{product}]$ decreases → Q decreases → $E_{cell}$ **increases** above $E°_{cell}$. Reactant concentration increases above 1 M → Q decreases → $E_{cell} > E°_{cell}$. Reactant concentration decreases → Q increases → $E_{cell} < E°_{cell}$.

> [!check] Salt Bridge Identity Does Not Affect E°
> Whether the salt bridge contains KNO₃ or NaNO₃ makes no difference to $E°_{cell}$. Bridge ions are spectators — they maintain electrical neutrality but are never oxidized or reduced.

> [!check] Kinetic vs. Thermodynamic Selectivity
> At low T: the pathway with **lower $E_a$** wins (kinetic control). At high T: thermodynamics can take over (thermodynamic control). A reaction can be thermodynamically favored (ΔG° < 0) yet not occur because of a high $E_a$ (e.g., strong N≡N bond).

> [!check] Electroplating Comparison: Same Charge = Same Moles of Electrons
> For the same $q = It$: $n_e = q/F$ is identical for both metals. The metal with **smaller $n$** (electrons per ion) deposits more moles. Compare masses by also accounting for molar mass.
