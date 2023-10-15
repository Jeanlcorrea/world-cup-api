from django.urls import path

from stadiums.views.insert_stadium_api_view import InsertStadiumsAPIView

app_name = 'stadiums'

urlpatterns = [
    path(f'{app_name}/insert', InsertStadiumsAPIView.as_view())
]
