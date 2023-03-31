# Yearly Weather Summary


This solution calculates the yearly weather summary for each weather station, including the average maximum temperature, average minimum temperature, and total accumulated precipitation, and stores the results in a PostgreSQL database using Python.


## Requirements

	Python 3.6 or higher
	PostgreSQL database
	psycopg2 library


## Installation

Install the psycopg2 library using pip:
	pip install psycopg2

## Configuration

Create a config.py file in the same directory as the calculate_yearly_weather_summary.py script.

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

Replace your_database, your_user, your_password, your_host, and your_port with your actual PostgreSQL connection details.

## Setup

Create a table in your PostgreSQL database using the provided DDL statement in create_yearly_weather_summary_table.sql.


## Running the script

Execute the calculate_yearly_weather_summary.py script:

	python calculate_yearly_weather_summary.py

The script will calculate the yearly weather summary for each weather station and store the results in the yearly_weather_summary table in your PostgreSQL database.

## How it works

The calculate_yearly_weather_summary.py script contains the following functions:


1. calculate_and_store_yearly_weather_summary(conn): This function calculates the average maximum temperature, average minimum temperature, and total accumulated precipitation for each year and weather station, and stores the results in the yearly_weather_summary table. It uses the NULLIF function to ignore missing data when calculating the statistics.

2. main(): Connects to the PostgreSQL database using the connection details provided in the config.py file, calls the calculate_and_store_yearly_weather_summary function to calculate the statistics and store them in the database, and closes the database connection.

The script calculates the required statistics, handles missing data, and stores the results in a new data model designed specifically for this purpose.
