from abc import ABC
from django.core.exceptions import ObjectDoesNotExist
from utils.entity import Entity


class IRepository(ABC):
    model: Entity = None

    def safe_get(self, *args, **kwargs) -> model:
        try:
            return self.model.objects.get(*args, **kwargs)
        except ObjectDoesNotExist:
            return None
