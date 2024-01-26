from django.contrib import admin
from django.contrib.auth.models import Group

from apps.user.models import User


admin.site.unregister(Group)
@admin.register(User)
class UserFilterAdmin(admin.ModelAdmin):
    list_display = ('username', 'first_name', 'age', 'phone', 'direction', 'coin')
    search_fields = ('username',)