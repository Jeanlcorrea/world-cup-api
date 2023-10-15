from django.urls import path

from editions.views.list_world_cup__editions_api_view import ListWorldCupEditionsAPIView

app_name = 'editions'

urlpatterns = [
    path(f'{app_name}/list', ListWorldCupEditionsAPIView.as_view())
]
