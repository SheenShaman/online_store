from django.urls import path
from django.views.decorators.cache import cache_page, never_cache
from catalog.apps import CatalogConfig
from catalog.views import (IndexView, contacts, CategoriesListView, CategoryListView, ProductListView,
                           ProductCreateView, ProductDetailView, ProductUpdateView, ProductDeleteView)
app_name = CatalogConfig.name

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('contacts/', contacts, name='contacts'),

    path('categories/', CategoriesListView.as_view(), name='categories'),
    path('category/<int:pk>/', CategoryListView.as_view(), name='category'),

    path('product/create/', never_cache(ProductCreateView.as_view()), name='product_create'),
    path('product/<int:pk>/', ProductListView.as_view(), name='product'),
    path('product/detail/<int:pk>/', cache_page(60)(ProductDetailView.as_view()), name='product_detail'),
    path('product/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),
]
