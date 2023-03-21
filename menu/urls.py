from django.urls import path
from .views import MenuView, ItemView

urlpatterns = [
    path('', MenuView.as_view(), name='menu'),
    path('<slug:slug>/', ItemView.as_view(), name='item'),
]