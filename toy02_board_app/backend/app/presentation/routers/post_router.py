from fastapi import APIRouter, HTTPException, status
from application.use_cases.create_post_usecase import CreatePostUseCase
from application.use_cases.get_post_usecase import GetPostUseCase
from application.use_cases.list_posts_usecase import ListPostsUseCase
from application.use_cases.update_post_usecase import UpdatePostUseCase
from application.use_cases.delete_post_usecase import DeletePostUseCase
from infrastructure.repositories.post_repo_impl import SQLAlchemyPostRepository
from presentation.schemas.post_schema import PostCreate, PostUpdate, PostResponse

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/", response_model=PostResponse, status_code=status.HTTP_201_CREATED)
def create_post(req: PostCreate):
    """게시물 작성 API"""
    repo = SQLAlchemyPostRepository()
    usecase = CreatePostUseCase(repo)
    result = usecase.execute(req.title, req.content, req.author_id)
    return result

@router.get("/", response_model=list[PostResponse])
def list_posts():
    """게시물 목록 조회 API"""
    repo = SQLAlchemyPostRepository()
    usecase = ListPostsUseCase(repo)
    results = usecase.execute()
    return results

@router.get("/{post_id}", response_model=PostResponse)
def get_post(post_id: int):
    """게시물 단건 조회 API"""
    repo = SQLAlchemyPostRepository()
    usecase = GetPostUseCase(repo)
    result = usecase.execute(post_id)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return result

@router.put("/{post_id}", response_model=PostResponse)
def update_post(post_id: int, req: PostUpdate):
    """게시물 수정 API"""
    repo = SQLAlchemyPostRepository()
    usecase = UpdatePostUseCase(repo)
    result = usecase.execute(post_id, req.title, req.content)
    if not result:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return result

@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(post_id: int):
    """게시물 삭제 API"""
    repo = SQLAlchemyPostRepository()
    usecase = DeletePostUseCase(repo)
    success = usecase.execute(post_id)
    if not success:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
