from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import Group

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
    )
    readonly_fields = (
        'last_login',
        'date_joined',
    )
    list_display_links = ('username',)
    fieldsets = (
        (None,
         {'fields': (
             'username',
             'password'
         )}),
        ('Персональная информация',
         {'fields': (
             'first_name',
             'last_name',
             'email',
         )}),
        ('Права доступа',
         {'fields': (
             'is_active',
             'is_staff',
             'is_superuser',
         )}),
        ('Важные даты',
         {'fields': (
             'last_login',
             'date_joined'
         )}),
    )


admin.site.unregister(Group)
