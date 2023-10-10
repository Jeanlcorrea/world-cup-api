from django.db import models


class StadiumsModels(models.Model):
    name = models.CharField(max_length=50, unique=True)
    city = models.CharField(max_length=50)
    owner = models.CharField(max_length=50)
    capacity = models.IntegerField()

    def __str__(self):
        return self.name
