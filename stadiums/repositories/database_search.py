from django.core.exceptions import ObjectDoesNotExist

from stadiums.contracts.repositories import IStadiumsRepository
from stadiums.models import StadiumsModels


class DataBaseSearchAtStadiums(IStadiumsRepository):

    def find_stadium_by_name(self, name) -> None:
        try:
            return StadiumsModels.objects.get(name=name)
        except ObjectDoesNotExist:
            return None
