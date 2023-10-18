from rest_framework import views, status
from rest_framework.request import Request as RestFrameworkRequest
from rest_framework.response import Response

from host_countries.factories import HostCountriesFactories
from host_countries.serializers import HostCountriesInputSerializer, HostCountriesOutputSerializer


class InsertHostCountriesAPIView(views.APIView):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.db_create_host_countries = HostCountriesFactories.make_host_cities_repository()

    def post(self, request: RestFrameworkRequest):
        serializer = HostCountriesInputSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        self.db_create_host_countries.create(name=serializer.validated_data['name'],
                                             host_cities=serializer.validated_data['host_cities'])

        output = HostCountriesOutputSerializer(data=serializer.validated_data)
        output.is_valid(raise_exception=True)

        return Response(status=status.HTTP_201_CREATED, data=output.data)
