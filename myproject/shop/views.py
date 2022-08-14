from multiprocessing import context
from django.shortcuts import render
from .models import *

# Create your views here.

def home(request):
    products = Product.objects.all()
    context = {
        'products':products
    }
    return render(request, 'home.html', context)


def detail(request,product_id):
    product = Product.objects.get(id = product_id)
    context = {
        'product':product
    }
    return render(request, 'detail.html',context )

def cart(request):
    return render(request, 'cart.html')