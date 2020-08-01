from django.urls import path

from cart import views

urlpatterns = [
    path('', views.cart_detail, name='cart_detail'),
    path('add/<pk_product>/', views.cart_add, name='cart_add'),
    path('remove/<pk_product>/', views.cart_remove, name='cart_remove')
]