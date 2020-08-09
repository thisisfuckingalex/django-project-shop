from django.shortcuts import render
from django.views.generic import CreateView


from author.models import Author


class AuthorCreate(CreateView):
    model = Author
    template_name = 'author/author_create.html'
    fields = ('user', 'bio', )