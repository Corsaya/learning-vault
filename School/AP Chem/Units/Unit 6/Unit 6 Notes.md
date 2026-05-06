# AP Chem — Unit 6 Notes: Thermochemistry
**Exam Weight: 7–9% | Topics: 6.1–6.9**
**Krug Videos:** [6.1 Endothermic/Exothermic](https://youtu.be/Zmhdr-8E1Mo) | [6.2/6.3 Energy Diagrams & Heat Transfer](https://youtu.be/fwe9ApxkxSU) | [6.4 Calorimetry](https://youtu.be/Xn-vRyWu7mI) | [6.5 Phase Changes](https://youtu.be/2IFMaefCIhk) | [6.6a Enthalpy Intro](https://youtu.be/LNPoyiCpLgM) | [6.6b Enthalpy Practice](https://youtu.be/Y97W1aqDcps) | [6.7 Bond Enthalpies](https://youtu.be/z3FziIDJjdk) | [6.8 Enthalpy of Formation](https://youtu.be/PVciNA7tVnM) | [6.9 Hess's Law](https://youtu.be/d0Qlv_uXVvU)

---

## Study Hub Quick Reference — Unit 6

> [!check] Q16 — Bond Enthalpy: ΔH = Σ(broken) − Σ(formed)
> Bonds broken in reactants → endothermic (energy IN, +). Bonds formed in products → exothermic (energy OUT, −). $\Delta H_{rxn} = \Sigma BE_{broken} - \Sigma BE_{formed}$. Negative result = more energy released forming bonds → exothermic. Count each bond × stoichiometric coefficient; don't forget to multiply by coefficients in the balanced equation.

> [!check] Q18 — Thermochemistry: Mass → Moles → Heat Released
> 1. Convert mass to moles: $n = m/M$
> 2. Divide by stoichiometric coefficient → mol_rxn
> 3. $q = mol_{rxn} \times |\Delta H°|$
> Sign: exothermic reaction has ΔH < 0, but "heat released" is reported as a positive value. Always state direction (released vs. absorbed).

> [!check] Q25 — Avogadro's Law: V ∝ n at Constant T and P
> From $PV = nRT$: at **constant T and P**, $V = (RT/P) \times n$ → volume is **directly proportional to moles**. $V_1/n_1 = V_2/n_2$. Double the moles → double the volume. This is Avogadro's Law. Use R = 0.08206 L·atm/mol·K; T must be in Kelvin.

> [!check] Q46 — Calorimetry: Minimum Data Needed for q = mcΔT
> To calculate $q = mc\Delta T$ you need ALL THREE: (1) **mass** of solution in grams, (2) **specific heat capacity** c (given, or assume 4.18 J/g·°C for dilute aqueous solutions), (3) **ΔT** = T_final − T_initial. Without all three, the calculation cannot be completed. Mass alone is never enough.

> [!check] FRQ Q1B — Ideal Gas Law: PV = nRT
> To find moles of gas: $n = PV/RT$. Constants: R = 0.08206 L·atm/mol·K. **T must be in Kelvin** (T(K) = T(°C) + 273). Pressure must be in atm. Volume must be in liters. Rearrange for any variable: $V = nRT/P$, $P = nRT/V$.

> [!check] FRQ Q1D — Thermochemistry: q = mol × ΔH_comb
> $q = n \times \Delta H_{comb}$. First convert mass to moles: $n = m/M$. Then multiply by the molar enthalpy of combustion. If ΔH < 0 (exothermic), the reaction releases heat; report the magnitude |q| as "heat released." Include units (kJ or J) in final answer.

> [!check] FRQ Q1E — Calorimetry: Solve for T_final
> $q_{rxn} = -q_{cal} = -(m)(c)(T_f - T_i)$. Rearrange: $T_f = T_i - q_{rxn}/(mc)$. For an exothermic reaction ($q_{rxn} < 0$), $T_f > T_i$ (solution warms). For endothermic ($q_{rxn} > 0$), $T_f < T_i$ (solution cools). The negative sign in $q_{rxn} = -q_{cal}$ is critical.

> [!check] FRQ Q2B(i) — Energy Diagrams: Exothermic = Products at Lower PE
> In an exothermic reaction, **products** are at **lower potential energy** than reactants (ΔH < 0). The energy diagram shows the product plateau **below** the reactant plateau. Activation energy Ea is measured from **reactants to the peak**, not from products. Surroundings warm in exothermic reactions.

> [!check] FRQ Q6B — Phase Change: q = n × ΔH_fus
> $q = n \times \Delta H_{fus}$. First convert grams to moles: $n = m/M$. Then multiply by ΔH_fus (in kJ/mol). Temperature is **constant** during melting — do NOT use $q = mc\Delta T$ here. The flat plateau on a heating curve = melting at constant T.

> [!warning] Trap — Phase Transition: Use q = nΔH, NOT mcΔT
> During melting or boiling (flat plateau on heating curve), temperature is **constant**. Energy goes into breaking IMFs (PE increases), not KE (T constant). Use $q = n\Delta H_{fus}$ or $q = n\Delta H_{vap}$ — NOT $q = mc\Delta T$.

> [!danger] q_rxn = −q_cal: Opposite Signs
> What the reaction releases, the calorimeter gains. If solution temperature rises ($q_{cal} > 0$), then $q_{rxn} < 0$ (exothermic reaction). Never give both the same sign.

> [!danger] ΔH°_f = 0 for ALL Elements in Standard State
> O₂(g), H₂(g), N₂(g), C(graphite), Na(s), Fe(s) all have $\Delta H°_f = 0$ **by definition**. Never assign a nonzero formation enthalpy to an element in its standard state.

---

## Topic 6.1: Endothermic and Exothermic Processes

**Essential Knowledge (Farabaugh CED):**
- A chemical or physical process is **exothermic** when the system releases energy to the surroundings — the surrounding temperature **increases**. $\Delta H < 0$.
- A chemical or physical process is **endothermic** when the system absorbs energy from the surroundings — the surrounding temperature **decreases**. $\Delta H > 0$.
- The classification (endo vs. exo) is always from the **reaction's** perspective, not the surroundings'. A rising thermometer in the solution means the **reaction** released heat (exothermic) — the surroundings gained it.
- Energy is conserved: $q_{\text{rxn}} = -q_{\text{surroundings}}$. What the system loses, the surroundings gain, and vice versa.
- Common exothermic processes: combustion, neutralization, most precipitation reactions, condensation, freezing.
- Common endothermic processes: dissolving $\text{NH}_4\text{NO}_3$, melting, vaporization, photosynthesis, decomposition of $\text{CaCO}_3$.

**Key Thermochemistry Vocabulary:**
- **System:** the chemical reaction or process under study.
- **Surroundings:** everything outside the system (solution, calorimeter, etc.).
- **Enthalpy ($H$):** a thermodynamic state function representing total heat content at constant pressure. $\Delta H = H_{\text{products}} - H_{\text{reactants}}$.
- **Enthalpy change ($\Delta H$):** heat transferred at constant pressure.

**Temperature-Change Diagnostic:**

| Observation | Interpretation |
|---|---|
| Solution temperature **rises** | Surroundings gained heat → system released heat → **Exothermic** ($\Delta H < 0$) |
| Solution temperature **falls** | Surroundings lost heat → system absorbed heat → **Endothermic** ($\Delta H > 0$) |

---

## Topic 6.2: Energy Diagrams

**Essential Knowledge (Farabaugh CED):**
- An energy diagram (reaction profile) plots **potential energy** of the system vs. **reaction progress** (not time).
- **Activation energy ($E_a$):** the minimum energy required for reactants to reach the transition state. Always positive. Equals the height of the energy "hill" above the reactants' level.
- **Transition state (TS‡):** the highest-energy point on the diagram — an unstable, transient species, not an intermediate. Cannot be isolated.
- **$\Delta H$** is read from the diagram as $E(\text{products}) - E(\text{reactants})$ — the height difference between reactant and product plateaus, not the peak.

**Reading a Two-Step (Multistep) Profile:**
- Each "hump" = one transition state; each "valley" between humps = one **intermediate** (can be isolated, unlike TS‡).
- The **rate-determining step** corresponds to the hump with the **largest $E_a$** measured from the preceding energy minimum, not the highest absolute energy.
- A catalyst lowers $E_a$ without changing $\Delta H$ (the reactant and product energy levels stay the same).

![[enthalpy_diagram_u6.svg|697]]
*Exothermic (left): products at lower energy, $\Delta H < 0$, surroundings warm. Endothermic (right): products at higher energy, $\Delta H > 0$, surroundings cool. $E_a$ is always measured from reactants to peak.*

**Comparing Exothermic vs. Endothermic on a Diagram:**

| Feature | Exothermic | Endothermic |
|---|---|---|
| Product energy level | **Lower** than reactants | **Higher** than reactants |
| $\Delta H$ sign | Negative ($< 0$) | Positive ($> 0$) |
| Surroundings effect | Temperature rises | Temperature falls |
| Reverse reaction | Endothermic | Exothermic |

**Catalyst Effect on Energy Diagram:**
- Catalyst provides an **alternative pathway** with a lower $E_a$.
- The diagram shows a lower, different-shaped peak — but the reactant and product energy levels are **unchanged**.
- $\Delta H$ is the same with or without a catalyst.

---

## Topic 6.3: Heat Transfer and Thermal Equilibrium

**Essential Knowledge (Farabaugh CED):**
- Thermal energy (heat) flows spontaneously from **higher temperature** to **lower temperature** — from higher average kinetic energy particles to lower average kinetic energy particles, via **molecular collisions at the boundary**.
- The direction of heat flow is determined solely by **temperature** (average KE), not by mass, volume, or number of moles. A small hot object heats a large cold one, not the other way around.
- **Thermal equilibrium:** when two objects in contact reach the same temperature, net heat transfer stops. At equilibrium, all particles share the same average kinetic energy.
- When two samples at different temperatures are mixed, the final equilibrium temperature lies **between** the two initial temperatures (conservation of energy).

**Mechanism of Heat Transfer:**
- At the interface between a hot solid and cooler liquid: collisions between higher-KE solid atoms and lower-KE liquid molecules transfer kinetic energy from hot to cold.
- This is purely **physical** (conduction/convection) — no chemical bonds are broken. Distinct from a chemical reaction releasing energy.

**Key Rule:**
$$q_{\text{lost by hot}} = -q_{\text{gained by cold}}$$

The final equilibrium temperature can be calculated:
$$m_1 c_1 (T_f - T_1) = -m_2 c_2 (T_f - T_2)$$
where $T_1 > T_f > T_2$ must hold for a physically reasonable answer.

---

## Topic 6.4: Heat Capacity and Calorimetry

**Essential Knowledge (Krug 6.4, Farabaugh CED):**
- **Specific heat capacity ($c$):** the amount of heat required to raise 1 gram of a substance by $1\ °\text{C}$ (or 1 K). Units: $\text{J/g·°C}$. Intensive property (independent of sample size).
- **Heat capacity ($C$):** the amount of heat required to raise the entire object by $1\ °\text{C}$. Units: $\text{J/°C}$. Extensive (depends on amount). Used for bomb calorimeters.
- Water has an unusually high specific heat: $c(\text{H}_2\text{O}) = 4.184\ \text{J/g·°C}$ (use $4.18$ or $4.2$ if problem specifies). This is why it is used in calorimetry and is a climate moderator.

**Key Equations:**

$$q = mc\Delta T \qquad \text{(sample with specific heat } c\text{)}$$

$$q = C\Delta T \qquad \text{(entire calorimeter with heat capacity } C\text{)}$$

$$q_{\text{rxn}} = -q_{\text{cal}} \qquad \text{(conservation of energy, insulated system)}$$

$$\Delta H = \frac{q_{\text{rxn}}}{n_{\text{rxn}}} \qquad \text{(divide by moles of limiting reagent)}$$

where $\Delta T = T_{\text{final}} - T_{\text{initial}}$ (can be positive or negative).

![[calorimetry_u6.svg|697]]
*Coffee cup calorimeter: reaction releases/absorbs heat, solution temperature changes. $q_{\text{rxn}} = -q_{\text{cal}}$ — opposite signs because energy lost by one equals energy gained by the other.*

**Coffee Cup vs. Bomb Calorimeter:**

| Feature | Coffee Cup | Bomb Calorimeter |
|---|---|---|
| Pressure | Constant (open to air) | Constant volume (sealed) |
| Equation | $q = mc\Delta T$ (mass of solution) | $q = C\Delta T$ ($C$ = heat capacity of entire bomb) |
| Measures | $\Delta H$ (enthalpy) | $\Delta E$ (internal energy) — close to $\Delta H$ |
| Use case | Dissolution, neutralization | Combustion reactions |

**Significant Figures in $\Delta T$:**
When reading $\Delta T$ from a thermometer or graph, apply the **subtraction rule**: the result has the same number of decimal places as the least precise reading. If both temperatures are read to $0.5\ °\text{C}$, $\Delta T$ is reported to $0.5\ °\text{C}$ — not extra decimal places.

**Reading $\Delta T$ from a Graph:**
Read the **initial plateau** (before mixing) and the **final plateau** (after equilibration) separately. Use those flat regions, not the peak of a transient spike. $\Delta T = T_{\text{final plateau}} - T_{\text{initial plateau}}$.

---

## Topic 6.5: Energy of Phase Changes

**Essential Knowledge (Krug 6.5, Farabaugh CED):**
- During a **phase transition** (melting, freezing, vaporization, condensation, sublimation, deposition), temperature remains **constant** even though heat is being added or removed. Energy goes into breaking or forming intermolecular forces (potential energy increases/decreases), not into increasing kinetic energy.
- Phase transition enthalpies are always quoted per mole of substance:
  - $\Delta H_{\text{fus}}$: molar enthalpy of fusion (melting). Endothermic ($> 0$).
  - $\Delta H_{\text{vap}}$: molar enthalpy of vaporization. Endothermic ($> 0$).
  - Reverse processes: $\Delta H_{\text{freezing}} = -\Delta H_{\text{fus}}$; $\Delta H_{\text{cond}} = -\Delta H_{\text{vap}}$.
- Vaporization requires far more energy than melting: $\Delta H_{\text{vap}} \gg \Delta H_{\text{fus}}$ for the same substance (gas phase requires near-complete separation of all IMFs; melting only loosens them).

**Key Equations for Phase Transitions:**

$$q = n \cdot \Delta H_{\text{fus}} \qquad \text{(at melting/freezing point)}$$

$$q = n \cdot \Delta H_{\text{vap}} \qquad \text{(at boiling/condensation point)}$$

![[heating_curve_u6.svg|697]]
*Complete heating curve: sloped segments use $q = mc\Delta T$; flat plateaus use $q = n\Delta H$ and have constant $T$. Vaporization plateau is much wider than melting plateau because $\Delta H_{\text{vap}} \gg \Delta H_{\text{fus}}$.*

**Reading the Heating Curve:**

| Segment | What is happening | Equation | Temperature |
|---|---|---|---|
| Slope (solid) | Solid warming | $q = m c_{\text{solid}} \Delta T$ | Increases |
| Flat plateau at $T_{\text{mp}}$ | Melting (IMFs loosening) | $q = n \Delta H_{\text{fus}}$ | Constant |
| Slope (liquid) | Liquid warming | $q = m c_{\text{liquid}} \Delta T$ | Increases |
| Flat plateau at $T_{\text{bp}}$ | Vaporization (IMFs breaking) | $q = n \Delta H_{\text{vap}}$ | Constant |
| Slope (gas) | Gas warming | $q = m c_{\text{gas}} \Delta T$ | Increases |

**Comparing substances by $\Delta H_{\text{vap}}$:**
$\text{H}_2\text{O}$ has a higher $\Delta H_{\text{vap}}$ ($44\ \text{kJ/mol}$) than $\text{H}_2\text{S}$ ($\approx 20\ \text{kJ/mol}$) because water has stronger hydrogen bonding. More energy is needed to fully separate water molecules into the gas phase. Consequently, more moles of $\text{H}_2\text{S}$ must condense to release the same heat as 1 mol $\text{H}_2\text{O}$ condensing.

---

## Topic 6.6: Introduction to Enthalpy of Reaction

**Essential Knowledge (Krug 6.6a/6.6b, Farabaugh CED):**
- The **enthalpy of reaction** ($\Delta H°_{\text{rxn}}$) is the heat transferred per mole of reaction **as written**. It is an extensive quantity — doubling moles doubles $\Delta H$.
- A thermochemical equation includes the state symbols and the $\Delta H$ value:
$$2\ \text{Al}(s) + \text{Fe}_2\text{O}_3(s) \to 2\ \text{Fe}(s) + \text{Al}_2\text{O}_3(s), \quad \Delta H° = -850\ \text{kJ/mol}_{\text{rxn}}$$
- To find heat for a different amount of reactant/product: scale by the mole ratio.

**Stoichiometric Scaling Procedure:**

$$q = \left(\frac{n_{\text{given}}}{n_{\text{stoich}}}\right) \times |\Delta H°|$$

**Step-by-step:**
1. Convert given mass to moles using molar mass.
2. Divide by the stoichiometric coefficient for that species in the balanced equation → mol rxn.
3. Multiply by $|\Delta H°|$ to get heat.
4. Apply sign: positive = released (exothermic) or absorbed (endothermic) based on context.

**Example:** For $2\ \text{Al} + \text{Fe}_2\text{O}_3 \to \ldots$, $\Delta H° = -850\ \text{kJ/mol}_{\text{rxn}}$.
How much heat when $54\ \text{g Al}$ reacts?
$$n_{\text{Al}} = \frac{54\ \text{g}}{27.0\ \text{g/mol}} = 2.00\ \text{mol Al}$$
$$\text{mol rxn} = \frac{2.00\ \text{mol Al}}{2\ \text{mol Al/mol rxn}} = 1.00\ \text{mol rxn}$$
$$q = 1.00 \times 850\ \text{kJ} = 850\ \text{kJ released}$$

**Reverse Reaction:** Reversing a reaction flips the sign of $\Delta H$. If the forward reaction is exothermic, the reverse is endothermic by the same magnitude.

---

## Topic 6.7: Bond Enthalpies

**Essential Knowledge (Krug 6.7, Farabaugh CED):**
- **Bond enthalpy (BE):** the average energy required to break 1 mol of a particular bond in the gas phase. Always positive (breaking bonds is endothermic).
- Breaking bonds absorbs energy; forming bonds releases energy.
- $\Delta H_{\text{rxn}}$ is estimated by comparing total energy in (bonds broken) vs. total energy out (bonds formed):

$$\Delta H_{\text{rxn}} = \Sigma\,\text{BE(bonds broken)} - \Sigma\,\text{BE(bonds formed)}$$

- Bond enthalpies are **average values** — they are the same regardless of the molecule they appear in. This makes the method approximate; standard enthalpies of formation give exact values.
- Only applicable to **gas-phase** reactions. Bond enthalpy values in tables assume gaseous reactants and products.

![[bond_enthalpy_u6.svg|697]]
*Left (red): bonds broken in reactants — energy absorbed. Right (green): bonds formed in products — energy released. Net $\Delta H$ = broken − formed. Methane combustion example: $+2652 - 3454 = -802\ \text{kJ/mol}$.*

**Counting Bonds Correctly:**
- In $\text{CH}_4$: **4** C–H bonds (one per H atom).
- In $\text{CO}_2$: **2** C=O bonds (one on each side of C).
- In $\text{H}_2\text{O}$: **2** O–H bonds.
- For the balanced equation $\text{CH}_4 + 2\ \text{O}_2 \to \text{CO}_2 + 2\ \text{H}_2\text{O}$: broken = $4(\text{C–H}) + 2(\text{O=O})$; formed = $2(\text{C=O}) + 4(\text{O–H})$.
- Multiply bond counts by stoichiometric coefficients from the **balanced** equation.

**Finding an Unknown Bond Enthalpy:**
Given $\Delta H_{\text{rxn}}$ and all other bond enthalpies, rearrange $\Delta H = \Sigma(\text{broken}) - \Sigma(\text{formed})$ and solve for the unknown. The result must be positive (bond enthalpies are always positive).

**Bond Strength Trends:**
- Triple bonds $>$ double bonds $>$ single bonds (same atoms).
- $\text{C}\equiv\text{C}$: ~835 kJ/mol; $\text{C=C}$: ~614 kJ/mol; $\text{C–C}$: ~347 kJ/mol.
- Stronger bonds = shorter bond length.
- For resonance structures (e.g., $\text{O}_3$ with 1.5-order O–O bonds), the bond enthalpy lies **between** the single and double bond values.

---

## Topic 6.8: Enthalpy of Formation

**Essential Knowledge (Krug 6.8, Farabaugh CED):**
- **Standard enthalpy of formation ($\Delta H°_f$):** the enthalpy change when **1 mole** of a compound is formed from its constituent elements in their **standard states** at 298 K and 1 atm.
- Standard state of an element = most stable form at 298 K, 1 atm. Examples: $\text{O}_2(g)$, $\text{H}_2(g)$, $\text{N}_2(g)$, $\text{F}_2(g)$, $\text{Cl}_2(g)$, $\text{Br}_2(l)$, $\text{I}_2(s)$, $\text{Hg}(l)$, $\text{C(graphite)}$, $\text{Na}(s)$, $\text{Fe}(s)$.
- $\Delta H°_f = 0$ for all elements in their standard state by definition.
- $\Delta H°_f$ can be positive (compound is less stable than its elements; formation is endothermic) or negative (compound is more stable; formation is exothermic). Most common compounds have negative $\Delta H°_f$.

**Key Equation:**

$$\Delta H°_{\text{rxn}} = \Sigma\,\Delta H°_f(\text{products}) - \Sigma\,\Delta H°_f(\text{reactants})$$

Apply stoichiometric coefficients from the balanced equation as multipliers. $\Delta H°_f$ is per 1 mol of compound, so it must be scaled.

![[formation_enthalpy_u6.svg|697]]
*Elements in standard state define the $\Delta H°_f = 0$ baseline. Compounds above the line have positive $\Delta H°_f$ (endothermic formation); below the line have negative $\Delta H°_f$ (exothermic formation). $\Delta H°_{\text{rxn}} = \Sigma\Delta H°_f(\text{prod}) - \Sigma\Delta H°_f(\text{react})$.*

**Worked Procedure:**
$$\text{CaCO}_3(s) \to \text{CaO}(s) + \text{CO}_2(g)$$
$$\Delta H°_{\text{rxn}} = [\Delta H°_f(\text{CaO}) + \Delta H°_f(\text{CO}_2)] - [\Delta H°_f(\text{CaCO}_3)]$$
$$= [(-635) + (-394)] - (-1207) = -1029 + 1207 = +178\ \text{kJ/mol}$$

**Why Standard Enthalpies of Formation Are More Accurate Than Bond Enthalpies:**
Bond enthalpies are averaged across many molecules; $\Delta H°_f$ values are measured calorimetrically for the specific compound. $\Delta H°_f$ gives exact $\Delta H°_{\text{rxn}}$ values; bond enthalpy calculations are estimates.

---

## Topic 6.9: Hess's Law

**Essential Knowledge (Krug 6.9, Farabaugh CED):**
- **Hess's Law:** Because enthalpy is a **state function** (depends only on initial and final states, not the path), $\Delta H°_{\text{rxn}}$ for any reaction is the same regardless of whether it occurs in one step or many.
- This means we can **algebraically combine** enthalpy values from known reactions to find $\Delta H°$ for a reaction that is difficult to measure directly.

**The Three Manipulation Rules:**

| Rule | What to do | Effect on $\Delta H$ |
|---|---|---|
| **Reverse** a reaction | Flip reactants and products | Multiply $\Delta H$ by $-1$ |
| **Scale** a reaction | Multiply all coefficients by factor $n$ | Multiply $\Delta H$ by $n$ |
| **Add** reactions | Combine two or more equations | Add their $\Delta H$ values; cancel species on both sides |

![[hess_law_u6.svg|697]]
*Thermodynamic cycle (left): $A \to C$ via $A \to B \to C$ gives the same $\Delta H$ as going directly $A \to C$. Three manipulation rules (right): reverse flips sign, scale multiplies, adding sums and cancels intermediates.*

**Algebraic Strategy:**
1. Write the **target reaction** first.
2. Examine which given reactions contain each species.
3. Arrange each given reaction so its species appear on the correct side (reactant or product) relative to the target. Reverse if needed.
4. Scale each equation so coefficients match the target.
5. Add all equations; cancel species that appear on both sides.
6. Sum all $\Delta H$ values.

**Identifying the "Missing" Reaction:**
When asked what additional data is needed: algebraically subtract all given reactions from the target. The remaining, uncanceled step identifies the missing reaction. The species in that step is what you need $\Delta H°_f$ for.

**Connection to Standard Enthalpies of Formation:**
$\Delta H°_{\text{rxn}} = \Sigma\Delta H°_f(\text{products}) - \Sigma\Delta H°_f(\text{reactants})$ is itself an application of Hess's Law. Each formation reaction ($\text{elements} \to \text{compound}$) is a step in the Hess's cycle.

---

## MCQ Pattern Recognition — Unit 6

| If you see... | It's testing... | Key move |
|---|---|---|
| Temperature of solution **rises** after reaction | Exo/endothermic identification | Rising $T$ in surroundings → system released heat → **exothermic** ($\Delta H < 0$) |
| Temperature of solution **falls** after reaction | Exo/endothermic identification | Falling $T$ → system absorbed heat → **endothermic** ($\Delta H > 0$) |
| "Endo/exo" classification with rising surroundings $T$ | Perspective trap | Classification is from the **reaction's** perspective — rising surroundings $T$ = exothermic reaction |
| Advertisement claiming "draws body's own heat" | Exo/endo mechanism | If heat flows *from* body to warmer → endothermic → body cools, not warms; hand warmer must be exothermic |
| Hot solid dropped in cooler liquid — why does liquid warm? | Thermal equilibration mechanism | Molecular collisions at interface transfer KE from hotter solid to cooler liquid |
| Which direction does heat flow when two samples mix? | Temperature determines direction | Heat flows from **higher $T$ (higher average KE)** to lower $T$ — never from larger mass to smaller |
| Two samples at different $T$ mix — what happens to each? | Thermal equilibrium | Cooler sample's average KE increases; warmer sample's decreases; final $T$ between the two |
| $q = mc\Delta T$ with density given | Unit conversion first | Convert volume (L or mL) to mass using density; $1.00\ \text{g/mL}$ for water |
| $\Delta T$ from reading a graph | Significant figures trap | Apply subtraction rule: decimal places limited by precision of each reading; $\Delta T = T_f - T_i$ |
| $-q_{\text{Al}} = q_{\text{H}_2\text{O}}$ vs. ratio involving mass | Calorimetry sign convention | Verify numerically: $q = mc\Delta T$ for both; ratio should be $\approx 1$ for insulated system |
| Heating curve: temperature stays constant | Phase transition | Flat plateau = melting or boiling — $T$ constant while IMFs break; $q = n\Delta H$ not $mc\Delta T$ |
| Evaporation vs. condensation energy | Reverse process magnitude | $|\Delta H_{\text{vap}}| = |\Delta H_{\text{cond}}|$; they are exact reverses |
| How many moles of substance B condense to equal heat from 1 mol of A condensing? | Mole ratio from $\Delta H_{\text{vap}}$ difference | Set $n \cdot \Delta H_{\text{cond}}(\text{B}) = 1 \cdot \Delta H_{\text{cond}}(\text{A})$; solve for $n$ |
| Heating curve — mole scaling for phase plateau | Proportional scaling | Half the moles → half the energy for the plateau; read $\Delta H_{\text{vap}}$ per mol from curve |
| Given $\Delta H°$ per mol rxn and moles of one species | Stoichiometric scaling | Divide given moles by stoichiometric coefficient → mol rxn; multiply by $|\Delta H°|$ |
| Given mass, asked for heat (thermochemical equation) | Moles → mol rxn → q | Convert g to mol; divide by coefficient; multiply by $|\Delta H°|$ |
| Bond enthalpy — $\Delta H$ from bond table | $\Sigma(\text{broken}) - \Sigma(\text{formed})$ | Count each bond type × stoichiometric coefficient; broken − formed (not the reverse) |
| Bond enthalpy — find unknown bond enthalpy | Algebraic rearrangement | Set up $\Delta H = \Sigma(\text{broken}) - \Sigma(\text{formed})$; let unknown = $x$; solve; answer must be positive |
| Bond enthalpy — ozone O–O bond | Resonance intermediate value | $\text{O}_3$ has 1.5-order bonds; value lies between single (150 kJ/mol) and double (500 kJ/mol) O–O bond enthalpies |
| Standard enthalpy of formation — $\Delta H°_f(\text{O}_2)$ or $\Delta H°_f(\text{H}_2)$ | Element in standard state | $\Delta H°_f = 0$ for all elements in standard state; $\text{O}_2(g)$, $\text{H}_2(g)$, $\text{N}_2(g)$ are all zero |
| $\Delta H°_{\text{rxn}}$ from $\Delta H°_f$ table | Products minus reactants | $\Sigma\Delta H°_f(\text{prod}) - \Sigma\Delta H°_f(\text{react})$; apply coefficients; never reverse |
| $\Delta H°_f$ expression — which is correct? | Correct formula structure | Products minus reactants; coefficients inside; elements contributing zero |
| Hess's law — what additional reaction is needed? | Missing step identification | Algebraically subtract all given reactions from target; identify the remaining uncanceled species |
| Hess's law — find Rxn 2 such that Rxn 1 + Rxn 2 = Overall | Algebraic subtraction | $\text{Rxn 2} = \text{Overall} - \text{Rxn 1}$; cancel species appearing on both sides; check with addition to verify |
| Two reactions need to be combined and one reversed | Hess's manipulation | Reverse → flip sign; add → sum $\Delta H$ values; intermediate species cancel if identical and opposite sides |
| Which method gives more accurate $\Delta H$? | Accuracy of methods | Standard enthalpies of formation (exact, measured) > bond enthalpies (approximate, averaged) |

---

## AP Answer Templates — Unit 6

> **Exo/endothermic identification from temperature change:** "The reaction is [exothermic / endothermic] because the temperature of the solution [increased / decreased] during the reaction. This indicates that the reaction [released / absorbed] thermal energy, causing the surroundings to [gain / lose] heat."

> **Direction of heat transfer:** "Heat flows from [the hotter object / sample at higher temperature] to [the cooler object / sample at lower temperature] because the particles in the hotter sample have greater average kinetic energy. Through molecular collisions at the interface, kinetic energy transfers from the higher-energy particles to the lower-energy particles until thermal equilibrium is reached."

> **Calorimetry calculation setup:** "The heat absorbed by the solution is $q_{\text{cal}} = mc\Delta T = ([m]\ \text{g})(4.18\ \text{J/g·°C})([T_f] - [T_i])$. By conservation of energy in the insulated calorimeter, $q_{\text{rxn}} = -q_{\text{cal}}$. The enthalpy per mole of reaction is $\Delta H = q_{\text{rxn}}/n_{\text{rxn}} = [q]/[n]\ \text{kJ/mol}$."

> **Stoichiometric scaling of enthalpy:** "The balanced equation shows $[n]$ mol of $[\text{species}]$ per mole of reaction. The $[m]\ \text{g}$ sample corresponds to $[m/M]$ mol, which equals $[mol/n]$ mol of reaction. The heat released is $[mol\_rxn] \times [|\Delta H°|] = [q]\ \text{kJ}$."

> **Heating curve plateau explanation:** "During the phase transition at [melting / boiling] point, the temperature remains constant because the energy added is used to overcome the intermolecular attractive forces between particles rather than increasing their kinetic energy. The potential energy of the system increases while kinetic energy (and temperature) stays the same."

> **Bond enthalpy $\Delta H$ calculation:** "Using $\Delta H_{\text{rxn}} = \Sigma\text{BE(broken)} - \Sigma\text{BE(formed)}$: bonds broken in reactants total $[+x]\ \text{kJ}$; bonds formed in products total $[y]\ \text{kJ}$. Therefore $\Delta H_{\text{rxn}} = [x] - [y] = [x-y]\ \text{kJ/mol}_{\text{rxn}}$. The [negative / positive] value indicates the reaction is [exothermic / endothermic]."

> **Standard enthalpy of formation calculation:** "Using $\Delta H°_{\text{rxn}} = \Sigma\Delta H°_f(\text{products}) - \Sigma\Delta H°_f(\text{reactants})$: products contribute $[\Sigma\Delta H°_f(\text{prod})]\ \text{kJ}$; reactants contribute $[\Sigma\Delta H°_f(\text{react})]\ \text{kJ}$. Therefore $\Delta H°_{\text{rxn}} = [prod] - [react] = [\Delta H°]\ \text{kJ/mol}_{\text{rxn}}$. Note: $\Delta H°_f = 0$ for $[\text{O}_2, \text{H}_2,\ldots]$ as elements in standard state."

> **Hess's law manipulation:** "To obtain the target reaction, Reaction 1 is [reversed / kept as written] ($\Delta H_1 \to [\pm\Delta H_1]$) and [scaled by factor $n$]. Reaction 2 is [reversed / kept] and [scaled]. Adding the two adjusted equations cancels $[\text{intermediate species}]$, giving the target reaction. $\Delta H_{\text{total}} = [\pm n\Delta H_1] + [\pm m\Delta H_2] = [sum]\ \text{kJ/mol}_{\text{rxn}}$."

---

## Critical Reminders — Unit 6

> [!danger] ΔH < 0 = Exothermic; ΔH > 0 = Endothermic — Never Reverse
> Classification is from the **reaction's** perspective. Rising solution temperature = exothermic reaction (surroundings gained heat). Do NOT say "endothermic because the water absorbed the heat."

> [!danger] q_rxn = −q_cal: They Have Opposite Signs
> What the reaction releases, the calorimeter gains. If solution temperature rises ($q_{cal} > 0$) → $q_{rxn} < 0$ (exothermic). Never give both the same sign.

> [!warning] ΔT = T_final − T_initial (Final Minus Initial Always)
> A cooling experiment gives a **negative** ΔT, not positive. Never take T_initial − T_final.

> [!warning] Phase Transition: T is Constant — Use q = nΔH, NOT mcΔT
> The flat plateau on a heating curve = melting or boiling at **constant temperature**. Energy goes into breaking IMFs (PE increases), not KE (T stays constant). Use $q = n\Delta H_{fus}$ or $q = n\Delta H_{vap}$.

> [!check] ΔH_vap >> ΔH_fus for the Same Substance
> Vaporization completely separates IMFs; melting only loosens them. The vaporization plateau on a heating curve is **much wider** than the melting plateau.

> [!danger] ΔH°_f = 0 for ALL Elements in Standard State
> O₂(g), H₂(g), N₂(g), C(graphite), Na(s), Fe(s) all have $\Delta H°_f = 0$ **by definition**. Never assign a nonzero formation enthalpy to an element in standard state.

> [!warning] Bond Enthalpy Formula: Broken FIRST, Formed SECOND
> $\Delta H = \Sigma BE_{broken} - \Sigma BE_{formed}$. Negative result = more energy released forming bonds than absorbed breaking → exothermic. Don't reverse the order.

> [!check] Bond Enthalpies Are Approximate; ΔH°_f Values Are Exact
> Bond enthalpies are gas-phase averages — **approximate**. Standard enthalpies of formation are measured calorimetrically — **exact**. Use ΔH°_f for accurate ΔH°_rxn when given a table.

> [!warning] Hess's Law Manipulation Rules
> Reversing a reaction → flip sign of ΔH. Scaling by n → multiply ΔH by n. Adding reactions → sum ΔH values. Enthalpy is a **state function** — path doesn't matter.

> [!check] ΔH°_rxn = Products Minus Reactants
> $\Delta H°_{rxn} = \Sigma \Delta H°_f(products) - \Sigma \Delta H°_f(reactants)$. Always **products minus reactants** with stoichiometric coefficients. Reactants minus products gives wrong sign.

> [!check] Avogadro's Law: V ∝ n at Constant T and P (PV = nRT)
> From $PV = nRT$: at constant T and P, $V = (RT/P) \times n$ → V is directly proportional to n. $V_1/n_1 = V_2/n_2$. Use R = 0.08206 L·atm/mol·K; T in Kelvin.

> [!warning] Heat Flow Direction: Temperature, NOT Mass or Volume
> Heat flows from **higher temperature** to **lower temperature**. Direction is determined by temperature (average KE), NOT by mass, volume, or number of moles. A small hot object heats a large cold one.
