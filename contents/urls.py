# coding=utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'contents.views.articles',
    url(regex='^articles/list$', view='list_articles', name=u'list_articles'),
    url(regex='^articles/new$', view='new_article', name=u'new_article'),
    url(regex='^articles/edit/(?P<id>\d+)$', view='edit_article', name=u'edit_article'),
    url(regex='^articles/delete/(?P<id>\d+)$', view='delete_article', name=u'delete_article'),
)
