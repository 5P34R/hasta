from rest_framework.serializers import ModelSerializer

from .models import Akshaya


class AkshayaSerializer(ModelSerializer):

    class Meta:
        model = Akshaya
        fields = ['id', 'name', 'address', 'city', 'location', 'is_full', 'services']


class AkshayaSFilterSerializer(ModelSerializer):

    class Meta:
        model = Akshaya
        depth = 1
        fields = ['id', 'name', 'address', 'city', 'location', 'is_full', 'services']   