from app.domain.posts.repository import PostRepository

class ListPostsUseCase:
    def __init__(self, repo: PostRepository):
        self.repo = repo

    def execute(self):
        return self.repo.get_all()