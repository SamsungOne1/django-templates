from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "index.html", {'tab': 'home'})


def shop(request):
    return render(request, "shop.html", {'tab': 'shop'})


def about(request):
<<<<<<< HEAD
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')
=======
    return render(request, 'about.html', {'tab': 'about'})


def services(request):
    return render(request, 'services.html', {'tab': 'services'})


def contact(request):
    return render(request, 'contact.html', {'tab': 'contact'})


def blog(request):
    return render(request, 'blog.html', {'tab': 'blog'})


def cart(request):
    return render(request, 'cart.html')


def checkout(request):
    return render(request, 'checkout.html')


def thankyou(request):
    return render(request, 'thankyou.html')
>>>>>>> 2f39c5a1ac59ba0b30e5435c9ba23aa3d5ef8b42
