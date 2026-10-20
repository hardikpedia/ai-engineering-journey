"""0.9 async/await + httpx  (asyncio.gather = Promise.all)"""
import asyncio
import time

import httpx


async def fake_call(name: str, seconds: float) -> str:
    await asyncio.sleep(seconds)          # like await new Promise(r => setTimeout(r, ms))
    return f"{name} done"


async def main() -> None:
    # Sequential: ~0.6s
    start = time.perf_counter()
    for n in ["a", "b", "c"]:
        await fake_call(n, 0.2)
    print(f"sequential: {time.perf_counter() - start:.2f}s")

    # Concurrent: ~0.2s
    start = time.perf_counter()
    results = await asyncio.gather(*(fake_call(n, 0.2) for n in ["a", "b", "c"]))
    print(results, f"concurrent: {time.perf_counter() - start:.2f}s")

    # Bounded concurrency with a semaphore (stay under API rate limits)
    limit = asyncio.Semaphore(2)

    async def limited(n: str) -> str:
        async with limit:
            return await fake_call(n, 0.2)

    start = time.perf_counter()
    await asyncio.gather(*(limited(str(i)) for i in range(4)))
    print(f"max 2 at a time: {time.perf_counter() - start:.2f}s")

    # Real HTTP with httpx (= fetch). Reuse ONE client; always set a timeout.
    async with httpx.AsyncClient(timeout=10) as client:
        try:
            r = await client.get("https://api.frankfurter.dev/v2/rate/usd/inr")
            r.raise_for_status()                 # throws on 4xx/5xx (fetch doesn't!)
            print("USD->INR:", r.json()["rate"])
        except httpx.HTTPError as e:
            print("network call failed (fine if offline):", type(e).__name__)


asyncio.run(main())                       # entry point: starts the event loop
