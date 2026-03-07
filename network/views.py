from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from network.models import RetailNetwork
from network.serializers import RetailNetworkSerializer


class RetailNetworkViewSet(viewsets.ModelViewSet):
    queryset = RetailNetwork.objects.all()
    serializer_class = RetailNetworkSerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = 'country'
