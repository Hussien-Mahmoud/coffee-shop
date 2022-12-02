from django.shortcuts import render
from django.views.generic.base import TemplateView


# Create your views here.
class BlogView(TemplateView):
    template_name = 'blog/index.html'
