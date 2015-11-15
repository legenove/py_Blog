# coding=utf-8
from django.shortcuts import render
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import json
from contents.models import Tag, ArticleTag


def list_tags(request):
    tags = Tag.objects.all()
    render(request, 'tags/list.html', {'tags': tags})
