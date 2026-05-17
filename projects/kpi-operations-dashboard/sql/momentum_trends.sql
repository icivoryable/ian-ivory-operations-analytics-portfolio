-- 3. Trend Analysis: Rolling 4-Week KPI Performance
-- Purpose: Uses Window Functions to calculate short-term momentum.
-- This shows pattern-finding skills beyond simple aggregations.

SELECT 
    InternID,
    WeekNumber,
    Weekly_KPI,
    AVG(Weekly_KPI) OVER (
        PARTITION BY InternID 
        ORDER BY WeekNumber 
        ROWS BETWEEN 3 PRECEDING AND CURRENT ROW
    ) AS Rolling_4Week_Avg
FROM (
    SELECT 
        f.InternID,
        c.WeekNumber,
        SUM(f.KPI_Total) AS Weekly_KPI
    FROM Fact_Performance f
    JOIN Dim_Calendar c ON f.PerformanceDate = c.FullDate
    GROUP BY f.InternID, c.WeekNumber
) sub;
