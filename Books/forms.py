from django.contrib.auth.models import User
from django import forms

from Books.models import Book


class BookForm(forms.ModelForm):

    class Meta:
        model = Book
        fields = ['title', 'author', 'book_logo', 'is_taken']


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']


class LoginForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
