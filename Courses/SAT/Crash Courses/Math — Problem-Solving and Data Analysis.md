---
tags: [pytheas, sat, math, psda, crash-course]
created: 2026-08-12
source: "Foundations Knowledge Check P1-P9"
related: ["[[../Foundations Knowledge Check]]", "[[../Diagnostic Gap Lessons (2026-08-07)]]"]
---

# Math — Problem-Solving & Data Analysis Crash Course

Per [[../Research/Official SAT Structure and Content Research (2026-08-07)|the Official SAT Structure research]], this domain is worth **~15% of the Math section (5–7 questions)** — this doc covers all nine skills tracked as P1–P9 in [[../Foundations Knowledge Check]].

---

### P1 — Percent of a number, percent increase/decrease (chained/multi-step)

Already fully covered — this was a confirmed diagnostic gap and got its own lesson. The short version: convert percent to a decimal and multiply; for a discount then tax (or any chained percent problem), each step applies to the **current** value, not the original. Full worked examples, practice, and answers here: [[../Diagnostic Gap Lessons (2026-08-07)#Lesson 4 — Problem-Solving & Data Analysis: percent-of-a-number refresher]].

**Worked example:** An $80 jacket is marked up 25%, and then a 10% discount is applied to the marked-up price. What is the final price?
$$80 \times 1.25 = 100$$
$$100 \times 0.90 = \$90$$

**Trips people up:** it's tempting to think a 25% increase followed by a 10% decrease nets out to a flat 15% increase — it doesn't, because the second percentage applies to the new, larger value ($100), not the original $80. Always chain the multipliers, never the raw percentages.

**Worked example 2:** A town's population of 2,000 grows by 8% in one year, then declines by 5% the following year. What is the population after the second year, rounded to the nearest whole number?
$$2000 \times 1.08 = 2160$$
$$2160 \times 0.95 = 2052$$

**Trips people up:** "grows 8%, then declines 5%" is not the same as a net 3% change — each percentage is applied to a different base value (2,000, then 2,160), so the two percentages don't simply subtract from each other.

---

### P2 — Ratios and proportions

**What this actually tests:** whether you can set up two equivalent fractions and solve for a missing piece — recipes scaled up, map scales, mixture problems, "for every X there are Y" setups.

**The core move:** write the ratio as a fraction, set it equal to a second fraction with the unknown, and cross-multiply.
$$\frac{a}{b} = \frac{c}{d} \implies ad = bc$$
Keep the same *quantity* in the same position in both fractions (e.g., always flour on top, sugar on bottom) — mixing up which number goes where is the #1 source of errors here, not the algebra itself.

**Worked example:** A recipe uses flour to sugar in a ratio of 5 : 3. A baker uses 40 cups of flour. How much sugar is needed?
$$\frac{5}{3} = \frac{40}{x}$$
$$5x = 120$$
$$x = 24 \text{ cups of sugar}$$

**Trips people up:** watch for ratios given as "5 to 3" vs. "5 : 8" (part-to-part vs. part-to-whole) — reread the question to confirm which one you're given before setting up the fraction.

**Worked example 2:** A map has a scale of 3 cm : 50 km. Two towns are 11 cm apart on the map. How many kilometers apart are they?
$$\frac{3}{50} = \frac{11}{x}$$
$$3x = 550$$
$$x = 183.\overline{3} \text{ km}$$

**Trips people up:** the answer isn't always a clean whole number — don't round the setup or the cross-multiplication early; keep the fraction exact until the final answer.

**Worked example 3:** A paint mixture uses blue and white paint in a ratio of 2 : 5. A painter needs 35 liters of the mixture total. How many liters of blue paint are needed?
The ratio 2 : 5 is part-to-part, so the mixture has $2 + 5 = 7$ total "parts." Each part is $35 \div 7 = 5$ liters.
$$\text{blue} = 2 \times 5 = 10 \text{ liters}$$

**Trips people up:** when a ratio is part-to-part but the question gives you the *total* amount, you must first find the whole (sum of the parts) before scaling — dividing 35 by 2 or by 5 directly is a common wrong-answer trap.

---

### P3 — Unit conversion / rate problems

**What this actually tests:** converting between units (minutes ↔ hours, miles ↔ feet) and applying a rate (amount per unit time) — often both in the same question.

**The core move:** treat a rate as a fraction (quantity / time) and multiply by a conversion factor written as a fraction that cancels the unit you don't want:
$$\text{rate} \times \text{new time} = \text{total amount}$$
When converting, write the conversion as a fraction equal to 1 (e.g., $\frac{60 \text{ min}}{1 \text{ hr}}$) so the unwanted unit cancels on paper — this keeps you from accidentally multiplying when you should divide.

**Worked example:** A pump fills bottles at a rate of 3 widgets every 8 minutes. At this rate, how many widgets does it produce in 6 hours?
$$6 \text{ hr} \times \frac{60 \text{ min}}{1 \text{ hr}} = 360 \text{ min}$$
$$\frac{3 \text{ widgets}}{8 \text{ min}} \times 360 \text{ min} = \frac{3 \times 360}{8} = 135 \text{ widgets}$$

**Shortcut:** convert everything to one consistent unit *first* (here, minutes), then apply the rate once — don't try to convert mid-calculation.

**Worked example 2:** A car travels at a constant 55 miles per hour. How many miles does it travel in 45 minutes?
$$45 \text{ min} = 0.75 \text{ hr}$$
$$55 \text{ mph} \times 0.75 \text{ hr} = 41.25 \text{ miles}$$

**Shortcut:** since the rate is already given per hour, convert the time to a fraction of an hour (45 min = 0.75 hr) instead of converting the rate to minutes — fewer conversion steps, fewer chances to slip.

**Worked example 3:** A printer produces 8 pages every 15 seconds. At this rate, how many pages does it produce in 10 minutes?
$$10 \text{ min} \times \frac{60 \text{ sec}}{1 \text{ min}} = 600 \text{ sec}$$
$$\frac{8 \text{ pages}}{15 \text{ sec}} \times 600 \text{ sec} = \frac{8 \times 600}{15} = 320 \text{ pages}$$

**Shortcut:** since the rate is given in seconds, convert the 10 minutes into seconds (not the rate into minutes) — always convert toward whichever unit the rate is already expressed in.

---

### P4 — Mean, median, mode, range — outliers

**What this actually tests:** computing the four basic stats and, more importantly, reasoning about how an outlier distorts each one differently.

**The core rules:**
- **Mean** = sum of values ÷ count. Pulled hard toward outliers.
- **Median** = middle value when sorted (average the middle two if the count is even). Resistant to outliers.
- **Mode** = most frequent value (can be none, one, or several).
- **Range** = max − min.

**Worked example:** Six data points: $4, 7, 7, 9, 12, 50$.
$$\text{mean} = \frac{4+7+7+9+12+50}{6} = \frac{89}{6} \approx 14.83$$
$$\text{median: sorted already} \to \frac{7+9}{2} = 8$$
$$\text{mode} = 7 \qquad \text{range} = 50 - 4 = 46$$
The mean (≈14.8) is dragged well above where most of the data actually sits, because the outlier ($50$) pulls it up; the median (8) stays representative of the typical value. This gap — mean noticeably higher/lower than median — is exactly what SAT questions are testing when they ask "which measure better represents the data" after showing an outlier.

**Trips people up:** "range" sounds like it should be an interval — it's a single number (max − min), not "4 to 50."

**Worked example 2:** Six data points: $10, 12, 12, 13, 15, 90$.
$$\text{mean} = \frac{10+12+12+13+15+90}{6} = \frac{152}{6} \approx 25.33$$
$$\text{median: sorted already} \to \frac{12+13}{2} = 12.5$$
$$\text{mode} = 12 \qquad \text{range} = 90 - 10 = 80$$
Just like before, the outlier (90) drags the mean up to ≈25.3, far above where five of the six values actually cluster (10–15), while the median (12.5) stays close to the typical value — and unlike the mean, the mode and the "typical" sense of the data are untouched by the outlier.

**Trips people up:** a large range (80) tells you the data is spread out somewhere, but by itself it doesn't tell you *where* the bulk of the data sits — don't confuse "big range" with "big mean shift"; here almost all the spread comes from a single point.

**Worked example 3:** Seven data points, all distinct: $5, 40, 42, 44, 46, 48, 90$.
$$\text{mean} = \frac{5+40+42+44+46+48+90}{7} = \frac{315}{7} = 45$$
$$\text{median: sorted already} \to 44 \text{ (the 4th of 7 values)}$$
$$\text{mode} = \text{none} \qquad \text{range} = 90 - 5 = 85$$
Here there are two outliers pulling in opposite directions (5 low, 90 high), and they partly offset each other — the mean (45) and median (44) end up close together despite the wide spread.

**Trips people up:** a data set doesn't have to have a mode — when every value is distinct, the correct answer is "no mode," not a forced guess at the closest repeated-looking number.

---

### P5 — Two-way frequency tables

**What this actually tests:** reading a table with two categories (rows and columns) and correctly picking the right row, column, or cell to answer a fraction/percent question — the hard part is identifying the right denominator, not the arithmetic.

**The core move:** identify whether the question wants a fraction of a **row total**, a **column total**, or the **grand total**, then divide the relevant cell(s) by that total.

**Table — survey of 100 students on preferred pet:**

|          | Dogs | Cats | Total |
|----------|------|------|-------|
| Freshman | 28   | 12   | 40    |
| Senior   | 22   | 38   | 60    |
| **Total**| 50   | 50   | 100   |

**Worked example:** Of the students who prefer cats, what percentage are seniors?
"Of the students who prefer cats" means the denominator is the **Cats column total** (50), not 100.
$$\frac{38}{50} = 0.76 = 76\%$$

**Trips people up:** using the grand total (100) by default instead of the column/row the question actually restricts you to — always find the phrase "of the ___" and use that group's total as the denominator.

**Worked example 2 (using the same table):** Of the freshmen, what percentage prefer dogs?
"Of the freshmen" means the denominator is the **Freshman row total** (40), not 100 and not the Dogs column total (50).
$$\frac{28}{40} = 0.70 = 70\%$$

**Trips people up:** it's easy to reflexively grab the Dogs column total (50) since the question mentions dogs — but "of the freshmen" is the restricting phrase, so the row total (40) is the correct denominator, and 28 (freshmen who prefer dogs) is the numerator.

**Worked example 3 (using the same table):** What percentage of all 100 surveyed students prefer dogs?
With no restricting phrase like "of the seniors" or "of the students who prefer cats," the denominator is the **grand total** (100).
$$\frac{50}{100} = 50\%$$

**Trips people up:** this is the one case where the grand total *is* correct — the skill isn't "never use 100," it's "read the question first and use whichever total it actually specifies."

---

### P6 — Scatterplot: line of best fit, interpreting slope

**What this actually tests:** using a given line-of-best-fit equation to predict a value, and translating the slope into a plain-English rate. You are never asked to compute the regression line by hand — it's either given or shown on the graph.

**The core rule:** a line of best fit has the form $y = mx + b$. To predict, plug in $x$. To interpret the slope $m$ in context: "for each additional [unit of $x$], [$y$] changes by $m$ [units of $y$], on average."

**Table — hours studied vs. test score (5 students):**

| Hours studied ($x$) | Test score ($y$) |
|---|---|
| 2 | 71 |
| 4 | 77 |
| 5 | 82 |
| 7 | 91 |
| 8 | 93 |

The points don't fall exactly on a line (real data scatters), but the line of best fit for this data is given as:
$$y = 62 + 4x$$

**Worked example:** Using the line of best fit, predict the score for a student who studies 7 hours, and interpret the slope.
$$y = 62 + 4(7) = 62 + 28 = 90$$
Slope interpretation: each additional hour studied is associated with an average increase of 4 points on the test.

**Trips people up:** the $y$-intercept ($62$ here) is *not* "the score with zero studying" in a literal sense if $x=0$ falls outside the tested range — the SAT sometimes asks you to note this ("no data point near $x=0$" is a valid critique of extrapolating).

**Worked example 2:** A line of best fit relating hours of TV watched per day ($x$) to practice-exam score ($y$) is given as $y = 95 - 3x$. Predict the score for someone who watches 4 hours of TV per day, and interpret the slope.
$$y = 95 - 3(4) = 95 - 12 = 83$$
Slope interpretation: each additional hour of TV watched per day is associated with an average **decrease** of 3 points on the exam.

**Trips people up:** a negative slope means $y$ goes *down* as $x$ goes up — after seeing a positive-slope example, it's easy to default to "increases by" out of habit even when the coefficient is negative.

**Worked example 3:** A line of best fit relating years of work experience ($x$) to hourly wage in dollars ($y$) is given as $y = 18 + 1.5x$. Predict the wage for someone with 12 years of experience, and interpret the slope.
$$y = 18 + 1.5(12) = 18 + 18 = 36$$
Slope interpretation: each additional **year** of experience is associated with an average increase of \$1.50 in hourly wage.

**Trips people up:** the slope's units come from the table's $x$-axis label — misreading "\$1.50 per year" as "\$1.50 per month" (or dropping the unit entirely) is a common way to lose the point even after doing the arithmetic correctly.

---

### P7 — Basic probability from a table or set

**What this actually tests:** probability = favorable outcomes ÷ total possible outcomes, usually pulled directly from a table, often with a "given that" condition that restricts the denominator to one row or column.

**The core rule:**
$$P(\text{event}) = \frac{\text{count of outcomes matching the event}}{\text{total count in the relevant group}}$$
"Given that" or "if selected from [group]" restricts your denominator to just that subgroup, same logic as P5.

**Worked example (using the P5 table):** If a student is selected at random from the seniors, what is the probability that the student prefers dogs?
"Given that" the student is a senior restricts the denominator to the Senior row total (60):
$$P(\text{dogs} \mid \text{senior}) = \frac{22}{60} = \frac{11}{30} \approx 0.367 = 36.7\%$$

**Shortcut:** this is the same skill as P5 with "probability" language instead of "percentage" language — if you can find the right cell and denominator for a two-way table, you already know how to do both.

**Worked example 2 (using the P5 table):** If a student is selected at random from the freshmen, what is the probability that the student prefers cats?
"Given that" the student is a freshman restricts the denominator to the Freshman row total (40):
$$P(\text{cats} \mid \text{freshman}) = \frac{12}{40} = \frac{3}{10} = 30\%$$

**Shortcut:** same move as example 1, just a different row/cell — lock in on the group named right after "given that" or "selected from," find its row or column total, then read off the matching cell.

**Worked example 3:** A bag contains 5 red marbles, 3 blue marbles, and 2 green marbles. If one marble is drawn at random, what is the probability that it is **not** red?
$$\text{total marbles} = 5 + 3 + 2 = 10 \qquad \text{not red} = 3 + 2 = 5$$
$$P(\text{not red}) = \frac{5}{10} = 50\%$$

**Shortcut:** for "not" questions, you can either count the complement directly (as above) or compute $1 - P(\text{red}) = 1 - \frac{5}{10} = \frac{5}{10}$ — same answer, use whichever is faster to count.

---

### P8 — Standard deviation (conceptual)

**What this actually tests:** whether you understand standard deviation as a measure of **spread** (how far values tend to be from the mean) — you are never asked to compute it by hand on the SAT, only to compare or reason about it.

**The core rule:** larger standard deviation = data points are more spread out from the mean; smaller standard deviation = data points are tightly clustered near the mean. Two data sets can have the *same mean* and very different standard deviations.

**Worked scenario:** Two vending machines both advertise 30-gram bags of chips. Sampled bag weights (grams):
- Machine A: $29, 30, 30, 31, 30$
- Machine B: $20, 25, 30, 35, 40$

Both sets have a mean of exactly 30 g. Which machine has the greater standard deviation, and what does that mean in practice?
Machine B's weights are much farther from 30 on average (as far as 10 g off) while Machine A's weights stay within 1 g of 30. So **Machine B has the greater standard deviation** — its bags are far less consistent, even though both machines average out to the advertised weight.

**Trips people up:** adding the same constant to every value in a set shifts the mean but does **not** change the standard deviation (the spread between values is unchanged); multiplying every value by a constant *does* scale the standard deviation by that same constant.

**Worked scenario 2:** Two classes both average an 80 on a test. Sampled scores:
- Class A: $78, 79, 80, 81, 82$
- Class B: $60, 70, 80, 90, 100$

Both sets have a mean of exactly 80. Which class has the smaller standard deviation, and what does that mean in practice?
Class A's scores stay within 2 points of 80, while Class B's scores range as far as 20 points from 80. So **Class A has the smaller standard deviation** — its scores are much more tightly clustered around the average, meaning performance was more consistent even though the class average is identical to Class B's.

**Trips people up:** two groups can have the exact same mean and completely different levels of consistency — "the average is the same" tells you nothing about how spread out the individual values are; that's what standard deviation is for.

**Worked scenario 3:** A data set has a standard deviation of 5. If every value in the set is increased by 10, what is the new standard deviation? If instead every value in the original set is doubled, what is the new standard deviation?
Adding a constant (10) to every value shifts the whole set up but does not change how far apart the values are from each other, so the standard deviation stays **5**. Doubling every value stretches the distances between values by the same factor, so the standard deviation becomes $5 \times 2 = 10$.

**Trips people up:** students often assume any transformation of the data changes the standard deviation — shifting (adding/subtracting a constant) never does; scaling (multiplying/dividing by a constant) always does, by that same factor.

---

### P9 — Margin of error / sampling (conceptual)

**What this actually tests:** reasoning about what actually makes a survey estimate trustworthy — sample size and randomness — without any computation.

**The core rules:**
- A **larger, randomly selected** sample produces a **smaller margin of error** (more precision), all else equal.
- Margin of error only accounts for random sampling variability — it does **not** fix a **biased** sample (e.g., a non-representative location or self-selected respondents). A huge biased sample can still be a bad estimate.
- "Margin of error" describes a range the true population value likely falls within — a smaller margin means a tighter, more confident estimate.

**Worked scenario:** A researcher wants to estimate what percentage of a city's residents support a new transit proposal. Option A: survey 50 people outside a single downtown train station. Option B: survey 800 randomly selected residents from across the whole city. Which gives a better estimate, and why?
Option B is better on *two* counts: its sample is random and representative of the whole city (Option A is biased toward people who already ride transit, regardless of sample size), and its much larger sample size would shrink the margin of error even if both were equally random. A bigger sample doesn't rescue a biased one — Option A's core problem is *who* was asked, not *how many*.

**Trips people up:** "increase the sample size" is only a valid fix for margin of error if the sampling method is already random/unbiased — the SAT sometimes offers "survey more people at the same biased location" as a wrong-answer trap.

**Worked scenario 2:** Two researchers each survey 100 people about a new product. Researcher A randomly selects 100 people from the entire customer database. Researcher B posts a link to an online survey and collects responses from the first 100 people who click it. Which survey gives the more trustworthy estimate, even though both have the same sample size?
Researcher A's survey is more trustworthy. Even though both samples are the same size (100), Researcher B's sample is **self-selected** — only people motivated enough to click the link responded, which is not representative of the full customer base. Random selection (Researcher A) is what makes a sample size's margin of error meaningful in the first place.

**Trips people up:** matching sample sizes does not make two surveys equally reliable — a self-selected or volunteer sample is biased regardless of how large it is, and the SAT tests whether you notice *how* the sample was chosen, not just *how many* people were in it.

**Worked scenario 3:** A pollster estimates state-wide opinion by calling 5,000 residents on landline phones only, in a state where the majority of adults under 40 no longer have a landline. Is a 5,000-person sample enough to guarantee a reliable estimate here? Why or why not?
No. Even though 5,000 is a large sample, calling landlines only systematically **excludes** most younger adults, so the sample is biased toward older residents regardless of its size. A larger sample reduces margin of error only for random sampling variability — it does nothing to correct for a group being left out of the sampling method entirely.

**Trips people up:** a big, precise-sounding sample size can create false confidence — always check *who could actually be reached* by the sampling method before trusting the size alone.

---

## Mini-Diagnostic

One question per skill, P1–P9. Work them cold, then check the answer key.

**P1.** A \$150 jacket is discounted 20%, and then a 6% sales tax is applied to the discounted price. What is the final price?

**P2.** A map has a scale of 2 inches : 15 miles. Two cities are 7 inches apart on the map. How many miles apart are they?

**P3.** A pump fills a tank at a rate of 12 gallons every 5 minutes. At this rate, how many gallons will it fill in 2 hours?

**P4.** Six employees have the following years of experience: $2, 3, 3, 4, 5, 25$. By how much does the mean exceed the median?

**P5.** Survey of 80 gym members:

|             | Cardio | Weights | Total |
|-------------|--------|---------|-------|
| Under 30    | 18     | 22      | 40    |
| 30 and over | 26     | 14      | 40    |
| **Total**   | 44     | 36      | 80    |

What percentage of members under 30 prefer weights?

**P6.** A line of best fit relating hours of sleep ($x$) to reaction time in milliseconds ($y$) is $y = 450 - 15x$. Based on this line, what is the predicted reaction time for someone who sleeps 6 hours, and what does the slope mean in context?

**P7.** Using the table from P5, if a member is selected at random from those aged 30 and over, what is the probability that the member prefers cardio?

**P8.** Two vending machines both advertise 30-gram bags of chips. Machine A's sampled bags weigh $29, 30, 30, 31, 30$ grams. Machine B's sampled bags weigh $20, 25, 30, 35, 40$ grams. Which machine has the greater standard deviation?

**P9.** A researcher wants to estimate the average number of hours per week adults in a state spend exercising. Which would produce a smaller margin of error, all else equal: surveying 200 randomly selected adults statewide, or surveying 1,000 randomly selected adults statewide? Why?

---

### Answer key

**P1.** $150 \times 0.80 = 120$; $120 \times 1.06 = \$127.20$.

**P2.** $\frac{2}{15} = \frac{7}{x} \Rightarrow 2x = 105 \Rightarrow x = 52.5$ miles.

**P3.** $2 \text{ hr} = 120 \text{ min}$; $\frac{12}{5} \times 120 = 288$ gallons.

**P4.** Mean $= \frac{2+3+3+4+5+25}{6} = \frac{42}{6} = 7$. Median (sorted, middle two are 3 and 4) $= 3.5$. Difference: $7 - 3.5 = 3.5$.

**P5.** Denominator is the Under-30 row total (40): $\frac{22}{40} = 55\%$.

**P6.** $y = 450 - 15(6) = 450 - 90 = 360$ ms. Slope: each additional hour of sleep is associated with a 15 ms decrease in reaction time, on average.

**P7.** Denominator is the 30-and-over row total (40): $\frac{26}{40} = \frac{13}{20} = 65\%$.

**P8.** Both average 30 g, but Machine B's weights are much farther from 30 (up to 10 g off) vs. Machine A's (within 1 g). **Machine B** has the greater standard deviation.

**P9.** The 1,000-person sample — a larger random sample size reduces margin of error (more precision), all else equal.
