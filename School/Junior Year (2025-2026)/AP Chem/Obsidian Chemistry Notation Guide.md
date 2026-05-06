## Setup — Plugins to Install First
 
Go to **Settings → Community Plugins → Browse** and install:
 
- **Latex Suite** — typing shortcuts that auto-expand into symbols
- **Easy Typing** — smart punctuation and auto-pairs
- **Completr** — autocomplete for LaTeX math
 
> To enable community plugins: Settings → Community Plugins → turn off Safe Mode
 
---
 
## How Math Works in Obsidian
 
Obsidian supports **LaTeX math** natively (no plugin needed).
 
| Mode | Syntax | Use for |
|---|---|---|
| Inline math | `$...$` | Symbols inside a sentence |
| Block math | `$$...$$` | Full equations on their own line |
 
**Latex Suite shortcuts to enter math mode:**
 
| You type | Result |
|---|---|
| `mk` | Opens inline math `$ $` |
| `dm` | Opens display/block math `$$ $$` on its own line |
 
---
 
## Greek Letters & Thermodynamic Symbols
 
All of these work **inside math mode** (`$ $`) with Latex Suite installed.
 
| Symbol | Latex Suite Trigger | Raw LaTeX fallback |
|---|---|---|
| Δ (delta) | `@D` | `\Delta` |
| δ (lowercase delta) | `@d` | `\delta` |
| α (alpha) | `@a` | `\alpha` |
| β (beta) | `@b` | `\beta` |
| γ (gamma) | `@g` | `\gamma` |
| Σ (sigma) | `@S` | `\Sigma` |
| θ (theta) | `@t` | `\theta` |
| ε (epsilon) | `@e` | `\epsilon` |
 
**Chemistry-specific:**
 
| Symbol | Latex Suite Trigger | Raw LaTeX fallback | Renders as |
|---|---|---|---|
| ΔG° | `@D` then `G^\circ` | `\Delta G^\circ` | ΔG° |
| ΔH°rxn | `@D` then `H^\circ_{rxn}` | `\Delta H^\circ_{rxn}` | ΔH°rxn |
| ΔS°rxn | `@D` then `S^\circ_{rxn}` | `\Delta S^\circ_{rxn}` | ΔS°rxn |
| → (reaction arrow) | `->` | `\rightarrow` | → |
| ⇌ (equilibrium) | custom `eq` snippet (see below) | `\rightleftharpoons` | ⇌ |
| × (multiply) | `xx` | `\times` | × |
| ° (degree) | `^\circ` | `^\circ` | ° |
| ≥ | `>=` | `\geq` | ≥ |
| ≤ | `<=` | `\leq` | ≤ |
| ∞ | `ooo` | `\infty` | ∞ |
| ± | `+-` | `\pm` | ± |
 
> **Note:** The built-in `<->` gives ↔ (double arrow), not ⇌ (harpoons). Use the custom snippet below for equilibrium.
 
---
 
## Subscripts and Superscripts
 
Latex Suite **auto-applies** subscripts inside math mode when you type a number after a letter.
 
| What | Trigger | Example | Renders as |
|---|---|---|---|
| Superscript (single) | `^` | `x^2` | x² |
| Superscript (multi-char) | `rd` | opens `^{$0}` | x^{rxn} |
| Subscript (auto) | number after letter | `H2` → `H_{2}` | H₂ |
| Subscript (manual) | `_` | opens `_{$0}` | H_{2}O |
| Squared | `sr` | `x sr` → `x^{2}` | x² |
| Cubed | `cb` | `x cb` → `x^{3}` | x³ |
| Inverse | `invs` | `K invs` → `K^{-1}` | K⁻¹ |
 
> **Multi-character subscripts/superscripts:** always wrap in `{}` curly braces.
> `$\Delta G_{rxn}$` → ΔGrxn ✓
> `$\Delta G_rxn$` → only `r` gets subscripted ✗
 
---
 
## Common Chemistry Formulas
 
| Formula | Type this in `$ $` | Renders as |
|---|---|---|
| H₂O | `H_2O` | H₂O |
| CO₂ | `CO_2` | CO₂ |
| SO₄²⁻ | `SO_4^{2-}` | SO₄²⁻ |
| Al³⁺ | `Al^{3+}` | Al³⁺ |
| NH₃ | `NH_3` | NH₃ |
| Al₂O₃ | `Al_2O_3` | Al₂O₃ |
| Ca²⁺ | `Ca^{2+}` | Ca²⁺ |
| 1s²2s²2p⁶ | `1s^2 2s^2 2p^6` | 1s²2s²2p⁶ |
| K = 5.6×10⁵ | `K = 5.6 xx 10^5` | K = 5.6×10⁵ |
 
---
 
## Full Equation Examples
 
**Gibbs Free Energy:**
```latex
$$\Delta G^\circ = \Delta H^\circ - T\Delta S^\circ$$
```
 
**Equilibrium Expression:**
```latex
$$\Delta G^\circ = -RT\ln K$$
```
 
**Entropy Change:**
```latex
$$\Delta S^\circ_{rxn} = \sum S^\circ_{prod} - \sum S^\circ_{react}$$
```
 
**Reaction with states:**
```latex
$$2\ H_2(g) + O_2(g) \rightarrow 2\ H_2O(l)$$
```
 
**Equilibrium reaction:**
```latex
$$N_2(g) + 3\ H_2(g) \rightleftharpoons 2\ NH_3(g)$$
```
 
---
 
## Adding a Custom Snippet for ⇌
 
Go to **Settings → Latex Suite → Snippets** and add this line inside the array (before the last `]`):
 
```javascript
{trigger: "eq", replacement: "\\rightleftharpoons", options: "mA"},
```
 
Now typing `eq` inside math mode gives ⇌ automatically.
 
---
 
## Quick Reference Card
 
```
Enter math:    mk → inline $ $       dm → block $$ $$
 
Delta:         @D       →  \Delta     →  Δ
Degree:        ^\circ   →  °
Arrow:         ->       →  \to        →  →
Equilibrium:   eq       →  ⇌  (custom snippet)
Multiply:      xx       →  \times     →  ×
Squared:       sr       →  ^{2}
Cubed:         cb       →  ^{3}
Subscript:     _        →  _{  }
Superscript:   rd       →  ^{  }
Fraction:      //       →  \frac{  }{  }
 
ΔG°rxn:   $\Delta G^\circ_{rxn}$
ΔH°rxn:   $\Delta H^\circ_{rxn}$
ΔS°rxn:   $\Delta S^\circ_{rxn}$
H₂O:      $H_2O$
Al³⁺:     $Al^{3+}$
SO₄²⁻:    $SO_4^{2-}$
1s²2s²2p⁶: $1s^2 2s^2 2p^6$
```
