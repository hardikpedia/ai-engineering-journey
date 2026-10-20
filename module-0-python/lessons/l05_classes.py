"""0.5 Classes, dataclasses, type hints"""
from dataclasses import dataclass, field


class Counter:
    def __init__(self, start: int = 0) -> None:   # constructor
        self.value = start                         # self = this (always explicit)

    def increment(self, by: int = 1) -> int:
        self.value += by
        return self.value

    def __repr__(self) -> str:                     # like toString() for debugging
        return f"Counter(value={self.value})"


c = Counter()
c.increment()
c.increment(5)
print(c)


# Inheritance
class LoudCounter(Counter):
    def increment(self, by: int = 1) -> int:
        new_value = super().increment(by)
        print("LOUD:", new_value)
        return new_value


LoudCounter(10).increment()


# dataclass = class that auto-writes __init__, __repr__, __eq__ (like a TS interface + constructor)
@dataclass
class Message:
    role: str
    content: str
    tokens: int = 0
    tags: list[str] = field(default_factory=list)   # safe mutable default


m = Message(role="user", content="Hi")
print(m, m == Message("user", "Hi"))


# Type hints: like TS types, but NOT enforced at runtime (tools like mypy/pyright check them)
def average(values: list[float]) -> float | None:  # float | None  = number | null
    if not values:
        return None
    return sum(values) / len(values)


print(average([1, 2, 3]), average([]))
# average(["oops"]) is NOT stopped by the hints - it crashes at runtime. Pydantic (0.6) fixes this.
