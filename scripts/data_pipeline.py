import psycopg2

def get_data(pg_config, sql_file_path):
    try:
        # Read the SQL query from the file
        with open(sql_file_path, 'r') as file:
            sql_query = file.read()

        # Connect to the PostgreSQL database
        connection = psycopg2.connect(
            host=pg_config['host'],
            port=pg_config['port'],
            database=pg_config['database'],
            user=pg_config['user'],
            password=pg_config['password']
        )
        cursor = connection.cursor()

        # Execute the SQL query
        cursor.execute(sql_query)
        result = cursor.fetchall()  # Fetch all rows from the query

        return result
    except Exception as e:
        print(f"Error: {e}")
        return None
    finally:
        # Ensure the connection is closed
        if connection:
            cursor.close()
            connection.close()
