from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Blog

# Create your views here.

class HomePageView(TemplateView):
    model = Blog
    template_name = 'pages/home.html'



class AboutPageView(TemplateView):
    template_name = 'pages/about.html'

class PricePageView(TemplateView):
    template_name = 'pages/price.html'

class ServicePageView(TemplateView):
    template_name = 'pages/service.html'

class ShopPageView(TemplateView):
    template_name = 'pages/shop.html'

class BlogPageView(TemplateView):
    template_name = 'pages/blog.html'

class ContactPageView(TemplateView):
    template_name = 'pages/contact.html'