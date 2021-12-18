from random import randint

from django.core.management import BaseCommand

from django_task.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        # категории
        cnt = 5
        while cnt > 0:
            obj = Category()
            obj.name = 'категория {0}'.format(cnt)
            obj.save()
            cnt -= 1
        print(self.style.NOTICE('Category'))

        # Продукты
        cnt = 50
        while cnt > 0:
            obj = Product()
            obj.category = Category.objects.order_by('?').first()
            obj.name = 'Продукт {0}'.format(cnt)
            obj.price = randint(1, 3000) / 10
            obj.save()
            cnt -= 1

        print(self.style.NOTICE('Product'))

        return self.style.SUCCESS('DONE')
