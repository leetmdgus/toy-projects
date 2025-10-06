from app.domain.posts.repository import PostRepository
from app.domain.users.entities import User, Role

class DeletePostUseCase:
    def __init__(self, post_repo: PostRepository):
        self.post_repo = post_repo

    def execute(self, post_id: int, current_user: User):
        # ✅ 관리자만 삭제 가능
        if current_user.role != Role.ADMIN:
            raise PermissionError("관리자만 게시글을 삭제할 수 있습니다.")
        self.post_repo.delete(post_id)
        return {"message": f"게시글 {post_id} 삭제 완료"}
