from django.shortcuts import render
from .models import  Product,Tag

def list_product(request):
    return render(request , "product-list.html")
    # raise NotImplementedError("Implement List Of Products Funtion")