from rest_framework import serializers

from host_countries.serializers import HostCountriesOutputSerializer


class EditionNationalTeamsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    world_cups = serializers.IntegerField()


class WorldCupEditionsOutputSerializer(serializers.Serializer):
    id = serializers.UUIDField(read_only=True)
    name = serializers.CharField(max_length=50)
    year = serializers.DateField()
    winner = serializers.CharField(max_length=50)
    edition_number = serializers.IntegerField()
    host_countries = HostCountriesOutputSerializer()
    national_teams = EditionNationalTeamsSerializer(many=True, source='nationalteamsmodels_set')
    mvp = serializers.CharField(max_length=100)
