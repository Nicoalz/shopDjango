from django.contrib import admin

# Register your models here.

from .models import Category, Product

class ProductAdmin(admin.ModelAdmin):
    fields = ['name','price','stock', 'image_url']

admin.site.register(Category)
admin.site.register(Product)