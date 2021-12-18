from django.contrib import admin

from django_task.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        '__str__',
    )
    search_fields = ['id']

