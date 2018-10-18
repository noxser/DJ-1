from django.shortcuts import render
from .models import Phones, Apple, Xiaomi, Samsung


def show_catalog(request):
    specification = set()
    specification_rus = {}
    phones_models = [Apple, Xiaomi, Samsung]
    features = set()
    features_rus = {}

    # возможно есть и более красивый способ )

    for phone in Phones.objects.all():
        for i in phone._meta.get_fields():
            if i.name not in ['samsung', 'xiaomi', 'id', 'apple']:
                specification.add(i.name)
                specification_rus[i.name] = i.verbose_name

    for model in phones_models:
        for f in model._meta.get_fields():
            if f.name not in ['id', 'phone_model']:
                features.add(f.name)
                features_rus[f.name] = f.verbose_name

    specification.update(features)
    specification_rus.update(features_rus)

    phones = Phones.objects.all()
    phones_data = {}
    for params in specification:
        ll = []
        for phone in phones:
            if hasattr(phone, params):
                ll.append(getattr(phone, params))
            else:
                for model in phones_models:
                    if model.objects.filter(phone_model_id=phone.id):
                        if hasattr(model.objects.get(phone_model_id=phone.id), params):

                            ll.append(getattr(model.objects.get(phone_model_id=phone.id), params))
                        else:
                            ll.append('-')
        phones_data[params] = ll

    return render(
        request,
        'catalog.html',
        {'phones': phones_data, 'names_spec': specification_rus}
    )
