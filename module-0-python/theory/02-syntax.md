# 0.2 Syntax vs JS

[← 0.1 Setup](01-setup.md) · [Module 0](../README.md) · Next: [0.3 Data structures →](03-data-structures.md)

**Python reads like JS with fewer symbols: no `{}`, no `;`, no `let`. Indentation is the syntax.**

| JS / TS | Python |
| --- | --- |
| `let userName = "Hardik"` | `user_name = "Hardik"` (snake_case) |
| `true` / `false` / `null` | `True` / `False` / `None` |
| `` `Hi ${name}` `` | `f"Hi {name}"` |
| `&&` `\|\|` `!` | `and` `or` `not` |
| `===` | `==` (compares values, even lists) |
| `x === null` | `x is None` |
| `else if` | `elif` |
| `cond ? a : b` | `a if cond else b` |
| `i++` | `i += 1` |
| `for (let i=0;i<3;i++)` | `for i in range(3):` |
| `arr.forEach((x, i) => …)` | `for i, x in enumerate(arr):` |
| `Math.floor(7/2)` | `7 // 2` |
| `2 ** 10` | `2 ** 10` (same) |
| `// comment` | `# comment` |

```python
user_name = "Hardik"
age = 25
is_admin = False

if age >= 18 and not is_admin:      # 4 spaces of indentation = the block
    print(f"{user_name} is an adult")
elif age >= 13:
    print("teen")
else:
    print("child")

for index, name in enumerate(["a", "b"]):
    print(index, name)
```

Falsy values: `0`, `""`, `[]`, `{}`, `None`, `False`. Unlike JS, an **empty list or dict is falsy**.

## Gotchas

- Mixed tabs and spaces → `IndentationError`. Let VS Code use 4 spaces.
- `[1, 2] == [1, 2]` is `True` in Python (JS says `false`).
- `/` always gives a float: `7 / 2 = 3.5`. Use `//` for whole-number division.

## Do

```bash
uv run python lessons/l02_syntax.py
uv run pytest -k ex02          # exercises/ex02_syntax.py: fizzbuzz, grade
```
