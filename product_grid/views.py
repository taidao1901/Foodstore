from xml.sax.handler import all_properties
from django.shortcuts import render
from .models import Products,ProductImage,Categories
from django.db.models import Prefetch

# Create your views here.
from django.http import HttpResponse
from django.conf import settings


def product_grid(request,filter):
    if filter=='tat-ca-san-pham':
            results= ProductImage.objects.select_related(('product'))
            slugs = []
            all_products=[]
            for row in results:
                if row.product.slug not in slugs:
                    all_products.append(row)
                    slugs.append(row.product.slug)
            print(len(all_products))
            return render(request, 'product_grid/product_grid.html',{
                'products': all_products,           
            })