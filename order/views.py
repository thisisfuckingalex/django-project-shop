from django.shortcuts import render
from django.views import generic

from order.forms import OrderCreateForm
from order.models import Order, OrderItem


class OrderCreate(generic.CreateView):
    form_class = OrderCreateForm


class OrderList(generic.ListView):
    model = Order
    template_name = 'order/order_list.html'


class OrderDetail(generic.ListView):
    model = OrderItem
    template_name = 'order/order_detail.html'

    def get_queryset(self):
        return OrderItem.objects.filter(product__id__in=self.kwargs['pk_order'])