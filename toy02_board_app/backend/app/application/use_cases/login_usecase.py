from app.core.security import verify_password, create_access_token
from datetime import datetime
from app.domain.users.repository import UserRepository

class LoginUseCase:
    def __init__(self, repo: UserRepository):
        self.repo = repo

    def execute(self, email: str, password: str):
        user = self.repo.get_by_email(email)
        if not user or not verify_password(password, user.password):
            raise ValueError("이메일 또는 비밀번호가 올바르지 않습니다.")

        access_token = create_access_token({
            "sub": str(user.id),
            "email": user.email,
            "role": user.role.value,
            "iat": datetime.utcnow().timestamp()
        })
        return {"access_token": access_token, "token_type": "bearer"}
