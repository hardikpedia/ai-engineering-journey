# Module 0 Project — City Brief API

[← Module 0](../README.md)

**Build an async FastAPI service that returns a city's weather and the USD exchange rate in one call, fetched concurrently, with graceful failure.** It uses every unit of Module 0, and its weather and currency calls become your first LLM tools in Module 2.

## What's given vs what you write

- **Given:** `app/models.py`, `app/config.py`, app setup in `app/main.py`, and **all tests** (the tests are the spec).
- **You write:** `app/clients.py`, `app/storage.py`, and the routes marked `TODO` in `app/main.py`.

External APIs are free and need no key:
- Geocoding: `https://geocoding-api.open-meteo.com/v1/search?name=Pune&count=1`
- Weather: `https://api.open-meteo.com/v1/forecast?latitude=..&longitude=..&current=temperature_2m,weather_code`
- Rate: `https://api.frankfurter.dev/v2/rate/usd/inr` → `{"date": "...", "base": "USD", "quote": "INR", "rate": 94.93}`

## Endpoints

| Endpoint | Behaviour |
| --- | --- |
| `GET /health` | `{"status": "ok"}` (already done) |
| `GET /brief?city=Pune&currency=INR` | location + current weather + USD→currency rate |
| `GET /favorites` | list saved favorites |
| `POST /favorites` | save `{city, currency}` → 201 with an id |
| `DELETE /favorites/{id}` | 204, or 404 if unknown |

## Requirements

1. Geocode the city first. Unknown city → 404 naming the city. Geocoding service down → 502.
2. Fetch weather and rate **at the same time** with `asyncio.gather`.
3. If weather or rate fails, still return 200: that field is `null` and `warnings` says what's missing.
4. Validate inputs: city 1–80 characters, currency exactly 3 letters (else 422).
5. One shared `httpx.AsyncClient` with a timeout; never one client per request.
6. Favorites persist in a JSON file (path from the `FAVORITES_FILE` env var).
7. Log every upstream failure with `log.warning`.

## Suggested order

1. `storage.py` → `GET/POST/DELETE /favorites` → `uv run pytest -k favorites`
2. `clients.py` → `geocode`, `get_weather`, `get_rate`
3. `/brief` happy path → `uv run pytest -k happy`
4. Error cases → `uv run pytest`

## Run

```bash
uv sync
uv run pytest                              # 6 fail now → make all 7 pass
uv run uvicorn app.main:app --reload       # http://127.0.0.1:8000/docs
```

## Done when

- [ ] `uv run pytest` → 7 passed
- [ ] `/docs` shows every endpoint
- [ ] A real call for your city returns live weather and rate
- [ ] Committed and pushed
- [ ] [0.12 exercise](../theory/12-claude-code.md) done on this project

## Stretch (optional)

- 5-minute in-memory cache for exchange rates (they change once a day).
- `GET /brief/many?cities=Pune,Delhi,Mumbai` — geocode all cities concurrently, max 2 at a time.
- A `Dockerfile` (Docker is needed from Module 4).

Stuck for more than 30 minutes? Paste the failing test output to Claude. A reference solution exists — ask for it only after your tests pass or you've tried for a full session.
