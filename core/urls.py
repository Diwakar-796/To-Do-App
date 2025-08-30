from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),

    path('add-task/', views.add_task, name="add-task"),
    path('del-task/', views.del_task, name="del-task"),
    path('done-task/', views.done_task, name="done-task"),
    path('edit-task/', views.edit_task, name="edit-task"),

    path('filter-task/', views.filter_task, name="filter-task"),

    path('add-category/', views.add_category, name="add-category"),

    path('donate/', views.donate_view, name="donate"),

    path('paypal/', include('paypal.standard.ipn.urls')),
    path('payment-completed/', views.payment_completed_view, name="payment-completed"),
    path('payment-failed/', views.payment_failed_view, name="payment-failed"),
]