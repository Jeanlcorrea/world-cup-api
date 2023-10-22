from abc import abstractmethod

from editions.models import WorldCupEditionsModel
from utils.contracts import IRepository


class IEditionsRepository(IRepository):
    model = WorldCupEditionsModel

    @abstractmethod
    def find_edition_by_name(self, name: str):
        raise NotImplementedError()
