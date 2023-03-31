import pytest
from app import app, db, WeatherData, YearlyWeatherSummary

# Define fixtures
@pytest.fixture
def client():
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test_weather_data.db'
    client = app.test_client()

    with app.app_context():
        db.create_all()

    yield client

    with app.app_context():
        db.drop_all()

def test_weather_endpoint(client):
    # Insert test data
    with app.app_context():
        weather_data = WeatherData(weather_station_id=1, date='20230101', max_temp=20, min_temp=-10, precipitation=5)
        db.session.add(weather_data)
        db.session.commit()

    # Test the /api/weather endpoint
    response = client.get('/api/weather?weather_station_id=1&date=20230101')
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) == 1
    assert json_data[0]['weather_station_id'] == 1
    assert json_data[0]['date'] == '20230101'
    assert json_data[0]['max_temp'] == 20
    assert json_data[0]['min_temp'] == -10
    assert json_data[0]['precipitation'] == 5

def test_weather_stats_endpoint(client):
    # Insert test data
    with app.app_context():
        weather_stats = YearlyWeatherSummary(weather_station_id=1, year='2023', avg_max_temp=25.5, avg_min_temp=15.5, total_precipitation=123.45)
        db.session.add(weather_stats)
        db.session.commit()

    # Test the /api/weather/stats endpoint
    response = client.get('/api/weather/stats?weather_station_id=1&year=2023')
    assert response.status_code == 200
    json_data = response.get_json()
    assert len(json_data) == 1
    assert json_data[0]['weather_station_id'] == 1
    assert json_data[0]['year'] == '2023'
    assert json_data[0]['avg_max_temp'] == 25.5
    assert json_data[0]['avg_min_temp'] == 15.5
    assert json_data[0]['total_precipitation'] == 123.45
