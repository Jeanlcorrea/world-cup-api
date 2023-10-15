from rest_framework import status, views
from rest_framework.response import Response
from rest_framework.request import Request as RestFrameworkRequest

from editions.models import WorldCupEditionsModel
from editions.serializers import WorldCupEditionsOutputSerializer
from utils.pagination import Pagination


class ListWorldCupEditionsAPIView(views.APIView):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.pagination = Pagination()

    def get(self, request: RestFrameworkRequest):

        all_editions = WorldCupEditionsModel.objects.all().order_by('year')

        page = self.pagination.paginate_queryset(all_editions, request=request)

        output = WorldCupEditionsOutputSerializer(instance=page, many=True)
        return Response(status=status.HTTP_200_OK, data=output.data)
