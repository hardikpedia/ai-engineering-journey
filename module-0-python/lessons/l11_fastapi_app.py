"""0.11 FastAPI - run with:  uv run uvicorn lessons.l11_fastapi_app:app --reload
Then open http://127.0.0.1:8000/docs
"""
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

app = FastAPI(title="Notes API")


class NoteIn(BaseModel):
    title: str = Field(min_length=1, max_length=100)
    body: str = ""


class Note(NoteIn):
    id: int


notes: dict[int, Note] = {}           # in-memory "database"


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/notes", status_code=201)
def create_note(data: NoteIn) -> Note:            # body validated by Pydantic automatically
    note = Note(id=len(notes) + 1, **data.model_dump())
    notes[note.id] = note
    return note


@app.get("/notes")
def list_notes(limit: int = 10) -> list[Note]:    # ?limit=5 -> query param, auto-converted to int
    return list(notes.values())[:limit]


@app.get("/notes/{note_id}")
def get_note(note_id: int) -> Note:                # path param
    if note_id not in notes:
        raise HTTPException(status_code=404, detail="Note not found")
    return notes[note_id]
