from rest_framework import serializers
from .models import Coin

class CoinInfoSerializer(serializers.Serializer):
    username = serializers.CharField(source='user.username')
    balance = serializers.IntegerField()
