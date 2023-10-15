from rest_framework import views, status
from rest_framework.request import Request as RestFrameworkRequest
from rest_framework.response import Response

from national_teams.models import NationalTeamsModels
from national_teams.serializers import NationalTeamsSerializer


class InsertNationalTeamsAPIView(views.APIView):

    def post(self, request: RestFrameworkRequest):
        serializer = NationalTeamsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create = NationalTeamsModels.objects.create(**serializer.validated_data)

        output = NationalTeamsSerializer(create)

        return Response(status=status.HTTP_201_CREATED, data=output.data)
