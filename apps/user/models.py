from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone

class User(AbstractUser):
    age = models.PositiveIntegerField(
        verbose_name = "Возраст студента",
        blank =True, null = True
    )
    phone = models.CharField(
        verbose_name = 'Телефонный номер',
        max_length = 255
    )
    direction = models.CharField(
        verbose_name = 'Направление ученника',
        max_length = 255
    )
    coin = models.SmallIntegerField(
        verbose_name = 'Gik-Coin(ученика)',
        default = 4,
        blank = True, null = True,
    )


    def __str__(self):
        return self.username
    
    class Meta:
        verbose_name = 'Данные ученика'
        verbose_name_plural = 'Данные ученика'