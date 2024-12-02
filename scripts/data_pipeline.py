import psycopg2

class Database:
    def __init__(self, pg_config):
        self.pg_config = pg_config
        self.connection = None
        self.connect()

    def connect(self):
        """
        Establishes a connection with the database and returns the connection object if successful.
        """
        try:
            self.connection = psycopg2.connect(
                host = self.pg_config['host'],
                port = self.pg_config['port'],
                database = self.pg_config['database'],
                user = self.pg_config['user'],
                password = self.pg_config['password']
            )
        except psycopg2.DatabaseError as db_error:
            print(f"Database connection error: {db_error}")
            return None


    def query(self, sql_query):
        """
        Returns the result of the query from the database.
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(sql_query)
                return cursor.fetchall()
        except psycopg2.Error as query_error:
            print(f"Query execution error: {query_error}")
            return None

    def read_sql(self, sql_file_path):
        """
        Reads SQL script.
        """
        try:
            with open(sql_file_path, 'r') as file:
                return file.read()
        except FileNotFoundError as fnf_error:
            print(f"SQL file not found: {fnf_error}")
            return None

    def close(self):
        if self.connection:
            self.connection.close()
            self.connection = None
