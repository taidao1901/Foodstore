from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.conf import settings


def index(request):
    print(settings.BASE_DIR)
    return render(request, 'home/index.html')
    #return HttpResponse("Hello, world.")