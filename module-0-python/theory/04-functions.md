# 0.4 Functions

[← 0.3 Data structures](03-data-structures.md) · [Module 0](../README.md) · Next: [0.5 Classes →](05-classes.md)

**Python functions add two things JS lacks: keyword arguments and decorators.**

| JS | Python |
| --- | --- |
| `function greet(name, greeting = "Hello")` | `def greet(name, greeting="Hello"):` |
| `greet("A", {greeting: "Hi"})` (options object) | `greet("A", greeting="Hi")` (keyword argument) |
| `(...nums) => …` | `def total(*nums):` (a tuple) |
| options object | `def describe(**info):` (a dict) |
| `fn(...args)` | `fn(*args)`, `fn(**opts)` |
| `n => n * n` | `lambda n: n * n` |
| higher-order fn / middleware | decorator `@timed` |

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("Hardik", greeting="Hi")      # keyword args: very common in AI SDKs
# e.g. client.chat(model="...", messages=[...], temperature=0.2)
```

## Decorators

A decorator wraps a function, like Express middleware around a handler. `@timed` above `def slow_add` is the same as `slow_add = timed(slow_add)`.

```python
import time
from functools import wraps

def timed(fn):
    @wraps(fn)                       # keeps fn's name and docstring
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = fn(*args, **kwargs)
        print(f"{fn.__name__} took {(time.perf_counter() - start) * 1000:.2f} ms")
        return result
    return wrapper

@timed
def slow_add(a, b):
    time.sleep(0.05)
    return a + b
```

You'll use decorators constantly: `@app.get("/")` in FastAPI, `@tool` in LangChain, `@pytest.fixture` in tests.

## Gotchas

- **Never use `[]` or `{}` as a default argument.** The same object is reused on every call. Use `items=None`, then `if items is None: items = []`.
- Closures can read outer variables, but changing one needs `nonlocal count`.
- A lambda is one expression only. For anything longer, write `def`.

## Do

```bash
uv run python lessons/l04_functions.py
uv run pytest -k ex04          # exercises/ex04_functions.py: make_counter (closure), retry (decorator)
```
