from rest_framework import views, status
from rest_framework.request import Request as RestFrameworkRequest
from rest_framework.response import Response

from editions.factories import EditionsFactories
from national_teams.models import NationalTeamsModels
from national_teams.serializers import NationalTeamsSerializer


class InsertNationalTeamsAPIView(views.APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.edition_repository = EditionsFactories.make_editions_repository()

    def post(self, request: RestFrameworkRequest):
        serializer = NationalTeamsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        edition = self.edition_repository.find_edition_by_name(name=request.data.get('edition'))

        validated_data = serializer.validated_data
        validated_data['edition'] = edition

        create = NationalTeamsModels.objects.create(**validated_data)

        output = NationalTeamsSerializer(create)

        return Response(status=status.HTTP_201_CREATED, data=output.data)
