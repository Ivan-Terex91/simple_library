from django.http import Http404
from django.shortcuts import render
from django.views import generic

from .models import *


def index(request):
    """
    Функция отображения для домашней страницы сайта.
    """
    # Генерация "количеств" некоторых главных объектов
    num_books = Book.objects.all().count()
    num_instances = BookInstance.objects.all().count()
    # Доступные книги (статус = 'a')
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()  # Метод 'all()' применен по умолчанию.
    # задание на дом урок 5
    num_books_task = Book.objects.filter(title__contains='Гарри').count
    num_genre_task = Genre.objects.filter(name__contains='Роман').count

    # Отрисовка HTML-шаблона index.html с данными внутри
    # переменной контекста context

    return render(
        request,
        'index.html',
        context={'num_books': num_books, 'num_instances': num_instances,
                 'num_instances_available': num_instances_available, 'num_authors': num_authors,
                 'num_books_task': num_books_task,
                 'num_genre_task': num_genre_task}
    )


class BookListView(generic.ListView):
    model = Book
    paginate_by = 2  # Постраничный вывод


class BookDetailView(generic.DetailView):
    model = Book

# def book_detail_view(request, pk):
#     try:
#         book_id = Book.objects.get(pk=pk)
#     except Book.DoesNotExist:
#         raise Http404("Book does not exist")
#
#     # book_id=get_object_or_404(Book, pk=pk)
#
#     return render(
#         request,
#         'catalog/book_detail.html',
#         context={'book': book_id, }
#     )
