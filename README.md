## Dataset

**london_weather** dataset is a collaction of data ranging from 1979-01-01 until 2020-12-31, which contains information about climate in London. Using scripts in sql/data_exploration folder it is possible to examine the corpus. 

### Weather Data Example

This dataset contains daily weather measurements including cloud cover, sunshine duration, global radiation, and various temperature metrics.

| Date       | Cloud Cover | Sunshine | Global Radiation | Max Temp | Mean Temp | Min Temp | Precipitation | Pressure | Snow Depth |
|------------|---------------------|------------------|--------------------------|---------------|----------------|---------------|--------------------|---------------|-----------------|
| 2006-06-01 | 6                   | 0.3              | 97                       | 16.2          | 10.8           | 5.3           | 0                  | 102810        | 0               |
| 2006-06-02 | 3                   | 7.7              | 244                      | 20.6          | 15.3           | 10            | 0                  | 103030        | 0               |
| 2006-06-03 | 0                   | 14.4             | 333                      | 24.2          | 17             | 9.9           | 0                  | 102950        | 0               |
| 2006-06-04 | 4                   | 8.4              | 255                      | 23.6          | 17.6           | 11.5          | 0.4                | 102650        | 0               |
| 2006-06-05 | 4                   | 10.5             | 284                      | 20.1          | 16.5           | 12.9          | 0                  | 102560        | 0               |


### Data Cleanup

Data cleanup can be performed using scripts in sql/data_cleanup folder. It **includes altering data types, handling missing values and identifying outliers**. 

- 01_alter_type.sql - changes the date type to timestamp without time zone.
- 02_missing_values.sql - updates the missing values in the original 'readings' table with the monthly averages.
- 03_monthly_averages.sql & 04_monthly_standard_deviations.sql - calculate monthly averages and standard deviations for each variable, values used in other scripts.
- 04_identifying_outliers.sql - Flags mean_temp values as outliers if their z-scores are greater than 3

## Database handler

In order to extract the data and use it later on in the dashboard, I designed a Database handler class, which covers connections and queries. It includes:
- connect method, which establishes a connection with the database,
- read_sql() - reads and returns the contents of an SQL file,
- query() - executes an SQL query from a provided file and returns the result,
- close method, which closes the database connection.

## Data Analysis

Using scripts from sql/data_analysis, it is possible to do a simple data exploration analysis. The scripts return min and max temperature observed in London during the whole time period covered by the dataset. Additionally, script get_monthly_avg.sql returns monthly average temperatures, which is later used in visualizations.

## Dashboard
The final step of the project was to create a dashboard to visualize the outcomes of the data analysis. The WeatherDashboard class, defined in dashboard.py, uses the Dash library to create the charts as shown below.




![Screenshot 2024-12-06 at 20 13 37](https://github.com/user-attachments/assets/0af63ef6-5577-4812-bffc-4c55b06bcd58)




