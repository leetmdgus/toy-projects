from fastapi import FastAPI
from presentation.routers import post_router
from core.database import Base, engine
from infrastructure.orm import post_model, user_model  # Import models to register them

# Create database tables
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="게시판 CRUD API",
    description="FastAPI 기반 게시판 CRUD 서비스",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Include routers
app.include_router(post_router.router)

@app.get("/")
def root():
    return {"message": "게시판 CRUD API 서버가 실행 중입니다."}
