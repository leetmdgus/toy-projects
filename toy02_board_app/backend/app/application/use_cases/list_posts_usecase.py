from app.domain.posts.entities import Post
from app.domain.posts.repository import PostRepository

class ListPostsUseCase:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self) -> list[Post]:
        return self.repo.get_all()
