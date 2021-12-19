from django.db import models
from .category import Category


class CategoryDiscount(models.Model):
    category = models.ForeignKey(Category, verbose_name='Category', on_delete=models.CASCADE)
    discount = models.DecimalField('discount', max_digits=10, decimal_places=2)
    date_begin = models.DateField(
        verbose_name=u'Дата начала',
    )

    date_end = models.DateField(
        verbose_name=u'Дата окончания',
    )
