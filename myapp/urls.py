from django.urls import path
from . import views

app_name = "myapp"
urlpatterns = [
<<<<<<< HEAD
    path("", views.home, name='home'),
    path("about", views.about, name='about'),
    path("contact", views.contact, name='contact')
]
=======
    path('', views.home, name='home'),
    path('shop', views.shop, name='shop'),
    path('about', views.about, name='about'),
    path('services', views.services, name='services'),
    path('contact', views.contact, name='contact'),
    path('blog', views.blog, name='blog'),
    path('cart', views.cart, name='cart'),
    path('checkout', views.checkout, name='checkout'),
    path('thankyou', views.thankyou, name='thankyou'),
]
>>>>>>> 2f39c5a1ac59ba0b30e5435c9ba23aa3d5ef8b42
