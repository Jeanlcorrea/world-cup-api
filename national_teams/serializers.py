from rest_framework import serializers


class NationalTeamsSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    year = serializers.DateField()
    world_cups = serializers.IntegerField()
    players = serializers.JSONField()
