# 0.8 Modules, packages, pyproject.toml

[← 0.7 Errors, files, env](07-errors-files-env.md) · [Module 0](../README.md) · Next: [0.9 async + httpx →](09-async.md)

**A `.py` file is a module; a folder of modules is a package. Imports work by dotted names from the project root, not by relative file paths.**

| JS | Python |
| --- | --- |
| `import { geocode } from "./app/clients.js"` | `from app.clients import geocode` |
| `import * as config from "./config"` | `from app import config` → `config.HTTP_TIMEOUT` |
| `export` | nothing — every top-level name can be imported |
| `index.js` in a folder | `__init__.py` (can be empty) |
| `if (require.main === module)` | `if __name__ == "__main__":` |
| `"dependencies"` in package.json | `dependencies = [...]` in pyproject.toml |
| `"devDependencies"` | `[dependency-groups] dev = [...]` |

The Module 0 project layout — the shape most Python services use:

```text
project/
├── pyproject.toml        # deps + tool config (pytest, etc.)
├── uv.lock               # exact versions (commit it)
├── .env                  # secrets (never commit)
├── app/
│   ├── __init__.py
│   ├── config.py         # reads env vars once
│   ├── models.py         # Pydantic models
│   ├── clients.py        # calls to external APIs
│   ├── storage.py        # persistence
│   └── main.py           # FastAPI routes
└── tests/
    ├── conftest.py       # shared pytest fixtures
    └── test_api.py
```

```toml
[project]
name = "city-brief"
requires-python = ">=3.13"
dependencies = ["fastapi==0.152.0", "httpx==0.28.1", "pydantic==2.14.1"]

[dependency-groups]
dev = ["pytest==9.1.1", "respx==0.23.1"]
```

## Rules that keep imports sane

- One responsibility per module: routes in `main.py`, API calls in `clients.py`, models in `models.py`.
- Run from the project root: `uv run pytest`, `uv run uvicorn app.main:app`. Running a file from inside a subfolder breaks imports.
- Two modules importing each other → `ImportError` (circular import). Move the shared part into a third module.

## Do

No separate exercise. Open `pyproject.toml` and `project/` and match them to the table above. You'll practise this in the project.
