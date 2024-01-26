from django.contrib import admin
from apps.coin.models import Coin
# Register your models here.

@admin.register(Coin)
class CoinFilterAdmin(admin.ModelAdmin):
    list_display = ('user', 'balance')
    list_filter = ('user', 'balance')
    search_fields = ('user', 'balance')