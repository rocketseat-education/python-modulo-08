from src.models.sqlite.interfaces.people_repository import (
    PeopleRepositoryInterface
)


class PersonCreatorController:
    def __init__(self, people_repository: PeopleRepositoryInterface) -> None:
        self.__people_repository = people_repository
