from django.urls import path

from user import views


urlpatterns = [
    path('', views.ProfileView.as_view(), name='profile_view'),
    # path('edit/<pk_profile>/', views.ProfileUpdate.as_view(), name='profile_update')

]