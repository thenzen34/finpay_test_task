from django.core.management import BaseCommand
from django.db.models import QuerySet, F, Prefetch

from django_task.models import *
from django_task.utils import get_sql


class Command(BaseCommand):
    def handle(self, *args, **options):
        today = datetime.now()
        qs: QuerySet = Product.objects\
            .prefetch_related(
                Prefetch(
                    "productdiscount_set",
                    queryset=ProductDiscount.objects.filter(date_begin__lte=today, date_end__gt=today),
                    to_attr="product_discount"
                ),
                Prefetch(
                    "category__categorydiscount_set",
                    queryset=CategoryDiscount.objects.filter(date_begin__lte=today, date_end__gt=today),
                    to_attr="category_discount"
                ),
                # 'productdiscount_set',
                # 'category__categorydiscount_set'
        ).all()
        x: Product
        for x in qs:
            # x.category.categorydiscount_set
            # x.productdiscount_set
            print('{0}\t{1}\t{2}\t{3}'.format(x.category.name, x.name, x.product_discount, x.category.category_discount))

        print('sql=', get_sql(qs))

        return self.style.SUCCESS('DONE')
