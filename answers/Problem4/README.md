# Weather Data API

This project is a REST API for weather data, allowing clients to fetch weather data records and yearly weather summaries for various weather stations. The API is built using Flask, SQLAlchemy, and SQLite as a database.

## Directory Structure

	weather_data_api/
	├── app.py
	├── config.py
	├── models.py
	├── static/
	│   └── swagger.json
	└── requirements.txt

weather_data_api/: The root folder containing all files and subfolders.

app.py: The main Flask application file with the API implementation.

config.py: The configuration file containing the database connection details.

models.py: The file containing the SQLAlchemy models for the WeatherData and YearlyWeatherSummary tables.

static/: A folder containing static files, such as the swagger.json file.

swagger.json: The Swagger/OpenAPI specification file for the API documentation.

requirements.txt: A file containing the required Python libraries for the project.


## Installation and Setup
Install Python 3.6+ if you haven't already.

Clone this repository:

	git clone https://github.com/username/weather_data_api.git
	cd weather_data_api

Replace https://github.com/username/weather_data_api.git with the URL of your repository.

Create a virtual environment and activate it:

	python -m venv venv
	source venv/bin/activate  # Linux/Mac
	venv\Scripts\activate     # Windows

Install the required Python libraries:

	pip install -r requirements.txt

Run the Flask application:

	python app.py

This will start the API locally at http://127.0.0.1:5000. The Swagger/OpenAPI documentation will be available at http://127.0.0.1:5000/api/docs.

## API Endpoints

The API provides the following endpoints:

/api/weather: Returns weather data records. Supports filtering by date and weather station ID.

/api/weather/stats: Returns yearly weather summaries. Supports filtering by year and weather station ID.

Both endpoints return JSON-formatted responses and support pagination.

## Usage

To fetch weather data for a specific date and weather station ID, send a GET request to /api/weather with the appropriate query parameters:

	curl "http://127.0.0.1:5000/api/weather?date=2022-12-25&weather_station_id=USC00110072"

To fetch yearly weather summaries for a specific year and weather station ID, send a GET request to /api/weather/stats with the appropriate query parameters:

	curl "http://127.0.0.1:5000/api/weather/stats?year=2022&weather_station_id=USC00110072"
