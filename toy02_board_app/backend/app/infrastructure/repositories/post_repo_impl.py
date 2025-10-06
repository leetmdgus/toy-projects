from domain.posts.entities import Post
from domain.posts.repository import PostRepository
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

    def get_all(self) -> list[Post]:
        orm_posts = self.db.query(PostModel).all()
        return [Post(**p.__dict__) for p in orm_posts]

    def update(self, post: Post) -> Post | None:
        orm_post = self.db.query(PostModel).filter_by(id=post.id).first()
        if not orm_post:
            return None
        if post.title:
            orm_post.title = post.title
        if post.content:
            orm_post.content = post.content
        self.db.commit()
        self.db.refresh(orm_post)
        return Post(**orm_post.__dict__)

    def delete(self, post_id: int) -> bool:
        orm_post = self.db.query(PostModel).filter_by(id=post_id).first()
        if not orm_post:
            return False
        self.db.delete(orm_post)
        self.db.commit()
        return True
