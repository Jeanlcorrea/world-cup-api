from host_countries.services.validate_stadiums_service import ValidateStadiumsService
from stadiums.factories import StadiumsFactories


class HostCountriesFactories:

    @staticmethod
    def make_validate_stadiums_service() -> ValidateStadiumsService:
        return ValidateStadiumsService(stadiums_repository=StadiumsFactories.make_stadiums_repository())
