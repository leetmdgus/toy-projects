from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime
from core.database import Base
from datetime import datetime

class PostModel(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100))
    content = Column(Text)
    author_id = Column(Integer, ForeignKey("users.id"))
    created_at = Column(DateTime, default=datetime.utcnow)