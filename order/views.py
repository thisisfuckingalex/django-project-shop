from django.shortcuts import render
from django.views.generic import *
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView

from order.forms import OrderCreateForm
from order.models import Order, OrderItem
from cart.cart import Cart
from order.utils import OrderListMixin, OrderCreateMixin


def order_create(request):
        cart = Cart(request)
        if request.method == 'POST':
            form = OrderCreateForm(request.POST)
            if form.is_valid():
                order = form.save()
                order.user = request.user.profile
                order.save()
                for item in cart:
                    OrderItem.objects.create(order=order,
                                             product=item['product'],
                                             price=item['price'],
                                             quantity=item['quantity'])
                # очистка корзины
                cart.clear()
                return render(request, 'order/order_created.html',
                              {'order': order})
        else:
            form = OrderCreateForm
        return render(request, 'order/order_create.html',
                      {'cart': cart, 'form': form})


class OrderList(ListView):
    model = Order
    template_name = 'order/order_list.html'


class OrderDetail(ListView):
    model = OrderItem
    template_name = 'order/order_detail.html'

    def get_queryset(self):
        return OrderItem.objects.filter(order_id=self.kwargs['pk_order'])