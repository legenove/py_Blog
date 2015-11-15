# coding=utf-8
from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=255, verbose_name="标题", default='')
    body = models.TextField(verbose_name='正文')
    is_private = models.BooleanField(verbose_name='是否私密', default=False)

    is_delete = models.BooleanField(verbose_name='是否删除', default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        app_label = 'contents'

