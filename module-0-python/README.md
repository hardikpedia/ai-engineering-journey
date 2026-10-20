# Module 0 — Python for JS/TS Devs

Lessons are in the Module 0 doc. This folder is the code.

```bash
uv sync                          # install pinned packages into .venv
uv run python lessons/l02_syntax.py   # run any lesson
uv run pytest                    # your exercises (12 fail until you solve them)
uv run pytest -k ex03            # one unit only
SOLUTIONS=1 uv run pytest        # check the reference solutions (all pass)
uv run uvicorn lessons.l11_fastapi_app:app --reload   # FastAPI lesson -> http://127.0.0.1:8000/docs
```

Windows PowerShell: `$env:SOLUTIONS=1; uv run pytest`

| Folder | What |
| --- | --- |
| lessons/ | one runnable file per unit (0.1–0.11) |
| exercises/ | TODO functions — make the tests pass |
| solutions/ | open after 20 minutes of trying |
| tests/ | tests for exercises + the FastAPI lesson |
| project/ | City Brief API starter (own pyproject, own tests) |
