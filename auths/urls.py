from django.urls import path
from . import views

# app_name = 'auths'

urlpatterns = [
    path('sign-in/', views.sign_in, name='sign-in'),
    path('sign-out/', views.sign_out, name='sign-out'),
    path('sign-up/', views.sign_up, name='sign-up'),

    path('profile/', views.profile, name='profile'),
    path('profile/edit/', views.edit_profile, name='edit-profile'),

    path('reset-password/', views.reset_password, name='reset-password'),
]