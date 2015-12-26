# coding=utf-8
__author__ = 'mrpp'
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from app.outside.lib.nav_helper import nav_tags_required
from app.contents.models.article import Article
from django.conf import settings


@nav_tags_required(with_news=True)
def all_page(request):
    """
    登陆后的首页显示所有分类和文章
    """
    return render(request, "all.html", {'nav_tags': request.nav_tags})

def index_page(request):
    """
    公共首页只显示主分类下面的文章
    """
    articles = Article.objects.filter(is_delete=False, category_id=settings.MAIN_CATEGORY_ID).order_by('-id')
    print [x.category_id for x in articles]
    return render(request, "index.html", {'articles': articles})

@login_required()
def manage_page(request):
    return render(request, "inner_index.html", {})

