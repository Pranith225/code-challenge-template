# Problem 1 - Data Modeling


The 6 columns chosen for the data model are based on the given weather data description and aim to represent each piece of information provided in the original dataset. 

Here's a breakdown of each column and the reasoning behind its inclusion


### id SERIAL PRIMARY KEY: 

This column serves as a unique identifier for each weather data record in the table. Using a primary key ensures that each row can be uniquely identified, which is essential for database operations like updating, deleting, or referencing specific records. The SERIAL data type is used to auto-increment the id, making it easier to insert new records without worrying about providing a unique id manually.

### weather_station_id CHAR(11) NOT NULL: 
        This column represents the weather station from which the data was recorded. It is included to differentiate and identify the source of the weather data. The CHAR(11) data type is used because weather station IDs are 11 characters long, and the NOT NULL constraint ensures that every weather data record is associated with a specific weather station.

### date DATE NOT NULL: 
        This column stores the date when the weather data was recorded. Including the date allows for querying and analysis based on time, such as finding the average temperature for a specific day or calculating trends over time. The DATE data type is used for efficient storage and manipulation of date information, and the NOT NULL constraint ensures that every record has an associated date.

### max_temperature DECIMAL(5,1) NOT NULL: 
        This column stores the maximum temperature recorded for a specific day, which is an essential piece of information in weather data analysis. The DECIMAL(5,1) data type is chosen to store the temperature in tenths of a degree Celsius with a fixed decimal point, ensuring accurate representation and efficient storage. The NOT NULL constraint guarantees that every record has a maximum temperature value.

### min_temperature DECIMAL(5,1) NOT NULL: 
        Similar to the max_temperature column, this column stores the minimum temperature recorded for a specific day. It is included for the same reasons as the max_temperature column, and it also uses the DECIMAL(5,1) data type and a NOT NULL constraint for accurate and efficient storage.

### precipitation DECIMAL(6,1) NOT NULL: 
        This column stores the amount of precipitation recorded for a specific day in tenths of a millimeter. Precipitation is an essential weather parameter and helps in understanding various weather patterns and conditions. The DECIMAL(6,1) data type is used to store the precipitation value with a fixed decimal point, ensuring accurate representation and efficient storage. The NOT NULL constraint ensures that every record has a precipitation value.

The 6 columns in the data model are chosen to represent all the information provided in the original weather data records while ensuring efficient storage, accurate representation, and easy querying or analysis.
