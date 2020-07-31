from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Category, Post, Product
from user.models import Profile


class HomePost(ListView):
    model = Post
    template_name = 'index.html'
    context_object_name = 'home_posts'
    queryset = Post.objects.filter(to_display=True)


class PostDetail(DetailView):
    model = Post
    template_name = 'post/post_detail.html'
    pk_url_kwarg = 'pk_post'


class ProductList(ListView):
    model = Product
    template_name = 'product/product_list.html'
    queryset = Product.objects.filter(to_display=True)


class ProductDetail(DetailView):
    model = Product
    template_name = 'product/product_detail.html'
    pk_url_kwarg = 'pk_product'


class CategoryList(ListView):
    model = Category
    template_name = 'category/category_list.html'


class CategoryDetail(ListView):
    model = Post
    template_name = 'category/category_detail.html'
    pk_url_kwarg = 'category_pk'
    context_object_name = 'postbycategory'

    def get_queryset(self):
        return Post.objects.filter(category__id=self.kwargs['category_pk'], to_display=True)