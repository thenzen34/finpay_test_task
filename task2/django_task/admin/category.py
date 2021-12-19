from django.contrib import admin

from django_task.models import Category, CategoryDiscount


class CategoryDiscountAdminInline(admin.TabularInline):
    model = CategoryDiscount
    extra = 0  # Количество полей


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        '__str__',
    )
    search_fields = ['id']

    inlines = [CategoryDiscountAdminInline]
