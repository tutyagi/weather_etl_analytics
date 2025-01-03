import psycopg2
from datetime import datetime

# Database configuration
db_config = {
    "dbname": "weather_data",  # Update with your actual database name
    "user": "postgres",        # Update with your actual PostgreSQL username
    "password": "asdfasdf",    # Update with your actual password
    "host": "localhost",
    "port": 5432
}

def store_weather_data(data):
    """Store weather data into the database."""
    with psycopg2.connect(**db_config) as conn:
        with conn.cursor() as cur:
            # Create table if it doesn't exist and drop the existing unique constraint if it exists
            cur.execute("""
                CREATE TABLE IF NOT EXISTS weather_data (
                    id SERIAL PRIMARY KEY,
                    city TEXT,
                    temperature REAL,
                    weather TEXT,
                    timestamp TIMESTAMP,
                    description TEXT,
                    date_part DATE,
                    CONSTRAINT unique_city_date UNIQUE (city, date_part)
                );
            """)

            # Insert data into weather_data table
            for record in data:
                record_date = record['timestamp'].date()

                # Check if the city and date already exist
                cur.execute("""
                    SELECT 1 FROM weather_data WHERE city = %s AND date_part = %s;
                """, (record['city'], record_date))

                if not cur.fetchone():  # Insert if not already present for the same city and date
                    cur.execute("""
                        INSERT INTO weather_data (city, temperature, weather, timestamp, description, date_part)
                        VALUES (%s, %s, %s, %s, %s, %s);
                    """, (record['city'], record['temperature'], record['weather'], record['timestamp'], record['description'], record_date))

            # Commit the transaction
            conn.commit()
