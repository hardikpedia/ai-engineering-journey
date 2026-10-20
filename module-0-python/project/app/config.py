import os

from dotenv import load_dotenv

load_dotenv()

HTTP_TIMEOUT = float(os.getenv("HTTP_TIMEOUT", "10"))
FAVORITES_FILE = os.getenv("FAVORITES_FILE", "data/favorites.json")
GEOCODE_URL = "https://geocoding-api.open-meteo.com/v1/search"
FORECAST_URL = "https://api.open-meteo.com/v1/forecast"
RATE_URL = "https://api.frankfurter.dev/v2/rate/{base}/{quote}"
