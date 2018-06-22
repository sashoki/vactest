# -*- coding: utf-8 -*

from django.forms import ModelForm
from models import Comments, Keywords, Article
from django.conf import settings

from django.contrib.admin.widgets import AdminDateWidget


class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = '__all__'
        fields = ['comments_text']

class KeywordsForm(ModelForm):
    class Meta:
        model = Keywords
        fields = ['name']

class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = '__all__'
        fields = [
            'article_title',
            'article_img',
            'article_video',
            'article_text',
            'article_date',
            #'author',
            'category',
            'keywords',
        ]


    class Media:
        js = ('/admin/jsi18n',
            settings.ADMIN_MEDIA_PREFIX + 'js/core.js',
            settings.ADMIN_MEDIA_PREFIX + "js/calendar.js",
            settings.ADMIN_MEDIA_PREFIX + "js/admin/DateTimeShortcuts.js")

        css = {
            'all': (
                settings.ADMIN_MEDIA_PREFIX + 'css/forms.css',
                settings.ADMIN_MEDIA_PREFIX + 'css/base.css',
                settings.ADMIN_MEDIA_PREFIX + 'css/widgets.css',)
        }

    def __init__(self, *args, **kwargs):
        super(ArticleForm, self).__init__(*args, **kwargs)
        self.fields['article_title'].widget = AdminDateWidget()
