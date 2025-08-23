from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# app_name = 'auths'

urlpatterns = [
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-out/', views.sign_out, name='sign-out'),
    path('sign-up/', views.sign_up, name='sign-up'),
    path('profile/', views.profile, name='profile'),
]