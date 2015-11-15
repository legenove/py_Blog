# coding=utf-8
from django.db import models
from contents.models.article import Article


class Tag(models.Model):
    title = models.CharField(verbose_name='名称', max_length=20, default='')
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        app_label = 'contents'


class ArticleTag(models.Model):
    article = models.ForeignKey(Article)
    tag = models.ForeignKey(Tag)

    class Meta:
        app_label = 'contents'
