import psycopg2
from config import database_config

def calculate_and_store_yearly_weather_summary(conn):
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO yearly_weather_summary (weather_station_id, year, avg_max_temperature, avg_min_temperature, total_precipitation)
        SELECT
            weather_station_id,
            EXTRACT(YEAR FROM date) AS year,
            AVG(NULLIF(max_temperature, -999.9)) AS avg_max_temperature,
            AVG(NULLIF(min_temperature, -999.9)) AS avg_min_temperature,
            SUM(NULLIF(precipitation, -999.9)) / 10 AS total_precipitation
        FROM weather_data
        GROUP BY weather_station_id, year
        ORDER BY weather_station_id, year;
    """)

    conn.commit()
    cursor.close()

def main():
    # Connect to the Postgres database
    conn = psycopg2.connect(**database_config)

    # Calculate and store the yearly weather summary
    calculate_and_store_yearly_weather_summary(conn)

    # Close the database connection
    conn.close()

if __name__ == '__main__':
    main()
