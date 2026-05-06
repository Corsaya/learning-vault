# Practice Exam 1 FRQ — Worked Solutions

> [!warning] Exam Mindset
> Show all work on every calculation. A correct answer with no work = 0 points. Units matter. Sig figs matter on final answers.

---

## Question 1 — Combustion of Ethanol (7 parts)
**Units: 3 (IMF), 5 (Thermochemistry), 7 (Equilibrium)**

**Reaction:** C₂H₅OH(l) + 3 O₂(g) → 2 CO₂(g) + 3 H₂O(g) &emsp; ΔH°comb = −1270 kJ/mol_rxn

---

### Part A — Oxidation/Reduction of O₂
*Topic: Unit 9 — Redox / determining oxidized/reduced species via oxidation numbers*
**Question:** Is O₂(g) oxidized or reduced? Justify in terms of oxidation numbers.

**Answer:**
O₂ is **reduced**.
- In O₂(g): oxidation number of O = **0**
- In CO₂(g) and H₂O(g): oxidation number of O = **−2**
- O₂ gains electrons (0 → −2), which is the definition of reduction.

> [!check] **What earns the point**
> Must state "reduced" AND provide oxidation numbers (0 → −2). Saying "gains electrons" alone without the numbers is incomplete.

> [!danger] **Trap**
> Students confuse O₂ as oxidizing agent (which causes something else to oxidize) with O₂ itself being reduced. O₂ is the **oxidizing agent** and is itself **reduced** — these are the same thing said two ways.

---

### Part B — Moles of CO₂ via Ideal Gas Law
*Topic: Unit 6 — Ideal gas law / PV = nRT (must convert °C → K)*
**Question:** Volume of CO₂ = 18.0 L at 21.7°C and 1.03 atm. Find moles of CO₂.

**Answer:**
Use PV = nRT. Solve for n:

$$n = \frac{PV}{RT} = \frac{(1.03 \text{ atm})(18.0 \text{ L})}{(0.08206 \text{ L·atm/mol·K})(294.85 \text{ K})}$$

T = 21.7 + 273.15 = 294.85 K (use 294.9 K)

$$n = \frac{18.54}{24.20} = \boxed{0.766 \text{ mol CO}_2}$$

> [!check] **What earns the point**
> Correct setup of PV=nRT with T in Kelvin. Answer ≈ 0.766 mol (accept 0.765–0.767 depending on rounding).

> [!danger] **Trap**
> Forgetting to convert °C → K. Using 21.7 K gives a wildly wrong answer and no points.

---

### Part C — Volume of Ethanol Combusted
*Topic: Unit 4 — Stoichiometry / mol CO₂ → mol EtOH → mass → volume via density*
**Question:** Find volume (mL) of C₂H₅OH(l) combusted. Density = 0.79 g/mL.

**Answer:**
From part B: 0.766 mol CO₂ produced.

Stoichiometry: 1 mol C₂H₅OH → 2 mol CO₂

$$\text{mol EtOH} = 0.766 \text{ mol CO}_2 \times \frac{1 \text{ mol EtOH}}{2 \text{ mol CO}_2} = 0.383 \text{ mol EtOH}$$

$$\text{mass EtOH} = 0.383 \text{ mol} \times 46.07 \text{ g/mol} = 17.65 \text{ g}$$

$$\text{volume} = \frac{17.65 \text{ g}}{0.79 \text{ g/mL}} = \boxed{22.3 \text{ mL}}$$

> [!check] **What earns the point**
> Correct stoichiometric ratio (1:2), correct molar mass of ethanol (46.07), correct density division. ECF applies — if part B answer is wrong but carried correctly, full credit.

---

### Part D — Heat Released
*Topic: Unit 6 — Thermochemistry / heat = mol × ΔHcomb*
**Question:** Determine heat (kJ) released by the combustion reaction.

**Answer:**
From part C: 0.383 mol C₂H₅OH combusted.

$$q = 0.383 \text{ mol} \times 1270 \text{ kJ/mol} = \boxed{486 \text{ kJ released}}$$

Sign: The reaction is exothermic (ΔH = −1270 kJ/mol), so heat is **released** = 486 kJ.

> [!check] **What earns the point**
> Multiply moles of ethanol × 1270 kJ/mol. State that heat is released. The answer should be positive (magnitude of heat released).

---

### Part E — Final Temperature of Air in Room
*Topic: Unit 6 — Calorimetry / q = mcΔT → solve for T_final*
**Question:** Room contains 5.56 × 10⁴ g air at 21.7°C. Specific heat = 1.005 J/(g·°C). Find final temperature.

**Answer:**
q = mcΔT → ΔT = q/mc

q from part D = 486 kJ = 486,000 J

$$\Delta T = \frac{486{,}000 \text{ J}}{(5.56 \times 10^4 \text{ g})(1.005 \text{ J/g·°C})} = \frac{486{,}000}{55{,}878} = 8.70°\text{C}$$

$$T_{final} = 21.7°\text{C} + 8.70°\text{C} = \boxed{30.4°\text{C}}$$

> [!check] **What earns the point**
> q = mcΔT setup, correct unit conversion (kJ → J), add ΔT to initial temperature. ECF from parts B/C/D.

---

### Part F — IMF and Boiling Point (Ethanol vs. Dimethyl Ether)
*Topic: Unit 3 — IMF / hydrogen bonding requires O–H, N–H, or F–H bond → higher BP*
**Question:** Ethanol bp = 78°C, dimethyl ether bp = −24°C. Identify the IMF most responsible and explain why ethanol's bp is higher.

**Answer:**
The IMF most responsible is **hydrogen bonding**.

Ethanol (CH₃CH₂–**O–H**) can form **hydrogen bonds** between molecules because it has an O–H bond (H directly bonded to electronegative O). Hydrogen bonds are significantly stronger than the dipole-dipole forces and London dispersion forces present in dimethyl ether (CH₃–O–CH₃), which **cannot** form hydrogen bonds because there is no O–H (or N–H, F–H) bond. More energy is required to overcome hydrogen bonds in ethanol, resulting in a higher boiling point.

> [!check] **What earns the point**
> (1) Name H-bonding specifically. (2) Explain that ethanol has O–H → can H-bond, dimethyl ether cannot. (3) Tie stronger IMF to higher boiling point.

> [!danger] **Trap**
> "Ethanol is more polar" is not sufficient — you must name H-bonding explicitly and explain WHY ethanol can H-bond and dimethyl ether cannot.

---

### Part G — Le Chatelier's Principle (Two Conditions)
*Topic: Unit 7 — Le Chatelier's principle / shift equilibrium right by lowering T (exothermic) or increasing P (fewer gas mol)*
**Reaction:** C₂H₄(g) + H₂O(g) ⇌ C₂H₅OH(g) &emsp; ΔH° = −45 kJ/mol_rxn

**Question:** Identify TWO ways to change conditions (not adding/removing species) to maximize C₂H₅OH.

**Answer:**
**Condition 1 — Decrease temperature:**
The reaction is exothermic (ΔH° = −45 kJ). Decreasing temperature shifts equilibrium **right** toward products (C₂H₅OH), because the system produces heat to counteract the lower temperature.

**Condition 2 — Increase pressure (decrease volume):**
Reactants: 1 mol C₂H₄(g) + 1 mol H₂O(g) = **2 mol gas**.
Products: 1 mol C₂H₅OH(g) = **1 mol gas**.
Increasing pressure favors the side with **fewer moles of gas** (products), shifting equilibrium right.

> [!check] **What earns the point**
> Each condition earns 1 point: state the change AND provide the justification linking it to Le Chatelier's principle. "Increase pressure" alone without the mol gas explanation = no credit.

> [!danger] **Trap**
> "Add a catalyst" does NOT count — it does not shift equilibrium, only speeds up approach to equilibrium. The question explicitly says "other than adding or removing any chemical species."

---

## Question 2 — H₂O₂ Decomposition / Kinetics (7 parts)
**Units: 4 (Kinetics), 5 (Thermochemistry)**

**Reaction:** 2 H₂O₂(aq) → 2 H₂O(l) + O₂(g)

**Context:** Thermodynamically favorable. Catalyst: MnO₂(s) (insoluble, heterogeneous).

**Data (Beaker 2 with MnO₂):**
| Time (s) | Mass (g) |
|---|---|
| 0 | 43.19 |
| 10 | 43.06 |
| 20 | 42.94 |
| 30 | 42.83 |
| 40 | 42.73 |
| 50 | 42.65 |
| 60 | 42.58 |

Mass lost = 43.19 − 42.58 = **0.61 g** (this is the mass of O₂ that escaped as gas)

---

### Part A — Particulate Representation
*Topic: Unit 4 — Particulate model / stoichiometric product counts from balanced equation*
**Question:** Draw products from 4 H₂O₂ molecules reacting.

**Answer:**
2 H₂O₂ → 2 H₂O + O₂
From 4 H₂O₂: → **4 H₂O** molecules + **2 O₂** molecules
- 4 H₂O: each is O bonded to 2 H (bent molecule, 1 large O + 2 small H)
- 2 O₂: each is 2 O bonded together

> [!check] **What earns the point**
> Correct number AND type of particles: 4 H₂O + 2 O₂. Ratio must be correct.

---

### Part B(i) — Exothermic or Endothermic from PE Diagram
*Topic: Unit 6 — Energy diagrams / exothermic = products lower PE than reactants*
**Question:** Is decomposition exothermic or endothermic? Justify from diagram.

**Answer:**
**Exothermic.** The potential energy of the products (2 H₂O + O₂) is **lower** than the potential energy of the reactants (2 H₂O₂). Energy is released to the surroundings.

> [!check] **What earns the point**
> State "exothermic" AND reference that products are lower in PE than reactants.

---

### Part B(ii) — Catalyzed Curve
*Topic: Unit 5 — Catalysis / catalyst lowers Ea only; same reactant and product PE*
**Question:** Draw catalyzed curve (MnO₂) on PE diagram.

**Answer:**
Draw a new curve with a **lower activation energy hump** (lower peak) but:
- Same reactant PE (same starting point)
- Same product PE (same ending point)
- The hump is shorter/lower than the uncatalyzed curve

> [!check] **What earns the point**
> Lower Ea (lower peak). Same reactant and product energy levels. The curve must still show an activation energy hill — not flat.

> [!danger] **Trap**
> Do NOT lower the products PE. A catalyst lowers Ea only — it does not change ΔH or the thermodynamics of the reaction.

---

### Part C(i) — Moles of O₂ Produced
*Topic: Unit 4 — Stoichiometry / mass lost = mass of escaped O₂ → moles via molar mass*
**Question:** Calculate moles of O₂(g) produced during 60 s.

**Answer:**
Mass lost = 43.19 − 42.58 = 0.61 g (mass of O₂ that left beaker as gas)

$$n_{O_2} = \frac{0.61 \text{ g}}{32.00 \text{ g/mol}} = \boxed{0.019 \text{ mol O}_2}$$

> [!check] **What earns the point**
> Δmass = 0.61 g, divide by molar mass of O₂ (32.00 g/mol). Answer ≈ 0.019 mol.

---

### Part C(ii) — Mass of H₂O₂ Decomposed
*Topic: Unit 4 — Stoichiometry / 2:1 mole ratio (H₂O₂:O₂) → mass of H₂O₂*
**Question:** Calculate mass of H₂O₂ that decomposed.

**Answer:**
2 H₂O₂ → 2 H₂O + O₂
Mole ratio: 2 mol H₂O₂ per 1 mol O₂

$$\text{mol H}_2\text{O}_2 = 0.019 \text{ mol O}_2 \times \frac{2 \text{ mol H}_2\text{O}_2}{1 \text{ mol O}_2} = 0.038 \text{ mol H}_2\text{O}_2$$

$$\text{mass} = 0.038 \text{ mol} \times 34.02 \text{ g/mol} = \boxed{1.29 \text{ g H}_2\text{O}_2}$$

> [!check] **What earns the point**
> Use 2:1 mole ratio, correct molar mass of H₂O₂ (34.02 g/mol). ECF from C(i).

---

### Part D — Rate in Second Minute vs. First Minute
*Topic: Unit 5 — Kinetics / rate decreases as [H₂O₂] decreases; read from data table*
**Question:** Will mass of H₂O₂ consumed in second minute be greater than, less than, or equal to first minute?

**Answer:**
**Less than.** The data shows the mass decreasing by smaller amounts each interval (from 0.13 g in first 10 s to 0.07 g in last 10 s), indicating the reaction rate is slowing down. As H₂O₂ is consumed, its concentration decreases, so the rate decreases further in the second minute.

> [!check] **What earns the point**
> State "less than" AND cite data showing the rate is already decreasing (shrinking mass differences over time), AND/OR explain that [H₂O₂] decreases so rate decreases.

---

### Part E — Zeroth-Order Kinetics Claim
*Topic: Unit 5 — Reaction order / zeroth-order = constant rate = equal Δmass per interval (data shows decreasing)*
**Question:** Student claims catalyzed reaction has zeroth-order kinetics. Agree?

**Answer:**
**No, disagree.** For zeroth-order kinetics, the rate would be constant — equal masses of H₂O₂ consumed in equal time intervals. The data shows the mass loss per interval is **decreasing** (not constant), indicating the rate is decreasing as [H₂O₂] decreases. This is consistent with first-order (or higher) kinetics, not zeroth-order.

> [!check] **What earns the point**
> Disagree + cite the non-constant mass differences from data. Explain what zeroth-order would look like (constant rate).

---

### Part F — Splash Error Analysis
*Topic: Unit 4 — Lab / systematic error analysis (splash inflates Δmass → inflates calculated mol O₂)*
**Question:** Second student used larger volumes; liquid splashed out. Student claims calculated moles of O₂ > actual. Agree?

**Answer:**
**Yes, agree.** The calculation is based on mass lost from the beaker (Δmass = moles O₂). If liquid splashes out, the mass of the beaker decreases due to both O₂ escaping AND liquid H₂O₂ leaving the beaker. The calculated Δmass is therefore **larger** than the true mass of O₂ produced, so the calculated moles of O₂ would be **greater than** the actual moles produced.

> [!check] **What earns the point**
> Agree + explain that splash loss is counted as additional mass loss → inflates the calculated O₂.

---

### Part G — Balanced Equation
*Topic: Unit 4 — Balancing chemical equations / atom and charge conservation*
**Question:** (NH₄)₂S₂O₈ + H₂O → H₂O₂ + NH₄HSO₄. Write balanced equation.

**Answer:**
(NH₄)₂S₂O₈ + 2 H₂O → 2 H₂O₂ + (NH₄)₂SO₄... let me re-examine.

Products are H₂O₂ and NH₄HSO₄ (ammonium bisulfate).

**(NH₄)₂S₂O₈ + 2 H₂O → 2 H₂O₂ + 2 NH₄HSO₄**

Wait: check atoms.
- Left: 2N, 8H(ammonium) + 4H(water) = 12H, 2S, 8O(peroxydisulfate) + 2O(water) = 10O
- Right: 4H(H₂O₂) + 2×(4H+1H)(NH₄HSO₄) = 4 + 10 = 14H? 

Let me redo: 
(NH₄)₂S₂O₈: contains N₂H₈S₂O₈
H₂O: H₂O
H₂O₂: H₂O₂
NH₄HSO₄: N, H₄+H=H₅, S, O₄

Balanced: (NH₄)₂S₂O₈ + 2 H₂O → 2 H₂O₂ + 2 NH₄HSO₄

Check:
- N: 2 = 2 ✓
- H: 8 + 4 = 12 left; 4 + 2×5 = 14 right ✗

Try: (NH₄)₂S₂O₈ + 2 H₂O → H₂O₂ + 2 NH₄HSO₄... no, then S: 2 = 2, but O: 8+2=10 left; 2 + 2×4=10 ✓, H: 8+4=12 left; 2 + 2×5=12 ✓, N: 2=2 ✓

$$\boxed{(\text{NH}_4)_2\text{S}_2\text{O}_8 + 2\ \text{H}_2\text{O} \rightarrow \text{H}_2\text{O}_2 + 2\ \text{NH}_4\text{HSO}_4}$$

> [!check] **What earns the point**
> Equation is balanced with correct formulas. H and O atoms must balance (peroxydisulfate → bisulfate + peroxide).

---

## Question 3 — SO₃ / Lewis Structures / Equilibrium (5 parts)
**Units: 2 (Bonding/Structure), 7 (Equilibrium)**

---

### Part A — Lewis Structure of SO₃
*Topic: Unit 2 — Lewis structures / count valence electrons, minimize formal charge, resonance*
**Question:** Complete valid Lewis electron-dot diagram for SO₃.

**Answer:**
SO₃ has 24 valence electrons total (S: 6, each O: 6, × 3 = 18 + 6 = 24).

The most common valid structure: S in center, double-bonded to one O and single-bonded to two O's, with formal charges minimized.

**Resonance structure (any one valid):**
```
    O
    ‖
O — S — O
```
With lone pairs:
- Double-bonded O: 2 lone pairs
- Single-bonded O: 3 lone pairs
- S: no lone pairs (in resonance structures with double bond)

OR draw the resonance structure where S forms a double bond with any one oxygen, with all other lone pairs correctly placed. All three are equally valid.

**Total electron count check:** 1 S=O (4 e⁻) + 2 S–O (4 e⁻) + 2 LP on double O (4 e⁻) + 6 LP on each single O (12 e⁻) = 24 ✓

> [!check] **What earns the point**
> Correct connectivity (S central, 3 O atoms bonded to S), correct total of 24 valence electrons, and all lone pairs shown. Any valid resonance structure earns the point.

> [!danger] **Trap**
> Forgetting lone pairs on oxygen atoms is the most common mistake. Every O must have its lone pairs drawn.

---

### Part B — Molecular Geometry
*Topic: Unit 2 — VSEPR / 3 bonding domains + 0 LP = trigonal planar (120° bond angles)*
**Question:** Predict shape of SO₃.

**Answer:**
**Trigonal planar.**
S has 3 bonding domains and 0 lone pairs → electron geometry = trigonal planar → molecular geometry = **trigonal planar**. Bond angles = 120°.

> [!check] **What earns the point**
> "Trigonal planar." Bonus if you add 120° bond angles, but the geometry name alone earns the point.

---

### Part C — Temperature Conditions for Thermodynamic Favorability
*Topic: Unit 9 — Thermodynamics / ΔH > 0 and ΔS > 0 → spontaneous only at high T (−TΔS dominates)*
**Reaction:** 2 SO₃(g) ⇌ 2 SO₂(g) + O₂(g) &emsp; ΔH° = +180 kJ/mol_rxn

**Question:** High T, low T, all T, or no T?

**Answer:**
**High temperatures.** 

- ΔH° = +180 kJ → **endothermic** → unfavorable enthalpy contribution (ΔH > 0 opposes spontaneity)
- ΔS°: reactants = 2 mol gas; products = 3 mol gas → more disorder → **ΔS > 0** → favorable entropy contribution

Using ΔG = ΔH − TΔS:
- At low T: ΔH term dominates → ΔG > 0 (not spontaneous)
- At high T: TΔS term dominates → ΔG < 0 (spontaneous)

Therefore: favorable at **high temperatures**.

> [!check] **What earns the point**
> State "high temperatures" AND justify: (1) ΔH > 0 is unfavorable, (2) ΔS > 0 (more moles of gas → more disorder), (3) high T makes TΔS large enough to overcome positive ΔH.

---

### Part D — Equilibrium Graph Analysis
*Topic: Unit 7 — Equilibrium / reading pressure-time graphs; identifying Q > K → reverse shift*
**Context:** SO₃(g) fills rigid vessel at 0.83 atm. Decomposes. Graph tracks P(SO₃), P(SO₂), P(O₂) vs. time. A change is made at t₁ — after which P(SO₃) **increases** and P(O₂) **decreases**.

#### Part D(i) — When did equilibrium first occur?
**Answer:** The X should be placed on the time axis at the point where all three partial pressure curves **level off** (become constant/flat) — before the change at t₁.

#### Part D(ii) — What change was made at t₁?
**Answer:** **SO₂(g) was added** to the system at t₁.

Reasoning: After t₁, P(SO₃) increased and P(O₂) decreased — the equilibrium shifted **left** (reverse reaction: 2SO₂ + O₂ → 2SO₃). Adding SO₂ would cause exactly this leftward shift. (Alternatively, removing O₂ would decrease P(O₂) but that would shift right, increasing SO₂ and decreasing SO₃ — doesn't match.)

#### Part D(iii) — Explain the observation after t₁
**Answer:** Adding SO₂ increased Q above Kp. The system shifted **left** (reverse reaction) to re-establish equilibrium: SO₂ and O₂ are consumed and SO₃ is produced. This caused P(SO₃) to increase and P(O₂) to decrease (O₂ is consumed as a reactant in the reverse direction).

> [!check] **What earns the point**
> D(ii): Identify "SO₂ was added." D(iii): Explain shift left via Q > Kp → reverse reaction consumes O₂ and produces SO₃.

---

### Part E — Kp Expression and Value
*Topic: Unit 7 — Equilibrium constant Kp / expression from balanced equation; ICE table from graph values*

#### E(i) — Write Kp expression
$$K_p = \frac{(P_{SO_2})^2(P_{O_2})}{(P_{SO_3})^2}$$

#### E(ii) — Calculate Kp
**From graph at equilibrium (before t₁):** Starting from P(SO₃) = 0.83 atm, let x = decrease in P(SO₃):

| Species | Initial | Change | Equilibrium |
|---|---|---|---|
| SO₃ | 0.83 | −2x | 0.83 − 2x |
| SO₂ | 0 | +2x | 2x |
| O₂ | 0 | +x | x |

Reading equilibrium values from graph: P(O₂) ≈ 0.22 atm → x ≈ 0.22
- P(SO₂)_eq = 2(0.22) = 0.44 atm
- P(SO₃)_eq = 0.83 − 2(0.22) = 0.83 − 0.44 = 0.39 atm

$$K_p = \frac{(0.44)^2(0.22)}{(0.39)^2} = \frac{(0.194)(0.22)}{0.152} = \frac{0.0426}{0.152} \approx \boxed{0.28 \text{ atm}}$$

> [!check] **What earns the point**
> Correct Kp expression (products over reactants, correct exponents). For the value, your read from the graph must be internally consistent with the 2:1 SO₂:O₂ stoichiometry. ECF applies.

> [!danger] **Trap**
> Forgetting the exponents (2 for SO₂ and SO₃, 1 for O₂). A common error is writing Kp = (P_SO₂)(P_O₂)/(P_SO₃) without squaring.

---

## Question 4 — HClO / Acid-Base / Titration (3 parts)
**Unit: 8 (Acids & Bases)**

**Reaction:** HClO(aq) + H₂O(l) ⇌ H₃O⁺(aq) + ClO⁻(aq)

---

### Part A — Conjugate Acid-Base Pair
*Topic: Unit 8 — Brønsted-Lowry / conjugate acid-base pairs (differ by one H⁺)*
**Question:** Identify one conjugate acid-base pair.

**Answer (either pair accepted):**
- **Pair 1:** HClO / ClO⁻ (HClO donates H⁺ to become ClO⁻)
- **Pair 2:** H₂O / H₃O⁺ (H₂O accepts H⁺ to become H₃O⁺)

> [!check] **What earns the point**
> Name BOTH members of ONE conjugate pair. "HClO and ClO⁻" earns the point. "HClO" alone does not.

---

### Part B — Titration Curve: HClO₄ vs. HClO
*Topic: Unit 8 — Titration curves / strong acid starts lower pH; equivalence at pH 7; no buffer region*
**Question:** Given the HClO titration curve, draw the curve for 25.0 mL of 0.200 M HClO₄ (strong acid) titrated with 0.200 M NaOH.

**Answer — Key differences for HClO₄ curve:**
1. **Starting pH is lower** (~1.0) because HClO₄ is a strong acid (fully dissociates); HClO is weak (starts ~3.5)
2. **No buffer region** — HClO₄ fully dissociates; no weak acid/conjugate base plateau in the buffer region
3. **Equivalence point pH = 7** (exactly) because NaClO₄ is a neutral salt; HClO reaches equivalence at pH > 7 (~8.5) due to ClO⁻ hydrolysis
4. **Same equivalence point volume** (25.0 mL NaOH) — same moles of acid
5. **Steeper initial slope** on the strong-acid curve

> [!check] **What earns the point**
> Draw curve starting at lower pH, equivalence point at pH 7 (not above 7), same volume of NaOH at equivalence point. The absence of a buffer region may also be scoreable.

> [!danger] **Trap**
> Many students draw both curves with the same shape, just shifted vertically. The shape changes fundamentally: the HClO₄ curve has no buffer region, and the equivalence point is at pH 7, not above 7.

---

### Part C — Buffer Explanation
*Topic: Unit 8 — Buffers / requires weak acid + conjugate base; strong acid (HClO₄) cannot form a buffer*
**Question:** Student dissolves 0.010 mol NaClO₄(s) in 100 mL of 0.100 M HClO₄. Explain why NOT a buffer.

**Answer:**
This is NOT a buffer because a buffer requires a **weak acid and its conjugate base** in comparable amounts. 

HClO₄ is a **strong acid** — it dissociates completely in solution. There is no weak acid present, only H₃O⁺ ions and ClO₄⁻. The ClO₄⁻ ion is the conjugate base of a strong acid and is an extremely weak base — it cannot neutralize added acid. Therefore, the system cannot resist changes in pH when acid or base is added.

> [!check] **What earns the point**
> Must state that HClO₄ is a strong acid (fully dissociates) AND that a buffer requires a weak acid/conjugate base pair. Simply saying "HClO₄ is strong" without connecting to buffer definition is insufficient.

> [!danger] **Trap**
> Confusing HClO (hypochlorous acid, weak) with HClO₄ (perchloric acid, strong). These are different acids. HClO CAN form a buffer with NaClO; HClO₄ CANNOT.

---

## Question 5 — Electrochemistry / NADH (4 parts)
**Unit: 9 (Electrochemistry)**

**Half-reactions:**
| Half-Reaction | E° (V) |
|---|---|
| O₂ + 4H⁺ + 4e⁻ → 2H₂O | +0.815 |
| NAD⁺ + H⁺ + 2e⁻ → NADH | −0.320 |

**Overall:** O₂ + 2H⁺ + 2 NADH → 2H₂O + 2 NAD⁺

---

### Part A — Moles of Electrons per Mole O₂
*Topic: Unit 9 — Redox / electrons transferred per O₂ via oxidation numbers (0 → −2, ×2 O atoms = 4e⁻)*
**Question:** How many moles of electrons transferred per mole of O₂?

**Answer:**
**4 moles of electrons** per mole of O₂.

Justification using oxidation numbers:
- O in O₂: oxidation state = **0**
- O in H₂O: oxidation state = **−2**
- Each O atom gains 2 electrons; O₂ has 2 O atoms → 2 × 2 = **4 electrons** transferred per O₂

Confirmed by the balanced half-reaction: O₂ + 4H⁺ + **4e⁻** → 2H₂O

> [!check] **What earns the point**
> State "4 moles" AND justify using oxidation numbers (0 → −2, ×2 oxygen atoms = 4 electrons) or cite the half-reaction coefficient.

---

### Part B — Electrochemical Potential
*Topic: Unit 9 — Electrochemistry / E°cell = E°cathode − E°anode (never multiply E° by stoichiometry)*
**Question:** Calculate E°cell for overall reaction.

**Answer:**
Cathode (reduction): O₂ + 4H⁺ + 4e⁻ → 2H₂O, E° = +0.815 V
Anode (oxidation): NADH → NAD⁺ + H⁺ + 2e⁻ (reversed), E°anode = −0.320 V

$$E°_{cell} = E°_{cathode} - E°_{anode} = 0.815 - (-0.320) = \boxed{+1.135 \text{ V}}$$

> [!check] **What earns the point**
> Correct identification of cathode/anode, correct subtraction. Note: do NOT multiply E° values by stoichiometric coefficients — E° is intensive.

> [!danger] **Trap**
> Multiplying E° by 2 (because you double the NADH half-reaction). E° values are NOT multiplied by stoichiometric coefficients. Only n changes.

---

### Part C — ΔG°
*Topic: Unit 9 — Electrochemistry / ΔG° = −nFE° (n = total electrons transferred)*
**Question:** Calculate ΔG° for overall reaction.

**Answer:**
$$\Delta G° = -nFE°$$

n = 4 mol e⁻ (per mole of reaction as written — O₂ gains 4e⁻, 2 NADH each lose 2e⁻ = 4e⁻ total)
F = 96,485 C/mol

$$\Delta G° = -(4)(96{,}485)(1.135) = -(4)(109{,}510) = -438{,}040 \text{ J/mol}$$

$$\Delta G° = \boxed{-438 \text{ kJ/mol}}$$

The large negative ΔG° confirms this is thermodynamically very favorable.

> [!check] **What earns the point**
> Correct formula (ΔG° = −nFE°), n = 4, F = 96,485 (or 96,500), E° from part B. Answer ≈ −438 kJ (accept −435 to −440 kJ range depending on rounding).

---

### Part D — Effect of Increasing [NADH] / Decreasing [NAD⁺]
*Topic: Unit 9 — Nernst equation / [NADH]↑ and [NAD⁺]↓ → Q decreases → E increases above E°*
**Question:** When [NADH]↑ and [NAD⁺]↓, does electrochemical potential increase, decrease, or stay same?

**Answer:**
The electrochemical potential **increases**.

Using the Nernst equation concept: Q = [NAD⁺]²/([NADH]²[H⁺]²·P_O₂). When [NADH] increases and [NAD⁺] decreases, Q **decreases** (more reactant relative to product). A smaller Q means E > E° — the reaction is driven more strongly forward, so the measured potential is **higher** than E°.

Conceptually: more NADH (fuel) available drives the reaction harder → higher cell potential.

> [!check] **What earns the point**
> State "increases" AND justify using Q: [NADH]↑ and [NAD⁺]↓ → Q decreases → E increases. Must connect the concentration change to Q and then to E.

---

## Question 6 — Paraffin Wax / Phase Changes / Thermochemistry (3 parts)
**Units: 3 (IMF/Phase), 6 (Thermodynamics)**

**Context:** Paraffin wax melts at 37°C. Molar mass = 282.62 g/mol. Molar heat of fusion = 48.78 kJ/mol.

---

### Part A — Direction of Heat Flow During Melting
*Topic: Unit 3 — Phase changes / melting is endothermic → energy flows from surroundings into system*
**Question:** Is net thermal energy flow from wax → surroundings or surroundings → wax?

**Answer:**
**From surroundings to the wax.** Melting is an endothermic process — energy must be absorbed by the wax to break the intermolecular forces between molecules. The surroundings (building material) must supply thermal energy to the wax to cause it to melt.

> [!check] **What earns the point**
> State "surroundings to wax" AND justify that melting is endothermic (energy input required to overcome IMFs / increase potential energy of molecules).

---

### Part B — Energy to Melt 15.2 g of Paraffin
*Topic: Unit 6 — Thermochemistry / g → mol × ΔH_fus = heat required*
**Question:** Calculate thermal energy (kJ) to melt 15.2 g.

**Answer:**
$$\text{mol paraffin} = \frac{15.2 \text{ g}}{282.62 \text{ g/mol}} = 0.05378 \text{ mol}$$

$$q = 0.05378 \text{ mol} \times 48.78 \text{ kJ/mol} = \boxed{2.62 \text{ kJ}}$$

> [!check] **What earns the point**
> Convert grams to moles using correct molar mass, multiply by heat of fusion. Answer ≈ 2.62 kJ.

---

### Part C — Density Decreases on Melting: Particle-Level
*Topic: Unit 3 — IMF / particle-level explanation: liquid = less ordered, farther apart → same mass, larger volume → lower density*
**Question:** When paraffin melts, density decreases. Provide particle-level explanation.

**Answer:**
In solid paraffin, molecules are held in a relatively ordered arrangement by **London dispersion forces** (paraffin is a nonpolar hydrocarbon), and they are closely and rigidly packed together. When paraffin melts, the molecules gain enough energy to partially overcome these IMFs and move more freely. In the liquid state, the molecular arrangement is less ordered and molecules are slightly further apart on average, occupying a larger total volume. Since the same mass now occupies a larger volume, density (mass/volume) decreases.

> [!check] **What earns the point**
> Must reference: (1) solid has more ordered/tightly packed molecular arrangement, (2) liquid molecules are farther apart / more disordered, (3) same mass, larger volume → lower density. All three ideas needed.

> [!danger] **Trap**
> "Water is unusual in that its solid is less dense than its liquid" — this is water, not paraffin. For most substances (including paraffin), solid is MORE dense than liquid. The question is asking you to explain the normal behavior.

---

## Question 7 — Phenol Red / Beer-Lambert Law / Spectrophotometry (4 parts)
**Unit: 1 (Lab / Measurement)**

**Context:** Phenol red solution. pH meter reads 11.20. Spectrophotometer set at 559 nm (wavelength of maximum absorbance). Measured absorbance = 0.35.

---

### Part A — Calculate [H⁺]
*Topic: Unit 8 — pH / [H⁺] = 10^−pH (use correct sig figs: 2 decimal places in pH = 2 sig figs in [H⁺])*
**Question:** Calculate [H⁺] in solution. pH = 11.20.

**Answer:**
$$[\text{H}^+] = 10^{-\text{pH}} = 10^{-11.20} = \boxed{6.3 \times 10^{-12} \text{ M}}$$

> [!check] **What earns the point**
> Correct calculation: 10^−11.20. Must express in scientific notation with correct sig figs (2 sig figs, matching 2 decimal places in pH).

---

### Part B — Read Concentration from Calibration Curve
*Topic: Unit 1 — Beer-Lambert law / reading calibration curve: absorbance → concentration*
**Question:** Absorbance = 0.35 at 559 nm. Find concentration (μM) from calibration curve.

**Answer:**
Locate absorbance = 0.35 on the y-axis of the calibration curve and read across to the best-fit line, then down to the x-axis.

From the curve: **≈ 4.5–5.0 μM** (read directly from graph).

> [!check] **What earns the point**
> Any value read consistently from the graph is accepted. Must show/indicate you are using the line of best fit (not individual data points).

---

### Part C — Dilution Effect on Absorbance
*Topic: Unit 1 — Beer-Lambert law / A ∝ c; halving concentration halves absorbance*
**Question:** 10 mL distilled water + 10 mL sample mixed. Absorbance greater than, less than, or equal to original?

**Answer:**
**Less than** the original absorbance.

Mixing equal volumes halves the concentration of phenol red. By **Beer-Lambert Law** (A = εlc), absorbance is directly proportional to concentration. Half the concentration → half the absorbance. The absorbance of the diluted solution would be approximately **0.35/2 ≈ 0.18**.

> [!check] **What earns the point**
> State "less than" AND cite Beer-Lambert law (A ∝ c) OR explain that dilution decreases concentration which decreases absorbance.

---

### Part D — Effect of Measuring at 650 nm Instead of 559 nm
*Topic: Unit 1 — Spectrophotometry / λmax gives maximum absorbance; off-peak wavelength gives lower absorbance*
**Question:** Absorbance at 650 nm vs. 559 nm — greater, less, or equal?

**Answer:**
**Less than** at 559 nm.

559 nm is the **wavelength of maximum absorbance** for phenol red — it is the color of light that phenol red absorbs most strongly. At 650 nm (a different wavelength, farther from the absorption peak), phenol red absorbs less light, so the measured absorbance would be lower.

> [!check] **What earns the point**
> State "less than" AND explain that 559 nm is the wavelength of maximum absorbance / phenol red absorbs less at 650 nm. Must connect to the absorption spectrum concept.

> [!danger] **Trap**
> Confusing the color of the solution with the color of light it absorbs. Phenol red is red — it absorbs its complementary color (green, ~559 nm). At 650 nm (red light), less is absorbed because red light is transmitted, not absorbed.

---

## Quick-Reference Summary

| Q | Topic | Key Concept |
|---|---|---|
| 1A | Redox | O₂ reduced: 0 → −2 |
| 1B | Gas Law | PV=nRT, T in Kelvin |
| 1F | IMF | H-bonding: need O–H, N–H, or F–H |
| 1G | Le Chatelier | Exothermic → lower T; fewer gas moles → higher P |
| 2Bi | Energy diagram | Exothermic = products lower PE |
| 2Bii | Catalyst | Lowers Ea ONLY — same ΔH |
| 2E | Kinetics | Zeroth order = constant rate = equal Δmass per interval |
| 3A | Lewis | SO₃ = 24 e⁻, 3 resonance structures |
| 3B | VSEPR | 3 bonding + 0 LP = trigonal planar |
| 3C | Thermodynamics | ΔH>0, ΔS>0 → favored at high T |
| 4B | Titration | Strong acid: starts lower pH, equiv. at pH 7 |
| 4C | Buffer | Requires weak acid + conjugate base — strong acid can't buffer |
| 5B | Electrochemistry | E°cell = E°cathode − E°anode; never multiply E° by n |
| 5C | ΔG° | ΔG° = −nFE°; n = total electrons transferred |
| 6A | Phase change | Melting = endothermic, surroundings → system |
| 7A | pH | [H⁺] = 10^−pH |
| 7C | Beer-Lambert | A = εlc; dilution halves A |
| 7D | Spectroscopy | Use λ_max for maximum sensitivity |
