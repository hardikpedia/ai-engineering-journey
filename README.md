# AI Engineering Journey

A hands-on path from **zero Python** to **job-ready AI Engineer**, one module at a time.
Based on the CampusX AI Engineering Roadmap 2026 (100-Days track), adapted for a JS/TS developer at 10 hrs/week.

## Quick start

```bash
# 1. Install uv (Python package + version manager) - once
curl -LsSf https://astral.sh/uv/install.sh | sh        # macOS / Linux
# Windows PowerShell:  powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"

# 2. Clone and start Module 0
git clone <this-repo-url>
cd ai-engineering-journey/module-0-python
uv sync                      # installs Python 3.13 + pinned packages
uv run pytest                # failing tests = your to-do list
```

## Modules

| # | Module | Weeks | Folder | Status |
|---|---|---|---|---|
| 0 | Python for JS/TS devs | 1–2 | [module-0-python](module-0-python) | Ready |
| 1 | LLM Fundamentals | 3 | module-1-llm-fundamentals | Coming next |
| 2 | Building with LLM APIs | 4–5 | module-2-llm-apis | — |
| 3 | Prompt Engineering | 6 | module-3-prompt-engineering | — |
| 4 | RAG | 7–12 | module-4-rag | — |
| 5 | Agents | 13–17 | module-5-agents | — |
| 6 | Shipping to Production | 18–20 | module-6-production | — |
| — | Portfolio projects | 21–26 | portfolio/ | — |
| — | Interview prep | 27–28 | interview/ | — |

New modules are added as **new folders only**. Existing folders (where your work lives) are never changed by course updates.

## How each module works

Every module folder has the same shape:

```text
module-N-name/
├── README.md        # commands for this module
├── pyproject.toml   # its own pinned dependencies (each module is independent)
├── lessons/         # runnable example per unit
├── exercises/       # TODO functions - make the tests pass
├── solutions/       # open after 20 minutes of trying
├── tests/           # the spec for exercises
└── project/         # the module project (own tests)
```

Loop: read the lesson doc → run `lessons/` → solve `exercises/` → build `project/` → get it reviewed → quiz → tick the tracker.

```bash
uv run pytest -k ex03          # one unit
SOLUTIONS=1 uv run pytest      # check reference solutions
```

## Getting new modules

```bash
git pull          # new module folders appear; your work is untouched
```

## Rules

1. A unit is done when its exercise passes, not when the lesson is read.
2. Type the code yourself.
3. Commit at least once a week (`git add -A && git commit -m "module 0: ex02-ex05"`).
4. Secrets go in `.env` (see `.env.example`). Never commit keys.
5. Fill `NOTES.md` every Sunday.
