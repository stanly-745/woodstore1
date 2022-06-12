"""woodstore URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django import views
from django.urls import path
from . import views
from .models import *

urlpatterns = [
    path('',views.home, name='home'),
    path('products/',views.Product,name='products'),
    path('customer/<str:pk_test>/',views.customer,name='customer'),
    path('worker/<str:pk>/',views.worker,name='worker'),
    path('add_prod/',views.productform,name='addpro'),
    path('bill/',views.billform,name='bill'),
    path('order',views.order,name='order'),
    path('update/<str:pk>/',views.update,name='update'),
    path('add_cus/',views.customerform,name='addcus'),
    path('addworker',views.workerform,name='addworker'),
    path('addstock',views.stockform,name='addstock'),
    path('stockin',views.stock,name='stock'),
    path('update-stock/<str:pk>/',views.update_stock,name='up-stock'),
]
