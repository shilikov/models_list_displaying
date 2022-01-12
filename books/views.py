from django.shortcuts import render
from books.models import Book


def books_view(request):
    template = 'books/books_list.html'
    books_query = Book.objects.all()
    context = {'books': books_query}
    return render(request, template, context)


def books_of_date_view(request, date):
    template = 'books/books_list.html'
    books_query = Book.objects.order_by('pub_date')

    books_query = Book.objects.filter(pub_date=date)
    prev = Book.objects.filter(pub_date__lt=date).order_by('pub_date')
    next = Book.objects.filter(pub_date__gt=date).order_by('pub_date')
    prev_page = prev[prev.count() - 1].pub_date.strftime("%Y-%m-%d")\
        if prev.count() > 0 else None
    next_page = next[0].pub_date.strftime("%Y-%m-%d")\
        if next.count() > 0 else None
    context = {'books': books_query,
               'prev_page_url': prev_page,
               'next_page_url': next_page,
               }
    print(context)
    return render(request, template, context)
