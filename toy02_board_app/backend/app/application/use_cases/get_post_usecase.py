from domain.posts.entities import Post
from domain.posts.repository import PostRepository

class GetPostUseCase:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, post_id: int) -> Post | None:
        return self.repo.get_by_id(post_id)
