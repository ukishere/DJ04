from django.shortcuts import render
from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'

    phone = Phone.objects.all()

    print(list(phone))

    if request.GET.get('sort') == 'name':
        phone = phone.order_by('name')
    elif request.GET.get('sort') == 'lower':
        phone = phone.order_by('-price')
    elif request.GET.get('sort') == 'higher':
        phone = phone.order_by('price')

    print(list(phone))

    context = {'Phones': phone}

    return render(request, template, context)

def show_product(request, slug):
    print(Phone.objects.filter(slug=slug))
    template = 'product.html'
    context = {'Phone': Phone.objects.get(slug=slug)}
    return render(request, template, context)