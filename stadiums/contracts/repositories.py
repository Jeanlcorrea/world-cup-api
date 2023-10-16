from abc import abstractmethod

from stadiums.models import StadiumsModels
from utils.contracts import IRepository


class IStadiumsRepository(IRepository):

    @abstractmethod
    def find_stadium_by_name(self, name) -> StadiumsModels:
        raise NotImplementedError()

    def safe_get(self, *args, **kwargs) -> StadiumsModels:
        raise NotImplementedError()
