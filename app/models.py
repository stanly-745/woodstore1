from secrets import choice
from django.db import models
from django.forms import CharField
from django.urls import reverse

# Create your models here.
class product(models.Model):
    name=models.CharField(max_length=200,null=True)
    price=models.CharField(max_length=200,null=True)

    def __str__(self):
        return self.name

class Customer(models.Model):
    name=models.CharField(max_length=20,null=True)
    phone=models.CharField(max_length=10,blank=True)
    email=models.EmailField(blank=True)

    def __str__(self):
        return self.name

class Bill(models.Model):
    status=(
        ('Delivered','Delivered'),
        ('Not-Delivered','not-Delivered'),
    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(product,null=True,on_delete=models.SET_NULL)
    date_cretated=models.DateTimeField(auto_now_add=True)
    status=models.CharField(max_length=20,null=True,choices=status)

    def __str__(self):
        return self.customer.name


# Workers model
class Worker(models.Model):
    name=models.CharField(max_length=15,null=True)
    phone=models.CharField(max_length=10,null=True)
    place=models.CharField(max_length=20,null=True)
    email=models.EmailField(blank=True)

    def __str__(self):
        return self.name

# Stock model
class Stock(models.Model):
    name=models.CharField(max_length=20,null=True)
    quantity=models.IntegerField(null=True)

    def __str__(self):
        return self.name
