from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_products),
    path('add/<slug:slug>/', views.add_product),
    path('remove/<slug:slug>/', views.remove_product),
]