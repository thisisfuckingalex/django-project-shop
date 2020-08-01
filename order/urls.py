from django.urls import path
from . import views

from order.views import OrderCreate


urlpatterns = [
    path('create/', OrderCreate.as_view(), name='order_create'),
]