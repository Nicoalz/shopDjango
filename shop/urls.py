from django.urls import path
from . import views

app_name = 'shop'
urlpatterns = [
    path('', views.index, name='index'),
    path('category/<int:id>', views.category_detail, name='category_detail'),
    path('category/create', views.category_create, name='category_create'),
    path('categories', views.category_list, name='category_list'),
    path('category/<int:id>/delete', views.category_delete, name='category_delete'),
    path('category/<int:id>/update', views.category_update, name='category_update'),
    path('product/<int:id>', views.product_detail, name='product_detail'),
    path('product/create', views.product_create, name='product_create'),
    path('products', views.product_list, name='product_list'),
    path('product/<int:id>/delete', views.product_delete, name='product_delete'),
    path('product/<int:id>/update', views.product_update, name='product_update'),
]
