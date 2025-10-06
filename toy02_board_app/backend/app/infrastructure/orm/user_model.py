from sqlalchemy import Column, Integer, String, Enum, DateTime
from app.core.database import Base
from datetime import datetime
import enum

class UserRole(str, enum.Enum):
    user = "user"
    admin = "admin"

class UserModel(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True)
    email = Column(String(120), unique=True)
    password = Column(String(255))
    role = Column(Enum(UserRole), default=UserRole.user)
    created_at = Column(DateTime, default=datetime.utcnow)
