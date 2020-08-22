from django.shortcuts import render, get_object_or_404
from django.utils import timezone
import logging

# logger = logging.getLogger('django.db.backends')


class PostDetailMixin:
    model = None
    template_name = None

    def get(self, request, pk_post):
        post = self.model.objects.filter(pk=pk_post)
        return render(request, self.template_name, context={'post': post})


class ProductDetailMixin:
    model = None
    template_name = None
    forms = None

    def get(self, request, pk_product):
        product = self.model.objects.get(pk=pk_product)
        cart_product_form = self.forms
        num_visits_product = request.session.get('num_visits_product', 0)
        request.session['num_visits_product'] = num_visits_product + 1
        return render(request, self.template_name, {'product': product,
                                                               'cart_product_form': cart_product_form,
                                                               'num_visits_product': num_visits_product,
                                                               })


