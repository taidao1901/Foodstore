from django.shortcuts import render

# Create your views here.
def product_detail(request):
    return render(request,"product_detail/product_detail.html")
