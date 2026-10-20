from typing import Literal

from pydantic import BaseModel, Field, ValidationError


class Product(BaseModel):
    name: str = Field(min_length=1)
    price: float = Field(gt=0)
    currency: Literal["INR", "USD"] = "INR"
    tags: list[str] = []


def parse_products(rows: list[dict]) -> tuple[list[Product], int]:
    valid: list[Product] = []
    invalid = 0
    for row in rows:
        try:
            valid.append(Product.model_validate(row))
        except ValidationError:
            invalid += 1
    return valid, invalid
