"""Async calls to the free public APIs (no API key needed).

Docs:
- Geocoding: https://open-meteo.com/en/docs/geocoding-api
- Forecast:  https://open-meteo.com/en/docs
- Rates:     https://frankfurter.dev
"""
import httpx

from app import config
from app.models import ExchangeRate, Location, Weather


class CityNotFound(Exception):
    pass


WEATHER_CODES = {
    0: "Clear sky",
    1: "Mainly clear", 2: "Partly cloudy", 3: "Overcast",
    45: "Fog", 48: "Fog",
    51: "Drizzle", 53: "Drizzle", 55: "Drizzle",
    61: "Rain", 63: "Rain", 65: "Heavy rain",
    71: "Snow", 73: "Snow", 75: "Heavy snow",
    80: "Rain showers", 81: "Rain showers", 82: "Violent rain showers",
    95: "Thunderstorm", 96: "Thunderstorm with hail", 99: "Thunderstorm with hail",
}


async def geocode(client: httpx.AsyncClient, city: str) -> Location:
    """GET config.GEOCODE_URL with params name=city, count=1.
    Raise for HTTP errors. If "results" is missing or empty -> raise CityNotFound(city).
    Return the first result as a Location."""
    raise NotImplementedError  # TODO


async def get_weather(client: httpx.AsyncClient, loc: Location) -> Weather:
    """GET config.FORECAST_URL with latitude, longitude and current="temperature_2m,weather_code".
    Read response["current"]. Map weather_code with WEATHER_CODES (unknown -> f"Code {code}")."""
    raise NotImplementedError  # TODO


async def get_rate(client: httpx.AsyncClient, base: str, quote: str) -> ExchangeRate:
    """GET config.RATE_URL formatted with lowercase base/quote.
    Response looks like {"date": "...", "base": "USD", "quote": "INR", "rate": 94.93}."""
    raise NotImplementedError  # TODO
