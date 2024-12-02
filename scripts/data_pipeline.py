import psycopg2

def db_connection(pg_config):
    """
    Establishes a connection with the database and returns the connection object if successful.
    """
    try:
        connection = psycopg2.connect(
            host=pg_config['host'],
            port=pg_config['port'],
            database=pg_config['database'],
            user=pg_config['user'],
            password=pg_config['password']
        )
        return connection

    except psycopg2.DatabaseError as db_error:
        print(f"Database connection error: {db_error}")
        return None