from django import template

from blog.utils import PostDetailMixin, ProductDetailMixin


register = template.Library()

# @register.simple_tag
# def get_the_best_categories(self, request):