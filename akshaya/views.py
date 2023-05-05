from rest_framework.views import APIView
from .models import Akshaya
from .serializers import AkshayaSerializer, AkshayaSFilterSerializer
from rest_framework.response import Response
from rest_framework import status

from django.views import generic
from django.contrib.gis.geos import fromstr
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.geos import Point


class AllAkshaya(APIView):
    """
    List all akshaya
    """
    def get(self, request):
        obj = Akshaya.objects.all()
        serializer = AkshayaSerializer(obj, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



longitude = 76.6249
latitude = 9.67406413

user_location = Point(longitude, latitude, srid=4326)

class FilterAkshaya(APIView):

    def get(self, request):
        queryset = Akshaya.objects.annotate(distance=Distance('location',
    user_location)
    ).order_by('distance')[0:6]
        serializer = AkshayaSFilterSerializer(queryset, many=True)
        return Response(serializer.data)

class GetAkshaya(APIView):

    def post(self, request):
        aid = request.data.get("akshaya", "")
        obj = Akshaya.objects.get(id=aid)
        serializer = AkshayaSerializer(obj)
        return Response(serializer.data)
        
