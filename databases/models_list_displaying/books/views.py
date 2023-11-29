from datetime import datetime

from django.shortcuts import render

from books.converters import DateConverter
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_list = Book.objects.all()
    context = {
        'books_list': books_list
    }
    return render(request, template, context)


def book_detail(request, pub_date: datetime):
    template = 'books/books_detail.html'
    book_current = Book.objects.filter(pub_date=pub_date)
    book_next = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').first()
    book_previous = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').first()

    context = {
        'book_current': book_current,
        'book_next': book_next,
        'book_previous': book_previous
    }
    return render(request, template, context)
