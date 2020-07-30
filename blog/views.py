from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Category, Post, Product
from user.models import Profile


class HomePost(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'home_posts'
    queryset = Post.objects.filter(to_display=True)


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    pk_url_kwarg = 'pk_post'


class ProductList(ListView):
    model = Product
    template_name = 'product_list.html'
    queryset = Product.objects.filter(to_display=True)


class ProductDetail(DetailView):
    model = Product
    template_name = 'product_detail.html'
    pk_url_kwarg = 'pk_product'
