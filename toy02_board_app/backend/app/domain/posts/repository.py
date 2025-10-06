from abc import ABC, abstractmethod
from domain.posts.entities import Post

class PostRepository(ABC):
    @abstractmethod
    def save(self, post: Post) -> Post:
        pass

    @abstractmethod
    def get_by_id(self, post_id: int) -> Post | None:
        pass