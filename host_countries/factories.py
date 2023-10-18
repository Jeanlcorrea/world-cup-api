from host_countries.contracts.repositories import IHostCountriesRepository
from host_countries.repositories.database import DataBaseHostCountriesRepository


class HostCountriesFactories:

    @staticmethod
    def make_host_cities_repository() -> IHostCountriesRepository:
        return DataBaseHostCountriesRepository()
