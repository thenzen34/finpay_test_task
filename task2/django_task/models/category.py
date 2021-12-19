from datetime import datetime

from django.db import models


class Category(models.Model):
    name = models.CharField('Группа товара', max_length=64)

    # ...
    def get_max_discount(self):
        today = datetime.now()
        result = 0
        
        for x in self.categorydiscount_set.filter(date_begin__lte=today, date_end__gt=today).all():
            if x.discount > result:
                result = x.discount

        return result
