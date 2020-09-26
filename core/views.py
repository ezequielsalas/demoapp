from django.shortcuts import render, redirect
from django.http import HttpResponse
import datetime
from .models import Product


# Create your views here.
def index(request):
    latest_product_list = Product.objects.order_by('id')
    return render(request,'index.html',{})

def list_products(request):
    latest_product_list = Product.objects.order_by('-id')
    return render(request,'products.html',{'products': latest_product_list})

def create_product(request):
    name = request.POST.get('name', '')
    description = request.POST.get('description', '')
    price = request.POST.get('price', 0.0)
    created_at = datetime.date.today()
    
    product = Product()
    product.name = name
    product.description = description
    product.price = price
    product.created_at = created_at

    product.save()
    return redirect('/products')
    