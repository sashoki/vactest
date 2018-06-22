# -*- coding: utf-8 -*-

from django.shortcuts import render, render_to_response, redirect, get_object_or_404, HttpResponse
from blogs.models import Article, Comments, Category, Keywords
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse, Http404
from forms import CommentForm, KeywordsForm, ArticleForm
from django.core.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.utils import timezone


def index(request):
    return render(request, 'index.html')


def articles(request, page_number=1):
    keywords_form = KeywordsForm
    args = {}
    all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 50)
    args['articles'] = current_page.page(page_number)
    args['projects'] = Category.objects.all()
    args['keywords'] = Keywords.objects.all()
    args['username'] = auth.get_user(request).username
    #args['authors'] = Author.objects.all()
    args['form_keywords'] = keywords_form
    return render(request, 'blogs/articles.html', args)

def article(request, article_id=1):
    comment_form = CommentForm
    keywords_form = KeywordsForm
    args = {}
    args.update(csrf(request))
    args['article'] = Article.objects.get(id=article_id)
    args['projects'] = Category.objects.all()
    args['category'] = Category.objects.filter(id=article_id)
    args['comments'] = Comments.objects.filter(comments_article_id=article_id)
    args['n_comments'] = args['comments'] .count()
    args['keywords'] = Keywords.objects.all()
    args['form'] = comment_form
    args['username'] = auth.get_user(request).username
    #args['authors'] = Author.objects.all()
    args['form_keywords'] = keywords_form
    return render(request, 'blogs/article1.html', args)


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save(commit=False)
            article.author =request.user
            article.article_date = timezone.now()
            article.save()
            return redirect('/author/%s/' % article.author_id)
    else:
        form = ArticleForm()
    return render(request, 'blogs/post_edit.html', {'form': form})


def post_edit(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            article = form.save(commit=False)
            article.author = request.user
            article.article_date = timezone.now()
            article.save()
            return redirect('/articles/get/%s/' % article_id)
    else:
        form = ArticleForm(instance=article)
    return render(request, 'blogs/post_edit.html', {'form': form})


def addcomment(request, article_id):
    if request.POST and ("pause" not in request.session):
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_author = request.user
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60)
            request.session['pause'] = True
    return redirect('/articles/get/%s/' % article_id)

def article_cat(request, category_id=1):
    keywords_form = KeywordsForm
    args = {}
    args['projects'] = Category.objects.all()
    args['category'] = Category.objects.get(id=category_id)
    args['articles'] = Article.objects.filter(category_id=category_id)
    args['username'] = auth.get_user(request).username
    args['keywords'] = Keywords.objects.all()
    args['form_keywords'] = keywords_form
    branch_categories = args['category'].get_descendants(include_self=True)
    args['category_articles'] = Article.objects.filter(category__in=branch_categories).distinct()
    #args['authors'] = Author.objects.all()
    return render(request, 'blogs/article_cat.html', args)

def keywords(request):
    keywords_form = KeywordsForm
    return_path = request.META.get('HTTP_REFERER', '/')
    args= {}
    #args['authors'] = Author.objects.all()
    args['keywords'] = Keywords.objects.all()
    args['projects'] = Category.objects.all()
    args['username'] = auth.get_user(request).username
    args['form_keywords'] = keywords_form
    args.update(csrf(request))
    if request.POST:
        key = request.POST.get('name', '')
        args['key_name'] = key
        args['articles'] = Article.objects.filter(keywords__name__exact=key)
        if args['articles']:
            return render(request, 'blogs/keywpage.html', args)
        else:
            return render(request, 'blogs/keywpage_no.html', args)
    else:
        return render(return_path)

def authors(request, id):
    args= {}
    args['username'] = auth.get_user(request).username
    args['articles'] = Article.objects.filter(author__username__exact=args['username'])
    #args['articles'] = Category.objects.all()
    args['keywords'] = Keywords.objects.all()
    return render(request, 'blogs/author_page.html', args)



