from django.db import models
from apps.user.models import User
from django.db.models import Sum

class Coin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='coin_info')
    balance = models.IntegerField(default=0)

    def __str__(self):
        return f'{self.user.username} - {self.balance} Gik-Coin'

    def get_balance_display(self):
        return f'У вас: {self.balance} Gik-Coin'