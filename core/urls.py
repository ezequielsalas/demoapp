from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('products', views.list_products, name='products'),
    path('product-create', views.create_product, name='product-create'),
]