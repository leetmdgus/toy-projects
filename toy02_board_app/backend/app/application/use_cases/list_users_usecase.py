from app.domain.users.repository import UserRepository

class ListUsersUseCase:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self):
        return self.repo.get_all()