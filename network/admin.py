from django.contrib import admin

from network.models import RetailNetwork


@admin.register(RetailNetwork)
class RetailNetworkAdmin(admin.ModelAdmin):
    list_display = ('name', 'city', 'provider', 'debt',)
    list_filter = ('city',)
    actions = ['clear_debt']

    # Ссылка на поставщика
    raw_id_fields = ('provider',)

    @admin.action(description='Очистить задолженность перед поставщиком')
    def clear_debt(self, queryset):
        queryset.update(debt=0.00)
