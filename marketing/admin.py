from django.contrib import admin
from .models import SubscribedUsers


class SubscribedAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'email',
        'created_date'
    )


admin.site.register(SubscribedUsers, SubscribedAdmin)
