from dataclasses import dataclass
from datetime import datetime
from typing import Optional, List

@dataclass
class Post:
    id: Optional[int]
    title: str
    content: str
    author_id: int
    image_paths: List[str]
    created_at: datetime