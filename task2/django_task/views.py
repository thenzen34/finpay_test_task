from datetime import datetime

from django.db.models import Prefetch, QuerySet
from django.shortcuts import render

from django_task.models import CategoryDiscount, ProductDiscount, Product


def main_index(request):
    """

    :type request: HttpRequest
    """
    today = datetime.now()
    qs: QuerySet = Product.objects \
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

    data = {
        'path': request.path,
        'product': qs
    }
    return render(request, 'main_index.html', data)
