---
name: apchem-notes-from-video
description: >
  Use this skill when Donny asks to build AP Chemistry notes for any unit. Triggers: "make notes
  for unit X", "build my notes", "give me full notes", "notes from video", "Krug video",
  "Farabaugh notes", "unit X notes", any request to produce Unit_X_Notes.md and
  Unit_X_Examples.md. This skill does NOT require any uploaded source material — it searches
  Jeremy Krug and Michael Farabaugh's YouTube channels and supplementary web sources directly.
  Do NOT use this skill if Unit_X_Notes.md already exists — use apchem-progress-check instead.
---

# AP Chem Notes From Video Skill

This skill produces the **Part 1 baseline** Unit_X_Notes.md and Unit_X_Examples.md for any AP
Chemistry unit by searching Krug and Farabaugh content from the web. No uploads required.

The quality bar is **Unit 3** (Properties of Substances and Mixtures). Unit 3 is the gold standard
because it is the most complete unit in the vault. Any new unit must match these concrete metrics:

| Metric | Unit 3 (gold standard) | Minimum for any new unit |
|---|---|---|
| CED topic sections | 13 dedicated sections | Every CED topic gets its own `## Topic X.N` heading — no merging |
| MCQ pattern rows | 50+ rows | 20+ rows |
| Worked examples | 40+ examples across all topics | 3 per topic; 4–5 for heavily-tested topics |
| AP Answer Templates | 8+ templates | 1 per major question type |
| Critical Reminders | 15 bullets | 10–15 bullets |
| SVG diagrams | 8+ diagrams | All visually essential concepts |

The files must be **self-sufficient**: a student with only these two files can answer every progress
check MCQ for the unit without any other resource.

---

## Step 0: Search the Web First — Always

Before writing a single word, run ALL of these searches. Do not skip. Do not rely on training
knowledge alone.

```
1. web_fetch: https://jeremykrug.com/ap-chem-videos/
   → Get the full video list. Note every Unit X video title and URL.

2. web_search: "Jeremy Krug AP Chemistry Unit [X] [unit title]"
   → Find Knowt transcriptions or notes pages of Krug content.

3. web_fetch: any Knowt.com page that appears
   → Knowt often has full transcriptions of Krug lectures. Fetch every relevant one.

4. web_search: "Michael Farabaugh AP Chemistry Unit [X] site:youtube.com"
   → Get Farabaugh video titles and descriptions for this unit.

5. web_search: "AP Chemistry Unit [X] [topic] Farabaugh OR Krug worked example"
   → Target specific topic coverage for each CED topic.

6. web_search: "AP Chemistry Unit [X] CED topics"
   → Confirm the full list of CED topics so no section is missed.
```

After searching, build a coverage map: list every CED topic, note what Krug and Farabaugh
covered for each, identify gaps. Flag thin topics with:
`> **Note:** Limited source coverage — constructed from CED.`

**CRITICAL: verify CED topic numbers against Krug's video organization before writing.**
Krug's groupings reveal the actual CED structure. Example failure mode: Unit 4 once had
Topics 4.7–4.9 wrong (acid-base and redox lumped under 4.7; a fake "advanced stoichiometry" 4.9).
The correct structure — 4.7 = types of reactions, 4.8 = acid-base, 4.9 = redox — was only
discoverable from Krug's video titles. Always use Krug's groupings to verify your topic map.

**KNOWN FAILURE MODES — avoid these in every new unit:**

| Failure | What happened | Prevention |
|---|---|---|
| Merged topic sections | Unit 5 had Topics 5.7–5.10 collapsed into one "Topic 5.7" section because Krug covers them in one video. Topics 5.8 (rate law from mechanism), 5.9 (steady-state), and 5.10 (multistep energy profile) had no dedicated notes. | One `## Topic X.N` heading per CED topic, even if a single Krug video covers 3–4 at once. |
| Calculation error in examples | Unit 4's back-titration example showed a visible mid-problem calculation error with "let me redo" text. | Verify every numeric answer before writing. A 2-step check: (1) forward-calculate to confirm the answer, (2) sanity-check that intermediate values are physically plausible (e.g., mass of product cannot exceed mass of sample). |
| Out-of-place content | Unit 1 Critical Reminders contained a bullet about S° (entropy of elements), which is Unit 9 thermodynamics content. | Only include content directly testable in that unit's progress check. Cross-unit references belong in the source unit's notes only. |
| Thin MCQ table | Unit 2 had only ~15 MCQ rows vs. Unit 3's 50+. Formal charge comparison, SO₄²⁻ structure selection, and alloy property prediction were missing. | Build the MCQ table after working all available progress check questions. Every question type that appeared in the progress check must appear in the table. |
| Missing Arrhenius worked example | Unit 5 Notes covered the Arrhenius equation formula but the Examples file had no two-temperature calculation. The most commonly tested Arrhenius FRQ question type was absent. | At least one fully worked numerical example per equation in the Notes. If a formula appears in "Key Equations", a worked example using it must exist in the Examples file. |

### Krug complete video list (confirmed from jeremykrug.com/ap-chem-videos/):

**Unit 1:** 1.1a https://youtu.be/wynFro1c09k | 1.1b https://youtu.be/dijmukeZ2WE | 1.2 https://youtu.be/bzky1T4RYIs | 1.3 https://youtu.be/_uqIROUX0js | 1.4 https://youtu.be/00RufJkBZy4 | 1.5a https://youtu.be/4tvfh15wYxY | 1.5b https://youtu.be/lvhHMbXLi-U | 1.6 https://youtu.be/EVn4_euvA6U | 1.7a https://youtu.be/MftSzSxIWBA | 1.7b https://youtu.be/6Uaub18RkAA | 1.7c https://youtu.be/u2aGKh_4HGI | 1.8 https://youtu.be/4tWZl3-_ZZU

**Unit 2:** 2.1 https://youtu.be/SQk9E_Y2EWw | 2.2–2.4 https://youtu.be/buRAe2IDBzQ | 2.5a https://youtu.be/_lFg4z0OOOY | 2.5b https://youtu.be/i4IqrxlrgDw | 2.6 https://youtu.be/Th3ZiNN313o | 2.7a https://youtu.be/8Xupo4rn2kA | 2.7b https://youtu.be/a8xDFQLYtYE

**Unit 3:** 3.1a https://youtu.be/a9YtU828MzM | 3.1b https://youtu.be/lOoLquXZH3M | 3.2 https://youtu.be/4_14asNzvc0 | 3.3 https://youtu.be/9G88-AcHVbA | 3.4a https://youtu.be/rZxN6Zfzipc | 3.4b https://youtu.be/77xhRWWpIi4 | 3.4c https://youtu.be/-Hu2xBrbgjU | 3.5 https://youtu.be/d3nEzAUWqfE | 3.6 https://youtu.be/BvGTzkVDcHI | 3.7 https://youtu.be/aob4zGMCVIM | 3.8a https://youtu.be/W19S_PQOqgw | 3.8b https://youtu.be/nFkcOaPpRHk | 3.9/3.10 https://youtu.be/mWxgxb-RHTE | 3.11 https://youtu.be/g2bG4AdDbKM | 3.12 https://youtu.be/trlFDyrjtOQ | 3.13 https://youtu.be/jD3_pN5gR8A

**Unit 4:** 4.1/4.2a https://youtu.be/KmI627EPza0 | 4.2b https://youtu.be/K5QDMQIOpmI | 4.2c https://youtu.be/HhH15-vkgeY | 4.3/4.4 https://youtu.be/3lzI1vO118g | 4.5a https://youtu.be/pZHDvyv_z0c | 4.5b https://youtu.be/b7mKXr7LZ3I | 4.5c https://youtu.be/zb6_ak50Jlw | 4.5d https://youtu.be/U9TGx77BWJ8 | 4.6 https://youtu.be/kxdu490P4Tw | 4.7a https://youtu.be/B4khUScKJS8 | 4.7b https://youtu.be/OEvI8yiSnxE | 4.8 https://youtu.be/eX7soWYIGv8 | 4.9a https://youtu.be/RySE0dy3Pfs | 4.9b https://youtu.be/eiNKXlhy0Ww | 4.9c https://youtu.be/-aypxLKg9B8

For all other units, always fetch fresh from jeremykrug.com/ap-chem-videos/ — do not guess URLs.

---

## What These Files Must Achieve

The notes and examples files must be **self-sufficient**: a student with only these two files can
answer every progress check MCQ for the unit without any other resource. This requires:

- Every CED topic covered at exam depth, not just mentioned
- Every MCQ question type pattern explicitly named with the key move
- Every common trap identified with reasoning
- Worked examples that match the difficulty of actual progress check questions
- SVG diagrams that make visual concepts immediately clear during study

---

## Phase 1: SVGs — Generate Before Writing Any Markdown

**SVGs must exist before any markdown references them.** Plan all SVG filenames during the web
search phase, generate them all, then write the markdown.

### Always generate an SVG for:
- Any spectrum: Maxwell-Boltzmann, PES, IR, UV-Vis, mass spectrum, absorption spectrum
- Any trend: periodic trends, thermodynamic trends, kinetic distributions
- Any filling order or orbital diagram
- Any comparison table that benefits from color coding: solid types, IMF types, error analysis
- Any multi-step process: Hess's law cycle, distillation, chromatography
- Any decision tree: solid identification, separation method selection, IMF ranking
- Any EM spectrum or wavelength/frequency/energy relationship

Do NOT generate diagrams for purely algebraic content with no visual component.

### SVG requirements (no exceptions):

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

- Width always 680; height fits content without crowding
- **Hex colors ONLY** — never `var(--)`, never CSS variables (Obsidian renders SVGs statically)
- Color palette (use consistently across all diagrams in a unit):
  - Blue: fill `#dbeafe` / stroke `#3b82f6` / text `#1d4ed8`
  - Green: fill `#dcfce7` / stroke `#16a34a` / text `#15803d`
  - Yellow: fill `#fef9c3` / stroke `#ca8a04` / text `#92400e`
  - Red: fill `#fee2e2` / stroke `#ef4444` / text `#991b1b`
  - Purple: fill `#ede9fe` / stroke `#7c3aed` / text `#4c1d95`
  - Panel: `#f8fafc` / `#e2e8f0`; axes: `#555`; grids: `#e5e5e5` dashed
- Arrow markers in `<defs>` using `<marker>` elements
- No external fonts, no `<script>`, no `foreignObject`
- Naming: `[concept]_u[X].svg` (e.g., `imf_ranking_u3.svg`)
- Save to `/home/claude/` before writing any markdown

### Embedding:
```markdown
![[filename.svg|697]]
*One sentence caption: what it shows and the single most important takeaway.*
```
In Notes: after the section header or key equation. In Examples: before Example 1 in that topic.
Never embed the same diagram more than twice total across both files.

---

## Phase 2: Notes File — `Unit_X_Notes.md`

### File structure:

```markdown
# AP Chem — Unit [X] Notes: [Unit Title]
**Exam Weight: [X–X]% | Topics: [X.1–X.Y]**
**Krug Videos:** [3.Xa title](url) | [3.Xb title](url) | ...

---

## Topic [X.1]: [Topic Name]

**Essential Knowledge (Farabaugh CED):**
- [bullet — not definitional; answers "why does this matter on the AP exam?"]

**Key Equations:**
$$[primary equation]$$

![[concept_uX.svg|697]]
*Caption.*

**[Subsection header if needed]**
[Content — prose, table, or numbered steps]

---

## Topic [X.2]: [Topic Name]
[repeat]

---

## MCQ Pattern Recognition — Unit [X]

| If you see... | It's testing... | Key move |
|---|---|---|

---

## AP Answer Templates — Unit [X]

> **[Template name]:** "[Complete sentence, AP grader language, bracketed placeholders]"

---

## Critical Reminders — Unit [X]

- [exam-critical bullet]
```

### Content depth requirements:

**Essential Knowledge bullets** — each must include: the concept, what changes it, the
exam-relevant consequence, and any exception the exam tests. Not definitions alone.

**Tables** — required for: solid type identification, IMF comparison, H-bond donor/acceptor,
gas law equations, EM spectrum regions, Beer's Law errors, separation method selection. Include
enough columns for direct comparison. Color-code rows by type where possible.

**Procedures** — numbered steps for: preparing solutions, reading calibration curves, TLC,
using the AP reference table. Include Farabaugh's lab error nuances.

**Topic section completeness check** — before writing, list every CED topic number for this unit.
Each one needs its own `## Topic X.N: [Name]` heading. If a single Krug video covers multiple topics,
still write separate sections. Never merge 5.7, 5.8, 5.9, 5.10 under one heading just because they
share a video. The heading is required even if the section is brief.

**MCQ Pattern Recognition table** — minimum 20 rows for a full unit. Format:
- "If you see..." — exact question framing
- "It's testing..." — precise concept name
- "Key move" — first thing to do, or critical fact to recall

**AP Answer Templates** — minimum one per major question type. Complete sentences with
[bracketed placeholders]. Must cite laws by name (Coulomb's law, Beer's law, Gay-Lussac's law),
name the specific forces (ion–dipole not just "intermolecular forces"), state the mechanism.

**Critical Reminders** — 10–15 bullets of the most commonly wrong things. State as short
declarative facts, not as topic summaries.

---

## Phase 3: Examples File — `Unit_X_Examples.md`

### File structure:

```markdown
# AP Chem — Unit [X] Examples: [Unit Title]

---

## Topic [X.1]: [Topic Name]

![[concept_uX.svg|697]]
*Caption.*

**Example 1 — [Source and description] (Krug / Farabaugh / AP exam difficulty):**
[Problem statement — all given information explicitly listed]

[Step 1: ... (unit)]
[Step 2: ... (unit)]
$$[display math if needed]$$
[Final answer clearly identified]

*Key move: [Transferable rule stated as a general principle, not a description of this problem.]*

---

**Example 2 — ...**
```

### Required per topic section:
- **Minimum 3 examples** — 4–5 for heavily-tested topics (gas laws, Beer's Law, molarity, chromatography)
- Every example has: problem statement with all given info, labeled steps with units,
  final answer, `*Key move:*` as general principle
- **At least one trap callout per topic section** — can appear in any example:
  `Trap: [wrong answer] — [why students pick it] — [why it's wrong]`
- At least one calculation example with math per topic
- At least one conceptual/MCQ-elimination example per topic
- At least one **FRQ-crossover example** somewhere in the full file (written AP justification,
  not just a number — show what a full-credit response looks like)
- At least one **"what can/cannot be concluded"** example for data interpretation topics
  (conductivity graphs, chromatography Rf, Beer's Law calibration curves, etc.)

---

## LaTeX Rules — Mandatory, No Exceptions

All ions, formulas, equations, and scientific notation use LaTeX. Zero raw Unicode anywhere.

| Write | NOT |
|---|---|
| `$\text{Fe}^{2+}$`, `$\text{Na}^{+}$` | Fe²⁺, Na⁺ |
| `$\text{H}_2\text{O}$`, `$\text{CO}_2$` | H₂O, CO₂ |
| `$\Delta H°$`, `$\Delta G°$` | ΔH°, ΔG° |
| `$Z_{eff}$`, `$E_a$`, `$K_{sp}$` | Z_eff, Ea, Ksp |
| `$1s^2\ 2p^6\ 3d^{10}$` | 1s²2p⁶3d¹⁰ |
| `$6.022 \times 10^{23}$` | 6.022 × 10²³ |
| `$$PV = nRT$$` (equations = display math) | PV = nRT |
| `$n = m/M$` (inline) | n = m/M |

Scan the complete output before delivering. Fix every raw Unicode found.

---

## Sourcing Priority

1. **Jeremy Krug YouTube** — worked examples, problem setups, solution steps. Label: `(Krug [topic])`
2. **Michael Farabaugh YouTube** — CED alignment, Essential Knowledge, FRQ tips, lab nuances. Label: `(Farabaugh)`
3. **AP CollegeBoard CED** — topic list, exam weights, gap filler
4. **Constructed** — when all above silent. Flag: `> *[Constructed — verify against Krug/Farabaugh.]*`

---

## Delivery

1. Copy all files to `/mnt/user-data/outputs/`
2. `present_files`: Notes MD first, Examples MD second, then all SVGs
3. End response with exactly:
> "Drop all SVG files into your vault's attachments folder (Settings → Files & Links →
> Default attachment folder). The `![[filename.svg]]` references will render automatically."

---

## Quality Checklist

- [ ] Listed every CED topic number for this unit; confirmed each has its own `## Topic X.N` heading
- [ ] Verified every equation in the Notes has at least one fully worked numerical example in the Examples file
- [ ] Checked that no Critical Reminders contain content from other units
- [ ] Verified all numeric examples: intermediate values are physically plausible (e.g., mass of product ≤ mass of sample)
- [ ] Searched web (all 6 searches) before writing anything
- [ ] Fetched jeremykrug.com/ap-chem-videos/ for accurate video URLs
- [ ] CED topic numbers verified against Krug's video groupings — no invented topic assignments
- [ ] Video URLs in Notes file header, hyperlinked
- [ ] Every CED topic has a section; thin ones flagged
- [ ] Every topic: Essential Knowledge bullets (not just definitions), equations, SVG embed, tables/procedures where needed
- [ ] Minimum 3 examples per topic; 4–5 for heavily-tested topics
- [ ] Every example: labeled steps with units, final answer, *Key move:* as general principle
- [ ] At least one trap callout per topic section
- [ ] At least one FRQ-crossover example in the full file
- [ ] At least one "what can/cannot be concluded" example in the full file
- [ ] MCQ pattern table: 20+ rows, all predictable question types for the unit
- [ ] AP Answer Templates: one per major question type, in complete-sentence grader language
- [ ] Critical Reminders: 10–15 bullets, the most exam-critical facts
- [ ] Zero raw Unicode — full LaTeX throughout both files
- [ ] All visually essential concepts have SVGs generated and embedded
- [ ] SVGs generated BEFORE markdown was written
- [ ] Every SVG: viewBox 0 0 680 h, xmlns, title, desc, style block, hex colors only, no CSS variables, no script
- [ ] Every SVG embed: `![[filename.svg]]` wiki-link with caption line
- [ ] File names: `Unit_[X]_Notes.md` and `Unit_[X]_Examples.md`
- [ ] All files (MDs + SVGs) in `/mnt/user-data/outputs/`
- [ ] `present_files`: Notes, Examples, SVGs in that order
- [ ] Obsidian setup reminder at end of response
