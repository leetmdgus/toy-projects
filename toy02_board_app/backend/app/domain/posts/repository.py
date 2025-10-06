from abc import ABC, abstractmethod
from app.domain.posts.entities import Post

class PostRepository(ABC):
    @abstractmethod
    def save(self, post: Post) -> Post:
        pass

    @abstractmethod
    def get_by_id(self, post_id: int) -> Post | None:
        pass

    @abstractmethod
    def get_all(self) -> list[Post]:
        pass

    @abstractmethod
    def update(self, post: Post) -> Post | None:
        pass

    @abstractmethod
    def delete(self, post_id: int) -> bool:
        pass
