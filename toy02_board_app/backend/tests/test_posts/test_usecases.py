import pytest
from datetime import datetime
from app.application.use_cases.create_post_usecase import CreatePostUseCase
from app.domain.posts.entities import Post
from app.domain.posts.repository import PostRepository

# ✅ Mock Repository
class FakePostRepository(PostRepository):
    def __init__(self):
        self._storage = []

    def save(self, post: Post) -> Post:
        post.id = len(self._storage) + 1
        self._storage.append(post)
        return post

    def get_by_id(self, post_id: int) -> Post | None:
        for p in self._storage:
            if p.id == post_id:
                return p
        return None

    def get_all(self) -> list[Post]:
        return self._storage.copy()

    def update(self, post: Post) -> Post | None:
        for i, p in enumerate(self._storage):
            if p.id == post.id:
                self._storage[i] = post
                return post
        return None

    def delete(self, post_id: int) -> bool:
        for i, p in enumerate(self._storage):
            if p.id == post_id:
                del self._storage[i]
                return True
        return False

# ✅ 테스트 함수
def test_create_post_usecase():
    repo = FakePostRepository()
    usecase = CreatePostUseCase(repo)

    result = usecase.execute(
        title="테스트 제목",
        content="내용입니다",
        author_id=1
    )

    assert result.id == 1
    assert result.title == "테스트 제목"
    assert result.content == "내용입니다"