from fastapi import APIRouter, Depends
from application.use_cases.create_post_usecase import CreatePostUseCase
from infrastructure.repositories.post_repo_impl import SQLAlchemyPostRepository
from presentation.schemas.post_schema import PostCreate, PostResponse

router = APIRouter(prefix="/posts")

@router.post("/", response_model=PostResponse)
def create_post(req: PostCreate):
    repo = SQLAlchemyPostRepository()
    usecase = CreatePostUseCase(repo)
    result = usecase.execute(req.title, req.content, req.author_id)
    return result