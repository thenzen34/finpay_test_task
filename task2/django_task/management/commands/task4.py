from django.core.management import BaseCommand
from django.db.models import QuerySet, F

from django_task.models import *
from django_task.utils import get_sql


class Command(BaseCommand):
    def handle(self, *args, **options):
        qs: QuerySet = Product.objects.prefetch_related('productdiscount_set', 'category__categorydiscount_set').all()
        x: Product
        for x in qs:
            # x.category.categorydiscount_set
            # x.productdiscount_set
            print('{0}\t{1}\t{2}'.format(x.category.name, x.name, x.price))

        print('sql=', get_sql(qs))

        return self.style.SUCCESS('DONE')
