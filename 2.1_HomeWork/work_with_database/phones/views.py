from django.shortcuts import get_object_or_404, render
from .models import Phone


def show_catalog(request):
    phones = Phone.objects.all()
    sort_type = request.GET.get('sort')
    if sort_type:
        # коряво но зато нет ифов) надо думаю регуляркой как то обойтись )
        phones = phones.order_by(sort_type.replace('min_', '').replace('max_', '-'))
    return render(
        request,
        'catalog.html',
        {'phones': phones}
    )


def show_product(request, slug):
    # ищем в модели объект по полю slug если нет то 404
    phone = get_object_or_404(Phone, slug=slug)
    return render(
        request,
        'product.html',
        {'phone': phone}
    )
