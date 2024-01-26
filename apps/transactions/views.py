from rest_framework import viewsets, status
from rest_framework.response import Response

from apps.transactions.models import Transaction
from apps.transactions.serializer import TransactionSerializer
from apps.user.models import User


class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request, *args, **kwargs):
        from_user_id = request.data.get('from_user')
        to_user_id = request.data.get('to_user')
        geeckoin_amount = request.data.get('geeckoin')
        try:
            geeckoin_amount = int(geeckoin_amount)
        except ValueError:
            return Response({"error": "Gik-Coin должен быть целым числом"}, status=status.HTTP_400_BAD_REQUEST)

        # Проверка наличия достаточного количества geeckoin у from_user
        from_user = User.objects.get(id=from_user_id)
        if from_user.coin < geeckoin_amount:
            return Response({"error": "Недостаточно Gik-Coin для перевода"}, status=status.HTTP_400_BAD_REQUEST)

        # Выполнение транзакции
        transaction = Transaction.objects.create(
            from_user=from_user,
            to_user_id=to_user_id,
            geeckoin=geeckoin_amount
        )

        # Вычитаем Gik-Coin у отправителя
        from_user.coin -= geeckoin_amount
        from_user.save()

        # Прибавляем Gik-Coin получателю
        to_user = User.objects.get(id=to_user_id)
        to_user.coin += geeckoin_amount
        to_user.save()

        serializer = TransactionSerializer(transaction)
        return Response(serializer.data, status=status.HTTP_201_CREATED)