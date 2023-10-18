from rest_framework import serializers


class StadiumsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    city = serializers.CharField(max_length=50)
    owner = serializers.CharField(max_length=50)
    capacity = serializers.IntegerField()
    host_country = serializers.CharField(max_length=50)
