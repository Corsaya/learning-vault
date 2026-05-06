# AP Chem — Unit 9 Examples: Thermodynamics & Electrochemistry

---

## Topic 9.1: Introduction to Entropy (S)

**Predicting Signs of ΔS — Key Examples:**

| Reaction | ΔS Sign | Reason |
|---|---|---|
| CO₂(s) → CO₂(g) | Positive | Solid to gas |
| HCl(g) + NH₃(g) → NH₄Cl(s) | Negative | Gas to solid |
| Pb²⁺(aq) + 2Cl⁻(aq) → PbCl₂(s) | Negative | Aqueous to solid |
| CaCO₃(s) → CaO(s) + CO₂(g) | Positive | Gas produced from solid |
| 2SO₂(g) + O₂(g) → 2SO₃(g) | Negative | 3 moles gas → 2 moles gas |
| N₂(g) + 3H₂(g) → 2NH₃(g) | Negative | 4 moles gas → 2 moles gas |

---

## Topic 9.2: Calculating Entropy Change (ΔS°)

**Formula:** $\Delta S°_{rxn} = \sum S°(\text{products}) - \sum S°(\text{reactants})$

Always multiply each $S°$ value by its stoichiometric coefficient.

**Example — Coal/Steam Reaction:** $\ce{C(s) + H2O(g) -> CO(g) + H2(g)}$

| Substance | S° (J/mol·K) |
|---|---|
| C(s) | 5.7 |
| H₂O(g) | 188.8 |
| CO(g) | 197.6 |
| H₂(g) | 130.7 |

$$\Delta S°_{rxn} = [197.6 + 130.7] - [5.7 + 188.8] = 328.3 - 194.5 = \mathbf{+133.8\ J/mol \cdot K}$$

Confirmed by logic: solid + gas → two gases = entropy increase ✓

**Algebraic Rearrangement — Solving for Unknown S°:**

Given $\Delta S°_{rxn} = +133.8$ J/mol·K and all values except $S°(H_2)$:

$$133.8 = [197.6 + x] - [5.7 + 188.8]$$
$$133.8 = [197.6 + x] - 194.5$$
$$328.3 = 197.6 + x$$
$$x = 130.7\ \text{J/mol·K} \leftarrow S°(\ce{H2})$$

**Example — Solving for S° When Stoichiometric Coefficients Apply (MCQ pattern):**

$\ce{Se(s) + 3F2(g) -> SeF6(g)}$, $\Delta S°_{rxn} = -337$ J/(mol·K). $S°$: Se(s) = 42, SeF₆(g) = 314 J/(mol·K). Find $S°(\ce{F2})$.

Set up: $\Delta S°_{rxn} = S°(\text{products}) - S°(\text{reactants})$

$$-337 = [314] - [42 + 3 \cdot S°(\ce{F2})]$$
$$-337 = 314 - 42 - 3 \cdot S°(\ce{F2})$$
$$3 \cdot S°(\ce{F2}) = 314 - 42 + 337 = 609$$
$$S°(\ce{F2}) = \mathbf{203\ \text{J/(mol·K)}}$$

> **Key move:** The coefficient 3 in front of F₂ divides the total entropy contribution — must solve for S° per mole. The AP MCQ form is: $S°(\ce{F2}) = -\frac{1}{3}[-337 - 314 + 42]$.

**Example — Largest ΔS° from Table (MCQ pattern):**

From S° values: C(s) = 6, CO(g) = 198, CO₂(g) = 214, CH₄(g) = 186, C₂H₆(g) = 229, H₂(g) = 131, O₂(g) = 205 J/(mol·K):

| Reaction | Calculation | ΔS° |
|---|---|---|
| 2C(s) + O₂(g) → 2CO(g) | 2(198) − [2(6) + 205] | **+179** J/(mol·K) ← largest |
| C(s) + O₂(g) → CO₂(g) | 214 − [6 + 205] | +3 J/(mol·K) |
| C(s) + 2H₂(g) → CH₄(g) | 186 − [6 + 2(131)] | −82 J/(mol·K) |
| 2C(s) + 3H₂(g) → C₂H₆(g) | 229 − [2(6) + 3(131)] | −176 J/(mol·K) |

> **Key move:** Reactions converting gas → gas (with same mol gas) have small ΔS°. The biggest gain comes from converting solid to gas (or increasing moles of gas).

---

## Topic 9.2b: Bond Enthalpy Calculation

**Formula:** $\Delta H°_{rxn} = \sum(\text{bonds broken}) - \sum(\text{bonds formed})$

**Example — Haber Process, solving for N≡N bond enthalpy:**

$$\ce{N2(g) + 3H2(g) -> 2NH3(g)}, \quad \Delta H° = -92.2\ \text{kJ/mol}$$

| Bond | Average Enthalpy (kJ/mol) |
|---|---|
| N−H | 391 |
| H−H | 436 |
| N≡N | ? |

Bonds broken: $1(\ce{N≡N}) + 3(\ce{H-H}) = x + 3(436) = x + 1308$

Bonds formed: $2\ \ce{NH3} \times 3\ \ce{N-H}\ \text{per molecule} = 6(391) = 2346$

$$-92.2 = (x + 1308) - 2346$$
$$x = -92.2 + 1038 = \mathbf{945.8\ kJ/mol}$$

Literature value ≈ 945 kJ/mol ✓

> **Critical:** 2 NH₃ has **6** N−H bonds, not 2. Missing this is the #1 error on bond enthalpy FRQs.

---

## Topic 9.3: Thermodynamic Favorability and ΔG

**Formula:** $\Delta G = \Delta H - T\Delta S$

A reaction is **thermodynamically favored** when $\Delta G < 0$.

**The Four-Quadrant Table:**

| ΔH | ΔS | Favored? | Driven by |
|---|---|---|---|
| Negative | Positive | Always | Both |
| Positive | Negative | Never | Neither |
| Positive | Positive | High T only | Entropy |
| Negative | Negative | Low T only | Enthalpy |

**Example 1 — Coal/Steam (+ΔH, +ΔS quadrant):**

$\ce{C(s) + H2O(g) -> CO(g) + H2(g)}$: ΔH = +131 kJ/mol, ΔS = +0.134 kJ/mol·K

$$\Delta G = 131 - (298)(0.134) = 131 - 39.9 = \mathbf{+91.1\ kJ/mol} \rightarrow \text{Not favored at 298 K}$$

Threshold temperature:

$$T = \frac{\Delta H}{\Delta S} = \frac{131}{0.134} = \mathbf{978\ K}$$

Above 978 K the reaction becomes thermodynamically favored.

> ⚠️ **Unit Warning:** ΔS was already in kJ/mol·K here. If given in J/mol·K, divide by 1000 first.

**Example 2 — Haber Process (−ΔH, −ΔS quadrant):**

$\ce{N2(g) + 3H2(g) <=> 2NH3(g)}$: ΔH° = −92.2 kJ/mol, ΔS° = −198.8 J/mol·K = −0.1988 kJ/mol·K

$$\Delta G° = -92.2 - (298)(-0.1988) = -92.2 + 59.2 = \mathbf{-33.0\ kJ/mol} \rightarrow \text{Favored at 298 K}$$

Threshold:

$$T = \frac{-92.2}{-0.1988} = \mathbf{464\ K}$$

Above 464 K, ΔG° > 0 (unfavored). Industrial Haber runs at ~700 K despite being thermodynamically unfavored — relies on Le Chatelier shifts (product removal) to produce NH₃.

**Example 3 — Lead(II) Chloride precipitation (using ΔG°f values):**

$\ce{Pb^2+(aq) + 2Cl^-(aq) -> PbCl2(s)}$

$$\Delta G° = (-314.1) - [(-24.4) + 2(-131.2)] = -314.1 - (-286.8) = \mathbf{-27.3\ kJ/mol} \rightarrow \text{Favored}$$

**Example 4 — ΔG°rxn from ΔG°f with all gas-phase species (MCQ pattern):**

$\ce{NH3(g) + 3F2(g) -> NF3(g) + 3HF(g)}$

| Compound | $\Delta G°_f$ (kJ/mol) |
|---|---|
| NH₃(g) | −16 |
| F₂(g) | 0 (element in standard state) |
| NF₃(g) | −91 |
| HF(g) | −280 |

$$\Delta G°_{rxn} = [(-91) + 3(-280)] - [(-16) + 0] = [-91 - 840] - [-16] = -931 + 16 = \mathbf{-915\ \text{kJ/mol}}$$

$\Delta G° \ll 0$ → strongly thermodynamically favored. Note: 4 mol gas → 4 mol gas, so $\Delta S° \approx 0$. The driving force is entirely enthalpic: the H−F bond (reflected in $\Delta G°_f(\text{HF}) = -280$ kJ/mol) is extremely stable.

**Example 5 — Threshold Temperature (tungsten melting, MCQ pattern):**

$\ce{W(s) -> W(l)}$, $\Delta H°_{fus} = 35\ \text{kJ/mol}$, $\Delta S°_{fus} = 10\ \text{J/(mol·K)} = 0.010\ \text{kJ/(mol·K)}$

Threshold (melting point): $T = \Delta H / \Delta S = 35/0.010 = \mathbf{3500\ K}$

At T = 3723 K:
$$\Delta G = 35 - (3723)(0.010) = 35 - 37.23 = \mathbf{-2.23\ \text{kJ/mol}} < 0 \rightarrow \text{melts}$$

Since T (3723 K) > T_threshold (3500 K), the entropy term dominates and melting is favorable. The condition: **T > ΔH/ΔS → favored; T < ΔH/ΔS → not favored** for a +ΔH, +ΔS process.

---

## Topics 9.4–9.5: Kinetic Control and Equilibrium

**Key Distinction:**
- Thermodynamics → tells you **if** a reaction will happen (ΔG, K)
- Kinetics → tells you **how fast** it happens (Eₐ, collision frequency)

**Example 1 — Haber Process Kinetic Control:**

At 298 K: ΔG° = −33.0 kJ/mol (favored) AND K ≈ 6 × 10⁵ (huge), yet the reaction is not observed. The N≡N triple bond has a bond enthalpy of ~946 kJ/mol, creating a massive $E_a$. Very few N₂−H₂ collisions at 298 K have enough kinetic energy to break that bond. This is the archetypal AP example of kinetic control.

**Example 2 — Calculating K from ΔG° (Haber at 298 K):**

$$\Delta G° = -33.0\ \text{kJ/mol} = -33{,}000\ \text{J/mol}$$
$$\ln K = \frac{-\Delta G°}{RT} = \frac{33{,}000}{(8.314)(298)} = 13.32$$
$$K = e^{13.32} \approx \mathbf{6.1 \times 10^5}$$

Products heavily favored at equilibrium ✓

**Example 3 — Calculating ΔG° from K (Haber at 773 K):**

$$K = 0.018 \text{ at 773 K}$$
$$\Delta G° = -RT\ln K = -(8.314)(773)\ln(0.018) = \mathbf{+25.8\ kJ/mol} \rightarrow \text{Not favored at high T}$$

**Q vs K — Le Chatelier in industrial Haber:**

Continuously condensing/removing NH₃ keeps $Q_p < K_p$, forcing the forward reaction to continue producing NH₃ even at 700 K where K is small.

---

## Topic 9.6: Free Energy of Dissolution

A substance is soluble if $\Delta G < 0$ for dissolution.

$\Delta H_{solution} = \Delta H_{lattice} + \Delta H_{hydration}$

| Substance | ΔH (kJ/mol) | ΔS | ΔG (kJ/mol) | Soluble? | Driven by |
|---|---|---|---|---|---|
| KCl | +17.1 (endo) | Positive (+76.4 J/mol·K) | −5.3 | Yes | Entropy |
| CaCl₂ | −81.4 (exo) | Negative | Negative | Yes | Enthalpy |
| Ag₂CrO₄ | +61.7 (endo) | Negative | +106.3 | No | Neither |
| BaSO₄ | — | — | +56.8 | No | Neither |
| FeCl₃ | Must be exo | Negative | Negative | Yes | Enthalpy |

**Key Insight on FeCl₃:** ΔS is negative but it's still soluble — the only way that works is if ΔH is large and negative (strongly exothermic) enough to make ΔG negative.

---

## Topic 9.7: Coupled Reactions

**Example 1 — Iron Ore Smelting (Fe₂O₃ + CO):**

| Equation | Reaction | ΔG° |
|---|---|---|
| Eqn 1 | $\ce{Fe2O3(s) -> 2Fe(s) + 3/2 O2(g)}$ | +742.2 kJ |
| Eqn 2 | $\ce{CO(g) + 1/2 O2(g) -> CO2(g)}$ | −283.5 kJ |
| **Target** | $\ce{Fe2O3(s) + 3CO(g) -> 2Fe(s) + 3CO2(g)}$ | ? |

Common intermediate: O₂. Multiply Eqn 2 × 3:

$$\text{Eqn 2*: } 3\ce{CO(g)} + \frac{3}{2}\ce{O2(g)} \rightarrow 3\ce{CO2(g)} \quad \Delta G° = 3(-283.5) = -850.5\ \text{kJ}$$

$$\Delta G°_{overall} = +742.2 + (-850.5) = \boxed{-108.3\ \text{kJ}}$$

Overall reaction is thermodynamically favorable ($\Delta G° < 0$) ✓

> **FRQ answer for "why suitable for coupling":** "These two reactions share a common intermediate (O₂), and when coupled, yield an overall reaction with a negative free energy change (ΔG° < 0)."

**Example 2 — Zinc Sulfide Decomposition:**

| Equation | Reaction | ΔG° |
|---|---|---|
| Eqn 1 | $\ce{ZnS(s) -> Zn(s) + S(s)}$ | +198.3 kJ |
| Eqn 2 | $\ce{S(s) + O2(g) -> SO2(g)}$ | −300.1 kJ |
| **Target** | $\ce{ZnS(s) + O2(g) -> Zn(s) + SO2(g)}$ | ? |

Common intermediate: S(s). Equations already scale 1:1.

$$\Delta G°_{overall} = +198.3 + (-300.1) = \boxed{-101.8\ \text{kJ}}$$

> **FRQ answer:** "These two reactions share a common intermediate (S), and when coupled, yield an overall reaction with a negative free energy change (ΔG° < 0)."

---

## Topic 9.8: Galvanic and Electrolytic Cells

**Reference Example — Mg–Cu Galvanic Cell:**

$$\ce{Mg(s) + Cu^2+(aq) -> Mg^2+(aq) + Cu(s)}$$

| Half-Cell | Electrode | Solution | E° (V) |
|---|---|---|---|
| Anode (oxidation) | Mg | Mg(NO₃)₂ — 1 M | −2.37 V |
| Cathode (reduction) | Cu | Cu(NO₃)₂ — 1 M | +0.34 V |
| Salt bridge | — | KNO₃ or NaCl | — |

$$E°_{cell} = +0.34 - (-2.37) = \mathbf{+2.71\ V}$$

Mg anode loses mass; Cu cathode gains mass.

**Electrolysis of Water:**

$$\text{Cathode: } 2H_2O + 2e^- \rightarrow H_2(g) + 2OH^-$$
$$\text{Anode: } 2H_2O \rightarrow O_2(g) + 4H^+ + 4e^-$$

External power source required because $\Delta G° > 0$ for decomposing water.

---

## Topic 9.9: Cell Potential and Free Energy

**The Thermodynamic Triangle:**

$$E°_{cell} \xleftrightarrow{\Delta G° = -nFE°} \Delta G° \xleftrightarrow{\Delta G° = -RT\ln K} K$$

**Example 1 — Calculating ΔG° for the Mg–Cu cell:**

Half-reactions:
- Anode: $\ce{Mg(s) -> Mg^2+(aq) + 2e^-}$
- Cathode: $\ce{Cu^2+(aq) + 2e^- -> Cu(s)}$
- $n = 2$ electrons transferred

$$E°_{cell} = +0.34 - (-2.37) = +2.71\ \text{V}$$
$$\Delta G° = -nFE°_{cell} = -(2)(96{,}485)(2.71) = -523{,}190\ \text{J/mol} = \mathbf{-523\ \text{kJ/mol}}$$

Highly spontaneous ✓

**Example 2 — Calculating K from E° (Zn–Cu cell):**

$\ce{Zn(s) + Cu^2+(aq) -> Zn^2+(aq) + Cu(s)}$, $E°_{cell} = +1.10$ V, $n = 2$

$$\Delta G° = -(2)(96{,}485)(1.10) = -212{,}267\ \text{J/mol}$$
$$\ln K = \frac{-\Delta G°}{RT} = \frac{212{,}267}{(8.314)(298)} = 85.7$$
$$K = e^{85.7} \approx \mathbf{10^{37}}$$

Reaction is essentially irreversible — goes to completion ✓

**Example 3 — Finding E° from ΔG° (reverse problem):**

Given $\Delta G° = -150\ \text{kJ/mol}$ for a cell reaction with $n = 3$:

$$E°_{cell} = \frac{-\Delta G°}{nF} = \frac{150{,}000\ \text{J}}{(3)(96{,}485)} = \mathbf{+0.518\ V}$$

**Example 4 — Fuel Cell: E°_red(cathode) from ΔG°_rxn (MCQ pattern):**

$\ce{2H2(g) + O2(g) -> 2H2O(l)}$, $\Delta G°_{rxn} = -474\ \text{kJ/mol}$

Half-reactions:
- Cathode: $\ce{O2(g) + 4H+(aq) + 4e- -> 2H2O(l)}$, $E°_{red} = ?$
- Anode: $\ce{2H+(aq) + 2e- -> H2(g)}$, $E°_{red} = 0.00\ \text{V}$ (SHE)

Step 1: Identify $n$. The overall balanced reaction transfers 4 electrons (4H⁺ + 4e⁻ → 2H₂; scaled from anode ×2 to match cathode).

Step 2: $E°_{cell} = \frac{-\Delta G°}{nF} = \frac{474{,}000\ \text{J}}{(4)(96{,}500\ \text{C/mol})} = \mathbf{+1.23\ V}$

Step 3: $E°_{cell} = E°_{cathode} - E°_{anode} = E°_{cathode} - 0.00$

$$E°_{cathode} = +1.23\ \text{V}$$

AP MCQ form: $E°_{red}(\text{cathode}) = -\!\left(\frac{-474{,}000}{4 \times 96{,}500}\right)$ — double negative because $E° = -\Delta G°/(nF)$ and $\Delta G°$ is negative.

**Example 5 — Comparing cell modifications for greatest increase in E°cell (MCQ pattern):**

Current cell: Pb/Pb(NO₃)₂ || Cu/Cu(NO₃)₂, $E°_{cell} = 0.34 - (-0.13) = +0.47\ \text{V}$

Available half-reactions: Ag⁺/Ag = +0.80 V; Cu²⁺/Cu = +0.34 V; Pb²⁺/Pb = −0.13 V; Al³⁺/Al = −1.66 V

| Modification | New $E°_{cell}$ | Change |
|---|---|---|
| Replace Cu cathode with Ag | $0.80 - (-0.13) = +0.93\ \text{V}$ | +0.46 V |
| Replace Pb anode with Al | $0.34 - (-1.66) = +2.00\ \text{V}$ | **+1.53 V** ← greatest |

Replacing the Pb anode with Al gives the greatest increase because Al has a much more negative $E°_{red}$, making it a much stronger reducing agent (more easily oxidized). The cathode choice matters too, but the anode replacement here dominates.

> **Key move:** Always calculate $E°_{cathode} - E°_{anode}$ for each option. Never multiply E° by moles.

---

## Topic 9.10: Cell Potential Under Nonstandard Conditions

**Nernst Equation at 25°C:**

$$E_{cell} = E°_{cell} - \frac{0.0592}{n}\log Q$$

**Example 1 — Zn–Cu cell with nonstandard concentrations:**

$\ce{Zn(s) + Cu^2+(aq) -> Zn^2+(aq) + Cu(s)}$, $E°_{cell} = +1.10$ V, $n = 2$

Conditions: $[\ce{Zn^2+}] = 0.10$ M, $[\ce{Cu^2+}] = 1.0$ M

$$Q = \frac{[\ce{Zn^2+}]}{[\ce{Cu^2+}]} = \frac{0.10}{1.0} = 0.10$$

$$E_{cell} = 1.10 - \frac{0.0592}{2}\log(0.10) = 1.10 - (0.0296)(-1) = 1.10 + 0.030 = \mathbf{+1.13\ V}$$

$Q < 1$ → $\log Q < 0$ → subtracting a negative adds to $E°$ → cell is more spontaneous than standard ✓

**Example 2 — Qualitative reasoning (no calculation):**

A Zn–Cu galvanic cell operates. As the reaction proceeds:
- $[\ce{Zn^2+}]$ increases (anode product)
- $[\ce{Cu^2+}]$ decreases (cathode reactant)
- $Q = [\ce{Zn^2+}]/[\ce{Cu^2+}]$ increases
- $E_{cell}$ decreases toward zero
- At equilibrium: $Q = K$, $E_{cell} = 0$ (dead battery)

**Example 4 — Nernst when a product ion precipitates (MCQ pattern — E increases):**

Cell: $\ce{Zn(s) + 2Ag+(aq) -> Zn^2+(aq) + 2Ag(s)}$, $E°_{cell} = +1.56\ \text{V}$

KNO₃ salt bridge is replaced with KOH. In the Zn half-cell, OH⁻ ions cause Zn(OH)₂(s) to precipitate:

$$Q = \frac{[\ce{Zn^2+}]}{[\ce{Ag+}]^2}$$

As Zn(OH)₂ precipitates, $[\ce{Zn^2+}]$ decreases → Q decreases → $\ln Q$ decreases (becomes more negative).

By Nernst: $E_{cell} = E°_{cell} - \frac{RT}{nF}\ln Q$

Subtracting a more negative value → $E_{cell}$ **increases** above $E°_{cell}$.

This is the less-intuitive direction: removing a product (Zn²⁺ precipitates) drives the forward reaction harder → more spontaneous → higher voltage.

**Example 5 — Increasing [reactant] above 1 M:**

Cell: $\ce{Ni^2+(aq) + Cd(s) -> Ni(s) + Cd^2+(aq)}$, $E°_{cell} = +0.15\ \text{V}$

$Q = [\ce{Cd^2+}]/[\ce{Ni^2+}]$ (Cd²⁺ = product, Ni²⁺ = reactant)

If $[\ce{Ni^2+}] = 2.0\ \text{M}$, $[\ce{Cd^2+}] = 1.0\ \text{M}$:
$$Q = \frac{1.0}{2.0} = 0.50 < 1$$

$E_{cell} = 0.15 - \frac{0.0592}{2}\log(0.50) = 0.15 - (0.0296)(-0.301) = 0.15 + 0.0089 = \mathbf{+0.159\ \text{V}} > E°_{cell}$ ✓

Increasing [reactant] → Q < 1 → forward reaction is more favorable than standard → $E_{cell} > E°_{cell}$.

**Example 3 — Concentration cell:**

Two Cu electrodes: cathode $[\ce{Cu^2+}] = 2.0$ M; anode $[\ce{Cu^2+}] = 0.010$ M. $E° = 0$ V (same half-reactions).

$$Q = \frac{[\ce{Cu^2+}]_{anode}}{[\ce{Cu^2+}]_{cathode}} = \frac{0.010}{2.0} = 0.005$$

$$E_{cell} = 0 - \frac{0.0592}{2}\log(0.005) = -(0.0296)(-2.30) = \mathbf{+0.068\ V}$$

Spontaneous despite $E° = 0$ — driven entirely by concentration difference ✓

---

## Topic 9.11: Electrolysis and Faraday's Law

**The Chain:** seconds → coulombs → moles e⁻ → moles substance → grams

**Example 1 — Mass of Cu deposited from CuSO₄(aq):**

Given: $I = 3.00$ A, $t = 2.00$ hours, $\ce{Cu^2+ + 2e^- -> Cu}$, $M_{Cu} = 63.55$ g/mol

Step 1: Convert time: $2.00 \times 3600 = 7200\ \text{s}$

Step 2: $q = It = (3.00)(7200) = 21{,}600\ \text{C}$

Step 3: $n_e = q/F = 21{,}600/96{,}485 = 0.2238\ \text{mol}\ e^-$

Step 4: $n_{Cu} = 0.2238 / 2 = 0.1119\ \text{mol Cu}$ (2 electrons per Cu²⁺)

Step 5: $m = 0.1119 \times 63.55 = \mathbf{7.11\ \text{g Cu}}$

**Example 2 — Time required to deposit a given mass of Al:**

Given: $I = 10.0$ A, target mass = 0.175 g Al, $\ce{Al^3+ + 3e^- -> Al}$, $M_{Al} = 26.98$ g/mol

Step 1: $n_{Al} = 0.175/26.98 = 0.006486\ \text{mol Al}$

Step 2: $n_e = 0.006486 \times 3 = 0.01946\ \text{mol}\ e^-$ (3 electrons per Al³⁺)

Step 3: $q = n_e \times F = 0.01946 \times 96{,}485 = 1877\ \text{C}$

Step 4: $t = q/I = 1877/10.0 = \mathbf{188\ \text{s}}$

**Example 3 — Moles of electrons from current and time:**

$I = 2.50$ A, $t = 45.0\ \text{min} = 2700\ \text{s}$

$$q = (2.50)(2700) = 6750\ \text{C}$$
$$n_e = 6750/96{,}485 = \mathbf{0.0700\ \text{mol}\ e^-}$$

**Example 4 — Comparing two metals under same current/time:**

At the same current for the same time, the same number of moles of electrons flows. To deposit the same number of moles of Au (Au³⁺ + 3e⁻ → Au) vs. Ag (Ag⁺ + e⁻ → Ag), three times as many electrons are needed for Au. Therefore, three times the current (or three times the time) is required to deposit equimolar amounts. This is a classic MCQ trap.

**Common trap — H₂:O₂ ratio in water electrolysis:**

$$\text{Cathode: } 2H_2O + 2e^- \rightarrow H_2 + 2OH^-$$
$$\text{Anode: } 2H_2O \rightarrow O_2 + 4H^+ + 4e^-$$

For every 4 mol e⁻, 2 mol H₂ form at cathode and 1 mol O₂ forms at anode. Mole ratio H₂:O₂ = **2:1**. Volume ratio at same T and P = 2:1.

**Example 5 — Comparing two electroplating setups (MCQ pattern):**

Two spoons are electroplated: Cell 1 uses Ag⁺ (Ag⁺ + e⁻ → Ag, $n = 1$), Cell 2 uses Cd²⁺ (Cd²⁺ + 2e⁻ → Cd, $n = 2$). Both run at $I = 5.00$ A for $t = 600$ s.

Total charge (same for both): $q = It = (5.00)(600) = 3{,}000\ \text{C}$

Moles of electrons: $n_e = 3{,}000/96{,}500 = 0.03109\ \text{mol}\ e^-$

- Ag deposited: $n_{Ag} = 0.03109/1 = 0.03109\ \text{mol}$; $m = 0.03109 \times 107.87 = \mathbf{3.35\ \text{g}}$
- Cd deposited: $n_{Cd} = 0.03109/2 = 0.01555\ \text{mol}$; $m = 0.01555 \times 112.41 = \mathbf{1.75\ \text{g}}$

Ag gains nearly twice the mass of Cd despite similar molar masses — the key variable is $n$ (electrons per ion), not molar mass.

**Example 6 — Finding which setup needs highest current (given moles and time):**

Four objects to plate with 0.10 mol metal each:

| Object | Metal | $n$ | Time | Charge needed | Current |
|---|---|---|---|---|---|
| 1 | Ag | 1 | 30 min (1800 s) | $0.10 \times 1 \times 96{,}500 = 9{,}650\ \text{C}$ | $9{,}650/1800 = \mathbf{5.36\ \text{A}}$ |
| 2 | Ag | 1 | 60 min (3600 s) | $9{,}650\ \text{C}$ | $9{,}650/3600 = \mathbf{2.68\ \text{A}}$ |
| 3 | Zn | 2 | 30 min (1800 s) | $0.10 \times 2 \times 96{,}500 = 19{,}300\ \text{C}$ | $19{,}300/1800 = \mathbf{10.72\ \text{A}}$ ← highest |
| 4 | Zn | 2 | 60 min (3600 s) | $19{,}300\ \text{C}$ | $19{,}300/3600 = \mathbf{5.36\ \text{A}}$ |

Object 3 needs the most current: it combines the largest charge requirement ($n = 2$) with the shortest time. The reasoning is: coulombs of charge needed and time of operation — not molar mass.
