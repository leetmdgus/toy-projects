from app.domain.users.repository import UserRepository
from app.domain.users.entities import User, Role

class DeleteUserUseCase:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, user_id: int, current_user: User):
        if current_user.role != Role.ADMIN:
            raise PermissionError("관리자만 유저를 삭제할 수 있습니다.")
        self.repo.delete(user_id)
        return {"message": f"유저 {user_id} 삭제 완료"}