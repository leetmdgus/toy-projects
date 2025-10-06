from pydantic import BaseModel
from datetime import datetime

class PostCreate(BaseModel):
    title: str
    content: str
    author_id: int

class PostUpdate(BaseModel):
    title: str | None = None
    content: str | None = None

class PostResponse(BaseModel):
    id: int
    title: str
    content: str
    author_id: int
    created_at: datetime

    class Config:
        from_attributes = True
