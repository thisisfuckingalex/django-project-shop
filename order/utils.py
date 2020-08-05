from django.contrib.auth.models import User
from django.shortcuts import render


class OrderCreateMixin:
    model = None
    form = None
    template_name_f = None
    template_name_s = None

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


class OrderListMixin:
    model = None
    template_name = None

    def get(self, request, username):
        orders = self.model.objects.filter()
        return render(request, self.template_name, context={'orders': orders})