from editions.contracts.repositories import IEditionsRepository
from editions.repositories.database import DataBaseEditionsRepository


class EditionsFactories:

    @staticmethod
    def make_editions_repository() -> IEditionsRepository:
        return DataBaseEditionsRepository()
