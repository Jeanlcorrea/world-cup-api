from django.urls import path

from host_countries.views.insert_host_countries_api_view import InsertHostCountriesAPIView

app_name = 'host-countries'

urlpatterns = [
    path(f'{app_name}/insert', InsertHostCountriesAPIView.as_view())
]
