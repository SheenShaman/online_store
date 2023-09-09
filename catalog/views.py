from django.shortcuts import render
from catalog.models import Category, Product
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, TemplateView


class IndexView(TemplateView):
    template_name = 'catalog/index.html'
    extra_context = {
        'title': 'SkyStore - Главная'
    }

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['object_list'] = Product.objects.all()
        return context_data


# def index(request):
#     context = {
#         'object_list': Product.objects.all(),
#         'title': 'SkyStore - Главная'
#     }
#     return render(request, 'catalog/index.html', context)


def contacts(request):
    context = {
        'title': 'Контакты'
    }
    return render(request, 'catalog/contacts.html', context)


# def category(request):
#     context = {
#         'object_list': Category.objects.all(),
#         'title': 'Категории Товаров'
#     }
#     return render(request, 'catalog/category_list.html', context)


class CategoriesListView(ListView):
    model = Category
    extra_context = {
        'title': 'Категории Товаров'
    }


# def category_products(request, pk):
#     category_item = Category.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(category_id=pk),
#         'title': f'Товары категории {category_item.name}'
#     }
#     return render(request, 'catalog/product_list.html', context)


class CategoryListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(category_id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        category_item = Category.objects.get(pk=self.kwargs.get('pk'))
        context_data['category_pk'] = category_item.pk,
        context_data['title'] = f'Товары категории {category_item.name}'
        return context_data


# def product(request, pk):
#     product_item = Product.objects.get(pk=pk)
#     context = {
#         'object_list': Product.objects.filter(id=pk),
#         'title': f'{product_item.name}'
#     }
#     return render(request, 'catalog/product_list.html', context)

class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        queryset = super().get_queryset()
        queryset = queryset.filter(id=self.kwargs.get('pk'))
        return queryset

    def get_context_data(self, *args, **kwargs):
        context_data = super().get_context_data(*args, **kwargs)

        product_item = Product.objects.get(pk=self.kwargs.get('pk'))
        context_data['product_pk'] = product_item.pk,
        context_data['title'] = f'{product_item.name}'
        return context_data


class ProductCreateView(CreateView):
    model = Product
    fields = ('name', 'category', 'price')
    success_url = reverse_lazy('catalog:categories')


class ProductUpdateView(UpdateView):
    model = Product
    fields = ('name', 'category', 'price')

    def get_success_url(self):
        return reverse('catalog:category', args=[self.object.category.pk])


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('catalog:categories')
