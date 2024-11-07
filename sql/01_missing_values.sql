-- Filling missing data with average value for a given month --
-- Step 1: Calculate monthly averages for each column --
WITH averages AS (
	SELECT
		EXTRACT(YEAR FROM date) AS year,
		EXTRACT(MONTH FROM date) AS month,
		AVG(cloud_cover) AS avg_cloud_cover,
		AVG(sunshine) AS avg_sunshine,
		AVG(global_radiation) AS avg_global_radiation,
		AVG(max_temp) AS avg_max_temp,
		AVG(mean_temp) AS avg_mean_temp,
		AVG(min_temp) AS avg_min_temp,
		AVG(precipitation) AS avg_precipitation,
		AVG(pressure) AS avg_pressure,
		AVG(snow_depth) AS avg_snow_depth
	FROM readings
	GROUP BY EXTRACT(YEAR FROM date), EXTRACT(MONTH FROM date)
)

-- Step 2: Update the missing values with the monthly average --
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
FROM averages AS a
WHERE EXTRACT(YEAR FROM r.date) = a.year AND EXTRACT(MONTH FROM r.date) = a.month;