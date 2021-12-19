from django.contrib import admin

from django_task.models import CategoryDiscount


@admin.register(CategoryDiscount)
class CategoryDiscountAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        '__str__',
    )
    search_fields = ['id']
