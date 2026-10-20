import asyncio

import httpx


async def fetch_status_codes(client: httpx.AsyncClient, urls: list[str], limit: int = 3) -> list[int]:
    semaphore = asyncio.Semaphore(limit)

    async def fetch(url: str) -> int:
        async with semaphore:
            try:
                response = await client.get(url)
                return response.status_code
            except httpx.HTTPError:
                return 0

    return await asyncio.gather(*(fetch(u) for u in urls))
