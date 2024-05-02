from typing import List
from src.models.sqlite.entities.pets import PetsTable
from sqlalchemy.orm.exc import NoResultFound


class PetsRepository:
    def __init__(self, db_connection) -> None:
        self.__db_connection = db_connection

    def list_pets(self) -> List:
        with self.__db_connection as database:
            try:
                pets = database.session.query(PetsTable).all()
                return pets
            except NoResultFound:
                return []
