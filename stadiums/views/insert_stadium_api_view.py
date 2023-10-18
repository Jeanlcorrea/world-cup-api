from rest_framework import views, status
from rest_framework.request import Request as RestFrameworkRequest
from rest_framework.response import Response

from host_countries.factories import HostCountriesFactories
from stadiums.factories import StadiumsFactories
from stadiums.models import StadiumsModels
from stadiums.serializers import StadiumsSerializer


class InsertStadiumsAPIView(views.APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.stadiums_repository = StadiumsFactories.make_stadiums_repository()
        self.host_countries_repository = HostCountriesFactories.make_host_cities_repository()

    def post(self, request: RestFrameworkRequest):
        serializer = StadiumsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        host_country = self.host_countries_repository.find_host_country_by_name(
            name=request.data.get('host_country'))

        validated_data = serializer.validated_data
        validated_data['host_country'] = host_country

        self.stadiums_repository.create(**validated_data)

        output = StadiumsSerializer(serializer.validated_data)

        return Response(status=status.HTTP_201_CREATED, data=output.data)
