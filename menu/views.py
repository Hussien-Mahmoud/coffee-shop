from django.views.generic import ListView, DetailView

from .models import Item, Category


# Create your views here.

class MenuView(ListView):
    template_name = 'menu/index.html'
    model = Category
    context_object_name = 'categories'


class ItemView(DetailView):
    template_name = 'menu/single-item.html'
    model = Item
    context_object_name = 'item'
