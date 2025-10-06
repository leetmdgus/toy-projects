from domain.posts.entities import Post
from domain.posts.repository import PostRepository
from datetime import datetime

class CreatePostUseCase:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, title: str, content: str, author_id: int):
        post = Post(id=None, title=title, content=content, author_id=author_id, created_at=datetime.utcnow())
        return self.repo.save(post)