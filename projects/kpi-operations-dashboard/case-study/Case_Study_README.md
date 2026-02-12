### Case Study: Intern KPI Performance Analysis

### Objective
Evaluate intern recruiting performance against defined targets while accounting for inconsistent KPI cutoff dates and submission timing effects.

### Challenge
The original KPI process suffered from:
- Mid-week tracking termination (4/24)
- Weekend submission spikes (5/3–5/5)
- Mixed use of weekly, monthly, and stretch targets
- Loss of original data sources

These issues made traditional month-end reporting misleading.

### Approach
- Rebuilt the data model using synthetic data aligned to observed totals
- Implemented a dedicated calendar table for time intelligence
- Created DAX measures to dynamically evaluate performance under different cutoff scenarios
- Designed visuals to emphasize trends, consistency, and rank rather than raw totals alone

### Outcome
The analysis revealed that:
- Several interns missed targets at the official cutoff but exceeded expectations during the submission window
- Top performers significantly exceeded standard goals while narrowly missing stretch goals
- A portion of underperformance was process-driven, not behavioral

This reframed performance discussions from “who failed” to “where the process breaks down.”
