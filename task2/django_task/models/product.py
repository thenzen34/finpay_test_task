from datetime import datetime

from django.db import models
from .category import Category


class Product(models.Model):
    category = models.ForeignKey(Category, verbose_name='Группа', on_delete=models.CASCADE)
    name = models.CharField('Название товара', max_length=128)
    price = models.DecimalField('Стоимость единицы, руб.', max_digits=10, decimal_places=2)

    def __str__(self):
        return ', '.join([self.name, str(self.price)])

    def get_max_discount(self):
        today = datetime.now()
        result = self.category.get_max_discount()

        for x in self.productdiscount_set.filter(date_begin__lte=today, date_end__gt=today).all():
            if x.discount > result:
                result = x.discount

        return result
