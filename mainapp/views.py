from django.shortcuts import render
from mainapp.models import Product, ProductCategory


def index(request):
    context = {
        'title': 'GeekShop'
    }
    return render(request, 'mainapp/index.html', context)


def products(request, pk=None):
    print(pk)
    category = ProductCategory.objects.all()
    product = Product.objects.all()[:6]
    context = {
        'title': 'GeekShop - Каталог',
        'category': category,
        'products': product,
    }
    return render(request, 'mainapp/products.html', context)
