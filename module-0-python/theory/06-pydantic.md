# 0.6 Pydantic — Python's Zod

[← 0.5 Classes](05-classes.md) · [Module 0](../README.md) · Next: [0.7 Errors, files, env →](07-errors-files-env.md)

**Pydantic validates data at runtime from a class definition. It is the most important library in this course: FastAPI, LangChain structured outputs and tool schemas are all built on it.**

| Zod | Pydantic |
| --- | --- |
| `z.object({...})` | `class X(BaseModel): ...` |
| `z.string().min(1)` | `str = Field(min_length=1)` |
| `z.number().min(0).max(2)` | `float = Field(ge=0, le=2)` |
| `z.enum(["user", "system"])` | `Literal["user", "system"]` |
| `.default(0.7)` | `= 0.7` |
| `schema.parse(data)` | `X.model_validate(data)` / `X(**data)` |
| `schema.parse(JSON.parse(s))` | `X.model_validate_json(s)` |
| `ZodError` | `ValidationError` |
| `z.infer<typeof X>` | the class itself is the type |

```python
from typing import Literal
from pydantic import BaseModel, Field, ValidationError

class ChatRequest(BaseModel):
    model: str
    prompt: str = Field(min_length=1)
    temperature: float = Field(default=0.7, ge=0, le=2)
    role: Literal["user", "system"] = "user"

req = ChatRequest(model="gpt", prompt="Hello", temperature="0.2")  # "0.2" -> 0.2
req.model_dump()        # -> dict
req.model_dump_json()   # -> JSON string

try:
    ChatRequest(model="gpt", prompt="", temperature=5, role="admin")
except ValidationError as e:
    for err in e.errors():
        print(err["loc"], "->", err["msg"])
# ('prompt',) -> String should have at least 1 character
# ('temperature',) -> Input should be less than or equal to 2
# ('role',) -> Input should be 'user' or 'system'
```

**Why it matters for AI:** an LLM's JSON output is untrusted input. In Module 2 you'll pass a Pydantic class to the model and validate every answer with it.

## Gotchas

- Pydantic **coerces** by default: `"0.2"` becomes `0.2`. Usually helpful; use `strict=True` when it isn't.
- `model_dump()` returns a dict, not JSON. `model_dump_json()` returns the JSON string.
- Pydantic v1 tutorials use `.dict()` and `.parse_obj()`. Those are outdated; v2 uses `model_dump()` and `model_validate()`.

## Do

```bash
uv run python lessons/l06_pydantic.py
uv run pytest -k ex06          # exercises/ex06_pydantic.py: Product model + parse_products
```
