from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


from . import views

urlpatterns = [
    path('', views.HomePost.as_view(), name='home_posts'),
    path('posts/<pk_post>/', views.PostDetail.as_view(), name='post_detail'),
    path('product/<int:pk_product>/', views.product_detail, name='product_detail'),
    path('products/', views.ProductList.as_view(), name='product_list'),
    path('categories/', views.CategoryList.as_view(), name='category_list'),
    path('category/<int:category_pk>/', views.CategoryDetail.as_view(), name='category_detail'),
    path('tags/', views.TagList.as_view(), name='tag_list'),
    # path('tags/<int:pk>/', views.TagDetail.as_view(), name='tag_detail')

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)