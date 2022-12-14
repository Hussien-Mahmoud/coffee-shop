from django.views.generic import ListView, DetailView
from .models import Product


# Create your views here.
class ProductsView(ListView):
    template_name = 'products/index.html'
    model = Product
    context_object_name = 'products'


class SingleProductView(DetailView):
    pass

class ConfirmationView:
    pass

class CheckoutView:
    pass