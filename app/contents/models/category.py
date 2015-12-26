# coding=utf-8
from django.db import models


class Category(models.Model):
    title = models.CharField(verbose_name='名称', max_length=20, default='', db_index=True)
    count = models.IntegerField(verbose_name='引用次数', default=0)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        app_label = 'contents'

