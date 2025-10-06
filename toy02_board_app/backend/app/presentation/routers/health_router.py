from fastapi import APIRouter
from app.core.config import settings
from datetime import datetime

router = APIRouter(prefix="/health", tags=["health"])

@router.get("/")
def health_check():
    return {
        "status": "ok",
        "service": settings.APP_NAME,
        "timestamp": datetime.utcnow().isoformat() + "Z",
    }
