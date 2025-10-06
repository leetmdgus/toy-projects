from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class Role(str, Enum):
    USER = "user"
    ADMIN = "admin"

@dataclass
class User:
    id: int | None
    username: str
    email: str
    password: str
    role: Role
    created_at: datetime