from domain.posts.repository import PostRepository

class DeletePostUseCase:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self, post_id: int) -> bool:
        return self.repo.delete(post_id)
