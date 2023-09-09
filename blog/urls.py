from django.urls import path
from blog.apps import BlogConfig
from blog.views import BlogCreateView

app_name = BlogConfig.name

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    # path('', BlogCreateView.as_view(), name='list'),
    # path('view/<int:pk>/', BlogCreateView.as_view(), name='view'),
    # path('edit/<int:pk>/', BlogCreateView.as_view(), name='edit'),
    # path('delete/<int:pk>/', BlogCreateView.as_view(), name='delete'),
]
