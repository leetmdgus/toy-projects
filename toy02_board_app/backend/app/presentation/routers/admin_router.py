from fastapi import APIRouter, Depends, HTTPException
from app.presentation.dependencies import admin_required
from app.application.use_cases.list_posts_usecase import ListPostsUseCase
from app.application.use_cases.list_users_usecase import ListUsersUseCase
from app.application.use_cases.delete_user_usecase import DeleteUserUseCase
from app.infrastructure.repositories.post_repo_impl import SQLAlchemyPostRepository
from app.infrastructure.repositories.user_repo_impl import SQLAlchemyUserRepository

router = APIRouter(prefix="/admin", tags=["admin"])
# ✅ 관리자 대시보드
@router.get("/dashboard")
def admin_dashboard(admin=Depends(admin_required)):
    return {"message": f"환영합니다, {admin.role.value} 님! 🎉"}

# ✅ 게시글 전체 조회
@router.get("/posts")
def get_all_posts(admin=Depends(admin_required)):
    repo = SQLAlchemyPostRepository()
    usecase = ListPostsUseCase(repo)
    return usecase.execute()

# ✅ 유저 전체 조회
@router.get("/users")
def get_all_users(admin=Depends(admin_required)):
    repo = SQLAlchemyUserRepository()
    usecase = ListUsersUseCase(repo)
    return usecase.execute()

# ✅ 유저 강제 삭제
@router.delete("/users/{user_id}")
def delete_user(user_id: int, admin=Depends(admin_required)):
    repo = SQLAlchemyUserRepository()
    usecase = DeleteUserUseCase(repo)
    try:
        return usecase.execute(user_id, admin)
    except ValueError as e:
        raise HTTPException(status_code=404, detail=str(e))