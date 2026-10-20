import logging
from contextlib import asynccontextmanager

import httpx
from fastapi import FastAPI, Request

from app import config
from app.storage import FavoritesStore

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(name)s: %(message)s")
log = logging.getLogger("city-brief")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # One shared HTTP client for the whole app (opened at startup, closed at shutdown)
    app.state.http = httpx.AsyncClient(timeout=config.HTTP_TIMEOUT)
    app.state.store = FavoritesStore(config.FAVORITES_FILE)
    yield
    await app.state.http.aclose()


app = FastAPI(title="City Brief API", lifespan=lifespan)


def get_http(request: Request) -> httpx.AsyncClient:
    return request.app.state.http


def get_store(request: Request) -> FavoritesStore:
    return request.app.state.store


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


# TODO 1: GET /brief?city=...&currency=INR  -> Brief
#   - validate: city 1-80 chars, currency = 3 letters (Query(..., pattern=...))
#   - geocode first: CityNotFound -> 404, httpx.HTTPError -> 502
#   - then weather + rate AT THE SAME TIME (asyncio.gather(..., return_exceptions=True))
#   - if one of them fails: set it to None and add "Weather unavailable" /
#     "Exchange rate unavailable" to warnings (still return 200)
#   - log failures with `log.warning`

# TODO 2: GET /favorites -> list[Favorite]
# TODO 3: POST /favorites (201) -> Favorite
# TODO 4: DELETE /favorites/{fav_id} (204), unknown id -> 404
