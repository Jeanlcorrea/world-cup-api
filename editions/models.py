import uuid

from django.db import models

from editions.enums import WorldCupWinners
from host_countries.models import HostCountriesModels
from national_teams.models import NationalTeamsModels
from stadiums.models import StadiumsModels


class WorldCupEditionsModel(models.Model):
    id = models.UUIDField(db_column='ID', primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=50, null=True)
    year = models.DateField()
    winner = models.CharField(max_length=10, choices=WorldCupWinners.choices())
    edition_number = models.IntegerField()
    host_countries = models.ForeignKey(HostCountriesModels, on_delete=models.DO_NOTHING, to_field='name', null=True)
    national_teams = models.ManyToManyField(NationalTeamsModels, null=True, blank=True)
    stadiums = models.ForeignKey(StadiumsModels, on_delete=models.DO_NOTHING, to_field='name', null=True)
    mvp = models.CharField(max_length=50)

    def __str__(self):
        return self.name
