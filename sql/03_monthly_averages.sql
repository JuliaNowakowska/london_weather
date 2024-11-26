-- Creates a new table to store the monthly averages of each feature --
CREATE TABLE monthly_averages AS
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
SELECT * FROM averages;