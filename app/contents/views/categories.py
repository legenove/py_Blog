# coding=utf-8
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

from app.contents.models import Category

def list_categories(request):
    categories = Category.objects.filter(is_delete=False).order_by('-id')
    return render(request, "categories/list.html", {'categories': categories})

@login_required()
def new_category(request):
    if request.method == 'POST':
        category = Category()
        category.title = request.POST.get('title', '')
        category.is_delete = False
        category.save()
        return HttpResponseRedirect(reverse('list_categories'))
    else:
        category = Category()
    return render(request, "categories/new.html", {'category': category, })

@login_required()
def edit_category(request, id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    if request.method == 'POST':
        category.title = request.POST.get('title', '')
        category.save()
        return HttpResponseRedirect(reverse('list_categories'))
    else:
        return render(request, "categories/edit.html", {'category': category, })

@login_required()
def delete_article(request, id):
    try:
        category = Category.objects.get(pk=id)
    except Category.DoesNotExist:
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    category.update(is_delete=False)
    return HttpResponseRedirect(reverse('list_articles'))

