-- 2. Star Schema View: reporting_denormalized_view
-- Purpose: Flattens the star schema into a high-performance view for BI tools.
-- This demonstrates the logic behind the Power BI "Source" transformation.

CREATE VIEW vw_Reporting_Performance AS
SELECT 
    f.PerformanceDate,
    f.KPI_Total,
    i.InternName,
    i.AssignedState,
    i.InternType,
    c.WeekNumber,
    c.MonthName,
    c.IsWorkDay
FROM Fact_Performance f
JOIN Dim_Intern i ON f.InternID = i.InternID
JOIN Dim_Calendar c ON f.PerformanceDate = c.FullDate;
