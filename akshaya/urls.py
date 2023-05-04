from django.urls import path
from .views import AllAkshaya, FilterAkshaya


urlpatterns = [
    path("", AllAkshaya.as_view()),
    path("filter/", FilterAkshaya.as_view())
]