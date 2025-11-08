from django.urls import path
from . import views

urlpatterns = [
    path('category/<int:id>/', views.categoryDetailView, name='category_detail'),
    path('categories/', views.categoryListView, name='category_list'),
    path('products/', views.productListView, name='product_list'),
]