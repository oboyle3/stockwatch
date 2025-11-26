from django.shortcuts import render, redirect, get_object_or_404
from .models import Stock
from .models import MLB
# Create your views here.
def homepage(request):
    return render(request, "core/homepage.html")

def dashboard(request):
    stocks = Stock.objects.all()
    return render(request,"core/dashboard.html",{"stocks":stocks})

def addstock(request):
    if request.method == "POST":
        name = request.POST.get("name")
        symbol = request.POST.get("symbol")
        Stock.objects.create(name=name,symbol=symbol)
    return render(request,"core/addstock.html")

def delete_stock(request,id):
    stock = get_object_or_404(Stock,id=id)
    stock.delete()
    return redirect("core/deletestock.html")

def mlb(request):
    if request.method == "POST":
        test = request.POST.get("test")
        state = request.POST.get("state")
        MLB.objects.create(test=test,state=state)
    return render(request, "core/mlb.html")

