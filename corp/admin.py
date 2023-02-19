from django.contrib import admin
from django.urls import reverse
from django.utils.safestring import mark_safe

from .models import Company, Product, Contacts


@admin.action(description='Очистить задолженность перед поставщиком')
def clear_debt(modeladmin, request, queryset):
    queryset.update(debt=0)


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = (
        'hierarchy',
        'title',
        'debt',
        'city',
        'provider_link'
    )
    list_display_links = ('title',)
    list_filter = ('hierarchy', 'contacts__city')
    actions = [clear_debt]

    @admin.display(description='Город')
    def city(self, obj):
        return obj.contacts.city

    @admin.display(description='Поставщик')
    def provider_link(self, obj):
        if obj.provider:
            link = reverse(
                'admin:corp_company_change',
                args=(obj.provider.id,)
            )
            return mark_safe(
                u"<a href='{0}'>{1}</a>".format(link, obj.provider)
            )


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'model',
        'release_date'
    )
    list_filter = ('title',)


@admin.register(Contacts)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'email',
        'country',
        'city',
        'street',
        'house_number',
    )
    list_filter = ('email',)
