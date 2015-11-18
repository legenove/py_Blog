# coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse
from app.contents.models import Tag
import json


def list_tags(request):
    tags = Tag.objects.filter(is_delete=False)
    return render(request, 'tags/list.html', {'tags': tags})

def add_tag(request):
    title = request.POST.get('title')
    info = Tag.add_tag(title)
    if info['status'] == 'success':
        return HttpResponse(json.dumps({'status': 'success'}), content_type='application/json')
    else:
        return HttpResponse(json.dumps(info), content_type='application/json')

def del_tag(request):
    title = request.POST.get('title')
    info = Tag.del_tag(title)
    if info['status'] == 'success':
        return HttpResponse(json.dumps({'status': 'success'}), content_type='application/json')
    else:
        return HttpResponse(json.dumps(info), content_type='application/json')
