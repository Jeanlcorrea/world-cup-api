from rest_framework.exceptions import ValidationError

from editions.contracts.repositories import IEditionsRepository
from editions.models import WorldCupEditionsModel


class DataBaseEditionsRepository(IEditionsRepository):

    def find_edition_by_name(self, name: str):
        try:
            return WorldCupEditionsModel.objects.get(name=name)
        except ValidationError:
            return 'This Edition does not exist in the our database'
