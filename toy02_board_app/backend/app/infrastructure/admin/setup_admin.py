from sqladmin import Admin
from app.core.security import AdminAuthBackend
from app.infrastructure.admin.views.user_admin_view import UserAdminView
from app.core.config import settings

def setup_admin(app, engine):
    """SQLAdmin 초기화 + 뷰 등록"""
    auth_backend = AdminAuthBackend(secret_key=settings.SECRET_KEY)
    admin = Admin(app, engine, authentication_backend=auth_backend)
    
    admin.add_view(UserAdminView)
    return admin