from unicodedata import name
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.conf import settings
from product_grid.models import  Products,ProductImage,Categories
from product_grid.views import getproduct

def index(request):
    queryset = Categories.objects.all()
    categories= [{'slug': category.slug, 'name': category.name, 'image': category.image} for category in queryset]
    queryset= Products.objects.prefetch_related('product_image')
    all_products= getproduct(queryset)
    queryset= Products.objects.prefetch_related('product_image').order_by("-created_date")
    newer_products= getproduct(queryset) 

    return render(request, 'home/index.html',{
        'categories': categories,
        'all_products': all_products,
        'newer_products': newer_products,
    })