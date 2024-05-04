from abc import ABC, abstractmethod
from src.models.sqlite.entities.people import PeopleTable


class PeopleRepositoryInterface(ABC):

    @abstractmethod
    def insert_person(self, first_name: str, last_name: str, age: int, pet_id: int) -> None:
        pass

    @abstractmethod
    def get_person(self, person_id: int) -> PeopleTable:
        pass
