from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.forms import inlineformset_factory

from basketapp.models import Basket
from orderapp.models import Order, OrderItem
from orderapp.forms import OrderItemForm


class OrderList(ListView):
    model = Order
    template_name = 'orderapp/order_list.html'

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderItemsCreate(CreateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:orders_list')


class OrderRead(ListView):
    pass


class OrderItemsUpdate(UpdateView):
    pass


class OrderDelete(DeleteView):
    pass


def order_forming_complete():
    pass
