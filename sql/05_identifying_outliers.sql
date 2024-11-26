-- Flags mean_temp as outliers if their z-scores are greater than 3 -- 
SELECT 
    r.date,
    r.mean_temp,
    ma.avg_mean_temp,
    ms.stddev_mean_temp,
    (r.mean_temp - ma.avg_mean_temp) / ms.stddev_mean_temp AS z_score,
    CASE 
        WHEN ABS((r.mean_temp - ma.avg_mean_temp) / ms.stddev_mean_temp) > 3 THEN 'Outlier'
        ELSE 'Not Outlier'
    END AS is_outlier
FROM 
    readings r
JOIN 
    monthly_averages ma 
    ON EXTRACT(YEAR FROM r.date) = ma.year 
    AND EXTRACT(MONTH FROM r.date) = ma.month
JOIN 
    monthly_std_dev ms 
    ON EXTRACT(YEAR FROM r.date) = ms.year 
    AND EXTRACT(MONTH FROM r.date) = ms.month
WHERE ABS((r.mean_temp - ma.avg_mean_temp) / ms.stddev_mean_temp) > 3;