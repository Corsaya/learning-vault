## Topic 9.8 — Galvanic (Voltaic) and Electrolytic Cells

---

## Core Concepts

An **electrochemical cell** links an oxidation and a reduction half-reaction, either harvesting or consuming electrical energy. **Oxidation always occurs at the anode** and **reduction always occurs at the cathode** — this is true for both cell types without exception.

A **galvanic (voltaic) cell** runs on a thermodynamically favorable (spontaneous) redox reaction. Chemical energy is converted to electrical energy. Because the reaction is spontaneous, $\Delta G° < 0$ and $E°_{cell} > 0$.

An **electrolytic cell** forces a non-spontaneous reaction using an external power source (battery or DC supply). $\Delta G° > 0$ for the reaction as written; the external voltage must overcome this barrier. Electroplating, recharging batteries, and splitting water are all electrolytic processes.

---

## Key Equations

$$\boxed{E°_{cell} = E°_{cathode} - E°_{anode}}$$

$$\Delta G° = -nFE°_{cell}$$

Where $n$ = moles of electrons transferred, $F$ = 96,485 C/mol e⁻.

- $E°_{cell} > 0 \Rightarrow \Delta G° < 0 \Rightarrow$ spontaneous → **galvanic cell**
- $E°_{cell} < 0 \Rightarrow \Delta G° > 0 \Rightarrow$ non-spontaneous → **electrolytic cell**

**AP rules for $E°$ values (critical):**
- **Never flip the sign** of a standard reduction potential — the subtraction formula already accounts for reversal
- **Never multiply $E°$** by a stoichiometric coefficient — $E°$ is an intensive property

---

## Galvanic Cell Components

### Anode (oxidation)
- Metal is oxidized; atoms leave as ions → electrode **mass decreases**
- Electrons flow **out of** the anode into the external wire
- If the reactant is a gas or in solution, use an **inert electrode** (Pt or graphite)

### Cathode (reduction)
- Metal ions from solution deposit as solid → electrode **mass increases**
- Electrons flow **into** the cathode from the external wire
- If the product doesn't plate as a solid, use an **inert electrode**

### Salt Bridge
- Contains an inert ionic solution (KNO₃, NaCl, etc.)
- Allows **ions** to flow between half-cells to maintain electrical neutrality
- **Cations** migrate toward the cathode; **anions** migrate toward the anode
- Without a salt bridge: charge builds up instantly and the cell stops

### External Circuit
- Electrons travel anode → wire → cathode (never through solution)
- Ion flow through salt bridge + solution completes the full circuit

---

## Mg–Cu Galvanic Cell — Reference Example

$$Mg_{(s)} + Cu^{2+}_{(aq)} \rightarrow Mg^{2+}_{(aq)} + Cu_{(s)}$$

| Half-Cell | Electrode | Solution | $E°$ (V) |
|---|---|---|---|
| Anode (oxidation) | Magnesium (Mg) | MgSO₄ or Mg(NO₃)₂ — 1 M | −2.37 V |
| Cathode (reduction) | Copper (Cu) | CuSO₄ or Cu(NO₃)₂ — 1 M | +0.34 V |
| Salt bridge | — | KNO₃ or NaCl (inert) | — |

$$E°_{cell} = +0.34 - (-2.37) = \textbf{+2.71 V}$$

- Mg anode **loses mass** (Mg → Mg²⁺ dissolves)
- Cu cathode **gains mass** (Cu²⁺ → Cu deposits)

---

## Electrolytic Cells

| Feature | Detail |
|---|---|
| Driving force | External power source required |
| Thermodynamics | Non-spontaneous ($\Delta G° > 0$) |
| Chambers | Both electrodes often in same chamber |
| Salt bridge | Not needed |
| Electron flow | Anode → power source → cathode |
| Ion flow | Cations → cathode; anions → anode |

### Electrolysis of Water

$$\text{Cathode (reduction): } 2H_2O + 2e^- \rightarrow H_2(g) + 2OH^-$$
$$\text{Anode (oxidation): } 2H_2O \rightarrow O_2(g) + 4H^+ + 4e^-$$

H₂ produced at cathode; O₂ produced at anode.

---

## Galvanic vs. Electrolytic — Full Comparison

| Feature | Galvanic | Electrolytic |
|---|---|---|
| Thermodynamics | Spontaneous ($\Delta G° < 0$) | Non-spontaneous ($\Delta G° > 0$) |
| $E°_{cell}$ | Positive | Negative (for reaction as written) |
| Energy direction | Produces electrical energy | Consumes electrical energy |
| Chambers | Separate half-cells | Often same chamber |
| Salt bridge | Required | Not needed |
| Power source | None | Required (battery/DC) |
| Real-world example | Battery, fuel cell | Electroplating, water splitting |

**True for BOTH types:**
- Oxidation at anode; reduction at cathode
- Cations migrate toward cathode; anions toward anode

---

## MCQ Pattern Recognition

| If you see... | It's testing... | Key move |
|---|---|---|
| "Which electrode increases in mass?" | Cathode = reduction = metal deposits | Cathode gains mass; anode loses mass |
| "Which solution is in each half-cell?" | Ion matches electrode metal | Anode half-cell has anode metal's ion; cathode has cathode metal's ion |
| "Calculate $E°_{cell}$" | $E°_{cathode} - E°_{anode}$ | Never flip signs; never scale $E°$ |
| "$\Delta G°$ is negative" | Spontaneous = galvanic | $\Delta G° < 0 \Leftrightarrow E°_{cell} > 0$ |
| "External power source required" | Electrolytic cell | $E°_{cell} < 0$ for the reaction |
| "Purpose of salt bridge" | Charge neutrality | Ions migrate to balance charge buildup |
| Inert electrode (Pt or graphite) | Non-solid reactant or product | Use inert when nothing plates or dissolves |

---

## FRQ Pattern Recognition

| Part says... | It's asking for... | Key move |
|---|---|---|
| "Identify anode and cathode" | Higher $E°$ = cathode; lower = anode | State reduction potentials and conclude |
| "Calculate $E°_{cell}$" | $E°_{cathode} - E°_{anode}$ | Show subtraction explicitly with sign |
| "Will the cell operate spontaneously?" | $E°_{cell} > 0$ check | State the sign and conclude |
| "Purpose of salt bridge" | Maintain electrical neutrality | State ion flow direction; state what happens without it |
| "What happens to electrode mass?" | Anode decreases; cathode increases | Link explicitly to oxidation/reduction |
| "What happens if concentration decreases?" | Nernst equation territory | Lower [cathode ion] → lower $E_{cell}$ |

---

## AP Answer Templates

**Identifying anode/cathode:**
> "Magnesium is the anode because it has the lower (more negative) standard reduction potential (−2.37 V), so it undergoes oxidation. Copper is the cathode because it has the higher standard reduction potential (+0.34 V), so it undergoes reduction."

**Cathode mass increases:**
> "The cathode mass increases because Cu²⁺ ions in solution are reduced and deposited as solid Cu: Cu²⁺(aq) + 2e⁻ → Cu(s)."

**Anode mass decreases:**
> "The anode mass decreases because solid Mg is oxidized to Mg²⁺ ions that enter solution: Mg(s) → Mg²⁺(aq) + 2e⁻."

**Salt bridge explanation:**
> "The salt bridge allows ions to flow between the two half-cells, maintaining electrical neutrality. Without it, positive charge would accumulate in the oxidation half-cell and negative charge in the reduction half-cell, stopping the reaction."

**Spontaneity:**
> "$E°_{cell}$ = +2.71 V > 0, therefore $\Delta G° < 0$, and the reaction is thermodynamically spontaneous. This cell operates as a galvanic cell."

---

## Critical Reminders

- **Never** change the sign of $E°$ — $E°_{cathode} - E°_{anode}$ already accounts for reversal
- **Never** multiply $E°$ by a coefficient — it is an intensive property
- Galvanic: spontaneous, $E°_{cell} > 0$, $\Delta G° < 0$, produces energy
- Electrolytic: non-spontaneous, $E°_{cell} < 0$, $\Delta G° > 0$, requires external voltage
- Anode always loses mass (metal oxidized); cathode always gains mass (metal deposits)
- Salt bridge electrolyte must be **inert** — cannot react with either half-cell solution
- Standard conditions: 1 M, 25°C, 1 atm — required for $E°$ values to apply exactly
