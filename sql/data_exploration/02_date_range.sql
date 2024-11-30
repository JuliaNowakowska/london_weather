-- Determines the range of dates included in the dataset --
SELECT MIN(date) AS range_start, MAX(date) AS range_end
FROM readings;
