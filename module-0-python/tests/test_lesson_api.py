"""0.10 + 0.11: testing a FastAPI app with TestClient (no server needed)."""
from fastapi.testclient import TestClient

from lessons.l11_fastapi_app import app, notes

client = TestClient(app)


def setup_function():
    notes.clear()           # fresh "database" for every test


def test_health():
    assert client.get("/health").json() == {"status": "ok"}


def test_create_and_get_note():
    r = client.post("/notes", json={"title": "Learn Python"})
    assert r.status_code == 201
    note_id = r.json()["id"]
    assert client.get(f"/notes/{note_id}").json()["title"] == "Learn Python"


def test_validation_error_returns_422():
    assert client.post("/notes", json={"title": ""}).status_code == 422


def test_missing_note_returns_404():
    assert client.get("/notes/999").status_code == 404
