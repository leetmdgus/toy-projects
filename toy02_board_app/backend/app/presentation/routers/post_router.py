from fastapi import APIRouter, UploadFile, Form
from typing import List
from app.application.use_cases.create_post_with_file_usecase import CreatePostWithFileUseCase
from app.infrastructure.repositories.post_repo_impl import SQLAlchemyPostRepository
from app.infrastructure.storage.local_storage import LocalStorage

router = APIRouter(prefix="/posts", tags=["posts"])

@router.post("/upload")
async def create_post_with_files(
    title: str = Form(...),
    content: str = Form(...),
    author_id: int = Form(...),
    files: List[UploadFile] = []
):
    usecase = CreatePostWithFileUseCase(SQLAlchemyPostRepository(), LocalStorage())
    post = usecase.execute(title, content, author_id, files)
    return {"id": post.id, "image_paths": post.image_paths}