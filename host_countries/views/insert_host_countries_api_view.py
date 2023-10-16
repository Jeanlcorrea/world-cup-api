from rest_framework import views, status
from rest_framework.request import Request as RestFrameworkRequest
from rest_framework.response import Response

from host_countries.factories import HostCountriesFactories
from host_countries.models import HostCountriesModels
from host_countries.serializers import HostCountriesInputSerializer, HostCountriesOutputSerializer
from stadiums.serializers import StadiumsSerializer


class InsertHostCountriesAPIView(views.APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.validate_stadiums_service = HostCountriesFactories.make_validate_stadiums_service()

    def post(self, request: RestFrameworkRequest):
        serializer = HostCountriesInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        validate_stadiums = self.validate_stadiums_service.execute(stadium_names=serializer.validated_data['stadiums'])

        serialized_stadiums = [StadiumsSerializer(stadium).data for stadium in validate_stadiums]

        HostCountriesModels.objects.create(name=serializer.validated_data['name'],
                                           host_cities=serializer.validated_data['host_cities'],
                                           stadiums=validate_stadiums)

        output_data = {
            'name': serializer.validated_data['name'],
            'host_cities': serializer.validated_data['host_cities'],
            'stadiums': serialized_stadiums
        }

        output = HostCountriesOutputSerializer(data=output_data)
        output.is_valid(raise_exception=True)

        return Response(status=status.HTTP_201_CREATED, data=output.data)
