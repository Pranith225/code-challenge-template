# app.py
from flask import Flask, request
from flask_restful import Api, Resource
from flask_sqlalchemy import SQLAlchemy
from flask_swagger_ui import get_swaggerui_blueprint
from config import database_config

from models import WeatherData, YearlyWeatherSummary

app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{database_config['user']}:{database_config['password']}@{database_config['host']}:{database_config['port']}/{database_config['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Import the models
from models import WeatherData, YearlyWeatherSummary

# Configure the API
api = Api(app)

# Swagger UI configuration
SWAGGER_URL = '/api/docs'
API_URL = '/static/swagger.json'
swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "Weather Data API"
    }
)
app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

class Weather(Resource):
    def get(self):
        # Get the query parameters
        date = request.args.get('date')
        weather_station_id = request.args.get('weather_station_id')

        # Filter the weather data based on the query parameters
        query = WeatherData.query

        if date:
            query = query.filter(WeatherData.date == date)

        if weather_station_id:
            query = query.filter(WeatherData.weather_station_id == weather_station_id)

        weather_data = query.all()

        # Convert the results to JSON
        result = [data.to_dict() for data in weather_data]

        return result

class WeatherStats(Resource):
    def get(self):
        # Get the query parameters
        year = request.args.get('year')
        weather_station_id = request.args.get('weather_station_id')

        # Filter the yearly weather summary based on the query parameters
        query = YearlyWeatherSummary.query

        if year:
            query = query.filter(YearlyWeatherSummary.year == year)

        if weather_station_id:
            query = query.filter(YearlyWeatherSummary.weather_station_id == weather_station_id)

        weather_stats = query.all()

        # Convert the results to JSON
        result = [stats.to_dict() for stats in weather_stats]

        return result

def main():
    # Add the resources to the API
    api.add_resource(Weather, '/api/weather')
    api.add_resource(WeatherStats, '/api/weather/stats')
    app.run(debug=True)

if __name__ == '__main__':
    main()
