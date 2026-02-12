# Intern KPI Performance Dashboard  
**Business Intelligence Case Study**

##  Project Overview

This project analyzes performance data from a multi-state internship training program designed to track placement activity and productivity across participants.

The goal was to design a **manager-friendly KPI dashboard** that fairly evaluates intern performance while accounting for varying start dates, shifting deadlines, and real-world reporting inconsistencies.

This repository focuses on **data modeling, KPI design, and dashboard decision-making** rather than only the final visual output.

Some implementation details, weighting formulas, and internal workflows have been generalized to protect proprietary methods while preserving the integrity of the framework design.

---

##  My Role

I served as a lead analyst on this project, contributing to both the performance measurement framework and the reporting design. My work focused on translating raw KPI activity into meaningful performance insights that leadership could use for evaluation and coaching.

I helped define the standardized benchmarking approach, structure individualized goal tiers, and design dashboard logic that balanced fair comparison with personalized performance expectations. This required not only technical data modeling in Power BI, but also thoughtful consideration of how metrics influence decision-making and employee development.

**Lead Analyst**

I was responsible for:
- Translating ambiguous KPI rules into measurable logic
- Designing the data model
- Writing DAX measures for performance evaluation
- Defining fair goal adjustments
- Designing manager-facing performance indicators

This project demonstrates not just dashboard building, but **how to think through messy real-world performance data**.

---

##  Business Problem

Managers needed to:
- Track intern placement performance
- Identify who was on track vs who needed support
- Account for interns joining at different times
- Interpret performance despite shifting reporting cutoffs

The challenge:  
**Performance data did not align to a single clean timeline**, making KPI evaluation ambiguous without structured logic.

---

##  Key Analytical Challenges

### 1 Multiple Valid KPI Totals
Performance could be measured using three different cutoffs:

| Cutoff | KPI Total | Interpretation |
|--------|-----------|---------------|
| 4/24/2018 | 521 | Official reporting deadline |
| 4/30/2018 | 654 | Calendar month total |
| 5/3–5/5/2018 | 755 | Final submissions processed |

Rather than picking one blindly, the dashboard distinguishes **official performance** from **workflow completion**.

---

### 2 Fair Goal Setting
Interns joined at different times, so static goals were replaced with:

- Adjusted monthly targets  
- Standard goals  
- Stretch goals for high performers  

This ensures comparisons are equitable and performance insights are meaningful.

---

##  KPIs Designed

| KPI | Purpose |
|-----|---------|
| Total KPI | Total placements completed |
| Monthly % of Goal | Performance vs adjusted target |
| Weekly % of Target | Short-term performance signal |
| Performance Status | Manager-friendly performance label |
| Total Placements | Raw productivity output |

---

##  Data Model

A star schema was used:

**Fact Table**
- Performance activity per intern

**Dimensions**
- Intern details and start date
- Calendar for time analysis

This structure supports scalable, time-based reporting and fair performance comparisons.

---

##  Dashboard Design Approach

The dashboard was built for **two audiences**:

### Managers
- Visual performance status icons
- Clear identification of interns needing support
- Quick filtering by intern or timeframe

### Leadership
- Aggregate KPI performance
- State-level trends
- Program effectiveness insights

---

##  Technical Environment

- Power BI Desktop (hosted via Azure VM)
- DAX for KPI calculations
- Star schema data modeling

Due to environment access limitations after development, the final PBIX file   
Instead, this repository documents the full analytical logic, schema design, and dashboard decisions.

---

##  Repository Contents

├── README.md                ← Case study narrative
├── Executive Summary README.md
├── data/
│   └── synthetic_schema.md  ← Tables + fields
├── dax/
│   ├── core_measures.md
│   └── advanced_measures.md
├── visuals/
│   ├── overview_page.png
│   ├── intern_table.png
│   └── performance_status.png
|── assumptions/
|   ├── assumptions and cutoffs.md
|── power-bi/
|   ├── kpi-week22.pbix
└── design-decisions.md      