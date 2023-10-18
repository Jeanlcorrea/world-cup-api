from django.db import models

from host_countries.models import HostCountriesModels


class StadiumsModels(models.Model):
    name = models.CharField(max_length=50, unique=True)
    city = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    capacity = models.IntegerField()
    host_country = models.ForeignKey(HostCountriesModels, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name
