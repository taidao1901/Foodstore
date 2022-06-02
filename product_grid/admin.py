from django.contrib import admin
# Register your models here.
from .models import Categories, ProductImage, Products

@admin.register(Categories)
class CategoriesAdmin(admin.ModelAdmin):
    list_display= ('name', 'slug')
    prepopulated_fields = {'slug': ('name',)}
@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    list_display= ('image','product')
class ProductImageInline(admin.TabularInline):
    model= ProductImage

class ProductAdmin(admin.ModelAdmin):
    list_display= ('name','slug','price','description','created_date','keyword')
    prepopulated_fields = {'slug': ('name',)}

    inlines = [ProductImageInline, ]

admin.site.register(Products, ProductAdmin)

