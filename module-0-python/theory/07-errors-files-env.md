# 0.7 Errors, files, JSON, env vars

[← 0.6 Pydantic](06-pydantic.md) · [Module 0](../README.md) · Next: [0.8 Modules & packages →](08-modules-packages.md)

**`try/except` replaces `try/catch`; `with` replaces manual cleanup; `.env` keeps secrets out of code.**

| JS | Python |
| --- | --- |
| `try { } catch (e) { } finally { }` | `try: … except SomeError as e: … finally: …` |
| `throw new Error("x")` | `raise ValueError("x")` |
| `class RateLimitError extends Error {}` | `class RateLimitError(Exception): pass` |
| `fs.readFileSync(p, "utf8")` | `Path(p).read_text(encoding="utf-8")` |
| `path.join(dir, "a.txt")` | `Path(dir) / "a.txt"` |
| `JSON.stringify(o, null, 2)` | `json.dumps(o, indent=2)` |
| `JSON.parse(s)` | `json.loads(s)` |
| `process.env.API_KEY` | `os.environ["API_KEY"]` or `os.getenv("API_KEY")` |
| `dotenv.config()` | `load_dotenv()` |

```python
import json, os
from pathlib import Path
from dotenv import load_dotenv

class RateLimitError(Exception):
    pass

def call_api(remaining: int) -> str:
    if remaining <= 0:
        raise RateLimitError("too many requests")
    return "ok"

try:
    call_api(0)
except RateLimitError as e:          # catch specific errors, not everything
    print("retry later:", e)

config = json.loads(Path("config.json").read_text(encoding="utf-8"))

with open("notes.txt", encoding="utf-8") as f:   # file closes itself when the block ends
    for line in f:
        print(line.strip())

load_dotenv()                         # reads .env into os.environ
api_key = os.getenv("OPENAI_API_KEY")
```

From Module 1 on, every API key lives in `.env`, and `.env` is git-ignored (see [`.env.example`](../../.env.example)). A leaked key gets used by someone else within minutes.

## Gotchas

- A bare `except:` catches everything, including Ctrl+C. Always name the error type.
- Always pass `encoding="utf-8"` when reading text. Windows defaults differ and break Hindi text.
- `os.environ["X"]` throws if missing; `os.getenv("X", "default")` doesn't.

## Do

```bash
uv run python lessons/l07_errors_files_env.py
uv run pytest -k ex07          # exercises/ex07_files.py: save_json, load_json that never crashes
```
