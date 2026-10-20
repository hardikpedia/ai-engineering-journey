import pytest
from fastapi.testclient import TestClient

from app import config
from app.main import app


@pytest.fixture
def client(tmp_path, monkeypatch):
    monkeypatch.setattr(config, "FAVORITES_FILE", str(tmp_path / "favorites.json"))
    with TestClient(app) as c:     # `with` runs the lifespan (startup/shutdown)
        yield c
