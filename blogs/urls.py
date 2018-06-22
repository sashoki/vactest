from django.conf.urls import url, include
from django.contrib import admin
from . import views

urlpatterns = [

    url(r'^$', 'blogs.views.articles', name='articles'),
    url(r'^articles/get/(?P<article_id>\d+)/$', 'blogs.views.article', name='article'),
    url(r'^articles/create/$', 'blogs.views.create', name='create'),
    url(r'^articles/(?P<article_id>\d+)/edit/$', 'blogs.views.post_edit', name='post_edit'),
    url(r'^articles/addcomment/(?P<article_id>\d+)/$', 'blogs.views.addcomment', name='addcomment'),
    url(r'^author/(?P<id>\d+)/$', 'blogs.views.authors', name='authors'),

    ]