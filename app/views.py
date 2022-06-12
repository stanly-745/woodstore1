from django.shortcuts import redirect, render
from .models import *
from .form import *
from django.views import generic

# Create your views here.
def home(request):
    no_order=Bill.objects.count()
    count=product.objects.count()
    not_paid=Bill.objects.filter(status='Not-Delivered').count()
    stock=Stock.objects.filter(quantity=0).count()
    customer=Customer.objects.all()
    worker=Worker.objects.all()
    Context={'count':count,'customer':customer,'not_paid':not_paid,'worker':worker,'no_order':no_order,'stock':stock}
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

# stock form
def stockform(request):
    form=StockForm()
    if request.method=='POST':
        print(request.POST)
        form=StockForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'app/stock_form.html',context)

# worker form
def workerform(request):
    form=WorkerForm()
    if request.method=='POST':
        print(request.POST)
        form=WorkerForm(request.POST)
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,'app/worker_form.html',context)

def update_stock(request,pk):
    stock=Stock.objects.get(id=pk)
    form=StockForm(instance=stock)
    if request.method=='POST':
        form=StockForm(request.POST,instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock')
    context={'form':form}
    return render(request,'app/stock_form.html',context)

def worker(request,pk):
    workers=Worker.objects.get(id=pk)
    context={'worker':workers}
    return render(request,'app/worker.html',context)

def order(request):
    orders=Bill.objects.all()
    context={'orders':orders}
    return render(request,'app/order.html',context)

def stock(request):
    stock=Stock.objects.all()
    stocks=Stock.objects.filter(quantity=0).all()
    context={'stock':stock,'stocks':stocks}
    return render(request,'app/stock.html',context)
