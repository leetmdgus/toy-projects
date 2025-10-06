from fastapi import APIRouter, HTTPException
from app.presentation.schemas.auth_schema import LoginRequest, TokenResponse
from app.application.use_cases.login_usecase import LoginUseCase
from app.infrastructure.repositories.user_repo_impl import SQLAlchemyUserRepository

router = APIRouter(prefix="/auth", tags=["auth"])

@router.post("/login", response_model=TokenResponse)
def login(req: LoginRequest):
    usecase = LoginUseCase(SQLAlchemyUserRepository())
    try:
        return usecase.execute(req.email, req.password)
    except ValueError as e:
        raise HTTPException(status_code=401, detail=str(e))
