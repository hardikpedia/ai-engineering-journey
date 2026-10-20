# 0.10 Testing with pytest

[← 0.9 async + httpx](09-async.md) · [Module 0](../README.md) · Next: [0.11 FastAPI →](11-fastapi.md)

**pytest is Jest without the boilerplate: any function named `test_*` in a `test_*.py` file is a test, and a plain `assert` is the assertion.**

| Jest | pytest |
| --- | --- |
| `test("adds", () => {...})` | `def test_adds():` |
| `expect(x).toBe(3)` | `assert x == 3` |
| `expect(() => f()).toThrow()` | `with pytest.raises(ValueError): f()` |
| `beforeEach` | a fixture (`@pytest.fixture`) or `setup_function()` |
| `jest.mock("axios")` | `respx` (mocks httpx) / `monkeypatch` |
| `npx jest -t "name"` | `uv run pytest -k name` |
| `--bail` | `uv run pytest -x` (stop at first failure) |

```python
import pytest

def test_grade():
    assert grade(95) == "A"
    with pytest.raises(ValueError):
        grade(101)

@pytest.fixture
def budget():                 # runs fresh for every test that asks for it
    return TokenBudget(limit=100)

def test_spend(budget):       # fixture injected by parameter name
    assert budget.spend(30) == 70

async def test_async_code():  # works because asyncio_mode = "auto" in pyproject.toml
    assert await fake_call("a") == "a done"
```

## Mocking HTTP with respx

Never hit real APIs in tests: slow, flaky, and with LLMs it costs money.

```python
import httpx, respx

@respx.mock
async def test_handles_404():
    respx.get("https://x.test/missing").mock(return_value=httpx.Response(404))
    respx.get("https://x.test/down").mock(side_effect=httpx.ConnectError("down"))
    ...
```

## Useful commands

```bash
uv run pytest                 # all tests
uv run pytest -k ex03         # only tests with "ex03" in the name
uv run pytest -x -v           # stop at first failure, verbose
SOLUTIONS=1 uv run pytest     # run the same tests against solutions/
```

In this course, **tests are the spec**. From Module 4 on, you'll write evals the same way — tests for LLM quality.

## Gotchas

- Test files and functions must start with `test_`, or pytest silently skips them.
- The built-in `tmp_path` fixture gives every test a fresh temp folder. Use it for file tests.

## Do

Read `tests/test_lesson_api.py` (it tests the 0.11 app) and `tests/test_exercises.py`. You'll write tests like these in later modules.
