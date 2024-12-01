-- Returns average mean temperature by year and month ascending --
SELECT year, month, avg_mean_temp
FROM monthly_averages
ORDER BY year ASC, month ASC;