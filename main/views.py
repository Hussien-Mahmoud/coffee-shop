from django.shortcuts import render
from django.views.generic.base import TemplateView
from .models import HomeImage, LogoImage, AboutImage


# Create your views here.
class BaseView(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo_image'] = LogoImage.objects.all()[0].image
        return context

class MainView(BaseView):
    template_name = 'main/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about_image'] = AboutImage.objects.all()[0].image
        context['home_image'] = HomeImage.objects.all()[0].image
        return context