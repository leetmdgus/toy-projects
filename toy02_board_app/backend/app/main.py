from fastapi import FastAPI
from sqladmin import Admin, ModelView
from app.core.config import settings
from app.presentation.routers import admin_router, auth_router
from app.core.security import AdminAuthBackend
from app.infrastructure.orm.user_model import UserModel
from app.core.database import Base, engine
from app.presentation.routers import health_router
from app.infrastructure.middleware.user_activity_middleware import log_user_activity
from app.infrastructure.admin.setup_admin import setup_admin
from app.infrastructure.admin.init_admin import init_admin

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="게시판 CRUD API",
    description="FastAPI 기반 게시판 CRUD 서비스",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# 사용자 활동 로깅 미들웨어 등록
app.middleware("http")(log_user_activity)

# 관리자 계정 자동 생성
init_admin()

# 라우터 등록
app.include_router(health_router.router)
app.include_router(prefix="/api", router=admin_router.router)
app.include_router(prefix="/api", router=auth_router.router)

# ✅ SQLAdmin 초기화
setup_admin(app, engine)