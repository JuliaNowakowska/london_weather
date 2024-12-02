import os
from config import PG_CONFIG
from data_pipeline import Database
from weather_dashboard import create_dashboard
from monthly_dataframe import convert_to_dataframe

if __name__ == "__main__":
    # Establishing a connection with the database
    db = Database(PG_CONFIG)

    # Identifying SQL scripts
    current_dir = os.path.dirname(__file__)
    max_temp_sql = os.path.join(current_dir, '../sql/07_max_temp.sql')
    min_temp_sql = os.path.join(current_dir, '../sql/06_min_temp.sql')
    monthly_avg_sql = os.path.join(current_dir, '../sql/08_get_monthly_avg.sql')

    # Querying the database
    if db.connection:
        try:
            max_temp_date, max_temp = db.query(max_temp_sql)[0][0], db.query(max_temp_sql)[0][1]
            min_temp_date, min_temp = db.query(min_temp_sql)[0][0], db.query(min_temp_sql)[0][1]
            monthly_avg_temp = convert_to_dataframe(db.query(monthly_avg_sql))
        finally:
            db.connection.close()

    # Running the dashboard
    app = create_dashboard(max_temp_date, max_temp, min_temp_date, min_temp, monthly_avg_temp)
    app.run_server(debug=True)
