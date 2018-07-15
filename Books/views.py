# from django.shortcuts import render, get_object_or_404
# from .models import Book
#
#
# def index(request):
#     all_books = Book.objects.all()
#     context = {'all_books': all_books}
#     return render(request, 'Books/index.html', context)
#
#
# def detail(request, book_id):
#     book = get_object_or_404(Book, id=book_id)
#     return render(request, 'Books/detail.html', {'book': book})

from django.views import generic
from .models import Book


class IndexView(generic.ListView):
    template_name = 'Books/index.html'
    context_object_name = 'all_books'

    def get_queryset(self):
        return Book.objects.all()


class DetailView(generic.DetailView):
    model = Book
    template_name = 'Books/detail.html'


