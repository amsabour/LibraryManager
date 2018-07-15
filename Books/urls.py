from django.conf.urls import url
from . import views

app_name = 'Books'

urlpatterns = [
    # /books/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # /books/<book_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),

    # /books/add
    url(r'^add/$', views.BookCreate.as_view(), name='book-add'),

    # /books/2/update/
    url(r'^(?P<pk>[0-9]+)/update/$', views.BookUpdate.as_view(), name='book-update'),

    # /books/2/delete
    url(r'^(?P<pk>[0-9]+)/delete/$', views.BookDelete.as_view(), name='book-delete'),

]
