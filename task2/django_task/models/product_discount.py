from django.db import models
from .product import Product


class ProductDiscount(models.Model):
    product = models.ForeignKey(Product, verbose_name='Product', on_delete=models.CASCADE)
    discount = models.DecimalField('discount', max_digits=10, decimal_places=2)
    date_begin = models.DateField(
        verbose_name=u'Дата начала',
    )

    date_end = models.DateField(
        verbose_name=u'Дата окончания',
    )
