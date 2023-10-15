from rest_framework import serializers

from host_countries.serializers import HostCountriesOutputSerializer
from national_teams.serializers import NationalTeamsSerializer
from stadiums.serializers import StadiumsSerializer


class WorldCupEditionsOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=50)
    year = serializers.DateField()
    winner = serializers.CharField(max_length=50)
    edition_number = serializers.IntegerField()
    host_countries = HostCountriesOutputSerializer()
    national_teams = NationalTeamsSerializer(many=True)
    stadiums = StadiumsSerializer()
    mvp = serializers.CharField(max_length=100)
