SELECT date, max_temp
FROM readings
WHERE max_temp = (
    SELECT MAX(max_temp) 
    FROM readings
);