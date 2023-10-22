from django.db import models

from editions.models import WorldCupEditionsModel


class NationalTeamsModels(models.Model):
    name = models.CharField(max_length=50, unique=True)
    year = models.DateField()
    world_cups = models.IntegerField()
    players = models.JSONField()
    edition = models.ForeignKey(WorldCupEditionsModel, on_delete=models.DO_NOTHING, null=True)

    def __str__(self):
        return self.name
