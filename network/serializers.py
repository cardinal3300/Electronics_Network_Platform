from rest_framework import serializers

from network.models import RetailNetwork


class RetailNetworkSerializer(serializers.ModelSerializer):
    class Meta:
        model = RetailNetwork
        fields = '__all__'
        read_only_fields = ('debt',) # Запрет редактирования задолженности
