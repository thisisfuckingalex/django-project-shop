from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, View
from django.db.models import Sum

from blog.models import Category, Post, Product
from user.models import Profile
from taggit.models import Tag
from cart.forms import AddProduct
from blog.utils import *


class HomePost(ListView):
    """
    Домашняя страница со списком
    постов

    """

    model = Post
    template_name = 'index.html'
    context_object_name = 'home_posts'
    queryset = Post.objects.filter(to_display=True)
    paginate_by = 2


class PostDetail(View, PostDetailMixin, ):
    """Отображение одного поста"""
    model = Post
    template_name = 'post/post_detail.html'

    # pk_url_kwarg = 'pk_post'


class ProductList(ListView):
    """Список постов"""
    model = Product
    template_name = 'product/product_list.html'
    queryset = Product.objects.filter(to_display=True)


class ProductDetail(View, ProductDetailMixin):
    model = Product
    template_name = 'product/product_detail.html'
    forms = AddProduct()


class CategoryList(ListView):
    """Список всех категорий"""
    model = Category
    template_name = 'category/category_list.html'


class CategoryDetail(ListView):
    """Фильтрация постов по категориям"""
    model = Post
    template_name = 'category/category_detail.html'
    pk_url_kwarg = 'category_pk'
    context_object_name = 'postbycategory'

    def get_queryset(self):
        return Post.objects.filter(category__id=self.kwargs['category_pk'], to_display=True)


class TagList(ListView):
    model = Tag
    template_name = 'tag/tag_list.html'


# class TagDetail(ListView):
#     model = Post
#     template_name = 'tag/tag_detail.html'
#
#     def get_queryset(self):
#         return Post.objects.filter(tag__name__in=self.kwargs['tag__name'], to_display=True)
