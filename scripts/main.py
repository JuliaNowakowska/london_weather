from data_pipeline import Database
from weather_dashboard import create_dashboard
from monthly_dataframe import convert_to_dataframe

if __name__ == "__main__":
    pg_config = {
        'host': 'localhost',
        'port': 5432,
        'database': 'london_weather',
        'user': '',
        'password': ''
    }

    # Establishing a connection with the database
    db = Database(pg_config)

    # Placeholder for the results
    results = []

    if db.connection:
        try:
            sql_scripts = ['/sql/07_max_temp.sql',
                           '/sql/06_min_temp.sql',
                           '/sql/08_get_monthly_avg.sql']

            for sql_script in sql_scripts:
                sql_query = db.read_sql(sql_script)
                results.append(db.query(sql_query))
        finally:
            db.connection.close()

    # Max temp
    max_temp_date = results[0][0][0]
    max_temp = results[0][0][1]

    # Min temp
    min_temp_date = results[1][0][0]
    min_temp = results[1][0][1]

    # Monthly averages
    monthly_avg_temp = convert_to_dataframe(results[2])

    app = create_dashboard(max_temp_date, max_temp, min_temp_date, min_temp, monthly_avg_temp)
    app.run_server(debug=True)
