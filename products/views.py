from django.views.generic import ListView, DetailView
from django.views import View

from .models import Product, Invoice


# Create your views here.

class ProductsView(ListView):
    template_name = 'products/index.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class SingleProductView(DetailView):
    template_name = 'products/single-product.html'
    model = Product
    context_object_name = 'product'


class CheckoutView(ListView):
    template_name = 'products/checkout.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(self.request.session.items())
        return context
