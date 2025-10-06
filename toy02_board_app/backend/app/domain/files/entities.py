from dataclasses import dataclass
from datetime import datetime

@dataclass
class File:
    id: int | None
    path: str
    filename: str
    uploaded_at: datetime