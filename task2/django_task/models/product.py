from django.db import models
from .category import Category


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Группа', on_delete=models.CASCADE)
    name = models.CharField('Название товара', max_length=128)
    price = models.DecimalField('Стоимость единицы, руб.', max_digits=10, decimal_places=2)

    def __str__(self):
        return ', '.join([self.name, str(self.price)])
