from fastapi import FastAPI
from sqladmin import Admin, ModelView
from app.core.config import settings
from app.presentation.routers import admin_router, auth_router
from app.core.security import AdminAuthBackend
from app.infrastructure.orm.user_model import UserModel
from app.infrastructure.init_admin import init_admin
from app.core.database import Base, engine
from app.presentation.routers import health_router

# DB 테이블 생성
Base.metadata.create_all(bind=engine)

# FastAPI 앱 생성
app = FastAPI(title="CleanBoard")



# 관리자 계정 자동 생성
init_admin()

# ✅ 관리자 API (REST)
app.include_router(admin_router.router)

# ✅ SQLAdmin + 인증 백엔드 연결
auth_backend = AdminAuthBackend(secret_key=settings.SECRET_KEY)
admin = Admin(app, engine, authentication_backend=auth_backend)

class UserAdmin(ModelView, model=UserModel):
    column_list = [UserModel.id, UserModel.username, UserModel.email, UserModel.role]
    column_searchable_list = [UserModel.username, UserModel.email]
    column_sortable_list = [UserModel.id]

admin.add_view(UserAdmin)


# ✅ 헬스체크
app.include_router(health_router.router)

# 라우터 등록
app.include_router(prefix="/api", router=auth_router.router)
