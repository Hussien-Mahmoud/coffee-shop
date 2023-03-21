from django.views.generic import ListView, DetailView
from django.views import View

from .models import Product, Invoice
from timeit import default_timer as timer
#
# from django.urls import reverse
# from django.shortcuts import render
# from django.http import HttpResponseRedirect, JsonResponse
#
# from django.utils.decorators import method_decorator
# from django.views.decorators.csrf import ensure_csrf_cookie


# Create your views here.

class ProductsView(ListView):
    template_name = 'products/index.html'
    model = Product
    context_object_name = 'products'

    def get_context_data(self, **kwargs):
        start = timer()
        context = super().get_context_data(**kwargs)
        end = timer()
        print(end - start)
        # print(self.request.session.items())
        return context

    # @method_decorator(ensure_csrf_cookie)
    # def dispatch(self, *args, **kwargs):
    #     return super(ProductsView, self).dispatch(*args, **kwargs)


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
