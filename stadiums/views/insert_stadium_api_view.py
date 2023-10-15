from rest_framework import views, status
from rest_framework.request import Request as RestFrameworkRequest
from rest_framework.response import Response

from stadiums.models import StadiumsModels
from stadiums.serializers import StadiumsSerializer


class InsertStadiumsAPIView(views.APIView):

    def post(self, request: RestFrameworkRequest):
        serializer = StadiumsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        create = StadiumsModels.objects.create(**serializer.validated_data)

        output = StadiumsSerializer(create)

        return Response(status=status.HTTP_201_CREATED, data=output.data)
