# coding=utf-8
from django.conf import settings
from app.contents.models import Tag
def nav_tags_required(with_news=False):
    def f(func):
        def handler(*args, **kwargs):
            request = args[0]
            tag_titles = [x[0] for x in settings.TAG_IN_INDEX]
            # tags = Tag.objects.filter(title__in=[x.title for x in settings.TAG_IN_INDEX])
            tags = Tag.objects.filter(title__in=tag_titles)
            tag_hash = {}
            for tag in tags:
                tag_hash[tag.title] = tag
            tags_res = []
            for tag_config in settings.TAG_IN_INDEX:
                tag_title, tag_alias = tag_config
                tag = tag_hash.get(tag_title, None)
                if tag:
                    tag.title_alias = tag_alias
                    if with_news:
                        include_private = request.user.is_authenticated()
                        tag.news = tag.news(include_private=include_private)
                    tags_res.append(tag)
            request.nav_tags = tags_res
            # func(args, kwargs)
            return func(*args, **kwargs)
        return handler
    return f

