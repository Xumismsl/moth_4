from django.shortcuts import render, get_object_or_404
from .models import Book
from django.db.models import Avg

def bookListView(request):
    books = Book.objects.all()
    context = {
        'books': books
    }
    return render(request, 'books/book.html', context)


def bookDetailView(request, id):
    book = get_object_or_404(Book, id=id)
    avg = book.average_mark()
    context = {
        'book': book,
        'avg': avg
    }
    return render(request, 'books/book_detail.html', context)
