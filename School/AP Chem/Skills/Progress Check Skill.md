---
name: apchem-progress-check
description: >
  Use this skill whenever Donny uploads AP Chemistry CollegeBoard Progress Check MCQ screenshots
  (any unit) along with his notes and examples files. This skill drives the exact workflow for
  working through all questions, gap-analyzing the notes, and delivering updated files. Triggers:
  any combination of AP Classroom MCQ screenshots + Unit notes/examples uploads, "progress check",
  "work through these questions", "update my notes", "AP Chem MCQ". Always use this skill before
  touching any AP Chem Progress Check question set.
---

# AP Chem Progress Check Skill

This skill defines the exact procedure for processing any AP Chemistry CollegeBoard Unit Progress
Check MCQ set. Three phases: work the questions → gap-analyze → deliver updated files.

The quality bar for the output is **Unit 3** (Properties of Substances and Mixtures) — the most
complete unit in the vault, with 50+ MCQ rows, 40+ worked examples, and dedicated sections for all
13 CED topics. Every question fully worked with complete calculations, an AP-language justification
citing laws by name, a trap callout, a summary pattern table, and updated notes/examples files that
are self-sufficient for future progress checks on that unit.

**Before updating any notes file, check for these structural problems:**
- **Merged topic sections:** If multiple CED topics share one `## Topic` heading (e.g., "Topic 5.7"
  covering 5.7–5.10 content), split them into separate sections before adding new content.
  Each CED topic number must have its own `## Topic X.N: [Name]` heading.
- **Missing equation examples:** If the notes contain a named equation (Arrhenius, van't Hoff, Nernst,
  etc.) that has no corresponding worked numerical example in the Examples file, add one.
- **Out-of-unit content:** If Critical Reminders contain bullets about other units (e.g., Unit 9
  thermodynamics in Unit 1 notes), remove them and place them in the correct unit's file.

Every question type covered in Units 1–5 and 9 has an established trap and template below — use
them for any unit.

---

## Inputs Expected

Donny will upload:
1. **MCQ screenshots** — AP Classroom Progress Check questions, any unit, any number
2. **`Unit_X_Notes.md`** — his existing notes for that unit
3. **`Unit_X_Examples.md`** — his existing worked examples for that unit

He may upload questions in batches. **Do not begin until all questions are posted.** If he says
"posting first half" or similar, reply "Got it — waiting for the rest before I start."

---

## Phase 1: Work Every Question → `Unit_X_Progress_Check.md`

**The progress check answers go in a `.md` file, never inline in chat.**

Write all Q&A to `Unit_X_Progress_Check.md`, save to `/home/claude/`. Do NOT print answers
in the chat response. Deliver only via `present_files` at the end.

### Per-question block format (use exactly):

```markdown
## Q[N]. [Brief one-line restatement of the question]

[Show all work with units. For non-calc questions show logical elimination step by step.]

**Answer: [Letter] — [Answer text exactly as written in the question]**

[1–3 sentence AP-language justification. Cite laws by name: Coulomb's law, Gay-Lussac's law,
Dalton's law, Beer's law, KMT, Maxwell-Boltzmann, etc. Name the specific force (ion–dipole,
not just "intermolecular forces"). State the mechanism, not just the conclusion.]

> **Trap:** [Most common wrong answer and why students pick it. Always include. Never skip.]
```

> **CRITICAL — Answer choices:** Do NOT list all four answer choices (A, B, C, D) in the file.
> The `**Answer:**` line contains only the correct choice's letter and its exact wording — nothing else.
> Copying verbatim A/B/C/D blocks before the answer line is explicitly prohibited.

### Calculation formatting rules:
- Display math `$$...$$` for multi-step calculations; inline `$...$` for variables and values
- Show the ratio explicitly in gas law problems: e.g., $P_2 = 2.1 \times \frac{313}{283}$
- Label every intermediate result: `n = 0.025 mol`, `M = 32.0 g/mol`
- Show unit cancellation for any dimensional analysis step

### Conceptual question rules:
- Always state the principle before applying it (e.g., "Same temperature → same average KE by KMT. Since $KE = \frac{1}{2}mv^2$, lighter molecules must move faster.")
- For IMF questions: name the specific IMF type, cite Coulomb's law for ion–dipole questions
- For solid type questions: state which inter-particle force is broken during melting
- For Beer's Law error questions: explain the $I_t$ mechanism ($A = -\log(I_t/I_0)$), not just "A goes up"
- For Maxwell-Boltzmann questions: always state "same T = same avg KE" before comparing speeds

### Trap callout rules:
- Every single question gets a Trap — no exceptions
- Name the specific wrong answer letter when possible
- Explain WHY students pick it (the intuition that leads them wrong)
- Explain WHY it's wrong (the correct principle it violates)

### End of progress check file:

```markdown
## Summary of Key Patterns — Unit X MCQ

| Pattern | Rule | Questions |
|---|---|---|
| [scenario from this question set] | [concept tested] | Q# |
```

Include a row for every distinct pattern that appeared, even if only one question tested it.

---

## Phase 2: Gap Analysis + SVG Planning

After working all questions, compare what was tested against the uploaded notes and examples.

**Identify silently:**
1. **Missing content** — concepts tested that have no coverage in the notes
2. **Thin coverage** — concepts present but without the MCQ-pattern framing the exam uses
3. **Missing examples** — question types tested that have no worked example in the file

**State gaps briefly before producing files** — one sentence per gap, maximum 8 gaps listed.
Only flag real gaps. Do not flag things already well covered.

**Plan SVGs at the same time.** For each gap that is visual in nature, decide: does it need an
SVG? Name the file now. Generate in Phase 3 before writing any markdown.

---

## Phase 3: SVGs First, Then Updated Files

**SVGs must be generated BEFORE writing any markdown.** The markdown files embed
`![[filename.svg]]` — those files must exist before the markdown references them.

### Step 3a: Generate SVGs for All New Gaps

Generate an SVG for a gap concept if ALL are true:
1. It appeared in this question set (tested or gap-identified)
2. It is inherently visual
3. No existing diagram for it in the uploaded notes file

**SVG requirements (same as notes-from-video skill):**

```xml
<svg viewBox="0 0 680 [height]" xmlns="http://www.w3.org/2000/svg">
  <title>[Descriptive title]</title>
  <desc>[One sentence accessible description]</desc>
  <style>
    .th { font-family: Arial, sans-serif; font-size: 14px; font-weight: bold; fill: #1e293b; }
    .ts { font-family: Arial, sans-serif; font-size: 12px; fill: #334155; }
    .tss { font-family: Arial, sans-serif; font-size: 11px; fill: #475569; }
  </style>
  <defs><!-- arrow markers --></defs>
</svg>
```

- Width always 680; hex colors only; no CSS variables; no script; no foreignObject
- Color palette: Blue `#dbeafe`/`#3b82f6`/`#1d4ed8` | Green `#dcfce7`/`#16a34a`/`#15803d` |
  Yellow `#fef9c3`/`#ca8a04`/`#92400e` | Red `#fee2e2`/`#ef4444`/`#991b1b` |
  Purple `#ede9fe`/`#7c3aed`/`#4c1d95` | Panel `#f8fafc`/`#e2e8f0`
- Naming: `[concept]_u[X].svg`. Save to `/home/claude/` before proceeding.

### Step 3b: Structural Audit Then Update `Unit_X_Notes.md`

**Before adding content, audit the file structure:**
1. List every CED topic number for this unit from the AP CED or Krug video list.
2. Verify each topic has its own `## Topic X.N: [Name]` heading in the notes.
3. If any topics share a heading (e.g., Topics 5.8/5.9/5.10 folded under 5.7), split them into
   separate sections now — before adding any new content. The existing content that belongs to the
   later topic numbers moves into the new heading.
4. Check: does every equation in the Key Equations blocks have a corresponding worked example in
   the Examples file? If not, flag it for addition in Step 3c.

**Preserve every existing section and bullet exactly.** Never delete or rewrite existing content.

Add only new material:
- New content goes in the correct existing topic section (e.g., new Beer's Law content in Topic 3.13)
- New equations: `$$...$$`
- New subsection: bold header matching existing style
- New MCQ patterns: add rows to the existing table — never replace existing rows
- New AP templates: add blockquotes to AP Answer Templates section
- New reminders: add bullets to Critical Reminders section
- New SVG embeds: `![[filename.svg|697]]` with caption, placed after the relevant section header

### Step 3c: Update `Unit_X_Examples.md`

**Preserve every existing example exactly.** Never delete or renumber existing examples.

Add new examples sequentially after the last existing example in each topic section:
- Bold title: `**Example N — [what it tests] (Progress Check Q#):**`
- Problem statement with all given information
- Step-by-step work with units at every step
- Final answer clearly identified
- `*Key move: [general transferable principle, not just a description of this problem.]*`

For "what can/cannot be concluded" question types: explicitly list what the data CAN support
AND 2–3 things it CANNOT support, with reasoning for each.

### Step 3d: Copy Everything and Present

Copy to `/mnt/user-data/outputs/`:
- `Unit_X_Progress_Check.md`
- `Unit_X_Notes.md`
- `Unit_X_Examples.md`
- All new SVG files

Call `present_files` in this order: Progress Check MD first, Notes second, Examples third,
SVGs last.

End response with:
> "Drop all SVG files into your vault's attachments folder (Settings → Files & Links →
> Default attachment folder). The `![[filename.svg]]` references will render automatically."

---

## LaTeX Rules — Mandatory, No Exceptions

All scientific notation, ions, formulas, and equations use LaTeX. Zero raw Unicode anywhere.

| Write | NOT |
|---|---|
| `$\text{Fe}^{2+}$`, `$\text{Na}^{+}$` | Fe²⁺, Na⁺ |
| `$\text{H}_2\text{O}$`, `$\text{CO}_2$` | H₂O, CO₂ |
| `$\Delta H°$`, `$\Delta G°$` | ΔH°, ΔG° |
| `$Z_{eff}$`, `$E_a$`, `$K_{sp}$` | Z_eff, Ea, Ksp |
| `$1s^2\ 2p^6$` | 1s²2p⁶ |
| `$6.022 \times 10^{23}$` | 6.022 × 10²³ |
| `$$PV = nRT$$` | PV = nRT |

Applies to: Q&A blocks, summary table, notes additions, example additions, trap callouts.

---

## AP Language Bank — Use These Formulations

**Gas laws — always Kelvin:**
> "Converting to Kelvin: $T_1 = [T]\ °\text{C} + 273 = [T_K]\ \text{K}$. By [law], $P \propto T$ at constant $V$ and $n$..."

**Ion–dipole strength:**
> "By Coulomb's law ($F \propto |q|/r^2$), [ion] has a higher charge-to-size ratio than [ion] because [charge comparison / radius comparison], resulting in stronger ion–dipole attractions with water."

**KMT — same T, different speeds:**
> "At the same temperature, all gases have the same average kinetic energy ($KE_{\text{avg}} = \frac{3}{2}RT$). Since $KE = \frac{1}{2}mv^2$, a gas with lower molar mass must have a higher average speed."

**Maxwell-Boltzmann higher T:**
> "At higher temperature, molecules have greater average kinetic energy and higher average speeds. The distribution broadens and the peak shifts to the right. The area under the curve remains the same because the number of molecules is unchanged."

**Beer's Law error — reduced I_t:**
> "[Error] reduces the transmitted light intensity $I_t$ reaching the detector. Since $A = -\log(I_t/I_0)$, a lower $I_t$ yields a higher measured absorbance than the actual value."

**Beer's Law error — dilution:**
> "Residual [water/solvent] dilutes the sample, reducing the molar concentration $c$. Since $A = \varepsilon bc$ and $A \propto c$, the measured absorbance is lower than the actual value."

**Melting a solid:**
> "Melting [solid] breaks only the [inter-particle force type] between [particle type]. The [intramolecular bonds] within each [molecule/unit] remain intact."

**Real gas deviation at high P:**
> "At very high pressure, the finite volume of the gas molecules becomes significant relative to the container volume. The actual volume exceeds the ideal prediction, causing the measured pressure to exceed the ideal value. This effect is greatest for [largest molecule]."

**Chromatography Rf:**
> "Component [X] has a higher $R_f$ value because it has greater affinity for the [mobile phase] than for the [stationary phase], indicating [X] is [less/more] polar than [Y]."

**TLC → column:**
> "The most effective solvent for column chromatography gives the greatest separation between $R_f$ values at intermediate positions in TLC. Solvent [X] produces this separation; spots near the top ($R_f \approx 1$) co-elute in a column and give no separation."

**Activity series justification:**
> "[Metal A] is located above [metal B / H₂] in the activity series, meaning [A] is a stronger reducing agent and more readily loses electrons. Therefore, [A] will [displace B²⁺ from solution / react with the acid to produce H₂ gas]. The reverse reaction does not occur because [B / Cu / Ag] is below [A / H₂] and is a weaker reducing agent."

**Back titration:**
> "A known excess of [reagent A] ($n_A = M_A \times V_A$) was added to react completely with the analyte. The remaining excess A was titrated with [reagent B], giving $n_{A,\text{remaining}} = M_B \times V_B \times (\text{ratio})$. The moles of A that reacted with the analyte = $n_{A,\text{added}} - n_{A,\text{remaining}}$. Applying the stoichiometric ratio from the balanced equation gives moles of analyte, and dividing by volume gives concentration."

**Disproportionation:**
> "This is a disproportionation reaction because [element] in the single reactant [species] has oxidation number [x]. In the products, the same element appears with oxidation numbers [y] and [z], where [y] < [x] < [z]. Therefore [element] is simultaneously reduced (to [y]) and oxidized (to [z]) in a single reaction, and [species] is both the oxidizing agent and the reducing agent."

**Lewis acid/base:**
> "[Species A] acts as the Lewis acid because it [has an empty p orbital / is electron-deficient] and accepts the electron pair donated by [species B], the Lewis base, which has a lone pair available on [atom]. This forms a coordinate covalent bond between them. No proton transfer occurs, so this is a Lewis acid-base reaction but not a Brønsted–Lowry reaction."

**Balancing redox in basic solution:**
> "The equation was first balanced under acidic conditions using the half-reaction method: atoms balanced with H₂O, hydrogen balanced with H⁺, charge balanced with e⁻. After combining half-reactions, [n] OH⁻ were added to both sides to neutralize the [n] H⁺. The resulting H₂O molecules on the same side were cancelled. The final equation contains only H₂O and OH⁻, consistent with basic conditions."

**Physical vs. chemical change:**
> "This is a [physical / chemical] change because [only intermolecular forces between the particles are broken; the chemical identity and formula of each substance is unchanged / covalent bonds are broken and/or formed, producing new substances with different chemical formulas]. [Reversibility is not the criterion.]"

**Titration buret error (water rinse):**
> "Rinsing the buret with distilled water before filling dilutes the titrant below its labeled concentration. A larger volume of diluted titrant is required to reach the equivalence point. Using the labeled (too high) concentration with the measured (too large) volume in $M_1V_1 = M_2V_2$ overestimates the moles of titrant used, so the calculated analyte concentration is too high."

---

## Common Traps by Topic — Reference During Q&A

| Topic | Trap | Correct reasoning |
|---|---|---|
| IMF ranking | "Polar always > nonpolar" | LDF of large nonpolar can beat dipole–dipole of small polar |
| H-bonding | "F present → H-bonds" | H must be directly bonded to N/O/F to donate |
| NH₄⁺ | "H on N → H-bond acceptor" | N has no lone pair in NH₄⁺ (4 bonds) → no acceptor |
| Ion–dipole | "Smallest ion = strongest force" | Compare charge first; $2+$ beats $1+$ almost always |
| Ion dissolving in water | "Hydrogen bonds" or "dipole–dipole" | Ion + polar solvent = always ion–dipole |
| Molecular vs. network solid MP | "P₄ has covalent bonds → high MP" | Those are intramolecular; only inter-particle forces break during melting |
| Gas laws | Using Celsius in $P/T$ or $V/T$ | Always Kelvin: $T(\text{K}) = T(°\text{C}) + 273$ |
| Gay-Lussac ratio | $283/313$ instead of $313/283$ | New T in numerator: $P_2 = P_1 \times (T_2/T_1)$ |
| Boyle's Law | Using $\Delta V$ instead of ratio | Use $V_1/V_2$, not $V_1 - V_2$ |
| Dalton's Law | "IMFs between gases change total P" | Ideal: no IMFs; partial pressures add independently |
| Maxwell-Boltzmann higher T | "Curve is taller" | Higher T = broader + right-shifted + LOWER peak |
| Maxwell-Boltzmann same T | "Same T = same speed" | Same T = same avg KE; lighter gas is faster |
| Real gas high P | "Lightest gas deviates most" | Largest molecule deviates most (volume effect) |
| C₂H₆ vs CH₄ deviation | "C₂H₆ has H-bonding" | H on C → no H-bonding; difference is LDF strength only |
| Dilution | Wrong variable in $M_1V_1 = M_2V_2$ | Stock (known) on left; target on right; solve for unknown |
| Ion concentration | "$[\text{compound}]\ M = [\text{ion}]\ M$" | Multiply by stoichiometric coefficient per formula unit |
| TLC selection for column | "Spots near top = best" | Both near top → co-elute in column; need intermediate spread |
| Separation method | "Chromatography for miscible liquids" | Miscible + different BPs → distillation |
| EM region | "IR causes electronic transitions" | IR → vibrational; UV/Vis → electronic |
| Beer's Law fingerprint | "Shifts peak wavelength" | Peak position unchanged; only absorbance value increases |
| Beer's Law frosted wall | "A too low, less light enters" | Less $I_t$ → A too high (same mechanism as fingerprints) |
| Beer's Law water droplets | "Water absorbs visible light" | Water transparent; error is dilution reducing $c$ |
| Conductivity graph linear | "Linear = infinitely soluble" | Graph only shows tested range; saturation may lie beyond |
| Solid type from data | "High MP = ionic" | Very high MP + never conducts → network covalent, not ionic |
| Periodic trends | "More protons = harder to remove going down" | Distance ($r^2$) dominates over $Z$ going down a group |
| IE exception | "O > N (further right)" | O < N due to paired $2p$ electron repulsion in O |
| Dissolution of NaCl | "Ionic bonds break → chemical change" | AP classifies dissolution as physical — no new compound formed |
| Electrolysis of water | "Phase change, so physical" | O–H covalent bonds broken → chemical change |
| Physical vs. chemical criterion | "Reversible = physical; irreversible = chemical" | Reversibility is never the criterion; bond type is |
| Activity series: Cu + HCl | "All metals react with acid" | Only metals above H₂ on activity series react with dilute acids; Cu, Ag, Au do not |
| Activity series: lower metal displaces higher | "Cu(s) + ZnSO₄(aq) → reaction" | Lower metal cannot displace higher from solution; NR |
| Halogen displacement | "Any halogen displaces any halide" | Only a more active halogen displaces a less active one: F₂ > Cl₂ > Br₂ > I₂ |
| Limiting reactant after doubling | "Doubling one reactant doubles yield" | Only true if that reactant was originally limiting; if originally stoichiometric, yield is unchanged |
| Buret rinsed with water | "Calculated concentration too low" | More volume needed → moles overestimated → calculated concentration **too high** |
| Analyte flask rinsed with water | "Changes the concentration" | No effect — moles of analyte are fixed; water in flask doesn't matter |
| Back titration setup | "Only one titration used" | Two titrations: first excess added to analyte; second back-titrates excess |
| Conjugate pair identification | "Acid and base in the same reaction are a conjugate pair" | Conjugate pairs are acid↔product or base↔product across the arrow; never reactant↔reactant |
| Amphoteric species | "Any conjugate base is amphoteric" | Must have both an ionizable H to donate AND a lone pair to accept; $\text{CH}_3\text{COO}^-$ fails — no ionizable H |
| NH₄⁺ as acid-base participant | "$\text{NH}_4^+$ is a base (N has lone pair)" | N in NH₄⁺ has 4 bonds; no lone pair → cannot accept H⁺ → NH₄⁺ is an acid only |
| Lewis vs. Brønsted-Lowry | "BF₃ + NH₃ is a Brønsted-Lowry reaction" | No H⁺ transferred → not Brønsted-Lowry; it is a Lewis acid-base reaction only |
| Disproportionation identification | "Two different reactants → must be two separate redox reactions" | If the same element from one species appears in two products at different ONs, it is one disproportionation |
| H₂O₂ decomposition | "O in H₂O₂ → −2 in both products" | O → −2 (H₂O) AND O → 0 (O₂); H₂O₂ is both OA and RA |
| Basic solution redox | "Add OH⁻ at the start before balancing" | Always balance acidically first; convert to basic at the end by adding OH⁻ equal to H⁺ count |
| Formal charge vs. bond strength | "Triple bond → best Lewis structure" | Bond strength is irrelevant; formal charge minimization determines the best structure |
| Electron count for charged ions | "Count atoms' electrons; ignore charge" | Add 1e⁻ per negative charge unit; subtract 1e⁻ per positive charge unit before drawing |
| Arrhenius R value | "Use R = 0.08206 in Arrhenius" | Arrhenius requires $R = 8.314\ \text{J/(mol·K)}$; convert $E_a$ to J/mol if given in kJ |
| Arrhenius — which rate is faster? | "Higher T always doubles the rate" | Rate increase depends on $E_a$: $\ln(k_2/k_1) = -E_a/R \cdot (1/T_2 - 1/T_1)$; large $E_a$ → greater rate sensitivity to T |
| Multistep energy diagram — slow step | "Highest hump from reactant baseline = slow step" | Measure each hump from its preceding energy minimum (valley or reactant), not always from the reactant baseline |
| Energy diagram intermediates | "Transition states are isolable" | Humps (peaks) = transition states (cannot be isolated); valleys between humps = intermediates (can in principle be isolated) |
| Steady-state vs. pre-equilibrium | "They're the same thing" | Pre-equilibrium requires a fast reversible step before the slow step. Steady-state only requires d[I]/dt = 0 with no assumption about which step is fast |
| Combustion analysis — oxygen in compound | "All sample mass is C and H" | Always subtract: $m_O = m_{\text{sample}} - m_C - m_H$. Never assume no oxygen without checking that C + H masses sum to sample mass |
| Single-isotope mass spectrum | "Single peak → calculate weighted average" | Single peak = one stable isotope → atomic mass = peak mass exactly; no weighted average needed |
| d-block cation configuration | "Remove 3d electrons to form cation" | Remove 4s first, THEN 3d. $\text{Fe}^{2+}$ is $[\text{Ar}]\ 3d^6$, not $[\text{Ar}]\ 3d^4\ 4s^2$ |

---

## Quality Checklist

- [ ] Structural audit complete: every CED topic has its own `## Topic X.N` heading; none merged
- [ ] Every Key Equation in the notes has a corresponding worked numerical example in the Examples file
- [ ] Numeric examples verified: intermediate values are physically plausible (e.g., mass ≤ sample mass)
- [ ] Out-of-unit Critical Reminders removed if found
- [ ] Progress check answers in `Unit_X_Progress_Check.md` — NOT printed in chat
- [ ] Every question has a Trap callout — no exceptions
- [ ] All calculations show units at each step with labeled intermediate results
- [ ] Gas law questions show temperature conversion explicitly
- [ ] Ion–dipole questions cite Coulomb's law and name charge-to-size ratio
- [ ] KMT questions state "same T = same avg KE" before comparing speeds
- [ ] Beer's Law error questions explain the $I_t$ mechanism
- [ ] Summary pattern table at end of progress check file covers all distinct patterns
- [ ] Gap analysis stated before writing files: one sentence per gap, max 8
- [ ] SVGs planned before Phase 3 begins; generated before any markdown written
- [ ] Every new SVG: viewBox 0 0 680 h, xmlns, title, desc, style, hex colors only, no CSS variables, no script
- [ ] Notes file: existing content preserved; new content added in correct sections
- [ ] Examples file: existing examples preserved; new examples numbered sequentially
- [ ] New examples have: problem statement, labeled steps with units, final answer, *Key move:*
- [ ] Zero raw Unicode anywhere — full LaTeX throughout all three output files
- [ ] All SVG embeds use `![[filename.svg]]` Obsidian wiki-link syntax with caption
- [ ] All files (3 MDs + new SVGs) copied to `/mnt/user-data/outputs/`
- [ ] `present_files` called: Progress Check first, Notes second, Examples third, SVGs last
- [ ] Obsidian setup reminder at end of response
