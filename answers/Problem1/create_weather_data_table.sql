CREATE TABLE weather_data (
    id SERIAL PRIMARY KEY,
    weather_station_id CHAR(11) NOT NULL,
    date DATE NOT NULL,
    max_temperature DECIMAL(5,1) NOT NULL,
    min_temperature DECIMAL(5,1) NOT NULL,
    precipitation DECIMAL(6,1) NOT NULL
);
