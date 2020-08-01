from django.shortcuts import render, get_object_or_404

from cart.forms import AddProduct


class AddProductMixin:
    template_name = None
    model = None

    def product_detail(self, request, pk_product):
        product = get_object_or_404(self.model,
                                    id=pk_product,
                                    available=True)
        cart_product_form = AddProduct()
        return render(request, self.template_name, context={'product': product,
                                                            'cart_product_form': cart_product_form})