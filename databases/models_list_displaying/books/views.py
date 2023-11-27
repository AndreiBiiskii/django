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


def book_detail(request, pub_date):
    template = 'books/books_detail.html'
    book_current = Book.objects.get(pub_date=pub_date)
    try:
        book_next = Book.objects.filter(pub_date__lt=pub_date).order_by('-pub_date').values('pub_date').first()['pub_date']
    except:
        book_next = ''
    try:
        book_previous = Book.objects.filter(pub_date__gt=pub_date).order_by('pub_date').values('pub_date').first()['pub_date']
    except:
        book_previous = ''
    context = {
        'book_current': book_current,
        'book_next': str(book_next),
        'book_previous': str(book_previous)
    }
    return render(request, template, context)
