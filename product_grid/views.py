from django.shortcuts import render
from .models import Products,Categories
# Create your views here.
from django.conf import settings

def getproduct(queryset):
    if len(queryset)>1:
        products=[]
        for product in queryset:
            images= [prod.image for prod in product.product_image.all()]
            products.append({'slug': product.slug, 'name': product.name, 'price': product.price, 'description': product.description, 'created_date': product.created_date, 'keyword': product.keyword, 'images': images})
        return products
    elif len(queryset)==1:
        product= queryset[0]
        images= [prod.image for prod in product.product_image.all()]
        return {'slug': product.slug, 'name': product.name, 'price': product.price, 'description': product.description, 'created_date': product.created_date, 'keyword': product.keyword, 'images': images}


def product_grid(request,filter):
    # Get names of all categories
    queryset = Categories.objects.all()
    categories= [{'name': category.name, 'slug': category.slug } for category in queryset]
    # Filter tat-ca-san-pham
    if filter=='tat-ca-san-pham':
        #Set title
        title = 'Tất cả sản phẩm'
        # Get all products 
        queryset = Products.objects.prefetch_related('product_image')
        products=getproduct(queryset)
    else:
        for category in categories :
            if filter == category['slug']:
                #Set title
                title= category['name']
                # Get products in category
                queryset = Categories.objects.prefetch_related('product_cate__product_image').filter(slug=category['slug'])
                queryset = [product for product in queryset[0].product_cate.all()]
                products=getproduct(queryset)
                break                          
    return render(request, 'product_grid/product_grid.html',{
            'title': title,
            'products': products,
            'categories': categories,           
        })
