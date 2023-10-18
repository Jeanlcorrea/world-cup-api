from rest_framework.exceptions import ValidationError

from host_countries.contracts.repositories import IHostCountriesRepository
from host_countries.models import HostCountriesModels


class DataBaseHostCountriesRepository(IHostCountriesRepository):

    def db_create_host_countries(self, name: str, host_cities: str):
        return HostCountriesModels.objects.create(name=name, host_cities=host_cities)

    def find_host_country_by_name(self, name: str):
        try:
            return HostCountriesModels.objects.get(name=name)
        except ValidationError:
            return 'This Host Country does not exist'
