from django.shortcuts import render


def index(request):
    return render(request, 'mainapp/index.html')


def prodacts(request):
    return render(request, 'mainapp/products.html')
