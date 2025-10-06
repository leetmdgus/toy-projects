from dataclasses import dataclass
from datetime import datetime

@dataclass
class Post:
    id: int | None
    title: str
    content: str
    author_id: int
    created_at: datetime