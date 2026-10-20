# 0.9 async/await + httpx

[← 0.8 Modules & packages](08-modules-packages.md) · [Module 0](../README.md) · Next: [0.10 pytest →](10-pytest.md)

**Same idea as JS: `async def` returns a coroutine (like a Promise), `await` waits for it. The difference: Python needs an event loop started explicitly with `asyncio.run()`.**

| JS | Python |
| --- | --- |
| `async function f() {}` | `async def f():` |
| `await f()` | `await f()` |
| `Promise.all([a(), b()])` | `await asyncio.gather(a(), b())` |
| `Promise.allSettled` | `asyncio.gather(..., return_exceptions=True)` |
| `setTimeout` promise | `await asyncio.sleep(0.2)` |
| top-level await / Node runs the loop | `asyncio.run(main())` |
| `fetch(url)` | `await client.get(url)` (httpx) |
| `if (!res.ok) throw ...` | `r.raise_for_status()` |
| `await res.json()` | `r.json()` (no await) |
| p-limit library | `asyncio.Semaphore(n)` |

```python
import asyncio, httpx

async def fake_call(name: str) -> str:
    await asyncio.sleep(0.2)
    return f"{name} done"

async def main():
    # 3 calls at once: ~0.2s total instead of ~0.6s
    results = await asyncio.gather(*(fake_call(n) for n in ["a", "b", "c"]))

    # At most 2 at a time (stay under API rate limits)
    limit = asyncio.Semaphore(2)
    async def limited(n):
        async with limit:
            return await fake_call(n)
    await asyncio.gather(*(limited(str(i)) for i in range(4)))   # ~0.4s

    # Real HTTP: create ONE client, reuse it, always set a timeout
    async with httpx.AsyncClient(timeout=10) as client:
        r = await client.get("https://api.frankfurter.dev/v2/rate/usd/inr")
        r.raise_for_status()
        print(r.json()["rate"])

asyncio.run(main())
```

**Why it matters:** this is the core skill for LLM apps. Model calls take seconds, so running independent calls concurrently (with a limit) is how you go fast without hitting rate limits.

## Gotchas

- Calling `fake_call("a")` without `await` does nothing; you only get a coroutine object and a warning.
- `time.sleep()` inside async code freezes everything. Use `await asyncio.sleep()`.
- Unlike `fetch`, httpx has a default timeout of 5s. Set it on purpose (`timeout=10`); LLM calls often need 60s+.
- Don't create a new client per request. Create one and reuse it; it pools connections.

## Do

```bash
uv run python lessons/l09_async.py
uv run pytest -k ex09          # exercises/ex09_async.py: fetch_status_codes with a concurrency limit
```
