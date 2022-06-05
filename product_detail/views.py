from django.shortcuts import render
from product_grid.views import getproduct
from product_grid.models import Products, Categories,ProductImage
from django.http import HttpResponse
# Create your views here.
def product_detail(request,product):
    queryset = Products.objects.prefetch_related('product_image').filter(slug=product)
    prod_detail= getproduct(queryset)
    imgs_count= len(prod_detail['images']) 
    print(imgs_count)
    if queryset:
        return render(request,"product_detail/product_detail.html",{
            'prod_detail' : prod_detail,
        })
    else:
        return HttpResponse('Không có sản phẩm này')
