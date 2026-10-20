# 0.11 FastAPI basics

[← 0.10 pytest](10-pytest.md) · [Module 0](../README.md) · Next: [0.12 Claude Code →](12-claude-code.md)

**FastAPI is Express + Zod + Swagger in one: you declare types, and it validates requests, converts params and writes API docs for you.**

| Express | FastAPI |
| --- | --- |
| `app.get("/notes", (req, res) => ...)` | `@app.get("/notes")` above a function |
| `req.params.id` | function parameter matching `{note_id}` in the path |
| `req.query.limit` | any other simple parameter: `limit: int = 10` |
| `req.body` + manual validation | parameter typed as a Pydantic model |
| `res.status(404).json(...)` | `raise HTTPException(status_code=404, detail=...)` |
| `res.status(201)` | `@app.post("/notes", status_code=201)` |
| middleware for shared deps | `Depends(...)` (dependency injection) |
| `app.listen(8000)` | `uv run uvicorn app.main:app --reload` |
| writing Swagger by hand | automatic at `/docs` |

```python
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Notes API")

class NoteIn(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    body: str = ""

class Note(NoteIn):
    id: int

notes: dict[int, Note] = {}

@app.post("/notes", status_code=201)
def create_note(data: NoteIn) -> Note:          # bad body -> automatic 422
    note = Note(id=len(notes) + 1, **data.model_dump())
    notes[note.id] = note
    return note

@app.get("/notes/{note_id}")
def get_note(note_id: int) -> Note:             # "/notes/abc" -> automatic 422
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    return notes[note_id]
```

## Two patterns the project uses

- **lifespan** — code that runs at startup and shutdown. Create the shared `httpx.AsyncClient` there, close it at the end.
- **Depends** — routes ask for what they need (`http: httpx.AsyncClient = Depends(get_http)`). Tests can swap these out.

## Gotchas

- Use `async def` routes when you `await` something inside. Plain `def` routes are fine for non-async code; FastAPI runs them in a thread.
- Never call blocking code (like `time.sleep` or a sync HTTP library) inside an `async def` route. It blocks every other request.
- Validation errors are `422`, not `400`. That's FastAPI's default.

## Do

```bash
uv run uvicorn lessons.l11_fastapi_app:app --reload
# open http://127.0.0.1:8000/docs and try every endpoint
uv run pytest tests/test_lesson_api.py
```
