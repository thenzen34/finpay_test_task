from django.contrib import admin

from django_task.models import Product


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        '__str__',
        'price',
    )
    search_fields = ['id']
