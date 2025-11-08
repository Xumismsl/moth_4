from django.urls import path
from . import views 

urlpatterns = [
    # path('about_me/', views.about_me, name='about_me'),
    # path('current_time/', views.current_time, name='current_time'),
    # path('random_quote/', views.random_quote, name='random_quote'),
    path('book_list/<int:id>/', views.bookDetailView, name='book_detail'),
    path('book_list/', views.bookListView, name='book_list'),
    
]