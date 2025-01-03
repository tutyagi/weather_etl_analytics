import psycopg2
import datetime

# Database configuration
db_config = {
    "dbname": "weather_data",
    "user": "postgres",
    "password": "asdfasdf",  # Replace with your actual password
    "host": "localhost",
    "port": 5432
}

def filter_and_store_rainy_weather():
    """Filter and store rainy weather data into rainy_weather table."""
    with psycopg2.connect(**db_config) as conn:
        with conn.cursor() as cur:
            current_date = datetime.date.today()  # Get today's date

            # Convert the date to string format ('YYYY-MM-DD') explicitly
            current_date_str = current_date.strftime('%Y-%m-%d')

            # Debugging: Print current date
            print(f"Current date: {current_date_str}")

            # Construct the SQL query with current_date_str embedded in the query
            query = f"""
                INSERT INTO rainy_weather (city, temperature, weather, timestamp, description, date_part)
                SELECT city, temperature, weather, timestamp, description, timestamp::date
                FROM weather_data
                WHERE (weather ILIKE '%rain%' OR weather ILIKE '%cloud%')
                AND temperature > 20
                AND timestamp::date = '{current_date_str}'
                ON CONFLICT (city, date_part) DO NOTHING;
            """

            # Debugging: Print the query being executed
            print(f"Executing query: {query}")

            try:
                # Execute the query directly with the current date string formatted
                cur.execute(query)
                conn.commit()
                print("Query executed successfully.")
            except Exception as e:
                print(f"Error executing query: {e}")

# Call the function to filter and store rainy weather
filter_and_store_rainy_weather()
