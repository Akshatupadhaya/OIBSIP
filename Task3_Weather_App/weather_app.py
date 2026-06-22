"""
Basic Weather App
A command-line tool that fetches and displays current weather for a
user-specified city using the free Open-Meteo API (no API key required).
"""

import requests

GEOCODING_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"

# WMO weather codes -> human readable description
WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear",
    2: "Partly cloudy",
    3: "Overcast",
    45: "Fog",
    48: "Depositing rime fog",
    51: "Light drizzle",
    53: "Moderate drizzle",
    55: "Dense drizzle",
    61: "Slight rain",
    63: "Moderate rain",
    65: "Heavy rain",
    71: "Slight snow fall",
    73: "Moderate snow fall",
    75: "Heavy snow fall",
    80: "Slight rain showers",
    81: "Moderate rain showers",
    82: "Violent rain showers",
    95: "Thunderstorm",
    96: "Thunderstorm with slight hail",
    99: "Thunderstorm with heavy hail",
}


def geocode_city(city_name):
    """Look up latitude/longitude/name for a city. Returns a dict or None."""
    params = {"name": city_name, "count": 1, "language": "en", "format": "json"}
    response = requests.get(GEOCODING_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()

    results = data.get("results")
    if not results:
        return None

    place = results[0]
    return {
        "name": place.get("name"),
        "country": place.get("country", ""),
        "admin1": place.get("admin1", ""),
        "latitude": place["latitude"],
        "longitude": place["longitude"],
    }


def get_current_weather(latitude, longitude, unit="celsius"):
    """Fetch current weather for a coordinate. Returns the 'current' dict."""
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "current": "temperature_2m,relative_humidity_2m,wind_speed_10m,weather_code",
        "temperature_unit": unit,
    }
    response = requests.get(FORECAST_URL, params=params, timeout=10)
    response.raise_for_status()
    data = response.json()
    return data.get("current", {})


def describe_weather_code(code):
    return WEATHER_CODES.get(code, "Unknown conditions")


def main():
    print("=" * 45)
    print("            BASIC WEATHER APP")
    print("=" * 45)

    city = input("Enter a city name (e.g. London): ").strip()
    if not city:
        print("City name cannot be empty.")
        return

    unit_choice = input("Temperature unit - Celsius or Fahrenheit? (C/F): ").strip().lower()
    unit = "fahrenheit" if unit_choice.startswith("f") else "celsius"
    unit_symbol = "°F" if unit == "fahrenheit" else "°C"

    try:
        place = geocode_city(city)
        if place is None:
            print(f"\nCould not find a location named '{city}'. "
                  f"Try a different spelling or add a country, e.g. 'Paris, France'.")
            return

        current = get_current_weather(place["latitude"], place["longitude"], unit)
        if not current:
            print("\nWeather data was not available for this location. Please try again.")
            return

        location_label = ", ".join(
            part for part in [place["name"], place["admin1"], place["country"]] if part
        )

        print("\n" + "-" * 45)
        print(f"Location    : {location_label}")
        print(f"Temperature : {current.get('temperature_2m')}{unit_symbol}")
        print(f"Humidity    : {current.get('relative_humidity_2m')}%")
        print(f"Wind speed  : {current.get('wind_speed_10m')} km/h")
        print(f"Conditions  : {describe_weather_code(current.get('weather_code'))}")
        print("-" * 45)

    except requests.exceptions.RequestException as err:
        print(f"\nNetwork error while fetching weather data: {err}")
    except (KeyError, ValueError) as err:
        print(f"\nUnexpected response from the weather service: {err}")


if __name__ == "__main__":
    while True:
        main()
        again = input("\nCheck another city? (y/n): ").strip().lower()
        if again != "y":
            print("Goodbye!")
            break
        print()
