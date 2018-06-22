# -*- coding: utf-8 -*-

from django.contrib import admin
from mptt.admin import MPTTModelAdmin
from blogs.models import Article, Comments, Category, Keywords

# Register your models here.
class ArticleInline(admin.StackedInline):
    model = Comments
    extra = 1


class ArticleAdmin(admin.ModelAdmin):
    fields = ['article_title', 'article_img',  'article_text', 'article_date', 'article_video', 'category', 'keywords']
    list_display = ('article_title', 'article_date', 'bit', 'category', 'author')
    inlines = [ArticleInline]
    list_filter = ['category']
    search_fields = ['article_title']

class CategoryAdmin(admin.ModelAdmin):
    fields = ['name', 'parent']

class KeywordsAdmin(admin.ModelAdmin):
    fields = ['name']

"""class AuthorAdmin(admin.ModelAdmin):
    fields = ['name', 'author_image']
    list_display = ['name', 'author_image']"""

admin.site.register(Article, ArticleAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Keywords, KeywordsAdmin)
#admin.site.register(Author, AuthorAdmin)
