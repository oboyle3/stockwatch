from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, "core/homepage.html")

def dashboard(request):
    return render(request,"core/dashboard.html")
