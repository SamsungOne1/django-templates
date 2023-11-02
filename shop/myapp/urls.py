from django.urls import path
from . import views
app_name = "myapp"

urlpatterns = [
    path("", views.home, name="home"),
    path("about", views.about, name="about"),
    path("blog", views.blog, name="blog"),
    path("cart/", views.cart, name="cart"),
    path("checkout", views.checkout, name="checkout"),
    path("contact", views.contact, name="contact"),
    path("index", views.index, name="index"),
    path("services", views.services, name="services"),
    path("shop", views.shop, name="shop"),
    path("thankyou", views.thankyou, name="thankyou"),
]
