from django.contrib import admin

from django_task.models import Product, ProductDiscount


class ProductDiscountAdminInline(admin.TabularInline):
    model = ProductDiscount
    extra = 0  # Количество полей


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        '__str__',
        'price',
    )
    search_fields = ['id']

    inlines = [ProductDiscountAdminInline]
