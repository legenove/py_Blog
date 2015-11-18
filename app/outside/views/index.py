# coding=utf-8
__author__ = 'mrpp'
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from app.outside.lib.nav_helper import nav_tags_required


@nav_tags_required(with_news=True)
def index_page(request):
    return render(request, "index.html", {'nav_tags': request.nav_tags})

@login_required()
def manage_page(request):
    return render(request, "inner_index.html", {})

