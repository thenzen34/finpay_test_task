from django.core.management import BaseCommand
from django.db.models import QuerySet, F

from django_task.models import *
from django_task.utils import get_sql


class Command(BaseCommand):
    def handle(self, *args, **options):
        # qs: QuerySet = Product.objects.select_related('category').all()
        # x: Product
        # for x in qs:
        #     print('{0}\t{1}\t{2}'.format(x.category.name, x.name, x.price))

        qs: QuerySet = Product.objects.all()

        qs = qs.annotate(**{
            'pname': F('name'),
            'cname': F('category__name'),
            'pprice': F('price')
        }).values('pname', 'cname', 'pprice')

        x: dict
        for x in qs:
            print('{0}\t{1}\t{2}'.format(x['cname'], x['pname'], x['pprice']))

        print('sql=', get_sql(qs))

        return self.style.SUCCESS('DONE')
