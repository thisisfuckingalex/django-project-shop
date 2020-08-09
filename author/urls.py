from django.urls import path
from author import views

urlpatterns = [
    path('', views.AuthorCreate.as_view(), name='author_create'),
]