from main.views import BaseView
from main.models import LogoImage

from django.views.generic import ListView, DetailView

from .models import Item, Category


# Create your views here.
class MenuView(ListView):
    template_name = 'menu/index.html'
    model = Category
    context_object_name = 'categories'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo_image'] = LogoImage.objects.all()[0].image
        return context


class ItemView(DetailView):
    template_name = 'menu/single-item.html'
    model = Item
    context_object_name = 'item'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo_image'] = LogoImage.objects.all()[0].image
        return context
