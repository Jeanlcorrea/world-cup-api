from abc import abstractmethod

from stadiums.models import StadiumsModels
from utils.contracts import IRepository


class IStadiumsRepository(IRepository):
    model = StadiumsModels

    @abstractmethod
    def find_stadium_by_name(self, name) -> StadiumsModels:
        raise NotImplementedError()
