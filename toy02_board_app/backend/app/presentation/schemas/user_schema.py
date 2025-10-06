from pydantic import BaseModel
from datetime import datetime
from enum import Enum

class Role(str, Enum):
    USER = "user"
    ADMIN = "admin"

class UserResponse(BaseModel):
    id: int
    username: str
    email: str
    role: Role
    created_at: datetime