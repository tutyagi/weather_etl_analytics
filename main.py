from fetch_data import fetch_weather_data
from store_data import store_weather_data
from filter_data import filter_and_store_rainy_weather

def main():
    """Main function to fetch, store, and filter weather data."""
    # Step 1: Fetch weather data from OpenWeather API
    weather_data = fetch_weather_data()

    # Step 2: Store the weather data in the database
    store_weather_data(weather_data)

    # Step 3: Filter and store rainy weather data in a separate table
    filter_and_store_rainy_weather()

if __name__ == "__main__":
    main()
