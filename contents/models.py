# coding=utf-8
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="标题", default='')
    body = models.TextField(verbose_name='正文')

    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    # tags

# class Tag(models.Model):
