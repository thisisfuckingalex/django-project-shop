from django.shortcuts import render
from django.views.generic import ListView, DetailView

from blog.models import Category, Post, Product
from user.models import Profile


class HomePost(ListView):
    model = Post
    template_name = 'home.html'
    context_object_name = 'home_posts'
    queryset = Post.objects.filter(to_display=True)

    # def get_queryset(self):
    #     Post.objects.filter(to_display=True)


class PostDetail(DetailView):
    model = Post
    template_name = 'post_detail.html'
    slug_field = 'post_id'


# class CategoryList(ListView):
#     model = Category
#     template_name = 'base.html'


# class CategoryDetail(DetailView):
#     model = Post
#     template_name = 'category_detail.html'
#
#     def get_queryset(self):
#         Post.objects.filter(category__slug=self.kwargs['category_slug'])



class ProductByPost(ListView):
    model = Product
    template_name = 'post_detail.html'

    def get_queryset(self):
        Product.objects.filter(to_display=True, post__slug=self.kwargs['post_detail'])