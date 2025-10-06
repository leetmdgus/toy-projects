import pytest
from datetime import datetime
from app.application.use_cases.get_post_usecase import GetPostUseCase
from app.application.use_cases.list_posts_usecase import ListPostsUseCase
from app.application.use_cases.update_post_usecase import UpdatePostUseCase
from app.application.use_cases.delete_post_usecase import DeletePostUseCase
from app.domain.posts.entities import Post
from app.domain.posts.repository import PostRepository

# ✅ Mock Repository
class FakePostRepository(PostRepository):
    def __init__(self):
        self._storage = []
        self._next_id = 1

    def save(self, post: Post) -> Post:
        post.id = self._next_id
        self._next_id += 1
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


# ✅ Test GetPostUseCase
def test_get_post_usecase():
    repo = FakePostRepository()
    # Create a post first
    post = Post(id=None, title="Test Title", content="Test Content", author_id=1, created_at=datetime.utcnow())
    saved = repo.save(post)
    
    # Test get
    usecase = GetPostUseCase(repo)
    result = usecase.execute(saved.id)
    
    assert result is not None
    assert result.id == saved.id
    assert result.title == "Test Title"


def test_get_post_usecase_not_found():
    repo = FakePostRepository()
    usecase = GetPostUseCase(repo)
    result = usecase.execute(999)
    
    assert result is None


# ✅ Test ListPostsUseCase
def test_list_posts_usecase():
    repo = FakePostRepository()
    # Create multiple posts
    post1 = Post(id=None, title="Title 1", content="Content 1", author_id=1, created_at=datetime.utcnow())
    post2 = Post(id=None, title="Title 2", content="Content 2", author_id=1, created_at=datetime.utcnow())
    repo.save(post1)
    repo.save(post2)
    
    # Test list
    usecase = ListPostsUseCase(repo)
    results = usecase.execute()
    
    assert len(results) == 2
    assert results[0].title == "Title 1"
    assert results[1].title == "Title 2"


def test_list_posts_usecase_empty():
    repo = FakePostRepository()
    usecase = ListPostsUseCase(repo)
    results = usecase.execute()
    
    assert len(results) == 0


# ✅ Test UpdatePostUseCase
def test_update_post_usecase():
    repo = FakePostRepository()
    # Create a post first
    post = Post(id=None, title="Original Title", content="Original Content", author_id=1, created_at=datetime.utcnow())
    saved = repo.save(post)
    
    # Test update
    usecase = UpdatePostUseCase(repo)
    result = usecase.execute(saved.id, "Updated Title", "Updated Content")
    
    assert result is not None
    assert result.id == saved.id
    assert result.title == "Updated Title"
    assert result.content == "Updated Content"


def test_update_post_usecase_partial():
    repo = FakePostRepository()
    # Create a post first
    post = Post(id=None, title="Original Title", content="Original Content", author_id=1, created_at=datetime.utcnow())
    saved = repo.save(post)
    
    # Test partial update (only title)
    usecase = UpdatePostUseCase(repo)
    result = usecase.execute(saved.id, "New Title", None)
    
    assert result is not None
    assert result.title == "New Title"
    assert result.content == "Original Content"


def test_update_post_usecase_not_found():
    repo = FakePostRepository()
    usecase = UpdatePostUseCase(repo)
    result = usecase.execute(999, "Title", "Content")
    
    assert result is None


# ✅ Test DeletePostUseCase
def test_delete_post_usecase():
    repo = FakePostRepository()
    # Create a post first
    post = Post(id=None, title="Test Title", content="Test Content", author_id=1, created_at=datetime.utcnow())
    saved = repo.save(post)
    
    # Test delete
    usecase = DeletePostUseCase(repo)
    result = usecase.execute(saved.id)
    
    assert result is True
    assert repo.get_by_id(saved.id) is None


def test_delete_post_usecase_not_found():
    repo = FakePostRepository()
    usecase = DeletePostUseCase(repo)
    result = usecase.execute(999)
    
    assert result is False
