from django.conf.urls import url

from Books.models import Book
from . import views

app_name = 'Books'

urlpatterns = [
    # /books/
    url(r'^$', views.index, name='index'),

    # /books/register/
    url(r'^register/$', views.register, name='register'),

    # /books/<book_id>/
    url(r'^(?P<book_id>[0-9]+)/$', views.detail, name='detail'),

    # /books/logout_user/
    url(r'^logout_user/$', views.logout_user, name='logout_user'),

    # /books/login_user/
    url(r'^login_user/$', views.login_user, name='login_user'),

    # /books/add
    url(r'^add/$', views.add_book, name='add_book'),

    # /books/update/2/
    url(r'^update/(?P<book_id>[0-9]+)/$', views.update_book, name='book-update'),

    # /books/delete/2
    url(r'^delete/(?P<pk>[0-9]+)/$', views.BookDelete.as_view(), name='book-delete'),

]
