from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import FormView, DetailView, CreateView
from django.views.decorators.http import require_POST

from cart.cart import Cart
from cart.forms import AddProduct
from blog.models import Product


@require_POST
def cart_add(request, pk_product):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk_product)
    form = AddProduct(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product,
                 quantity=cd['quantity'],
                 update_quantity=cd['update'])
    return redirect('cart_detail')


def cart_remove(request, pk_product):
    cart = Cart(request)
    product = get_object_or_404(Product, pk=pk_product)
    cart.remove(product)
    return redirect('cart_detail')


def cart_detail(request):
    cart = Cart(request)
    return render(request, 'cart/cart_detail.html', {'cart': cart})