from django.urls import path

from national_teams.views.insert_national_teams_api_view import InsertNationalTeamsAPIView

app_name = 'national-teams'

urlpatterns = [
    path(f'{app_name}/insert', InsertNationalTeamsAPIView.as_view())
]
