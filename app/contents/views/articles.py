# coding=utf-8
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from app.contents.models import Article


def list_articles(request):
    articles = Article.objects.all().order_by('-id')
    return render(request, "articles/list.html", {'articles': articles})
    # return render(request, "articles/article_1.html", {'articles': articles})


@login_required()
def new_article(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('title', '')
        article.body = request.POST.get('body', '')
        article.save()
        return HttpResponseRedirect(reverse('list_articles'))
    else:
        article = Article()
    return render(request, "articles/new.html", {'article': article})


@login_required()
def edit_article(request, id):
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    if request.method == 'POST':
        article.title = request.POST.get('title', '')
        article.body = request.POST.get('body', '')
        article.save()
        return HttpResponseRedirect(reverse('list_articles'))
    else:
        return render(request, "articles/edit.html", {'article': article})


def delete_article(request, id):
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    article.delete()
    return HttpResponseRedirect(reverse('list_articles'))

