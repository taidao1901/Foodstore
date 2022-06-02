from pyexpat import model
from unicodedata import category
from django.db import models
from matplotlib import image
from django.template.defaultfilters import slugify
from django.contrib.contenttypes.fields import GenericForeignKey

# Create your models here.
class Categories(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to ='images/categories')
    created_date = models.DateTimeField(auto_now_add=True)

class Products(models.Model):
    slug = models.SlugField(max_length=50, primary_key=True)
    name = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10,decimal_places=2)
    description = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    keyword = models.CharField(max_length=300)
    categories = models.ManyToManyField(Categories)


class ProductImage(models.Model):
    image = models.ImageField(upload_to='images/products')
    product= models.ForeignKey(Products,on_delete=models.CASCADE)

    




    