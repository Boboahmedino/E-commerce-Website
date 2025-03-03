from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('store', views.store, name = 'store'),
    path('checkout', views.checkout, name = 'checkout'),
    path('cart', views.cart, name = 'cart'),
    path('updateitem', views.updateitem, name = 'updateitem'),
    path('product_view', views.product_view, name = 'product_view'),
    path('contact', views.contact, name = 'contact'),
    path('about', views.about, name = 'about'),
]