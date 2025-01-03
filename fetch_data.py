import requests
from datetime import datetime

# OpenWeather API configuration
api_key = "9f1caf98d85b9f44a5a9a437d1effabf"  # Replace with your actual API key
cities = ["Delhi", "Haridwar", "Bangalore", "Roorkee", "Noida","Ara"]
api_url = "http://api.openweathermap.org/data/2.5/weather"

def fetch_weather_data():
    """Fetches weather data for multiple cities from OpenWeather API."""
    weather_data = []
    for city in cities:
        response = requests.get(api_url, params={"q": city, "appid": api_key, "units": "metric"})
        if response.status_code == 200:
            data = response.json()
            weather_data.append({
                "city": city,
                "temperature": data["main"]["temp"],
                "weather": data["weather"][0]["main"],
                "timestamp": datetime.now(),
                "description": data["weather"][0]["description"]
            })
    return weather_data
