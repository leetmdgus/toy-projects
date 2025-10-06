from app.domain.posts.entities import Post
from app.infrastructure.repositories.post_repo_impl import SQLAlchemyPostRepository
from app.infrastructure.storage.local_storage import LocalStorage
from datetime import datetime
from typing import List

class CreatePostWithFileUseCase:
    def __init__(self, post_repo: SQLAlchemyPostRepository, storage: LocalStorage):
        self.post_repo = post_repo
        self.storage = storage

    def execute(self, title: str, content: str, author_id: int, files: List):
        image_paths = [self.storage.save_file(f) for f in files]
        post = Post(
            id=None,
            title=title,
            content=content,
            author_id=author_id,
            image_paths=image_paths,
            created_at=datetime.utcnow()
        )
        return self.post_repo.save(post)