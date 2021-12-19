from django.contrib import admin

from django_task.models import ProductDiscount


@admin.register(ProductDiscount)
class ProductDiscountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        '__str__',
    )
    search_fields = ['id']
