CREATE TABLE yearly_weather_summary (
    id SERIAL PRIMARY KEY,
    weather_station_id CHAR(11) NOT NULL,
    year INTEGER NOT NULL,
    avg_max_temperature DECIMAL(5,2),
    avg_min_temperature DECIMAL(5,2),
    total_precipitation DECIMAL(7,2)
);
