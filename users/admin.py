from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import User


@admin.register(User)
class UserAdmin(UserAdmin):
    list_display = (
        'username',
        'first_name',
        'last_name',
        'email',
        'company_link',
    )
    readonly_fields = (
        'last_login',
        'date_joined',
    )
    list_display_links = ('username',)

    add_fieldsets = (
        (None,
         {'fields': (
             'username',
             'password1',
             'password2',
         )}),
        ('Персональная информация',
         {'fields': (
             'first_name',
             'last_name',
             'email',
             'company',
         )}),
        ('Права доступа',
         {'fields': (
             'is_active',
             'is_staff',
         )}),
    )

    @admin.display(description='Компания')
    def company_link(self, obj):
        if obj.company:
            link = reverse(
                'admin:corp_company_change',
                args=(obj.company.id,)
            )
            return mark_safe(
                u"<a href='{0}'>{1}</a>".format(link, obj.company)
            )
