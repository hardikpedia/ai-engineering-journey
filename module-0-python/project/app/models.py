from typing import Annotated

from pydantic import BaseModel, Field, StringConstraints

CurrencyCode = Annotated[str, StringConstraints(pattern=r"^[A-Za-z]{3}$", to_upper=True)]


class Location(BaseModel):
    name: str
    country: str
    latitude: float
    longitude: float
    timezone: str


class Weather(BaseModel):
    temperature_c: float
    condition: str


class ExchangeRate(BaseModel):
    base: str
    quote: str
    rate: float
    date: str


class Brief(BaseModel):
    location: Location
    weather: Weather | None
    exchange_rate: ExchangeRate | None
    warnings: list[str] = []


class FavoriteIn(BaseModel):
    city: str = Field(min_length=1, max_length=80)
    currency: CurrencyCode = "INR"


class Favorite(FavoriteIn):
    id: int
