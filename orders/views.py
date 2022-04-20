from django.forms import inlineformset_factory
from django.http import  HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView

from baskets.models import Basket
from orders.models import Order, OrderItem
from orders.forms import OrderItemForm, OrderForm


class OrderListView(ListView):
    model = Order

    def get_queryset(self):
        return Order.objects.filter(user=self.request.user)


class OrderDetailView(DetailView):
    model = Order


class OrderCreateView(CreateView):
    model = Order
    fields = []
    success_url = reverse_lazy('orders:order_list')


class OrderDeleteView(DeleteView):
    pass


class OrderUpdateView(UpdateView):
    pass


def order_forming_complete():
    pass

