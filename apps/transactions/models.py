from django.db import models

from apps.user.models import User


class Transaction(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_get')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user_post')
    geeckoin = models.SmallIntegerField()
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    
    def __str__(self):
        return f'{self.from_user} - {self.to_user} - {self.geeckoin}'
    
    class Meta:
            verbose_name = 'Транзакция'
            verbose_name_plural = 'Транзакции'