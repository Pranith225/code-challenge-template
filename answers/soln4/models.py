# models.py
from app import db

class WeatherData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weather_station_id = db.Column(db.String(11), nullable=False)
    date = db.Column(db.Date, nullable=False)
    max_temperature = db.Column(db.Float, nullable=False)
    min_temperature = db.Column(db.Float, nullable=False)
    precipitation = db.Column(db.Float, nullable=False)

    def to_dict(self):
        return {
            'id': self.id,
            'weather_station_id': self.weather_station_id,
            'date': self.date.isoformat(),
            'max_temperature': self.max_temperature,
            'min_temperature': self.min_temperature,
            'precipitation': self.precipitation
        }

class YearlyWeatherSummary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    weather_station_id = db.Column(db.String(11), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    avg_max_temperature = db.Column(db.Float)
    avg_min_temperature = db.Column(db.Float)
    total_precipitation = db.Column(db.Float)

    def to_dict(self):
        return {
            'id': self.id,
            'weather_station_id': self.weather_station_id,
            'year': self.year,
            'avg_max_temperature': self.avg_max_temperature,
            'avg_min_temperature': self.avg_min_temperature,
            'total_precipitation': self.total_precipitation
        }

