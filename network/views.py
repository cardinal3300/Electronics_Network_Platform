from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets

from network.models import ElectronicsRetailNetwork
from network.permissions import IsActiveEmployee
from network.serializers import ElectroRetailNetworkSerializer


class ElectroRetailNetworkViewSet(viewsets.ModelViewSet):
    """Контроллер отображения эндпоинтов розничной сети электроники."""

    queryset = ElectronicsRetailNetwork.objects.all()
    serializer_class = ElectroRetailNetworkSerializer
    permission_classes = [IsActiveEmployee]

    filter_backends = [DjangoFilterBackend]
    filter_fields = ['country']
