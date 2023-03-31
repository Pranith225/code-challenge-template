# Weather Data Ingestion

This solution ingests weather data from raw text files into a PostgreSQL database using Python.


## Requirements

1. Python 3.6 or higher
2. PostgreSQL database
3. psycopg2 library


## Installation

		pip install requirement.txt

## Configuration

Create a config.py file in the same directory as the weather_data_ingestion.py script.

Add your PostgreSQL database connection details to the config.py file:

	# config.py

	# Database connection details
	database_config = {
	    'database': 'your_database',
	    'user': 'your_user',
	    'password': 'your_password',
	    'host': 'your_host',
	    'port': 'your_port'
	}

Replace your_database, your_user, your_password, your_host, and your_port with your actual PostgreSQL connection details

## Setup

Create a table in your PostgreSQL database using the provided DDL statement in create_weather_data_table.sql.

Place the weather data text files in a directory named wx_data under the code-challenge-template directory.


## Running the script

Execute the weather_data_ingestion.py script:

	python weather_data_ingestion.py

The script will ingest the weather data from the text files and insert them into the weather_data table in your PostgreSQL database. It will also print log output indicating the start and end times, the number of records ingested, and the total time taken.

## How it works

The weather_data_ingestion.py script contains the following functions:

1. parse_weather_line(line): Parses a line from the raw text file and converts it to a dictionary with the required data types (e.g., date, float).

2. ingest_weather_data(directory_path, conn): Takes a directory path and a database connection, then iterates over all the text files in the directory, parsing the weather data and inserting it into the weather_data table.

3. main(): Connects to the PostgreSQL database using the connection details provided in the config.py file, calls the ingest_weather_data function to ingest the weather data, and closes the database connection.

The script uses the ON CONFLICT clause in the INSERT statement to handle duplicates. If a record with the same weather_station_id and date already exists in the table, the DO NOTHING action is taken, ensuring no duplicates are inserted.
