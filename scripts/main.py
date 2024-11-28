from data_pipeline import get_data

if __name__ == "__main__":
    pg_config = {
        'host': 'localhost',
        'port': 5432,
        'database': 'london_weather',
        'user': '',
        'password': ''
    }

    # Path to your SQL file
    sql_file_path = 'sql/07_max_temp.sql'

    # Execute the SQL script and fetch results
    results = get_data(pg_config, sql_file_path)

    # Display the results
    print(results)
