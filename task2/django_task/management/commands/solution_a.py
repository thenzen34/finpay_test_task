from django.core.management import BaseCommand
from django.db.models import QuerySet, Count

from django_task.models import *
from django_task.utils import print_result, get_sql


class Command(BaseCommand):
    def handle(self, *args, **options):
        qs: QuerySet = Product.objects.filter(price__gte=100)

        total = {
            'product_cnt': Count('id'),
        }

        qs = qs.values('category').annotate(**total)

        print('sql=', get_sql(qs))
        print_result(qs)

        return self.style.SUCCESS('DONE')
