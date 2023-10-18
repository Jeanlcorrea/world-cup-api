from abc import abstractmethod

from host_countries.models import HostCountriesModels
from utils.contracts import IRepository


class IHostCountriesRepository(IRepository):
    model = HostCountriesModels

    @abstractmethod
    def db_create_host_countries(self, name: str, host_cities: str):
        raise NotImplementedError()

    @abstractmethod
    def find_host_country_by_name(self, name: str):
        raise NotImplementedError()
