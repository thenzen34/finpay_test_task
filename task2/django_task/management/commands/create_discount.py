from datetime import timedelta
from random import randint

from django.core.management import BaseCommand

from django_task.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        today = datetime.now()
        # скидки продукт
        cnt = 25
        while cnt > 0:
            obj = ProductDiscount()
            obj.product = Product.objects.order_by('?').first()
            obj.date_begin = today + timedelta(days=randint(-100, 100))
            obj.date_end = obj.date_begin + timedelta(days=randint(5, 30))
            obj.discount = randint(1, 500) / 10
            obj.save()
            cnt -= 1
        print(self.style.NOTICE('ProductDiscount'))

        # скидки категория
        cnt = 2
        while cnt > 0:
            obj = CategoryDiscount()
            obj.category = Category.objects.order_by('?').first()
            obj.date_begin = today + timedelta(days=randint(-100, 100))
            obj.date_end = obj.date_begin + timedelta(days=randint(5, 30))
            obj.discount = randint(1, 500) / 10
            obj.save()
            cnt -= 1

        print(self.style.NOTICE('CategoryDiscount'))

        return self.style.SUCCESS('DONE')
