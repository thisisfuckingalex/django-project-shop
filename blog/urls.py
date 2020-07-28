from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePost.as_view(), name='home_posts'),
    path('<pk>/', views.PostDetail.as_view(), name='post_detail'),
]