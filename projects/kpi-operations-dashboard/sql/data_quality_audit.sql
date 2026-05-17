-- 1. Data Quality Audit: Orphaned Records & Boundary Checks
-- Purpose: Identify performance records that don't match any known intern 
-- or fall outside the official program start/end dates.

SELECT 
    f.PerformanceID,
    f.InternID,
    f.PerformanceDate,
    f.KPI_Total
FROM Fact_Performance f
LEFT JOIN Dim_Intern i ON f.InternID = i.InternID
WHERE i.InternID IS NULL -- Orphaned records
   OR f.PerformanceDate < '2018-01-01' -- Pre-program logic check
   OR f.KPI_Total < 0; -- Anomaly detection
