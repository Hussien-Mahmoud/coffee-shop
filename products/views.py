from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
class ProductsView(TemplateView):
    template_name = 'products/index.html'
