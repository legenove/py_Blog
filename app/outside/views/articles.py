# coding=utf-8
__author__ = 'mrpp'
from django.shortcuts import render
from django.http import HttpResponseBadRequest
from app.contents.models import Article, Tag, ArticleTag
from app.outside.lib.nav_helper import nav_tags_required

@nav_tags_required()
def show_article(request, article_id):
    try:
        article = Article.objects.get(pk=article_id)
    except Tag.DoesNotExist:
        return HttpResponseBadRequest('invalid id')
    return render(request, "outside_articles/show.html", {'article': article, 'nav_tags': request.nav_tags})

@nav_tags_required()
def list_articles_by_tag(request, tag_id):
    try:
        tag = Tag.objects.get(pk=tag_id)
    except Tag.DoesNotExist:
        return HttpResponseBadRequest('invalid id')
    article_ids = [x.article_id for x in ArticleTag.objects.filter(tag=tag)]
    articles = Article.objects.filter(id__in=article_ids)
    return render(request, "outside_articles/list_by_tag.html",
                  {'articles': articles, 'tag': tag, 'nav_tags': request.nav_tags})


@nav_tags_required()
def list_articles_by_search(request):
    keyword = request.GET.get('keyword', '')
    articles = Article.objects.filter(title__contains=keyword)
    return render(request, "outside_articles/list_by_search.html",
                  {'articles': articles, 'keyword': keyword, 'nav_tags': request.nav_tags})

