"""0.5 exercises. Run: uv run pytest tests -k ex05"""
from dataclasses import dataclass


@dataclass
class TokenBudget:
    """Tracks LLM token spend.
    - fields: limit (int), used (int, default 0)
    - property `remaining` -> limit - used
    - method spend(tokens) -> adds to used, returns remaining.
      Raise ValueError if tokens < 0 or if it would exceed the limit."""
    limit: int
    used: int = 0

    # TODO: add the `remaining` property and the `spend` method
