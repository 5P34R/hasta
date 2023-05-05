from django.urls import path
from .views import AllAkshaya, FilterAkshaya, GetAkshaya


urlpatterns = [
    path("", AllAkshaya.as_view()),
    path("filter/", FilterAkshaya.as_view()),
    path("akshaya/", GetAkshaya.as_view()),
]