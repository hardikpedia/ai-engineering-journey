# 0.1 Setup

[← Module 0](../README.md) · Next: [0.2 Syntax vs JS →](02-syntax.md)

**uv is Python's npm + nvm in one tool.** It installs Python, creates the project's isolated environment, and manages packages.

| You know (JS) | Python with uv |
| --- | --- |
| `nvm install 20` | `uv python install 3.13` |
| `npm init` | `uv init` |
| `package.json` | `pyproject.toml` |
| `package-lock.json` | `uv.lock` |
| `node_modules/` | `.venv/` (the virtual environment) |
| `npm install` | `uv sync` |
| `npm install axios` | `uv add httpx` |
| `npm install -D jest` | `uv add --dev pytest` |
| `npx tsx file.ts` / `node file.js` | `uv run python file.py` |

## Install (once)

```bash
# macOS / Linux
curl -LsSf https://astral.sh/uv/install.sh | sh
# or: brew install uv

# Windows (PowerShell)
powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
```

Open a new terminal, then:

```bash
uv --version
uv python install 3.13
```

## Run the module

```bash
cd ai-engineering-journey/module-0-python
uv sync                                   # creates .venv and installs pinned packages
uv run python lessons/l01_setup.py        # prints Python version + the .venv path
uv run pytest                             # 12 fail = expected; your exercises aren't done yet
```

## VS Code

Install the "Python" extension (by Microsoft). Then Cmd/Ctrl+Shift+P → "Python: Select Interpreter" → pick `./.venv`. Now autocomplete and type checks work.

## Gotchas

- Always run through `uv run …`. It uses the project's `.venv`, so you never "install globally" by mistake.
- Never commit `.venv/`. Do commit `pyproject.toml` and `uv.lock`.
- `pip install` is the old way. You'll see it in tutorials; with uv you use `uv add`.

## Do

- [ ] `uv run python lessons/l01_setup.py` prints Python 3.13
- [ ] VS Code uses `.venv`
