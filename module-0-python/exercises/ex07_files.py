"""0.7 exercises. Run: uv run pytest tests -k ex07"""
from pathlib import Path


def save_json(path: Path, data) -> None:
    """Write data as pretty JSON. Create parent folders if missing."""
    raise NotImplementedError  # TODO


def load_json(path: Path, default=None):
    """Read JSON from path. Return `default` if the file is missing or not valid JSON."""
    raise NotImplementedError  # TODO
