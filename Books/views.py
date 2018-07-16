from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import View
from django.urls import reverse_lazy
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, JsonResponse
from .forms import *
from .models import Book


def log_out(request):
    logout(request)
    return redirect('Books:index')


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
    fields = ['title', 'author', 'book_logo', 'is_taken']


class BookUpdate(UpdateView):
    model = Book
    fields = ['title', 'author', 'book_logo', 'is_taken']


class BookDelete(DeleteView):
    success_url = reverse_lazy('Books:index')
    model = Book


class UserFormView(View):
    form_class = UserForm
    template_name = 'Books/registration_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process registration data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            # cleaned data
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # returns User objects if data is correct
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('Books:index')

        return render(request, self.template_name, {'form': form})


class UserLoginView(View):
    form_class = LoginForm
    template_name = 'Books/login_form.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            # cleaned data
            print(form.cleaned_data['username'])
            print(form.cleaned_data['password'])

            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if user is not None:
                if user.is_active:
                    login(request, user)
                    print('login successful')
                    return redirect('Books:index')

        return render(request, self.template_name, {'form': form})
