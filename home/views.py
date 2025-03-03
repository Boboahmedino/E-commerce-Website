from django.shortcuts import render
from.models import *
from django.http import JsonResponse
# Create your views here.


def home(request):
    return render(request, 'home/home.html')

def store(request):
    products = Product.objects.all()
    context = {'products':products}
    return render(request, 'home/store.html', context)

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
    #to display all child selected objects
        items = order.orderitem_set.all() 
    else:
        # this creates an empty cart for non-logged in users
        items = []
        order = {'get_cart_total': 0,
                 'get_cart_items': 0,}

    context = {'items' : items,
               'order' : order}
    return render(request, 'home/checkout.html', context)

def cart(request):
    if request.user.is_authenticated:
        customer = request.user.customer
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
    #to display all child selected objects
        items = order.orderitem_set.all() 
    else:
        # this creates an empty cart for non-logged in users
        items = []
        order = {'get_cart_total': 0,
                 'get_cart_items': 0,}

    context = {'items' : items,
               'order' : order}
    return render(request, 'home/cart.html', context)

def updateitem(request):
    return JsonResponse('Item was added', safe=False)

def product_view(request):
    return render(request, 'home/product_view.html')

def contact(request):
    return render(request, 'home/contact.html')

def about(request):
    return render(request, 'home/about.html')