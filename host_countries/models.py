
from django.db import models

from stadiums.models import StadiumsModels


class HostCountriesModels(models.Model):
    name = models.CharField(max_length=50, unique=True)
    host_cities = models.CharField(max_length=50)
    stadiums = models.ForeignKey(StadiumsModels, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name
