from stadiums.contracts.repositories import IStadiumsRepository
from stadiums.repositories.database_search import DataBaseSearchAtStadiums


class StadiumsFactories:

    @staticmethod
    def make_stadiums_repository() -> IStadiumsRepository:
        return DataBaseSearchAtStadiums()
