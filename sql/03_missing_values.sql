-- Update the missing values in the original 'readings' table with the monthly averages --
UPDATE readings AS r
SET
    cloud_cover = COALESCE(r.cloud_cover, a.avg_cloud_cover),
    sunshine = COALESCE(r.sunshine, a.avg_sunshine),
    global_radiation = COALESCE(r.global_radiation, a.avg_global_radiation),
    max_temp = COALESCE(r.max_temp, a.avg_max_temp),
    mean_temp = COALESCE(r.mean_temp, a.avg_mean_temp),
    min_temp = COALESCE(r.min_temp, a.avg_min_temp),
    precipitation = COALESCE(r.precipitation, a.avg_precipitation),
    pressure = COALESCE(r.pressure, a.avg_pressure),
    snow_depth = COALESCE(r.snow_depth, a.avg_snow_depth)
FROM monthly_averages AS a
WHERE EXTRACT(YEAR FROM r.date) = a.year AND EXTRACT(MONTH FROM r.date) = a.month;
