from django.urls import path

import mainapp.views as mainapp

from mainapp.views import products


app_name = 'mainapp'

urlpatterns = [
    path('', products, name='index'),
    path('<int:category_id>/', products, name='category'),
    path('page/<int:page>/', products, name='page'),
]
