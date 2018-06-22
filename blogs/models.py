# -*- coding: utf-8 -*-

from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from tinymce.models import HTMLField
from embed_video.fields import EmbedVideoField
import mptt
from mptt.models import MPTTModel, TreeForeignKey
from django.utils import timezone

class Keywords(models.Model):
    class Meta():
        db_table = 'keywords'
        verbose_name_plural = 'Keywords'
        verbose_name = 'Keyword'

    name = models.CharField(max_length=50, unique=True, verbose_name=u'Site search:')

    def __unicode__(self):
        return self.name

"""class Author(models.Model):
    class Meta():
        db_table = 'author'
        verbose_name_plural = 'Authors'
        verbose_name = 'Author'

    name = models.CharField(max_length=150)
    author_image = models.ImageField(null=True, blank=True, upload_to="img/", verbose_name="Фото автора",  help_text="250x25")

    def __unicode__(self):
        return self.name

    def bit_author(self):
        if self.author_image:
            return u'<img src="%s" width="70"/>' % self.author_image.url
        else:
            return u'(none)'
    bit_author.short_descriptio = u'Image'
    bit_author.allow_tags = True"""


class Category(MPTTModel):
    class Meta():
        db_table = 'category'
        verbose_name_plural = 'Categories'
        verbose_name = 'category'
        ordering = ('tree_id', 'level')

    name = models.CharField(max_length=150, verbose_name = 'Category')
    parent = TreeForeignKey('self', null=True, blank=True, related_name='children', verbose_name=u'Famely class')

    def __unicode__(self):
        return self.name

    class MPTTMeta:
        order_insertion_by = ['name']

mptt.register(Category, order_insertion_by=['name'])


class Article(models.Model):
    class Meta():
        ordering = ['-article_date']
        db_table = 'article'
        verbose_name_plural = 'Article'
        verbose_name = 'Articles'

    article_title = models.CharField(max_length=200, verbose_name=u'Articles')
    article_img = models.ImageField(null=True, blank=True, upload_to="img/", verbose_name='Image',  help_text="150x150")
    article_video = EmbedVideoField(null=True, blank=True, verbose_name=u'Video')
    article_text = HTMLField(null=True, blank=True)
    article_date = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    category = TreeForeignKey(Category, blank=True, null=True, related_name='cat')
    keywords = models.ManyToManyField(Keywords, null=True, blank=True, related_name='keywords', related_query_name='keyword', verbose_name=u'Tags')

    def __unicode__(self):
        return self.article_title

    def __str__(self):
        return self.article_title

    def bit(self):
        if self.article_img:
            return u'<img src="%s" width="70"/>' % self.article_img.url
        else:
            return '(none)'
    bit.short_description = u'Image'
    bit.allow_tags = True



class Comments(models.Model):
    class Meta():
        ordering = ['-comments_date']
        db_table = 'comments'

    comments_text = models.TextField(null=True, blank=True, verbose_name='Comment text')
    comments_article = models.ForeignKey(Article)
    comments_date = models.DateField(u'date', auto_now=True)
    comments_author = models.ForeignKey(User)
