# Dashboard Design Decisions  
**Project:** Intern KPI Performance Dashboard  
**Tooling:** Power BI (Desktop via Azure VM)  
**Author Role:** Lead Analyst

---

## 1. KPI Date Logic — Handling Conflicting Timelines

One of the biggest analytical challenges in this project was that **performance tracking did not follow a single clean calendar**.

Three different “valid” KPI cutoffs existed:

| Date | Meaning | KPI Total | Use Case |
|------|--------|-----------|----------|
| **4/24/2018** | Official tracking cutoff (when reporting stopped) | 521 | Operational performance snapshot |
| **4/30/2018** | True end of calendar month | 654 | Monthly productivity view |
| **5/3–5/5/2018** | End of work cycle when late submissions came in | 755 | Workflow completion view |

### Decision
Rather than forcing a single “correct” number, the dashboard was designed to:
- Treat **4/24 as the official KPI performance benchmark**
- Acknowledge later dates in analysis to show **operational lag and workflow behavior**

### Why This Matters
This reflects real-world analytics:  
**Data timing affects performance evaluation**, and good BI design makes these assumptions transparent.

---

## 2. Fair Performance Targets (Floating Goals)

Interns joined the program at different times, so a fixed monthly goal would unfairly penalize newer participants.

### Decision
Performance was evaluated using:
- **Standard Goal** → Baseline expected output
- **Stretch Goal** → Aspirational target for high performers
- **Adjusted Monthly Goals** → Based on intern start date

### Why This Matters
This prevents misleading comparisons and demonstrates:
✔ Context-aware metrics  
✔ Fair performance modeling  
✔ Practical workforce analytics

---

## 3. KPI Metrics Chosen

| Metric | Purpose |
|-------|---------|
| **Total KPI** | Total placements completed |
| **Monthly % of Goal** | Measures performance vs adjusted target |
| **Weekly % of Target** | Detects short-term momentum or slowdown |
| **Performance Status** | Categorical summary for managers |
| **Total Placements** | Raw productivity volume |

### Design Principle
Executives get **summary performance**, managers get **action signals**, and analysts get **trend data**.

---

## 4. Performance Status Icons (Manager View Optimization)

The dashboard uses **icon-based indicators** instead of dense numeric tables for performance status.

| Status | Logic | Icon Meaning |
|--------|------|--------------|
| **Exceeds Target** | ≥ 100% of goal | Strong performer |
| **On Track** | 80–99% of goal | Stable performance |
| **Needs Support** | < 80% of goal | Manager attention needed |

### Decision
Icons were used because:
- Managers scan dashboards quickly
- Visual alerts outperform raw numbers
- Enables future drill-through to detailed views

Future enhancement: Separate visuals for **weekly vs monthly performance**.

---

## 5. Data Model Structure

A star schema was used for clarity and scalability.

**Fact Table**
- `Fact_Performance` → KPI activity per intern per date

**Dimension Tables**
- `Dim_Intern` → Intern details and start dates
- `Dim_Calendar` → Time intelligence

### Why This Matters
This supports:
✔ Time-based analysis  
✔ Fair goal adjustments  
✔ Scalable reporting structure

---

## 6. Slicers and Interactivity

Planned slicers:
- Intern Name
- Date / Week
- Performance Status

Purpose:
Allow managers to quickly isolate **who needs attention** without filtering manually.

---

## 7. Handling Ambiguity Transparently

Instead of hiding inconsistencies, the dashboard design:
- Documents assumptions
- Explains multiple valid KPI totals
- Distinguishes **operational cutoff vs calendar reporting**

This reflects how analytics is actually practiced in business environments.

## 8. KPI Goal Modeling Strategy

A key design decision in this project was how to model performance goals fairly across interns who:

Started at different times
Produced at different output levels
Were evaluated for both development and performance benchmarking

A single fixed KPI goal would have unfairly penalized newer interns while under-challenging experienced ones. To address this, a two-layer goal framework was implemented.

## Layer 1: Standardized Benchmark Goal

A fixed rate of 10.4 KPIs per week was used as a universal performance benchmark.

Purpose:

- Enable fair cross-intern comparisons
- Provide consistent visual reference lines in charts
- Support trend analysis over time

This benchmark is used in visuals such as:

- Weekly performance tracking
- Performance status indicators
- Goal vs actual comparisons

## Layer 2: Individualized Goal Tiers

In addition to the universal benchmark, each intern was evaluated against tiered goals:

Goal Tier	Description	                            Purpose
Safe Goal	Minimum sustainable performance level	Early warning indicator
Modest Goal	Standard expected performance	        Core performance measure
Reach Goal	High-performance stretch target	        Identifies top performers

These goals were derived within the Power BI model using tenure-based extrapolation and performance banding. They were not directly stored in the source data, reflecting how real performance systems often rely on modeled expectations rather than static targets.

Why This Approach Matters

This structure allows stakeholders to answer two different business questions:

Business Question	                                            Goal Type Used
“Who is performing above or below average?”	                    Standardized Benchmark
“Is this intern meeting expectations for their stage?”	        Individualized Goals

By separating comparison metrics from coaching metrics, the dashboard supports both executive reporting and performance development conversations.

## Real-World Relevance

This modeling approach reflects how workforce analytics operates in practice:

- Performance expectations change with tenure
- Not all employees are evaluated against identical targets
- Leadership needs both fairness and personalization in reporting

Designing this framework required balancing data integrity, fairness, and interpretability — a core challenge in people analytics and performance intelligence.
---

## 9. Author Contribution

As a lead analyst, responsibilities included:
- Defining KPI logic
- Designing the data model
- Building DAX measures
- Translating ambiguous reporting rules into structured metrics
- Designing manager-friendly performance views
