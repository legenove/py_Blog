# coding=utf-8
from django.conf.urls import patterns, url

urlpatterns = patterns(
    'app.contents.views',
    url(regex='^articles/list$', view='list_articles', name=u'list_articles'),
    url(regex='^articles/new$', view='new_article', name=u'new_article'),
    url(regex='^articles/edit/(?P<id>\d+)$', view='edit_article', name=u'edit_article'),
    url(regex='^articles/delete/(?P<id>\d+)$', view='delete_article', name=u'delete_article'),

    url(regex='^tags/list', view='list_tags', name=u'list_tags'),
    url(regex='^tags/add', view='add_tag', name=u'add_tag'),
    url(regex='^tags/del', view='del_tag', name=u'del_tag'),

    url(regex='^categories/list', view='list_categories', name=u'list_categories'),
    url(regex='^categories/new', view='new_category', name=u'new_category'),
    url(regex='^categories/edit/(?P<id>\d+)$', view='edit_category', name=u'edit_category'),
    url(regex='^categories/delete/(?P<id>\d+)$', view='delete_category', name=u'delete_category'),
)
