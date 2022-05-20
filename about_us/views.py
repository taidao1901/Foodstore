from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.conf import settings


def about_us(request):
    return render(request, 'about_us/about_us.html')
