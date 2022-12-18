from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect
from .models import Product, Category
from .forms import ProductForm, CategoryForm
# Create your views here.


def index(request):
    context = {}
    context["categories"] = Category.objects.all()
    return render(request, "index.html", context)


def category_list(request):
    context = {}
    context["categories"] = Category.objects.all()
    return render(request, "category_list.html", context)


def category_detail(request, id):
    context = {}
    context["categories"] = Category.objects.all()
    context["category"] = Category.objects.get(id=id)
    context["products"] = Product.objects.filter(category=id)
    return render(request, "category_detail.html", context)


def category_create(request):
    context = {}
    form = CategoryForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/categories")
    context["form"] = form
    context["categories"] = Category.objects.all()
    return render(request, "category_create.html", context)


def category_delete(request, id):
    context = {}
    obj = get_object_or_404(Category, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/categories")
    return render(request, "category_delete.html", context)


def category_update(request, id):
    context = {}
    obj = get_object_or_404(Category, id=id)
    form = CategoryForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/categories")
    context["form"] = form
    context["categories"] = Category.objects.all()
    return render(request, "category_create.html", context)


def product_list(request):
    context = {}
    context["products"] = Product.objects.all()
    context["categories"] = Category.objects.all()
    return render(request, "product_list.html", context)


def product_create(request):
    context = {}
    form = ProductForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/products")
    context["form"] = form
    context["categories"] = Category.objects.all()
    return render(request, "product_create.html", context)


def product_detail(request, id):
    context = {}
    context["product"] = Product.objects.get(id=id)
    context["categories"] = Category.objects.all()
    return render(request, "product_detail.html", context)


def product_delete(request, id):
    context = {}
    obj = get_object_or_404(Product, id=id)
    if request.method == "POST":
        obj.delete()
        return HttpResponseRedirect("/products")
    return render(request, "product_delete.html", context)


def product_update(request, id):
    context = {}
    obj = get_object_or_404(Product, id=id)
    form = ProductForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/products")
    context["form"] = form
    context["categories"] = Category.objects.all()
    return render(request, "product_create.html", context)
