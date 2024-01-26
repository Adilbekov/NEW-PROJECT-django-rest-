from django.contrib import admin

from apps.transactions.models import Transaction


@admin.register(Transaction)
class TransactionAdminFilter(admin.ModelAdmin):
    list_display = ('from_user', 'to_user', 'geeckoin', 'created_at')
    list_filter = ('from_user', 'to_user', 'geeckoin', 'created_at') 
    search_fields = ('username',)