# Basic Weather App (Python Programming Internship – Task 3)

## Objective
Build a command-line application that fetches and displays current
weather data (temperature, humidity, wind speed, conditions) for a
user-specified city.

## Tools Used
- Python 3
- `requests` library
- [Open-Meteo API](https://open-meteo.com/) – a free weather API that
  requires **no API key**, used for both geocoding (city name → coordinates)
  and the current weather forecast.

## Steps Performed
1. Used Open-Meteo's geocoding endpoint to convert a user-entered city name
   into latitude/longitude coordinates, handling the case where the city
   is not found.
2. Called Open-Meteo's forecast endpoint with the `current` parameter to
   retrieve temperature, relative humidity, wind speed, and a WMO weather
   code for that location.
3. Mapped the numeric WMO weather code to a human-readable description
   (e.g. "Partly cloudy", "Slight rain") using a lookup table.
4. Let the user choose between Celsius and Fahrenheit.
5. Added error handling for network failures (`requests.exceptions.RequestException`)
   and malformed/unexpected API responses.
6. Displayed the results in a clean formatted summary, and added a loop so
   the user can check multiple cities in one session.

## How to Run
```bash
pip install -r requirements.txt
python3 weather_app.py
```
Follow the on-screen prompts to enter a city name and your preferred
temperature unit.

## Sample Output
```
Enter a city name (e.g. London): London
Temperature unit - Celsius or Fahrenheit? (C/F): C

---------------------------------------------
Location    : London, England, United Kingdom
Temperature : 18.4°C
Humidity    : 62%
Wind speed  : 11.3 km/h
Conditions  : Partly cloudy
---------------------------------------------
```

## Outcome
A working command-line weather app that retrieves and displays live
weather data for any city worldwide, without requiring users to sign up
for an API key.
