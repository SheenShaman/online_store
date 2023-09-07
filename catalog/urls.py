from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import index, contacts, category, category_products, product

app_name = CatalogConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contacts/', contacts, name='contacts'),
    path('category/', category, name='category'),
    path('<int:pk>/category_products', category_products, name='category_products'),
    path('<int:pk>/product/', product, name='product')
]
