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


def db_query(connection, sql_query):
    """
    Returns the result of the query from the database.
    """
    try:
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            return cursor.fetchall()
    except psycopg2.Error as query_error:
        print(f"Query execution error: {query_error}")
        return None