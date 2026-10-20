"""0.9 exercises. Run: uv run pytest tests -k ex09"""
import httpx


async def fetch_status_codes(client: httpx.AsyncClient, urls: list[str], limit: int = 3) -> list[int]:
    """GET every url concurrently, at most `limit` at a time.
    Return status codes in the SAME order as `urls`.
    If a request fails with a network error (httpx.HTTPError), use 0 for that url.
    Hints: asyncio.Semaphore, asyncio.gather."""
    raise NotImplementedError  # TODO
