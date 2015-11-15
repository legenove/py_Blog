# coding=utf-8
__author__ = 'mrpp'
from django.shortcuts import render
from django.contrib.auth.decorators import login_required


def index_page(request):
    return render(request, "index.html", {})

@login_required()
def manage_page(request):
    return render(request, "inner_index.html", {})

