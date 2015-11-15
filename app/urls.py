from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^$', 'outside.views.index.index_page', name='index_page'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^manage/', 'outside.views.index.manage_page', name='manage_page'),
    url(r'^contents/', include('contents.urls')),

    url(r'^signin/$', 'django.contrib.auth.views.login', {'template_name': 'signin.html'}, name="signin"),
    url(r'^signout/$', 'django.contrib.auth.views.logout_then_login',  name="signout"),
)
