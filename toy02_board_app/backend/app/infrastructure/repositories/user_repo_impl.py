from app.core.database import SessionLocal
from app.domain.users.entities import User, Role
from app.domain.users.repository import UserRepository
from app.infrastructure.orm.user_model import UserModel
from datetime import datetime

class SQLAlchemyUserRepository(UserRepository):
    def __init__(self):
        self.db = SessionLocal()

    def get_all(self) -> list[User]:
        users = self.db.query(UserModel).all()
        return [
            User(
                id=u.id,
                username=u.username,
                email=u.email,
                role=Role(u.role),
                created_at=u.created_at or datetime.utcnow()
            )
            for u in users
        ]

    def delete(self, user_id: int):
        user = self.db.query(UserModel).filter_by(id=user_id).first()
        if not user:
            raise ValueError("존재하지 않는 유저입니다.")
        self.db.delete(user)
        self.db.commit()
        
    def get_by_email(self, email: str):
        user = self.db.query(UserModel).filter_by(email=email).first()
        if not user:
            return None
        return User(
            id=user.id,
            username=user.username,
            email=user.email,
            password=user.password,
            role=Role(user.role),
            created_at=user.created_at,
        )
        
    def get_by_username(self, username: str):
        user = self.db.query(UserModel).filter_by(username=username).first()
        if not user:
            return None
        return User(
            id=user.id,
            username=user.username,
            email=user.email,
            password=user.password,
            role=Role(user.role),
            created_at=user.created_at,
        )