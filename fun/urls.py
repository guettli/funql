from django.urls import path

from . import views

urlpatterns = [
    path('accounts/profile/', views.accounts_profile),
    path('', views.start),
]