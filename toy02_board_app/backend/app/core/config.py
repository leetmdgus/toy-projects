from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    APP_NAME: str = "CleanBoard"
    DEBUG: bool = True

    # 🔐 Security
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60

    # 🗄️ DB
    DATABASE_URL: str

    # 👑 Admin
    ADMIN_USERNAME: str | None = None
    ADMIN_EMAIL: str | None = None
    ADMIN_DEFAULT_PASSWORD: str | None = None

    # 📦 Storage
    UPLOAD_DIR: str = "uploads"

    class Config:
        env_file = ".env"

settings = Settings()