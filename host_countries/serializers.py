from rest_framework import serializers

from stadiums.serializers import StadiumsSerializer


class HostCountriesInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    host_cities = serializers.CharField(max_length=50)
    stadiums = serializers.ListField()


class HostCountriesOutputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    host_cities = serializers.CharField(max_length=50)
    stadiums = StadiumsSerializer(many=True)
