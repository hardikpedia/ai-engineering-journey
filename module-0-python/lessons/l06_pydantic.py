"""0.6 Pydantic - runtime validation, like Zod"""
from typing import Literal

from pydantic import BaseModel, Field, ValidationError


class ChatRequest(BaseModel):
    model: str
    prompt: str = Field(min_length=1)
    temperature: float = Field(default=0.7, ge=0, le=2)
    role: Literal["user", "system"] = "user"         # like z.enum([...])
    tags: list[str] = []                               # Pydantic copies defaults, safe here


# Valid input; "0.2" string is coerced to float 0.2
req = ChatRequest(model="gpt", prompt="Hello", temperature="0.2")
print(req)
print(req.model_dump())            # -> dict      (like JSON.parse(JSON.stringify(obj)))
print(req.model_dump_json())       # -> JSON string

# Invalid input raises ValidationError with every problem listed
try:
    ChatRequest(model="gpt", prompt="", temperature=5, role="admin")
except ValidationError as e:
    for err in e.errors():
        print(err["loc"], "->", err["msg"])

# Parse straight from JSON
raw = '{"model": "claude", "prompt": "Hi", "tags": ["test"]}'
print(ChatRequest.model_validate_json(raw))


# Nested models
class Conversation(BaseModel):
    id: int
    messages: list[ChatRequest]


conv = Conversation.model_validate({"id": 1, "messages": [{"model": "m", "prompt": "p"}]})
print(conv.messages[0].temperature)
