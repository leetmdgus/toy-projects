from app.domain.posts.entities import Post
from app.domain.posts.repository import PostRepository
from app.infrastructure.orm.post_model import PostModel
from app.core.database import SessionLocal

class SQLAlchemyPostRepository(PostRepository):
    def __init__(self):
        self.db = SessionLocal()

    def _to_entity(self, orm_post: PostModel) -> Post:
        """Convert ORM model to domain entity"""
        return Post(
            id=orm_post.id,
            title=orm_post.title,
            content=orm_post.content,
            author_id=orm_post.author_id,
            created_at=orm_post.created_at
        )

    def save(self, post: Post) -> Post:
        orm_post = PostModel(
            title=post.title,
            content=post.content,
            author_id=post.author_id,
            created_at=post.created_at
        )
        self.db.add(orm_post)
        self.db.commit()
        self.db.refresh(orm_post)
        return self._to_entity(orm_post)

    def get_by_id(self, post_id: int) -> Post | None:
        orm_post = self.db.query(PostModel).filter_by(id=post_id).first()
        return self._to_entity(orm_post) if orm_post else None

    def get_all(self) -> list[Post]:
        orm_posts = self.db.query(PostModel).all()
        return [self._to_entity(p) for p in orm_posts]

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
        return self._to_entity(orm_post)

    def delete(self, post_id: int) -> bool:
        orm_post = self.db.query(PostModel).filter_by(id=post_id).first()
        if not orm_post:
            return False
        self.db.delete(orm_post)
        self.db.commit()
        return True
