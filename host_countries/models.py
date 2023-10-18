from django.db import models


class HostCountriesModels(models.Model):
    name = models.CharField(max_length=50, unique=True)
    host_cities = models.CharField(max_length=50)

    def __str__(self):
        return self.name
