from django.views import generic
from books.models import Book

from django.shortcuts import get_object_or_404


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'book_list.html'

    # формируем запрос к базе, сортируем книги по дате, если в урле есть дата то отдаем одну книгу
    def get_queryset(self):
        if self.kwargs:
            book_name = get_object_or_404(Book, pub_date=self.kwargs['date']).name
            return Book.objects.filter(name=book_name)
        else:
            return Book.objects.order_by('pub_date')

    # добавляем в контекст данные на основании даты в урле
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.kwargs:

            list_books = Book.objects.order_by('pub_date')
            cur_book = Book.objects.filter(name=get_object_or_404(Book, pub_date=self.kwargs['date']).name)
            page = (list(list_books).index(cur_book[0]) + 1)
            count_books = list_books.count()
            context['is_paginated'] = True
            if 1 < page < count_books:
                context['next_page'] = str(list(list_books)[page].pub_date)
                context['previous_page'] = str(list(list_books)[page - 2].pub_date)
            elif 1 == page:
                context['next_page'] = str(list(list_books)[page].pub_date)
            elif count_books == page:
                context['previous_page'] = str(list(list_books)[page - 2].pub_date)
            return context
        return context
