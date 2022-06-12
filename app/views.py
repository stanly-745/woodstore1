from django.shortcuts import redirect, render
from .models import *
from .form import *
from django.views import generic

# Create your views here.
def home(request):
    count=product.objects.count()
    customer=Customer.objects.all()
    Context={'count':count,'customer':customer,}
    return render(request,'app/home.html',Context)

def Product(request):
    products=product.objects.all()
    context={'product':products}
    return render(request,'app/product.html',context)
# ---product form---

def productform(request):
    form=ProductForm()
    if request.method=='POST':
        print(request.POST)
        form=ProductForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'app/add_product.html',context)

# ---bill form---

def billform(request):
    form=BillForm()
    if request.method=='POST':
        form=BillForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('bill')
    context={'form':form}
    return render(request,'app/bill.html',context)

def customer(request,pk_test):
    customer=Customer.objects.get(id=pk_test)
    orders=customer.order_set.all()
    total_bill=orders.count()
    context={'customer':customer,'order':orders,'total_bill':total_bill}
    return render(request,'app/customer.html',context)

def update(request,pk):
    bill=Bill.objects.get(id=pk)
    form=BillForm(instance=bill)
    if request.method=='POST':
        form=BillForm(request.POST,instance=bill)
        if form.is_valid():
            form.save()
            return redirect('/')
    context={'form':form}
    return render(request,'app/bill.html',context)

# customerform
def customerform(request):
    form=CustomerForm()
    if request.method=='POST':
        print(request.POST)
        form=CustomerForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'app/add_customer.html',context)







