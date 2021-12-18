from django.db import models


class Category(models.Model):
    name = models.CharField('Группа товара', max_length=64)
    # ...
