# coding=utf-8
from django.db import models
from article import Article


class Tag(models.Model):
    title = models.CharField(verbose_name='名称', max_length=20, default='', db_index=True)
    count = models.IntegerField(verbose_name='引用次数', default=0)
    is_delete = models.BooleanField(verbose_name='是否删除', default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        app_label = 'contents'

    @classmethod
    def add_tag(cls, title):
        if Tag.objects.filter(title=title):
            return {'status': 'failed', 'info': 'exist', 'obj': None}
        tag = Tag(title=title, is_delete=False, count=0)
        tag.save()
        return {'status': 'success', 'info': '', 'obj': tag}

    @classmethod
    def del_tag(cls, title):
        tags = Tag.objects.filter(title=title)
        if not tags:
            return {'status': 'success', 'info': 'not exist'}
        tag_ids = [x.id for x in tags]
        ArticleTag.objects.filter(tag_id__in=tag_ids).delete()
        tags.update(is_delete=True, count=0)
        return {'status': 'success', 'info': ''}

    def news(self, include_private=False, count=4):
        from app.contents.models import ArticleTag
        article_ids = [x.article_id for x in ArticleTag.objects.filter(tag=self)]
        articles = Article.objects.filter(id__in=article_ids)
        if not include_private:
            articles = articles.filter(is_private=False)
        return articles.order_by('-id')[:count]


class ArticleTag(models.Model):
    article = models.ForeignKey(Article)
    tag = models.ForeignKey(Tag)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')

    class Meta:
        app_label = 'contents'
