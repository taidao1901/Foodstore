from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.conf import settings


def product_grid(request):
    return render(request, 'product_grid/product_grid.html')