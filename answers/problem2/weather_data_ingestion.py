import os
import psycopg2
from datetime import datetime
from config import database_config

def parse_weather_line(line):
    date_str, max_temp, min_temp, precipitation = line.strip().split('\t')
    return {
        'date': datetime.strptime(date_str, '%Y%m%d').date(),
        'max_temperature': float(max_temp) / 10,
        'min_temperature': float(min_temp) / 10,
        'precipitation': float(precipitation) / 10
    }

def ingest_weather_data(directory_path, conn):
    start_time = datetime.now()
    print(f'Starting ingestion at {start_time}')

    cursor = conn.cursor()
    count = 0

    for filename in os.listdir(directory_path):
        if filename.endswith('.txt'):
            weather_station_id = filename[:-4]
            with open(os.path.join(directory_path, filename), 'r') as file:
                for line in file:
                    weather_data = parse_weather_line(line)
                    weather_data['weather_station_id'] = weather_station_id

                    # Insert the data into the weather_data table if not exists
                    cursor.execute("""
                        INSERT INTO weather_data (weather_station_id, date, max_temperature, min_temperature, precipitation)
                        VALUES (%(weather_station_id)s, %(date)s, %(max_temperature)s, %(min_temperature)s, %(precipitation)s)
                        ON CONFLICT (weather_station_id, date) DO NOTHING;
                    """, weather_data)

                    count += 1

    conn.commit()
    cursor.close()

    end_time = datetime.now()
    print(f'Finished ingestion at {end_time}')
    print(f'Ingested {count} records')
    print(f'Total time taken: {end_time - start_time}')

def main():
    # Connect to the Postgres database
    conn = psycopg2.connect(**database_config)

    # Ingest the weather data
    directory_path = 'code-challenge-template/wx_data/'
    ingest_weather_data(directory_path, conn)

    # Close the database connection
    conn.close()

if __name__ == '__main__':
    main()
