from domain.posts.entities import Post
from domain.posts.repositories import PostRepository
from infrastructure.orm.post_model import PostModel
from core.database import SessionLocal

class SQLAlchemyPostRepository(PostRepository):
    def __init__(self):
        self.db = SessionLocal()

    def save(self, post: Post) -> Post:
        orm_post = PostModel(**post.__dict__)
        self.db.add(orm_post)
        self.db.commit()
        self.db.refresh(orm_post)
        return Post(**orm_post.__dict__)

    def get_by_id(self, post_id: int) -> Post | None:
        orm_post = self.db.query(PostModel).filter_by(id=post_id).first()
        return Post(**orm_post.__dict__) if orm_post else None