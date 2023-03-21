from django.urls import path
from .views import ProductsView, SingleProductView, CheckoutView

urlpatterns = [
    path('', ProductsView.as_view(), name='products'),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('<slug:slug>/', SingleProductView.as_view(), name='product'),
]
