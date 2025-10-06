from domain.posts.entities import Post
from domain.posts.repository import PostRepository
from datetime import datetime

class UpdatePostUseCase:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, post_id: int, title: str | None, content: str | None) -> Post | None:
        existing = self.repo.get_by_id(post_id)
        if not existing:
            return None
        
        updated_post = Post(
            id=post_id,
            title=title if title else existing.title,
            content=content if content else existing.content,
            author_id=existing.author_id,
            created_at=existing.created_at
        )
        return self.repo.update(updated_post)
