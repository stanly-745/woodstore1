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
    payment=(
        ('Paid','Paid'),
        ('Not-paid','Not-paid'),
    )
    customer=models.ForeignKey(Customer,null=True,on_delete=models.SET_NULL)
    product=models.ForeignKey(product,null=True,on_delete=models.SET_NULL)
    date=models.DateTimeField(auto_now_add=True,null=True)
    payment=models.CharField(max_length=50,null=True,choices=payment)
    

