# 0.3 Data structures

[← 0.2 Syntax](02-syntax.md) · [Module 0](../README.md) · Next: [0.4 Functions →](04-functions.md)

**Four containers cover almost everything: list (array), dict (object/Map), tuple (fixed list), set (Set).**

| JS | Python |
| --- | --- |
| `arr.push(x)` / `arr.pop()` | `lst.append(x)` / `lst.pop()` |
| `arr.length` | `len(lst)` |
| `arr.at(-1)` | `lst[-1]` |
| `arr.slice(1, 3)` | `lst[1:3]` |
| `obj.name` | `d["name"]` (dot access doesn't work on dicts) |
| `obj.email ?? "n/a"` | `d.get("email", "n/a")` |
| `Object.entries(obj)` | `d.items()` |
| `"name" in obj` | `"name" in d` |
| `{...a, role: "x"}` | `{**a, "role": "x"}` |
| `const [x, y] = pt` | `x, y = pt` |
| `const [first, ...rest] = arr` | `first, *rest = arr` |
| `new Set([1, 2])` | `{1, 2}` |
| `arr.map(n => n*n)` | `[n * n for n in arr]` |
| `arr.filter(n => n%2===0)` | `[n for n in arr if n % 2 == 0]` |

```python
user = {"name": "Hardik", "role": "SDE"}
user["city"] = "Gurugram"
print(user.get("email", "n/a"))          # n/a

for key, value in user.items():
    print(key, "=", value)

evens = [n for n in range(10) if n % 2 == 0]       # comprehension = map + filter
lengths = {name: len(name) for name in ["ana", "bob"]}
```

Comprehensions are everywhere in AI code (building messages, cleaning chunks). Learn to read them fluently.

## Gotchas

- `d["missing"]` throws `KeyError`. Use `d.get("missing")` when the key may not exist.
- `sorted(lst)` returns a new list; `lst.sort()` changes it in place and returns `None`.
- Tuples can't be changed after creation. Use them for fixed pairs like `(word, count)`.

## Do

```bash
uv run python lessons/l03_data_structures.py
uv run pytest -k ex03          # exercises/ex03_data.py: word_count, top_n, unique_sorted
```
