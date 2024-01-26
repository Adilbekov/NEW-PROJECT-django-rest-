from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from django.db import connection
from django.db.utils import OperationalError
from django.db.models import Sum

from apps.user.serializer import UserSerializer
from apps.user.models import User
from apps.transactions.models import Transaction


class CoinViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        try:
            user = User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return Response({"error": "Пользователь не найден"}, status=status.HTTP_404_NOT_FOUND)

        try:
            coin_balance = Transaction.objects.filter(from_user=user).aggregate(Sum('coin'))['coin__sum']

            if coin_balance is None:
                coin_balance = 0
            return Response({"user": user.username, "coin_balance": coin_balance})
        except OperationalError:
            return Response({"error": "Ошибка при выполнении запроса к базе данных"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)