# coding=utf-8
from django.db import models


class Article(models.Model):
    SCAN_MODES = ['simple', 'preview', 'full']

    title = models.CharField(max_length=255, verbose_name="标题", default='')
    body = models.TextField(verbose_name='正文')
    is_private = models.BooleanField(verbose_name='是否私密', default=False)

    is_delete = models.BooleanField(verbose_name='是否删除', default=False)
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新时间')

    class Meta:
        app_label = 'contents'

    @property
    def tags(self):
        from app.contents.models.tag import ArticleTag, Tag
        article_tags = ArticleTag.objects.filter(article=self)
        tag_ids = [x.tag_id for x in article_tags]
        return Tag.objects.filter(pk__in=tag_ids).order_by('-count')

    def update_tags(self, tag_ids):
        """
        :param tag_ids:  e.g. [2,4,5]
        :return:
        """
        from app.contents.models.tag import ArticleTag, Tag
        now_ids = [x.id for x in self.tags]
        for tag_id in tag_ids:
            if tag_id not in now_ids:
                ArticleTag(article=self, tag_id=tag_id).save()
        for tag_id in now_ids:
            if tag_id not in tag_ids:
                objs = ArticleTag.objects.filter(article=self, tag_id=tag_id)
                tag = Tag.objects.get(pk=tag_id)
                tag.count -= len(objs)
                if tag.count < 0:
                    tag.count = 0
                tag.save()
                objs.delete()



    # def add_tag(self, tag_title):
    #     from app.contents.models.tag import ArticleTag, Tag
    #     tags = Tag.objects.filter(title=tag_title)
    #     if tags:
    #         tag = tags[0]
    #         if ArticleTag.objects.filter(article=self, tag=tag):
    #             return {'status': 'failed', 'info': 'exist', 'obj': None}
    #         else:
    #             obj = ArticleTag(article=self, tag=tag)
    #             return {'status': 'success', 'info': '', 'obj': obj}
    #     else:
    #         info = Tag.add_tag(tag_title)
    #         # TODO: add exception
    #         tag = info['obj']
    #         obj = ArticleTag(article=self, tag=tag)
    #         return {'status': 'success', 'info': '', 'obj': obj}
    #
    # def del_tag(self, tag_title):
    #     from app.contents.models.tag import ArticleTag, Tag
    #     tags = Tag.objects.filter(title=tag_title)
    #     if tags:
    #         tag_ids = [x.id for x in tags]
    #         ArticleTag.objects.filter(article=self, tag_id__in=tag_ids).delete()
    #         return {'status': 'success', 'info': ''}
    #     else:
    #         return {'status': 'success', 'info': 'not exist'}

