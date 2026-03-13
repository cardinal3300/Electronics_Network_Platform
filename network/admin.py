from django.contrib import admin

from network.models import Product, ElectronicsRetailNetwork


@admin.action(description='Очистить задолженность перед поставщиком')
def clear_debt(modeladmin, request, queryset):
    updated = queryset.update(debt=0.00)
    modeladmin.message_user(
        request,
        f'Очищено задолженностей: {updated}'
    )

@admin.register(ElectronicsRetailNetwork)
class ElectroRetailNetworkAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'level',
        'city',
        'provider',
        'debt',
        'created_at',
    )

    list_filter = ('city',)
    filter_horizontal = ('products',)
    search_fields = ('name',)
    actions = [clear_debt]
    # Ссылка на поставщика
    raw_id_fields = ('provider',)

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'model',
        'release_date',
    )
