from django.shortcuts import render
from django.views import generic

from order.forms import OrderCreateForm
from order.models import Order, OrderItem
from cart.cart import Cart


def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
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


class OrderList(generic.ListView):
    model = Order
    template_name = 'order/order_list.html'


class OrderDetail(generic.ListView):
    model = OrderItem
    template_name = 'order/order_detail.html'

    def get_queryset(self):
        return OrderItem.objects.filter(product__id__in=self.kwargs['pk_order'])