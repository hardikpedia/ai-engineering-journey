"""0.7 Errors, files, JSON, env vars"""
import json
import os
from pathlib import Path

from dotenv import load_dotenv

# try / except / finally  (= try / catch / finally)
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print("caught:", e)
finally:
    print("always runs")


# Raise your own errors (= throw new Error())
class RateLimitError(Exception):
    pass


def call_api(remaining: int) -> str:
    if remaining <= 0:
        raise RateLimitError("too many requests")
    return "ok"


try:
    call_api(0)
except RateLimitError as e:
    print("retry later:", e)

# Files with pathlib + `with` (closes the file automatically, like try/finally)
data_dir = Path(__file__).parent / "tmp"
data_dir.mkdir(exist_ok=True)
notes = data_dir / "notes.txt"
notes.write_text("line 1\nline 2\n", encoding="utf-8")
with notes.open(encoding="utf-8") as f:
    for line in f:
        print("read:", line.strip())

# JSON (= JSON.stringify / JSON.parse)
config = {"model": "gpt", "max_tokens": 256}
(data_dir / "config.json").write_text(json.dumps(config, indent=2))
loaded = json.loads((data_dir / "config.json").read_text())
print(loaded["model"])

# Env vars: put secrets in .env, never in code. load_dotenv() reads .env into os.environ
(data_dir / ".env").write_text("API_KEY=demo-123\n")
load_dotenv(data_dir / ".env")
print("API_KEY:", os.environ.get("API_KEY"))
print("MISSING:", os.getenv("NOT_SET", "default"))
