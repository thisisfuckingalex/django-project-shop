from django.urls import path
from . import views

from order.views import order_create


urlpatterns = [
    path('create/', order_create, name='order_create'),
    path('myorders/', views.OrderList.as_view(), name='myorder_list'),
    path('myorders/<int:pk_order>/', views.OrderDetail.as_view(), name='order_detail'),
]