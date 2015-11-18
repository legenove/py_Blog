# coding=utf-8
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from app.contents.models import Article


def list_articles(request):
    articles = Article.objects.filter(is_delete=False).order_by('-id')
    return render(request, "articles/list.html", {'articles': articles})
    # return render(request, "articles/article_1.html", {'articles': articles})


@login_required()
def new_article(request):
    if request.method == 'POST':
        article = Article()
        article.title = request.POST.get('title', '')
        article.body = request.POST.get('body', '')
        article.is_private = request.POST.get('is_private', 'False') == 'True'
        article.save()
        return HttpResponseRedirect(reverse('list_articles'))
    else:
        article = Article()
        from app.contents.models.tag import Tag
        all_tags = Tag.objects.filter(is_delete=False)
    return render(request, "articles/new.html", {'article': article, 'tags': [], 'all_tags': all_tags})


@login_required()
def edit_article(request, id):
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    if request.method == 'POST':
        article.title = request.POST.get('title', '')
        article.body = request.POST.get('body', '')
        article.is_private = request.POST.get('is_private', 'False') == 'True'
        article.save()
        tag_ids = request.POST.get('tags', '').split(';')
        article.update_tags([int(x) for x in tag_ids])
        return HttpResponseRedirect(reverse('list_articles'))
    else:
        article_tags = article.tags
        article_tag_ids = ';'.join([str(x.id) for x in article_tags])
        # article_tag_titles = ';'.join([x.title for x in article_tags])
        from app.contents.models.tag import Tag
        all_tags = Tag.objects.filter(is_delete=False)
        # for i, x in enumerate(all_tags):
        #     x.selected = x.id in article_tag_ids
        return render(request, "articles/edit.html",
                      {'article': article, 'tags': article_tags, 'all_tags': all_tags,
                       'article_tag_ids': article_tag_ids,
                      })


def delete_article(request, id):
    try:
        article = Article.objects.get(pk=id)
    except Article.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    article.update(is_delete=False)
    return HttpResponseRedirect(reverse('list_articles'))

