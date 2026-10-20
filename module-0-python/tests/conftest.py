import importlib
import os

import pytest

# Test your work:          uv run pytest
# Check the solutions:     SOLUTIONS=1 uv run pytest   (Windows PowerShell: $env:SOLUTIONS=1; uv run pytest)
PACKAGE = "solutions" if os.getenv("SOLUTIONS") else "exercises"


@pytest.fixture
def load():
    return lambda name: importlib.import_module(f"{PACKAGE}.{name}")
