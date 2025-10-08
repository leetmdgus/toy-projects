from app.core.database import SessionLocal
from app.infrastructure.orm.user_model import UserModel, UserRole
from app.core.config import settings
from app.core.security import hash_password

def init_admin():
    """최초 서버 실행 시 관리자 계정을 생성합니다."""
    db = SessionLocal()

    # 1️⃣ 관리자 이메일 확인
    admin_username = settings.ADMIN_USERNAME or "admin"
    admin_email = settings.ADMIN_EMAIL
    admin_password = settings.ADMIN_DEFAULT_PASSWORD

    if not admin_email or not admin_password:
        print("⚠️ 관리자 정보가 .env에 없습니다. 생성을 건너뜁니다.")
        return

    # 2️⃣ 이미 관리자 존재하는지 확인
    existing_admin = db.query(UserModel).filter_by(email=admin_email).first()
    if existing_admin:
        print(f"✅ 이미 관리자 계정이 존재합니다: {existing_admin.email}")
        db.close()
        return

    # 3️⃣ 새 관리자 생성
    admin = UserModel(
        username=admin_username,
        email=admin_email,
        password=hash_password(admin_password),
        role=UserRole.admin
    )
    db.add(admin)
    db.commit()
    db.close()

    print(f"🎉 관리자 계정 생성 완료: {admin_email}")
