SELECT date, min_temp
FROM readings
WHERE min_temp = (
    SELECT MIN(min_temp) 
    FROM readings
);