from django.shortcuts import render
from .models import Category, Product


def categoryListView(request):
    categories = Category.objects.all()
    context = {
        'categories': categories
    }
    return render(request, 'shop/category_list.html', context)

def productListView(request):
    products = Product.objects.all()
    context = {
        'products': products
    }
    return render(request, 'shop/product_list.html', context)

def categoryDetailView(request, id):
    category = Category.objects.get(id=id)
    products = category.products.all()
    context = {
        'category': category,
        'products': products
    }
    return render(request, 'shop/category_detail.html', context)