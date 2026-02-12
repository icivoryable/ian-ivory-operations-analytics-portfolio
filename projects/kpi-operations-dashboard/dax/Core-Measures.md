# Core DAX Measures  
These measures form the foundation of the Intern KPI Performance Dashboard and were successfully implemented in the working Power BI data model.

They power the primary visuals used by managers to evaluate performance and identify where support is needed.

---

## Implementation Note

These measures were originally developed in Power BI Desktop.  
Due to environment access limitations and differences between the desktop model and the synthetic dataset used for documentation, not all measures are currently active in the shared version of the project.

The logic is preserved here to demonstrate KPI design, performance modeling, and analytical approach.

---

## 1. Total KPI (Total Placements)

**Purpose:** Measures total completed placements per intern or filtered group.

DAX
Total KPI =
SUM ( Fact_Performance[KPI_Actual] )

## 2. Monthly Goal
**Purpose:** Returns the expected KPI target for the selected intern and timeframe.

Monthly Goal =
SUM ( Fact_Performance[Monthly_Goal] )

## 3. Monthly % of Goal
**Purpose:** Evaluates performance relative to assigned targets.

Monthly % of Goal =
DIVIDE ( [Total KPI], [Monthly Goal], 0 )

## 4. Weekly Goal 
**Purpose:** Provides a normalized weekly target for performance pacing.

Weekly Goal =
AVERAGE ( Fact_Performance[Weekly_Goal] )

## 5. Weekly % of Target
**Purpose:** Identifies short-term performance momentum.

Weekly % of Target =
DIVIDE ( SUM(Fact_Performance[KPI_Actual]), [Weekly Goal], 0 )

## 6. Performance Status
**Purpose: Converts numeric performance into a manager-friendly category.**

Performance Status =
SWITCH(
    TRUE(),
    [Monthly % of Goal] >= 1, "Exceeds Target",
    [Monthly % of Goal] >= 0.8, "On Track",
    "Needs Support"
)

## 7. Performance Icon Rank
**Purpose: Supports conditional icon formatting in tables and KPI cards.**

Performance Icon Rank =
SWITCH(
    [Performance Status],
    "Exceeds Target", 3,
    "On Track", 2,
    "Needs Support", 1
)

## 8. Cumulative Performance
**Purpose: Tracks total performance over time.**

Cumulative KPI =
CALCULATE(
    [Total KPI],
    FILTER(
        ALL('Dim_Calendar'[Date]),
        'Dim_Calendar'[Date] <= MAX('Dim_Calendar'[Date])
    )
)

## 9. Variance from Goal
**Purpose: Shows how far above or below target an intern is.**

Variance from Goal =
[Total KPI] - [Monthly Goal]

## 10. Standard Weekly Goal 

Standard Weekly Goal = 10.4

Tenure Weeks =
DATEDIFF ( MIN(Fact_Performance[Start Date]), TODAY(), WEEK )

Adjusted Goal =
[Standard Weekly Goal] * [Tenure Weeks]

Safe Goal   = [Adjusted Goal] * 0.8
Modest Goal = [Adjusted Goal] * 1.0
Reach Goal  = [Adjusted Goal] * 1.3



# Summary

These core measures provide:

- KPI tracking
- Fair goal comparison
- Manager-ready performance categorization
- Time-based cumulative insights