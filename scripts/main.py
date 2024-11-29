from data_pipeline import get_data
from weather_dashboard import create_dashboard

if __name__ == "__main__":
    pg_config = {
        'host': 'localhost',
        'port': 5432,
        'database': 'london_weather',
        'user': '',
        'password': ''
    }

    # Path to your SQL file
    sql_file_path = '/sql/07_max_temp.sql'

    # Execute the SQL script and fetch results
    results = get_data(pg_config, sql_file_path)
    max_temp_date = results[1][0]
    max_temp = results[1][1]

    # Path to your SQL file
    sql_file_path = '/sql/06_min_temp.sql'

    # Execute the SQL script and fetch results
    results = get_data(pg_config, sql_file_path)
    min_temp_date = results[0][0]
    min_temp = results[0][1]

    sql_file_path = '/sql/08_get_monthly_avg.sql'

    # Execute the SQL script and fetch results
    results_monthly_avg = get_data(pg_config, sql_file_path)
    monthly_avg_temp = convert_to_dataframe(results_monthly_avg)

    app = create_dashboard(max_temp_date, max_temp, min_temp_date, min_temp, monthly_avg_temp)
    app.run_server(debug=True)
