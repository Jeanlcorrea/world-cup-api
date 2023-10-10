from django.db import models


class NationalTeamsModels(models.Model):
    name = models.CharField(max_length=50, unique=True)
    year = models.DateField(format('%d/%m/%Y'))
    world_cups = models.IntegerField()
    players = models.JSONField()

    def __str__(self):
        return self.name
