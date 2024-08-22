from django.shortcuts import render

# Create your views here.
from django.shortcuts import render

# Create your views here.

def about(request):
    return render(request, "home/about.html")

def company(request):
    return render(request, "home/company.html")

def contact(request):
    return render(request,"home/contact.html")

def index(request):
    return render(request, "home/index.html")

def service(request):
    return render(request,"home/service.html")

def shop(request):
    return render(request, "home/shop.html")


