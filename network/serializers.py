from rest_framework import serializers

from network.models import ElectronicsRetailNetwork


class ElectroRetailNetworkSerializer(serializers.ModelSerializer):
    """Сериализатор розничной сети электроники."""

    class Meta:
        model = ElectronicsRetailNetwork
        fields = '__all__'
        read_only_fields = ('debt',) # Запрет редактирования задолженности
