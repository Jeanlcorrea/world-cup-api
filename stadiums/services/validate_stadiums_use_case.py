from rest_framework.exceptions import ValidationError

from stadiums.contracts.repositories import IStadiumsRepository


class ValidateStadiumsUseCase:

    def __init__(self, stadiums_repository: IStadiumsRepository):
        self.stadiums_repository = stadiums_repository

    def execute(self, stadium_names: list):
        not_validated = []
        stadium_validated = []

        for name in stadium_names:
            validated = self.stadiums_repository.find_stadium_by_name(name=name)

            if validated:
                stadium_validated.append(validated)
            else:
                not_validated.append(validated)

        if len(stadium_validated) == len(stadium_names):
            return stadium_validated
        else:
            raise ValidationError(f'There are stadiums not found in our system,'
                                  f' please check the list and register new stadiums if necessary')
