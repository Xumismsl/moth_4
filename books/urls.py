from django.urls import path
from . import views 

urlpatterns = [
    path('', views.bookListView, name='home'),
    path('book_list/<int:id>/', views.bookDetailView, name='book_detail'),
    path('book_list/', views.bookListView, name='book_list'),
]
