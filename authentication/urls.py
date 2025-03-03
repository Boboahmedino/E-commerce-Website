from django.urls import path
from .import views

urlpatterns = [
    path('register', views.register, name = 'register'),
    # path('activate/<uidb64>/<token>/', activate_account, name='activate'),
    path('login', views.login, name = 'login'),
    # path('verify-2fa', views.verify_2fa, name='verify_2fa'),
    path('logout', views.logout, name = 'logout'),     
]