from django import forms
from .models import Product, Category
# creating a form

class CategoryForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Category
        # specify fields to be used
        fields = [
            "name",
        ]

class ProductForm(forms.ModelForm):

    # create meta class
    class Meta:
        # specify model to be used
        model = Product
        # specify fields to be used
        fields = [
            "name",
            "price",
            "category",
            "stock",
            "image_url"
        ]
