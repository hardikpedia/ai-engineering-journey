import httpx
import respx

from app import config

GEO = {"results": [{"name": "Gurugram", "country": "India", "latitude": 28.46,
                    "longitude": 77.03, "timezone": "Asia/Kolkata"}]}
WEATHER = {"current": {"time": "2026-10-20T12:00", "interval": 900,
                       "temperature_2m": 31.2, "weather_code": 1}}
RATE = {"date": "2026-10-18", "base": "USD", "quote": "INR", "rate": 94.93}


def mock_all(weather=None, rate=None):
    respx.get(config.GEOCODE_URL).mock(return_value=httpx.Response(200, json=GEO))
    respx.get(config.FORECAST_URL).mock(return_value=weather or httpx.Response(200, json=WEATHER))
    respx.get("https://api.frankfurter.dev/v2/rate/usd/inr").mock(return_value=rate or httpx.Response(200, json=RATE))


def test_health(client):
    assert client.get("/health").json() == {"status": "ok"}


@respx.mock
def test_brief_happy_path(client):
    mock_all()
    body = client.get("/brief", params={"city": "Gurugram"}).json()
    assert body["location"]["country"] == "India"
    assert body["weather"] == {"temperature_c": 31.2, "condition": "Mainly clear"}
    assert body["exchange_rate"]["rate"] == 94.93
    assert body["warnings"] == []


@respx.mock
def test_brief_city_not_found(client):
    respx.get(config.GEOCODE_URL).mock(return_value=httpx.Response(200, json={}))
    r = client.get("/brief", params={"city": "Nowhereville"})
    assert r.status_code == 404
    assert "Nowhereville" in r.json()["detail"]


@respx.mock
def test_brief_partial_when_rate_api_down(client):
    mock_all(rate=httpx.Response(503))
    r = client.get("/brief", params={"city": "Gurugram"})
    assert r.status_code == 200
    assert r.json()["exchange_rate"] is None
    assert r.json()["warnings"] == ["Exchange rate unavailable"]


@respx.mock
def test_brief_502_when_geocoding_down(client):
    respx.get(config.GEOCODE_URL).mock(side_effect=httpx.ConnectTimeout("timeout"))
    assert client.get("/brief", params={"city": "Gurugram"}).status_code == 502


def test_brief_validates_currency(client):
    assert client.get("/brief", params={"city": "Gurugram", "currency": "RUPEES"}).status_code == 422


def test_favorites_crud(client):
    assert client.get("/favorites").json() == []
    r = client.post("/favorites", json={"city": "Pune", "currency": "usd"})
    assert r.status_code == 201 and r.json() == {"id": 1, "city": "Pune", "currency": "USD"}
    assert len(client.get("/favorites").json()) == 1
    assert client.delete("/favorites/1").status_code == 204
    assert client.delete("/favorites/1").status_code == 404
    assert client.post("/favorites", json={"city": ""}).status_code == 422
