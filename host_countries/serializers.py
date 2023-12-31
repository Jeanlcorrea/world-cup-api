from rest_framework import serializers


class HostCountriesInputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    host_cities = serializers.CharField(max_length=50)


class HostCountriesOutputSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    host_cities = serializers.CharField(max_length=50)

