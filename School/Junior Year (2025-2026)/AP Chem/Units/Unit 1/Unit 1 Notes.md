# AP Chem — Unit 1 Notes: Atomic Structure and Properties
**Exam Weight: 7–9% | Topics: 1.1–1.8**
**Hub:** [[../../Study Hub/AP Chem Master Overview]] | **Memorize:** [[../../Study Hub/Memorization/Must Memorize]] (polyatomic ions, VSEPR, periodic trends)
**Krug Videos:** [1.1a](https://youtu.be/wynFro1c09k) | [1.1b](https://youtu.be/dijmukeZ2WE) | [1.2](https://youtu.be/bzky1T4RYIs) | [1.3](https://youtu.be/_uqIROUX0js) | [1.4](https://youtu.be/00RufJkBZy4) | [1.5a](https://youtu.be/4tvfh15wYxY) | [1.5b](https://youtu.be/lvhHMbXLi-U) | [1.6](https://youtu.be/EVn4_euvA6U) | [1.7a](https://youtu.be/MftSzSxIWBA) | [1.7b](https://youtu.be/6Uaub18RkAA) | [1.7c](https://youtu.be/u2aGKh_4HGI) | [1.8](https://youtu.be/4tWZl3-_ZZU)

---

## Study Hub Quick Reference — Unit 1

> [!check] Q4 — Successive Ionization Energies → Group Identification
> A large jump between IE_n and IE_{n+1} means the (n+1)th electron is a core electron. The element has **n valence electrons** and belongs to **Group n**. Example: if IE₄ >> IE₃, the element is in Group 3. Look for where the jump is dramatically larger than the surrounding gaps.

> [!check] Q14 — He vs. H Ionization Energy
> He has a **higher IE₁ than H** despite being in the same period. Both have electrons in n=1, but He (Z=2) has greater nuclear charge than H (Z=1). By Coulomb's law, stronger nuclear attraction → higher IE. He's IE₁ ≈ 2372 kJ/mol; H's ≈ 1312 kJ/mol.

> [!check] Q15 — Combustion Analysis → Empirical and Molecular Formula
> 1. $n_C = m_{CO_2}/44.01$ → $m_C = n_C \times 12.01$
> 2. $n_H = 2 \times m_{H_2O}/18.02$ → $m_H = n_H \times 1.008$
> 3. $m_O = m_{sample} - m_C - m_H$ (O found by **subtraction** — never assume no oxygen)
> 4. $n_O = m_O/16.00$; divide all moles by smallest → whole-number empirical ratio
> 5. Molecular formula = empirical × ($M_{molecular}/M_{empirical}$)

> [!check] Q31 — Na More Reactive Than Mg (Lower IE₁ = Easier to Oxidize)
> Na (Group 1, Z=11) has **lower IE₁** than Mg (Group 2, Z=12). Lower IE₁ means electrons are lost more easily → stronger reducing agent → more reactive with water. Na reacts vigorously with water; Mg reacts only slowly with steam. On the activity series, Na is above Mg.

> [!check] FRQ Q7B — Beer-Lambert Calibration Curve
> Prepare standards of known concentration → measure absorbance at $\lambda_{max}$ → plot A vs. [C]. Graph is **linear** ($A = \varepsilon bc$; $A \propto c$). Slope = $\varepsilon b$ (molar absorptivity × path length). To find unknown: measure A → read [C] off the line.

> [!check] FRQ Q7C — Beer-Lambert: Dilution Effect
> Diluting the sample lowers concentration c → lowers absorbance A. If sample is diluted by factor of 2, measured A is **half** the undiluted value. To recover original concentration: multiply the read-off [C] by the dilution factor. A ∝ c at constant $\varepsilon$ and b.

> [!check] FRQ Q7D — Choosing λ_max for Spectrophotometry
> Always measure at the **wavelength of maximum absorbance** ($\lambda_{max}$). Reasons: (1) highest sensitivity — small concentration changes produce large A changes; (2) most linear Beer's Law response; (3) maximizes accuracy of concentration readings from the calibration curve.

> [!warning] Trap — IE Exception: O Has Lower IE₁ Than N
> Oxygen's IE₁ < nitrogen's IE₁ despite being to the right. O's 2p⁴ has a **paired electron** that repels → easier to remove. Also: Al < Mg (Al's 3p is farther out and better shielded than Mg's 3s). Don't rank IE₁ purely by left-to-right position.

> [!warning] Trap — PES: Peak Height ≠ Peak Position
> Peak **HEIGHT** = number of electrons in that subshell. Peak **POSITION** = binding energy (how hard to remove). They are completely independent. A tall peak at LOW binding energy = many valence electrons, NOT core electrons.

> [!danger] Critical — Cation Formation: 4s Empties Before 3d
> Remove **4s electrons BEFORE 3d** when forming cations. Fe²⁺ = [Ar]3d⁶ (both 4s removed), NOT [Ar]3d⁴4s². This is the **reverse** of the filling order.

---

## Topic 1.1: Moles and Molar Mass

**Essential Knowledge (Farabaugh CED):**
- One mole contains exactly $6.022 \times 10^{23}$ entities (Avogadro's number, $N_A$). This connects atomic-scale particles to macroscopic, measurable mass.
- The molar mass of an element in g/mol is numerically equal to its atomic mass in amu.
- For compounds, molar mass is the sum of the atomic masses of all atoms in the formula, each multiplied by its subscript.

**Key Equations:**
$$n = \frac{m}{M} \qquad N = n \times N_A$$

**The Conversion Chain:**
$$\text{mass (g)} \xrightarrow{\div M} \text{moles} \xrightarrow{\times N_A} \text{particles}$$

**Critical Reminders:**
- Molar mass has units g/mol; atomic mass (amu) is per individual atom — never mix them.
- For ionic compounds: $\text{Na}_2\text{SO}_4$ has 2 Na + 1 S + 4 O → molar mass = 142.05 g/mol.
- Always track units through every step of a dimensional analysis chain.

---

## Topic 1.2: Mass Spectra of Elements

**Essential Knowledge (Farabaugh CED):**
- A mass spectrum plots % relative abundance vs. mass-to-charge ratio (m/z). Each peak = one isotope.
- Peak height is proportional to natural abundance of that isotope.
- Average atomic mass = weighted average of all naturally occurring isotopes.

**Key Equation:**
$$\bar{m} = \sum (\text{isotope mass} \times \text{fractional abundance})$$

**Reading a Spectrum:**
- Number of peaks = number of naturally occurring isotopes.
- Taller peak = more abundant isotope.
- The calculated average will be closer in mass to the more abundant isotope.
- To identify an unknown element: count peaks first (= number of stable isotopes), then match the mass range and approximate average to the periodic table.

![[mass_spectrum_weighted_average.svg|697]]
*The weighted average always falls between the two peaks, pulled toward the taller (more abundant) one. Never report the tallest peak mass as the average.*

**Common Mistake:** Using % abundance directly — always convert to decimal first (69.2% → 0.692).

---

## Topic 1.3: Elemental Composition of Pure Substances

**Essential Knowledge (Farabaugh CED):**
- Percent composition by mass can be calculated from the chemical formula.
- An **empirical formula** gives the simplest whole-number ratio of atoms.
- A **molecular formula** is a whole-number multiple of the empirical formula.

**Percent Composition:**
$$\% \text{ element} = \frac{\text{total mass of that element per mole of compound}}{\text{molar mass of compound}} \times 100$$

**Empirical Formula from % Composition — Procedure:**
1. Assume 100 g sample → % directly becomes grams.
2. Convert each mass to moles: $n = m/M$.
3. Divide all by the smallest mole value.
4. If ratios aren't whole numbers (e.g., 1.5), multiply all by the same integer (×2).

**Molecular Formula:**
$$n = \frac{M_{\text{molecular}}}{M_{\text{empirical}}} \quad \text{→ multiply all subscripts by } n$$

**Common Mistakes (Farabaugh):**
- **Not dividing by the smallest:** In step 3, always divide ALL mole values by the smallest one — never skip this.
- **Rounding too early:** Ratios like 1.499 should be rounded to 1.5, not 1 — then multiply through by 2.
- **Combustion analysis:** Mass of C comes from CO₂ ($n_C = n_{\text{CO}_2}$); mass of H from H₂O ($n_H = 2 \times n_{\text{H}_2\text{O}}$). Any remaining mass (total − C − H) is oxygen in the compound.
- **Molar mass from combustion:** The empirical formula only gives the atom ratio, not the molar mass. A separate molar mass measurement is required to find the molecular formula.

---

## Topic 1.4: Composition of Mixtures

**Essential Knowledge (Farabaugh CED):**
- A pure substance has a fixed composition; a mixture has variable composition.
- Mass percent describes the fraction of a component in a mixture.

**Key Equations:**
$$\text{mass \% of A} = \frac{\text{mass of A}}{\text{total mass of mixture}} \times 100$$

$$\chi_A = \frac{n_A}{n_{\text{total}}} \qquad \text{(mole fraction of A)}$$

**Mole Fraction — Critical Points:**
- Mole fraction ($\chi$) is unitless and always between 0 and 1. All mole fractions in a mixture sum to 1.
- Converting mass data to mole fraction **always requires molar mass** as the intermediate step: mass → ($\div M$) → moles → mole fraction.
- Mole percent = mole fraction × 100.

**Purity and Experimental Reasoning (MCQ Pattern):**

A pure substance has a **fixed, characteristic composition**. The AP exam regularly asks which measurement best determines purity or answers a specific question about a mixture. Use this decision framework:

| Goal | What data you need | Key move |
|---|---|---|
| Determine if sample is pure | Compare measured elemental % to theoretical % for the pure formula | Calculate theoretical mass % from formula; compare to measured |
| Find % purity of impure sample | Mass of pure product formed via reaction | Use stoichiometry to back-calculate moles of pure reactant; compare to original mass |
| Find mole % or mole fraction | Masses of each component + molar masses | Convert each mass → moles → mole fraction |
| Find molar mass of unknown M in MO | Initial mass of M and final mass of MO | Mass of O = $\Delta$mass; moles O = moles M (1:1); molar mass M = mass M / moles M |

**What mass measurement alone cannot tell you:** volume, density, melting point, molar mass (without formula), or any kinetic/stability property.

**MCQ Pattern:** Given mass of product from an impure sample → work backward to find moles of pure reactant → calculate % purity of the original sample.

---

## Topic 1.5: Atomic Structure and Electron Configuration

**Essential Knowledge (Farabaugh CED):**
- Electrons occupy orbitals (probability regions). Three rules govern filling:
  - **Aufbau principle:** Fill lowest-energy orbitals first: 1s → 2s → 2p → 3s → 3p → 4s → 3d → 4p → ...
  - **Pauli exclusion principle:** Max 2 electrons per orbital, opposite spins.
  - **Hund's rule:** Within a subshell, place one electron in each orbital before pairing.
- **Coulomb's law** governs attraction between nucleus and electrons:
$$F \propto \frac{q_1 q_2}{r^2}$$
  - Larger nuclear charge ($q_1$) → stronger attraction → harder to remove electrons.
  - Larger distance ($r$) → weaker attraction → easier to remove electrons.

![[aufbau_orbital_filling.svg|697]]
*Key trap: 4s fills before 3d in neutral atoms, but 4s empties before 3d when forming cations. $\text{Fe}^{2+}$ is $[\text{Ar}]\ 3d^6$, not $[\text{Ar}]\ 3d^4 4s^2$.*

**Orbital Subshell Capacities:**

| Subshell | Orbitals | Max electrons |
|---|---|---|
| s | 1 | 2 |
| p | 3 | 6 |
| d | 5 | 10 |
| f | 7 | 14 |

**Notable Exceptions (must memorize):**
- Cr: $[\text{Ar}]\ 3d^5\ 4s^1$ (not $3d^4\ 4s^2$) — half-filled d is more stable.
- Cu: $[\text{Ar}]\ 3d^{10}\ 4s^1$ (not $3d^9\ 4s^2$) — fully-filled d is more stable.

**Ions — remove/add from highest energy orbital first:**
- Cations (metals): remove 4s before 3d. $\text{Fe}^{2+}$ is $[\text{Ar}]\ 3d^6$, not $[\text{Ar}]\ 3d^4\ 4s^2$.
- Anions: add electrons to the next available orbital.

**Counting unpaired electrons:**
- Apply Hund's rule only to *incomplete* subshells. A filled subshell ($s^2$, $p^6$, $d^{10}$) always has 0 unpaired electrons.
- Verify total electron count matches atomic number (or $Z \pm$ charge for ions).

---

## Topic 1.6: Photoelectron Spectroscopy (PES)

**Essential Knowledge (Farabaugh CED):**
- PES measures the energy required to remove electrons from each subshell (binding energy).
- A PES spectrum plots binding energy (x-axis, increasing right to left) vs. relative number of electrons (peak height/area).
- **Peak position** = binding energy of that subshell. Higher binding energy = closer to nucleus = harder to remove.
- **Peak height** = relative number of electrons in that subshell.

![[pes_spectrum_nitrogen.svg|697]]
*Peak position and peak height are completely independent. A tall peak at low binding energy means many valence electrons, not inner-shell electrons.*

**Reading a PES Spectrum:**
- Leftmost peak (highest binding energy) = innermost electrons ($1s$).
- Rightmost peak (lowest binding energy) = valence electrons.
- Identify the element by counting total electrons from peak heights and matching to atomic number.
- Peak at ~40 MJ/mol with height 2 = $1s^2$ subshell.

**"Consistent with the electron shell model" questions:** Map each peak to its subshell assignment (leftmost = 1s, then 2s, then 2p, etc.) and verify the peak height matches the electron count for that subshell. A peak height of 1 at the valence end = single electron in that subshell (e.g., Boron's $2p^1$).

**Coulomb's Law Connection to PES:**
- Going left to right on the periodic table: increasing $Z_{eff}$ → valence electrons held more tightly → higher binding energy → PES peak shifts left.
- Going down a group: valence electrons farther from nucleus → lower binding energy → PES peak shifts right.

**Common Mistake:** Confusing peak height (number of electrons) with peak position (binding energy). A tall peak at low binding energy = valence subshell with many electrons.

---

## Topic 1.7: Periodic Trends

**Essential Knowledge (Farabaugh CED):**
- Three factors explain all periodic trends via Coulomb's law: (1) effective nuclear charge ($Z_{eff}$), (2) distance between nucleus and valence electrons (atomic/ionic radius), (3) electron–electron repulsions.
- $Z_{eff}$ increases across a period (more protons, same shielding) and stays roughly constant down a group.

![[periodic_trends.svg|697]]
*Circle size represents atomic radius. Both trends operate simultaneously — comparing across a period uses $Z_{eff}$; comparing down a group uses principal quantum number $n$.*

**Trend Summary:**

| Property | Across a Period (→) | Down a Group (↓) | Explanation |
|---|---|---|---|
| Atomic radius | Decreases | Increases | $Z_{eff}$ increases across; more shells added down |
| Ionization energy (IE) | Increases | Decreases | $Z_{eff}$ pulls $e^-$ tighter across; farther from nucleus down |
| Electron affinity | More negative (generally) | Less negative | Same logic as IE |
| Electronegativity | Increases | Decreases | F is highest (3.98); Fr is lowest |

**IE Exceptions (MCQ trap):**
- $\text{IE}_1(\text{O}) < \text{IE}_1(\text{N})$: O has a paired electron in 2p that repels → easier to remove.
- $\text{IE}_1(\text{Al}) < \text{IE}_1(\text{Mg})$: Al's $3p$ electron is farther out and better shielded than Mg's $3s$.

**Comparing across a period vs. down a group (mixed comparisons):**
- Same period: $Z_{eff}$ is the dominant factor → higher $Z$ = smaller radius, higher IE.
- Same group: principal quantum number ($n$) is the dominant factor → higher $n$ = larger radius, lower IE.
- Mixed (e.g., K vs Br): both have valence electrons in $n=4$, so $Z_{eff}$ decides — Br's much higher $Z_{eff}$ ($Z=35$ vs $Z=19$) gives it a smaller radius.

**Ionic Radius:**
- Cations are smaller than parent atom (lost electrons, same $Z$, more attraction per electron).
- Anions are larger than parent atom (added electrons, same $Z$, electron-electron repulsion swells cloud).
- Isoelectronic series (same # electrons): higher nuclear charge → smaller radius. $\text{Na}^+ > \text{Mg}^{2+} > \text{Al}^{3+}$.

---

## Topic 1.8: Valence Electrons and Ionic Compounds

**Essential Knowledge (Farabaugh CED):**
- Valence electrons are in the outermost principal energy level and determine chemical reactivity.
- For main-group elements: group number = number of valence electrons (Group 1 → 1, Group 17 → 7).
- Transition metals: valence electrons include $4s$ and $3d$ electrons.
- Ionic compounds form when metals transfer electrons to nonmetals. The resulting ions adopt noble-gas configurations.
- Common ionic charges to know: Group 1 → $+1$, Group 2 → $+2$, Group 13 → $+3$, Group 16 → $-2$, Group 17 → $-1$, transition metals → variable.
- Elements in the **same group** have the same number of valence electrons → same ionic charge → same stoichiometric ratio with any given counterion.

**Coulomb's Law and Ionic Compound Properties:**
$$F \propto \frac{q_1 q_2}{r^2}$$

![[coulombs_law_ionic.svg|697]]
*Higher ion charges AND smaller radii both increase the attractive force. MgO has 4× the charge product and a 25% shorter interionic distance compared to NaCl — that combination produces a 3.5× higher melting point.*

- Higher ion charges → stronger ionic attractions → higher melting/boiling point, higher lattice energy.
- Smaller ionic radii → shorter interionic distance → stronger attraction → higher melting point.
- Example: MgO melts at 2852°C; NaCl melts at 801°C. $\text{Mg}^{2+}$ and $\text{O}^{2-}$ have higher charges and smaller radii than $\text{Na}^+$ and $\text{Cl}^-$.

---

## MCQ Pattern Recognition — Unit 1

| If you see... | It's testing... | Key move |
|---|---|---|
| Mass spectrum with two peaks | Weighted average atomic mass | Each peak = one isotope; convert % to decimal |
| Mass spectrum with many peaks, asked to ID element | Number of stable isotopes + mass range | Count peaks = # isotopes; match mass range and average to periodic table |
| % composition data | Empirical formula | Assume 100 g; divide moles by smallest; clear fractions |
| PES spectrum with 3 peaks, heights 2/2/3 | Electron configuration | Count total electrons: 2+2+3=7 → N |
| PES peak at highest binding energy | Innermost (core) electrons | Leftmost peak = $1s$; rightmost = valence |
| "Which statement is consistent with the electron shell model?" | Matching peak height to subshell electron count | Assign each peak left→right to subshells; verify height = # electrons |
| "Which has the highest $\text{IE}_1$?" | Periodic trend + exceptions | N > O (paired $2p$ electron in O) |
| "Why does $\text{Mg}^{2+}$ have a smaller radius than $\text{Na}^+$?" | Isoelectronic series | Same electrons, higher $Z$ → stronger pull → smaller |
| "Which lattice energy is highest?" | Coulomb's law with ionic charges | Higher charge AND smaller radius → highest |
| Cr or Cu electron configuration | Anomalous filling | Cr: $[\text{Ar}]\ 3d^5\ 4s^1$; Cu: $[\text{Ar}]\ 3d^{10}\ 4s^1$ |
| Ion electron configuration | Remove from highest $n$ first | $\text{Fe}^{2+}$: remove both $4s$ before $3d$ → $[\text{Ar}]\ 3d^6$ |
| "What is $Z_{eff}$?" | Effective nuclear charge trend | Increases left to right; explains all trends |
| "What additional info is needed to find mole fraction?" | Mole fraction requires molar mass | mass → ($\div M$) → moles → $\chi$; molar mass is always the missing link |
| "Which data best determines purity?" | Fixed composition of pure substances | Compare measured elemental % to theoretical; deviation = impurity |
| "Which question can be answered from this experiment?" | What mass measurements actually tell you | Mass data → stoichiometry → moles/empirical formula/purity; NOT volume, melting point, or stability |
| Same group as a known element | Same valence electrons → same ionic charge | Same group = same stoichiometric ratio with any given counterion |
| Combustion analysis — how to find oxygen in the compound? | Compound contains C, H, and O — oxygen is found by subtraction | mass of O = total sample mass − mass of C (from CO₂) − mass of H (from H₂O). Never assume the compound has no oxygen just because combustion products contain only C and H products |
| Mass spectrum: element with 1 stable isotope — what does spectrum look like? | Single-isotope elements need no weighted average | Single peak; no weighted average needed; the peak mass = the atomic mass. Fluorine (F), iodine (I), and phosphorus (P) each have exactly one stable isotope |
| Electron configuration of a d-block transition metal ion — special rule? | 4s empties before 3d when forming cations | Remove 4s electrons before 3d electrons when forming cations. $\text{Fe}^{2+}$ is $[\text{Ar}]\ 3d^6$ not $[\text{Ar}]\ 3d^4\ 4s^2$. Then apply Hund's rule to the remaining d electrons |

---

## AP Answer Templates — Unit 1

> **Periodic trend justification (across a period):** "As you move across a period from left to right, the number of protons increases while the number of shielding electrons remains approximately constant. This increases the effective nuclear charge ($Z_{eff}$), which increases the attraction between the nucleus and the valence electrons. Therefore, [atomic radius decreases / ionization energy increases / etc.]."

> **Periodic trend justification (down a group):** "Moving down a group, each successive element adds a new principal energy level. The valence electrons occupy orbitals farther from the nucleus and experience increased shielding from inner-shell electrons. By Coulomb's law ($F \propto q_1q_2/r^2$), the reduced attractive force results in a larger atomic radius and lower ionization energy."

> **IE exception (N vs O):** "Although oxygen is to the right of nitrogen and has a higher $Z_{eff}$, oxygen's first ionization energy is lower because its $2p$ subshell contains a paired electron. The repulsion between the two electrons in the same orbital makes it easier to remove one of them."

> **PES peak identification:** "The peak at the highest binding energy corresponds to the $1s$ electrons, which are closest to the nucleus and experience the strongest nuclear attraction. The peak at the lowest binding energy corresponds to the valence electrons, which are farthest from the nucleus and most easily removed."

> **Lattice energy comparison:** "MgO has a higher lattice energy than NaCl because the ions $\text{Mg}^{2+}$ and $\text{O}^{2-}$ have greater charges and smaller ionic radii than $\text{Na}^+$ and $\text{Cl}^-$. According to Coulomb's law, the attractive force between ions increases with greater charge magnitude and decreases with greater interionic distance."

> **Purity determination:** "A pure substance has a fixed elemental composition. The theoretical mass percent of [element] in pure [compound] is [calculated value]%. Since the measured value differs from this, the sample is not pure [compound]."

> **Mole fraction explanation:** "To determine the mole fraction of each gas, the mass of each gas must first be converted to moles using the relationship $n = m/M$. The mole fraction is then $\chi_A = n_A / n_{\text{total}}$. Therefore, the molar mass of each gas is the additional information required."

> **Combustion analysis with oxygen present:** "From the combustion data, $n_C = n_{\text{CO}_2} = m_{\text{CO}_2}/44.01$, giving $m_C = n_C \times 12.01$. Similarly, $n_H = 2 \times n_{\text{H}_2\text{O}} = 2 \times m_{\text{H}_2\text{O}}/18.02$, giving $m_H = n_H \times 1.008$. The mass of oxygen in the compound is $m_O = m_{\text{sample}} - m_C - m_H$. Convert each mass to moles using the respective molar mass, then divide all mole values by the smallest to obtain the empirical formula ratio."

---

## Critical Reminders — Unit 1

> [!danger] Cation Formation: 4s Empties Before 3d
> 4s fills before 3d in neutral atoms, but **4s empties before 3d** when forming cations. Fe²⁺ = [Ar]3d⁶, NOT [Ar]3d⁴4s². This is the reverse of filling order.

> [!warning] PES: Peak Height and Position Are Independent
> Peak **height** = number of electrons in that subshell. Peak **position** = binding energy. A tall peak at LOW binding energy = many valence electrons, NOT core electrons. Never confuse them.

> [!warning] IE Exceptions: O < N, and Al < Mg
> O has lower IE₁ than N (paired 2p electron repels — easier to remove). Al has lower IE₁ than Mg (3p is farther out and better shielded than 3s). Both are MCQ-tested regularly — don't rank IE₁ purely left-to-right.

> [!check] Weighted Average Pulls Toward Most Abundant Isotope
> Average atomic mass is always closest in value to the most abundant isotope's mass. The taller peak on a mass spectrum = more abundant = closer to the average.

> [!check] Coulomb's Law Explains ALL Unit 1 Periodic Trends
> $F \propto q_1q_2/r^2$. Larger nuclear charge → stronger attraction → smaller radius, higher IE. More shielding → weaker attraction → larger radius, lower IE. Always cite Coulomb's law explicitly on FRQs.

> [!warning] Mole Fraction Always Requires Molar Mass
> You cannot convert from mass to mole fraction without molar mass. mass → (÷M) → moles → $\chi$. Molar mass is always the missing link when this calculation is requested.

> [!check] Same Group = Same Valence Electrons = Same Ionic Charge
> Elements in the same group have the same valence electrons → same ionic charge → same stoichiometric formula with any given counterion.

> [!warning] Mass Data Alone Cannot Answer Everything
> Mass data → stoichiometry → moles/empirical formula/purity. Mass data CANNOT answer: volume, melting point, density, or chemical stability questions.

> [!check] Mixed Comparison: Identify the Dominant Factor
> Comparing atomic radius across a period AND down a group: across a period → $Z_{eff}$ dominates; down a group → principal quantum number n dominates. Identify which factor applies before ranking.
