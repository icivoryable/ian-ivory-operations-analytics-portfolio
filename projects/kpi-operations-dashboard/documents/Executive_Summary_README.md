### Executive Summary

This dashboard represents an operational KPI tracking system built under real-world infrastructure constraints. Due to source system limitations, the model was reconstructed using synthetic data and partial exports. The goal of this project is to demonstrate KPI design, performance logic, and executive reporting — not production data fidelity.
This project reconstructs and analyzes intern recruiting KPIs using Power BI under real-world constraints: incomplete source data, inconsistent reporting cutoffs, and conflicting performance definitions. Names anonymized for privacy. Dataset reconstructed using synthetic data to preserve confidentiality.

Rather than enforcing a single interpretation, the model supports multiple reporting lenses (official cutoff, month-end, and submission window) to surface how timing decisions materially impact performance narratives.

The dashboard enables leadership to:
- Identify top and bottom performers with confidence
- Separate individual underperformance from process-driven delays
- Evaluate consistency and momentum, not just totals

The solution emphasizes transparent assumptions, robust DAX modeling, and executive-ready visual storytelling.

Some implementation details, weighting formulas, and internal workflows have been generalized to protect proprietary methods while preserving the integrity of the framework design.

### Business Context
This analysis supported a multi-state intern training program designed to:

Teach data collection discipline
Introduce Tableau and Power BI workflows
Track KPI accountability across geographic regions
As a result, the data reflects learning curves, reporting delays, and shifting definitions — all explicitly handled in the model.

### Infrastructure & Environment

- Azure Virtual Machine (Windows)
- Secure RDP access from macOS (M1)
- Cross-OS development workflow
- Power BI Desktop (VM-hosted)
- Power BI Service (Web)

This setup enabled enterprise BI development without native Windows hardware and mirrors real-world remote analytics environments where local tooling constraints require cloud-based development.


### Data Model
The model follows a simplified star schema:

Fact_Performance: KPI activity by intern and date
Dim_Intern: Intern metadata
Dim_Calendar: Time intelligence support
Synthetic data was used to reconstruct observed KPI totals after original source files became unavailable.

### Key Capabilities
Dynamic KPI evaluation using DAX measures
Time-aware performance analysis (WoW, cumulative)
Performance tiering with icon-based indicators
Intern-level and state-level rollups
Explicit handling of reporting cutoff ambiguity

### Environment Note
This dashboard was developed in Power BI Desktop within a cloud VM environment. Due to environment access limitations after development, the final PBIX file does not include all calculations.

To ensure reproducibility, this repository documents:

The full data schema
KPI logic
DAX measures
Dashboard layout decisions
Business interpretation of results

### Repository Structure
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