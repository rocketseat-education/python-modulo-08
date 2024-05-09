from abc import ABC, abstractmethod

class PetDeleterControllerInterface(ABC):

    @abstractmethod
    def delete(self, name: str) -> None:
        pass
