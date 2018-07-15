from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Book


class IndexView(generic.ListView):
    template_name = 'Books/index.html'
    context_object_name = 'all_books'

    def get_queryset(self):
        return Book.objects.all()


class DetailView(generic.DetailView):
    model = Book
    template_name = 'Books/detail.html'


class BookCreate(CreateView):
    model = Book
    fields = ['title', 'author', 'image_url', 'is_taken']


class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author', 'image_url', 'is_taken']


class BookDelete(DeleteView):
    model = Book
    success_url = reverse_lazy('Books:index')
