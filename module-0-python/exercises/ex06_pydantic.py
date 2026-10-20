"""0.6 exercises. Run: uv run pytest tests -k ex06"""
from pydantic import BaseModel


class Product(BaseModel):
    """TODO:
    - name: non-empty string
    - price: float, must be > 0
    - currency: only "INR" or "USD", default "INR"
    - tags: list of strings, default empty"""
    pass


def parse_products(rows: list[dict]) -> tuple[list[Product], int]:
    """Validate each row. Return (valid_products, number_of_invalid_rows)."""
    raise NotImplementedError  # TODO
