from django import template
from django.utils.safestring import mark_safe
import markdown
from taggit.models import Tag

from ..models import Post

register = template.Library()


@register.simple_tag
def total_posts():
    return Post.published.count()


@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    return {'latest_posts': Post.published.order_by('-publish')[:count]}


@register.inclusion_tag('blog/post/tags.html')
def tags():
    return {'tags': Tag.objects.all()}


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
