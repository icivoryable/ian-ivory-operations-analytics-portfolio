### Advanced DAX Measures  
These measures were designed to extend the dashboard with trend analysis, peer comparison, and performance stability metrics.

They represent advanced KPI modeling that depends on consistent time-series data and a fully aligned production data model.

---

## Implementation Note

These measures were prototyped in Power BI Desktop but were not fully operationalized in the shared version of the project due to:

- Environment access limitations (Azure VM session ended)
- Differences between the desktop dataset and synthetic documentation dataset
- Inconsistent historical reporting cutoffs

The logic is included to demonstrate advanced analytical design.

---

## 1. Previous Week KPI

**Purpose:** Captures KPI value from the prior week for comparison.

Previous Week KPI =
CALCULATE(
    [Total KPI],
    DATEADD('Dim_Calendar'[Date], -7, DAY)
)

## 2. Week-over-Week Change
**Purpose: Measures week-to-week performance change.**

WoW Change =
[Total KPI] - [Previous Week KPI]

## 3. Week-over-Week % Change
**Purpose: Shows performance growth or decline rate.**

WoW % Change =
DIVIDE ( [WoW Change], [Previous Week KPI], 0 )

## 4. Trend Direction
**Purpose: Converts change into a readable indicator.**

Trend Direction =
SWITCH(
    TRUE(),
    [WoW Change] > 0, "Improving",
    [WoW Change] < 0, "Declining",
    "Stable"
)

## 5. Performance Rank
**Purpose: Ranks interns based on total KPI performance.**

Performance Rank =
RANKX(
    ALL('Dim_Intern'[Intern Name]),
    [Total KPI],
    ,
    DESC,
    DENSE
)

## 6. Average Weekly Performance
**Purpose: Normalizes output across weeks for fair comparison.**

Average Weekly Performance =
DIVIDE(
    [Total KPI],
    DISTINCTCOUNT('Dim_Calendar'[Week]),
    0
)

## 7. Performance Consistency (Standard Deviation)
**Purpose: Measures stability of weekly output.**

Performance Consistency =
STDEV.P ( Fact_Performance[KPI_Actual] )

# Lower values indicate more consistent performance.

## 8. Normalized Performance Score
**Purpose: Combines volume and consistency into a comparative score.**

Normalized Performance Score =
DIVIDE(
    [Average Weekly Performance],
    [Performance Consistency],
    0
)

## Summary
These advanced measures were designed to provide:

- Trend monitoring
- Peer benchmarking
- Stability analysis
- Predictive performance signals