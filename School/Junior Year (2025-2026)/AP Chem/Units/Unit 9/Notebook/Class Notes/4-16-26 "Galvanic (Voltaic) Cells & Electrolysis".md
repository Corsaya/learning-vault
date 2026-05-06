## Topic 9.8 — Cell Potential, Spontaneity, and Electrolysis

---

## Core Concepts

A **galvanic (voltaic) cell** converts chemical energy to electrical energy via a spontaneous redox reaction. Spontaneity is confirmed by $E°_{cell} > 0$ and equivalently $\Delta G° < 0$. These two conditions always go together — if you know one, you know the other.

**Electrolysis** is the reverse process: an external power source drives a non-spontaneous reaction. The minimum voltage required equals the magnitude of the negative $E°_{cell}$ for that reaction. Real electrolytic cells require slightly more due to overpotential losses.

Understanding which species goes in which half-cell, how to calculate $E°_{cell}$ without making sign errors, and how to explain electrode mass changes are the three highest-frequency skills tested for this topic.

---

## Key Equations

$$\boxed{E°_{cell} = E°_{cathode} - E°_{anode}}$$

$$\Delta G° = -nFE°_{cell}$$

$$\text{At non-standard conditions: } E_{cell} = E°_{cell} - \frac{RT}{nF}\ln Q \quad \text{(Nernst equation)}$$

| Quantity | Relation to spontaneity |
|---|---|
| $E°_{cell} > 0$ | Spontaneous (galvanic) |
| $E°_{cell} < 0$ | Non-spontaneous (electrolytic) |
| $\Delta G° < 0$ | Spontaneous |
| $\Delta G° > 0$ | Non-spontaneous |
| $K > 1$ | Products favored at equilibrium |

The three quantities $E°_{cell}$, $\Delta G°$, and $K$ are all related and encode the same thermodynamic information.

---

## Mg–Cu Galvanic Cell — Full Setup

| Species | $E°$ (V) |
|---|---|
| $Cu^{2+}/Cu$ (cathode) | +0.34 V |
| $Mg^{2+}/Mg$ (anode) | −2.37 V |

$$E°_{cell} = +0.34 - (-2.37) = \textbf{+2.71 V}$$

**Half-cell solutions:**
- Anode half-cell: MgSO₄ or Mg(NO₃)₂ at 1 M — contains the ion of the anode metal
- Cathode half-cell: CuSO₄ or Cu(NO₃)₂ at 1 M — contains the ion of the cathode metal
- Salt bridge: KNO₃ or NaCl (inert, won't react with either solution)

**Standard conditions** (required for $E°$ to apply): 1 M, 25°C, 1 atm

---

## Electrolysis of Water — Reference Reaction

$$\text{Cathode: } 2H_2O + 2e^- \rightarrow H_2(g) + 2OH^-_{(aq)}$$
$$\text{Anode: } 2H_2O \rightarrow O_2(g) + 4H^+_{(aq)} + 4e^-$$

This reaction is non-spontaneous ($\Delta G° > 0$) — requires external electrical energy. H₂ is produced at the cathode (2:1 volume ratio vs. O₂).

---

## Concentration Effects (Nernst)

Under non-standard conditions, cell voltage shifts:

- Decreasing $[Cu^{2+}]$ (cathode ion) → Q increases → $E_{cell}$ decreases
- Increasing $[Mg^{2+}]$ (anode ion) → Q increases → $E_{cell}$ decreases
- At equilibrium: $E_{cell} = 0$ (dead battery)

The AP exam tests this qualitatively: know the direction of shift, not the calculation (unless given $RT/F$).

---

## MCQ Pattern Recognition

| If you see... | It's testing... | Key move |
|---|---|---|
| "Which solution is used in each half-cell?" | Matching ion to electrode metal | Anode cell → anode metal's ion; cathode cell → cathode metal's ion |
| "Calculate $E°_{cell}$" | $E°_{cathode} - E°_{anode}$ | Never flip signs; never scale $E°$ |
| "$\Delta G°$ is negative" | Spontaneous → galvanic | $\Delta G° = -nFE°$; negative $\Delta G°$ means positive $E°$ |
| "External power source required" | Electrolytic cell | $E°_{cell} < 0$ — not galvanic |
| "Salt bridge function" | Ion flow / charge neutrality | Ions migrate to balance charge buildup |
| "Concentration of cathode ion decreases" | Nernst — voltage drops | Lower [cathode ion] → lower $E_{cell}$ |
| "Cell at equilibrium" | $E_{cell} = 0$ | Dead battery condition |

---

## FRQ Pattern Recognition

| Part says... | It's asking for... | Key move |
|---|---|---|
| "Identify anode and cathode" | Higher $E°$ = cathode; lower = anode | State both $E°$ values; compare explicitly |
| "Calculate $E°_{cell}$" | $E°_{cathode} - E°_{anode}$ | Show the subtraction; include sign |
| "Is the reaction spontaneous?" | $E°_{cell} > 0$ check | State sign → conclude spontaneous or not |
| "Purpose of salt bridge" | Maintain electrical neutrality | Name ion flow directions; state consequence of removing it |
| "What happens if $[Cu^{2+}]$ decreases?" | Nernst qualitative | Q increases → $E_{cell}$ decreases below $E°_{cell}$ |
| "What is needed to make this non-spontaneous reaction proceed?" | External voltage = electrolysis | Minimum voltage = $|E°_{cell}|$ |

---

## AP Answer Templates

**Identifying anode/cathode:**
> "Magnesium is the anode because it has the lower (more negative) standard reduction potential (−2.37 V), so it undergoes oxidation. Copper is the cathode because it has the higher standard reduction potential (+0.34 V), so it undergoes reduction."

**Calculating $E°_{cell}$:**
> "$E°_{cell} = E°_{cathode} - E°_{anode} = (+0.34\text{ V}) - (-2.37\text{ V}) = +2.71\text{ V}$"

**Spontaneity justification:**
> "$E°_{cell}$ = +2.71 V > 0, therefore $\Delta G° < 0$, and the reaction is thermodynamically spontaneous."

**Effect of decreasing $[Cu^{2+}]$:**
> "Decreasing $[Cu^{2+}]$ shifts the reaction quotient Q to a larger value, which according to the Nernst equation causes $E_{cell}$ to decrease below $E°_{cell}$."

**Electrolysis requires:**
> "Because $E°_{cell} < 0$, the reaction is non-spontaneous and requires an external power source supplying a minimum voltage equal to the magnitude of $E°_{cell}$ to proceed."

---

## Critical Reminders

- **Never** change the sign of $E°$ — the formula handles reversal automatically
- **Never** multiply $E°$ by a coefficient — it is an intensive property
- $E°_{cell} > 0 \Leftrightarrow \Delta G° < 0 \Leftrightarrow K > 1$ — all three say the same thing
- Galvanic: produces energy, $E° > 0$, spontaneous
- Electrolytic: consumes energy, $E° < 0$, non-spontaneous
- Salt bridge must be inert — it cannot react with either half-cell solution
- Anode loses mass; cathode gains mass — always link this to the half-reaction
- Standard conditions (1 M, 25°C, 1 atm) are required for $E°$ values to apply exactly; deviations invoke Nernst
