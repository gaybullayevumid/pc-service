from django.urls import path
from .views import HomePageView, AboutPageView, PricePageView, ServicePageView, ShopPageView, BlogPageView, ContactPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('about/', AboutPageView.as_view(), name='about'),
    path('price/', PricePageView.as_view(), name='price'),
    path('service/', ServicePageView.as_view(), name='service'),
    path('shop/', ShopPageView.as_view(), name='shop'),
    path('blog/', BlogPageView.as_view(), name='blog'),
    path('contact/', ContactPageView.as_view(), name='contact'),
]