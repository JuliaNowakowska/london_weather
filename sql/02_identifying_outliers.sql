-- Step 1: Create a new table to store the monthly standard deviations --
CREATE TABLE monthly_std_dev AS
WITH std_dev AS (
    SELECT
        EXTRACT(YEAR FROM date) AS year,
        EXTRACT(MONTH FROM date) AS month,
        STDDEV(cloud_cover) AS stddev_cloud_cover,
        STDDEV(sunshine) AS stddev_sunshine,
        STDDEV(global_radiation) AS stddev_global_radiation,
        STDDEV(max_temp) AS stddev_max_temp,
        STDDEV(mean_temp) AS stddev_mean_temp,
        STDDEV(min_temp) AS stddev_min_temp,
        STDDEV(precipitation) AS stddev_precipitation,
        STDDEV(pressure) AS stddev_pressure,
        STDDEV(snow_depth) AS stddev_snow_depth
    FROM readings
    GROUP BY EXTRACT(YEAR FROM date), EXTRACT(MONTH FROM date)
)
SELECT * FROM std_dev;