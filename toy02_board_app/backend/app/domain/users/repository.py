from abc import ABC, abstractmethod
from app.domain.users.entities import User

class UserRepository(ABC):
    @abstractmethod
    def get_all(self) -> list[User]:
        pass

    @abstractmethod
    def delete(self, user_id: int):
        pass
