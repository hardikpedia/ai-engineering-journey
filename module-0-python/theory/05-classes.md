# 0.5 Classes, dataclasses, type hints

[← 0.4 Functions](04-functions.md) · [Module 0](../README.md) · Next: [0.6 Pydantic →](06-pydantic.md)

**Classes work like JS classes, but `this` is written out as `self`. Type hints look like TS types but are never checked at runtime.**

| JS / TS | Python |
| --- | --- |
| `constructor(start = 0)` | `def __init__(self, start: int = 0) -> None:` |
| `this.value` | `self.value` (every method takes `self` first) |
| `class B extends A` | `class B(A):` |
| `super.increment()` | `super().increment()` |
| `toString()` | `__repr__` |
| `get remaining()` | `@property def remaining(self):` |
| `interface Msg { role: string; tokens?: number }` | `@dataclass class Msg: role: str; tokens: int = 0` |
| `number \| null` | `float \| None` |
| `string[]` | `list[str]` |
| `Record<string, number>` | `dict[str, int]` |

```python
class Counter:
    def __init__(self, start: int = 0) -> None:
        self.value = start

    def increment(self, by: int = 1) -> int:
        self.value += by
        return self.value
```

```python
from dataclasses import dataclass, field

@dataclass                      # auto-writes __init__, __repr__, __eq__
class Message:
    role: str
    content: str
    tokens: int = 0
    tags: list[str] = field(default_factory=list)   # safe mutable default

m = Message(role="user", content="Hi")
print(m)        # Message(role='user', content='Hi', tokens=0, tags=[])

def average(values: list[float]) -> float | None:
    return sum(values) / len(values) if values else None
```

Type hints are for you, VS Code and type checkers. Wrong data still gets through at runtime. When data comes from outside (an API, a user, an LLM), use Pydantic ([0.6](06-pydantic.md)) to actually validate it.

## Gotchas

- Forgetting `self` in a method signature → `TypeError: takes 0 positional arguments but 1 was given`.
- In a dataclass, list defaults must use `field(default_factory=list)`.

## Do

```bash
uv run python lessons/l05_classes.py
uv run pytest -k ex05          # exercises/ex05_classes.py: TokenBudget (property + method)
```
