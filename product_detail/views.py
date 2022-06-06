from django.shortcuts import render
from product_grid.views import getproduct
from product_grid.models import Products, Categories,ProductImage
from django.http import HttpResponse
# Create your views here.
def product_detail(request,product):
    # get a product via slug
    queryset = Products.objects.prefetch_related('product_image').filter(slug=product)
    prod_detail= getproduct(queryset)
    # Get products in features
    queryset1 = Products.objects.order_by('?')
    prods_cate= getproduct(queryset1)
    if queryset:
        return render(request,"product_detail/product_detail.html",{
            'prod_detail': prod_detail,
            'prods_cate' : prods_cate[:10], 
        })
    else:
        return HttpResponse('Không có sản phẩm này')
