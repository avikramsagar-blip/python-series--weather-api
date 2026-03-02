import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        data = response.json()

        if response.status_code != 200:
            print(f"❌ Error: {data.get('message', 'Something went wrong')}")
            return

        print("\n🌤️ Weather Report")
        print("-" * 30)
        print(f"📍 City: {data['name']}")
        print(f"🌡️ Temperature: {data['main']['temp']}°C")
        print(f"🌥️ Condition: {data['weather'][0]['description'].title()}")
        print(f"💧 Humidity: {data['main']['humidity']}%")
        print(f"🌬️ Wind Speed: {data['wind']['speed']} m/s")

    except requests.exceptions.RequestException:
        print("⚠️ Network error. Please check your internet connection.")


def main():
    print("=== Simple Weather App (CLI) ===")
    city = input("Enter city name: ").strip()

    if not city:
        print("❌ City name cannot be empty.")
        return

    get_weather(city)


if __name__ == "__main__":
    main()