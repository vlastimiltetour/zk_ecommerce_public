from django.shortcuts import render, redirect, get_object_or_404
from .models import Category, Product
from orders.models import OrderItem
from django.http import request,response
from django.http import HttpResponse
from cart.forms import CartAddProductForm
from django.db.models import Q 
from .recommender import *
from .converter import *

# connect to redis
from django.conf import settings
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
def products(request, category_slug=None):
    category = None
    categories = Category.objects.all()
    products = Product.objects.filter(available=True) #filtering available products
    search_results = request.GET.get('search')


    #print(search_results)
    if search_results:
        products = products.filter(Q(name__icontains=search_results))
    else:
        pass

    if category_slug:
        category = get_object_or_404(Category, slug=category_slug)
        products = products.filter(category=category)
    

    return render(request,
    'shop/product/list.html', 
    {'category':category,
    'categories': categories,
    'products': products})


def product_detail(request, id, slug):
    cz_price = Product.objects.get(id=id).price
    cz_price = round(int(cz_price),0)
    eng_price = round(float(cz_price) * float(exchange_rate),2)
    product = get_object_or_404(Product, id=id, slug=slug, available=True)
    #print(product)

    
    cart_product_form = CartAddProductForm()
    re = Recommender()
    #recommended_products = re.suggest_products_for([product], 4) #this is a product instace???
    recommended_products = re.suggest_products_for([product], 1)
    #print(type(recommended_products))
    recom_products = get_recommendation()


    return render(request,'shop/product/detail.html',
    {'product': product,
    'cart_product_form': cart_product_form,
    'recommended_products': recommended_products,
    'recom_products': recom_products,
    'cz_price': cz_price,
    'eng_price':eng_price,
    })

def home(request):
    products = Product.objects.filter(available=True) #filtering available products
    headline = Product.objects.filter(headline=True) #filtering available products
    cart_product_form = CartAddProductForm()
    return render(request, 'shop/home.html', {'products': products, 'headline': headline, 'cart_product_form': cart_product_form})


def about(request):
    return render(request, 'shop/about.html', {})


def admin(request):
    return render(request)

