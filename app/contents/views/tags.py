# coding=utf-8
from django.shortcuts import render

from app.contents.models import Tag


def list_tags(request):
    tags = Tag.objects.all()
    render(request, 'tags/list.html', {'tags': tags})
