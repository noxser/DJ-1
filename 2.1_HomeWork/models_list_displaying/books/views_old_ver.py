from django.views import generic
from books.models import Book
from django.core.paginator import Paginator
from django.core.paginator import EmptyPage
from django.core.paginator import PageNotAnInteger

from django.shortcuts import get_object_or_404


class BookListView(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'book_list.html'

    # формируем запрос к базе и сортируем книги по дате и отдаем в представление
    def get_queryset(self, **kwargs):
        return Book.objects.order_by('pub_date')


class BookListViewSort(generic.ListView):
    model = Book
    context_object_name = 'book_list'
    template_name = 'book_list.html'
    paginate_by = 1  # включаем пагинацию с шагом 1

    # формируем запрос к базе и сортируем книги по дате и отдаем в представление
    def get_queryset(self, **kwargs):
        return Book.objects.order_by('pub_date')

    # добавляем в контекст данные на основании даты в урле
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        list_books = Book.objects.order_by('pub_date')
        cur_book = Book.objects.filter(name=get_object_or_404(Book, pub_date=self.kwargs['date']).name)

        paginator = Paginator(list_books, self.paginate_by)
        page = (list(list_books).index(cur_book[0]) + 1)

        try:
            pagess = paginator.page(page)
            if pagess.has_next():
                context['next_page'] = str(list(list_books)[page].pub_date)
            if pagess.has_previous():
                context['previous_page'] = str(list(list_books)[page - 2].pub_date)
        except PageNotAnInteger:
            pagess = paginator.page(1)
        except EmptyPage:
            pagess = paginator.page(paginator.num_pages)

        #  пришлось переопределить дефолтную пагинацию нехотела брать то что надо (((
        #  мозги все сломал в конец
        context['page_obj'] = pagess
        context['book_list'] = cur_book
        return context
