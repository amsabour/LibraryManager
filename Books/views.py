from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from .forms import *
from .models import Book


def index(request):
    if not request.user.is_authenticated:
        return redirect('Books:login_user')
    books = Book.objects.all()
    return render(request, 'Books/index.html', {'all_books': books, 'user': request.user})


def detail(request, book_id):
    if not request.user.is_authenticated:
        return render(request, 'Books/login_form.html')
    else:
        user = request.user
        book = get_object_or_404(Book, pk=book_id)
        return render(request, 'Books/detail.html', {'book': book, 'user': user})


def register(request):
    form = UserForm(request.POST or None)

    if form.is_valid():
        user = form.save(commit=False)
        username = form.cleaned_data['username']
        password = form.cleaned_data['password']
        user.set_password(password)
        user.save()
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                books = Book.objects.all()
                return render(request, 'Books/index.html', {'all_books': books, 'user': user})

    return render(request, 'Books/registration_form.html', {'form': form})


def logout_user(request):
    logout(request)
    return redirect('Books:login_user')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                books = Book.objects.all()
                return render(request, 'Books/index.html', {'all_books': books, 'user': user})
            else:
                return render(request, 'Books/login_form.html', {'error_message': 'Your account has been disabled'})
    return render(request, 'Books/login_form.html')


def add_book(request):
    if not request.user.is_authenticated:
        return redirect('Books:login_user')
    else:
        form = BookForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            book = form.save(commit=False)
            book.book_logo = request.FILES['book_logo']
            book.save()
            return redirect('Books:detail', book.id)
        else:
            return render(request, 'Books/create_book.html', {'form': form})


def update_book(request, book_id):
    if not request.user.is_authenticated:
        return redirect('Books:login_user')
    else:
        book = get_object_or_404(Book, pk=book_id)

        if request.method == "POST":
            form = BookForm(request.POST or None, request.FILES or None)
            if form.is_valid():
                book.title = form.cleaned_data['title']
                book.author = form.cleaned_data['author']
                book.book_logo = form.cleaned_data['book_logo']
                book.is_taken = form.cleaned_data['is_taken']
                book.save()
                return redirect('Books:detail', book.id)
        else:
            data = {'title': book.title, 'author': book.author, 'book_logo': book.book_logo, 'is_taken': book.is_taken}
            form = BookForm(initial=data)

        context = {'form': form}
        return render(request, 'Books/update_book.html', context)


class BookDelete(DeleteView):
    success_url = reverse_lazy('Books:index')
    model = Book
