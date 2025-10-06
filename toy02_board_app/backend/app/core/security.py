from datetime import datetime, timedelta
from jose import jwt, JWTError
from passlib.context import CryptContext
from starlette.requests import Request
from app.core.config import settings
from sqladmin.authentication import AuthenticationBackend
from app.infrastructure.repositories.user_repo_impl import SQLAlchemyUserRepository

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

# =====================================================
# 🔐 기본 JWT & bcrypt 인증 유틸
# =====================================================
def hash_password(password: str):
    """비밀번호 해시 생성"""
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str):
    """입력된 비밀번호와 해시 일치 여부 확인"""
    return pwd_context.verify(plain, hashed)

def create_access_token(data: dict, expires_minutes: int = None):
    """JWT Access Token 생성"""
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes or settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

def decode_access_token(token: str):
    """JWT Access Token 복호화"""
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=[settings.ALGORITHM])
        return payload
    except JWTError:
        return None


# =====================================================
# 🧩 SQLAdmin 전용 로그인 인증 백엔드
# =====================================================
class AdminAuthBackend(AuthenticationBackend):
    """
    SQLAdmin 로그인용 Authentication Backend.
    관리자 계정(role=admin)만 로그인 허용.
    """

    async def login(self, request: Request) -> bool:
        """로그인 시 호출됨"""
        form = await request.form()
        username = form.get("username")
        password = form.get("password")

        repo = SQLAlchemyUserRepository()
        user = repo.get_by_username(username)

        # ❌ 유저 없음 or 비밀번호 불일치
        if not user or not verify_password(password, user.password):
            return False

        # ❌ 관리자(role != admin)
        if user.role.value != "admin":
            return False

        # ✅ JWT 생성 후 세션 저장
        token = create_access_token({"sub": user.email})
        request.session.update({"token": token})
        return True

    async def logout(self, request: Request) -> bool:
        """로그아웃 시 호출됨"""
        request.session.clear()
        return True

    async def authenticate(self, request: Request):
        """세션 유효성 검사"""
        token = request.session.get("token")
        if not token:
            return None
        payload = decode_access_token(token)
        return payload
