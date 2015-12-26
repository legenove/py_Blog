# coding=utf-8
from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # 只显示技术页面
    url(r'^$', 'outside.views.index.index_page', name='index_page'),
    # 全部页面
    url(r'^all/$', 'outside.views.index.all_page', name='all_page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^manage/', 'outside.views.index.manage_page', name='manage_page'),
    url(r'^contents/', include('contents.urls')),

    url(r'^signin/$', 'django.contrib.auth.views.login', {'template_name': 'signin.html'}, name="signin"),
    url(r'^signout/$', 'django.contrib.auth.views.logout_then_login',  name="signout"),

    url(r'^a/(?P<article_id>\d+)', 'outside.views.articles.show_article', name='show_article'),
    url(r'^t/(?P<tag_id>\d+)', 'outside.views.articles.list_articles_by_tag', name='list_articles_by_tag'),
    url(r'^s$', 'outside.views.articles.list_articles_by_search', name='list_articles_by_search'),
)
