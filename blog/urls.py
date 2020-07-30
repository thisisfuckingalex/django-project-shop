from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views

urlpatterns = [
    path('', views.HomePost.as_view(), name='home_posts'),
    path('post/<int:pk_post>/', views.PostDetail.as_view(), name='post_detail'),
    path('products/<int:pk_product>/', views.ProductDetail.as_view(), name='product_detail'),
    path('products/', views.ProductList.as_view(), name='product_list'),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)