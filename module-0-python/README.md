# Module 0 — Python for JS/TS Devs

**Goal:** go from zero Python to a typed, tested, async FastAPI service in 2 weeks (~20 hrs).
Everything is taught as "you know this in JS — here's the Python way".

## How to study one unit

1. **Read** the theory page (15–20 min).
2. **Run** the lesson file, and match each output line to its code.
3. **Play** — change values, break things, read the errors.
4. **Exercise** — fill the `TODO`s until `uv run pytest -k exNN` is green.
5. **Close** — tick the unit below, then `git commit`.

Stuck for 20 min → peek at `solutions/`. Stuck for 30 min → paste the error to Claude.

## Units

| Week | Unit | Theory | Run | Exercise |
| --- | --- | --- | --- | --- |
| 1 | 0.1 Setup | [01-setup](theory/01-setup.md) | `lessons/l01_setup.py` | — |
| 1 | 0.2 Syntax vs JS | [02-syntax](theory/02-syntax.md) | `lessons/l02_syntax.py` | `ex02_syntax.py` |
| 1 | 0.3 Data structures | [03-data-structures](theory/03-data-structures.md) | `lessons/l03_data_structures.py` | `ex03_data.py` |
| 1 | 0.4 Functions | [04-functions](theory/04-functions.md) | `lessons/l04_functions.py` | `ex04_functions.py` |
| 1 | 0.5 Classes, type hints | [05-classes](theory/05-classes.md) | `lessons/l05_classes.py` | `ex05_classes.py` |
| 1 | 0.6 Pydantic | [06-pydantic](theory/06-pydantic.md) | `lessons/l06_pydantic.py` | `ex06_pydantic.py` |
| 1 | 0.7 Errors, files, env | [07-errors-files-env](theory/07-errors-files-env.md) | `lessons/l07_errors_files_env.py` | `ex07_files.py` |
| 2 | 0.8 Modules & packages | [08-modules-packages](theory/08-modules-packages.md) | — | — |
| 2 | 0.9 async + httpx | [09-async](theory/09-async.md) | `lessons/l09_async.py` | `ex09_async.py` |
| 2 | 0.10 pytest | [10-pytest](theory/10-pytest.md) | read `tests/` | — |
| 2 | 0.11 FastAPI | [11-fastapi](theory/11-fastapi.md) | `uvicorn lessons.l11_fastapi_app:app` | `tests/test_lesson_api.py` |
| 2 | 0.12 Claude Code | [12-claude-code](theory/12-claude-code.md) | — | after the project |
| 2 | **Project** | [City Brief API spec](project/README.md) | `cd project` | `uv run pytest` → 7 passed |

## Commands

```bash
uv sync                                   # install pinned packages into .venv
uv run python lessons/l02_syntax.py       # run a lesson
uv run pytest                             # all exercises (12 fail until you solve them)
uv run pytest -k ex03                     # one unit
SOLUTIONS=1 uv run pytest                 # reference solutions (all 16 pass)
uv run uvicorn lessons.l11_fastapi_app:app --reload   # then open http://127.0.0.1:8000/docs
```

Windows PowerShell: `$env:SOLUTIONS=1; uv run pytest`

## Folder map

| Folder | What |
| --- | --- |
| `theory/` | lesson pages — read these first |
| `lessons/` | one runnable file per unit |
| `exercises/` | TODO functions — make the tests pass |
| `solutions/` | open after 20 minutes of trying |
| `tests/` | the spec for the exercises |
| `project/` | City Brief API — the module project (own `pyproject.toml` and tests) |

## Done with Module 0 when

- [ ] All exercise tests pass (`uv run pytest` → 16 passed)
- [ ] Project tests pass (`cd project && uv run pytest` → 7 passed)
- [ ] 0.12 Claude Code exercise done
- [ ] Quiz ≥ 80% (ask Claude: "Module 0 quiz")

## Versions & sources

Verified 20 Oct 2026, pinned in `pyproject.toml`: Python 3.13, fastapi 0.152.0, pydantic 2.14.1, httpx 0.28.1, pytest 9.1.1, pytest-asyncio 1.4.0, respx 0.23.1, uvicorn 0.54.0, python-dotenv 1.2.4, httpx2 2.15.1 (test client only — newer Starlette's test client warns without it; app code still uses `httpx`).

Python 3.14 is the newest release, but 3.13 has the widest AI-library support today.

- [uv docs](https://docs.astral.sh/uv/) · [Pydantic](https://docs.pydantic.dev/latest/) · [FastAPI](https://fastapi.tiangolo.com/) · [httpx](https://www.python-httpx.org/) · [pytest](https://docs.pytest.org/)
- [Open-Meteo geocoding](https://open-meteo.com/en/docs/geocoding-api) · [Open-Meteo forecast](https://open-meteo.com/en/docs) · [Frankfurter](https://frankfurter.dev/)
- [Claude Code](https://code.claude.com/docs/en/overview)
