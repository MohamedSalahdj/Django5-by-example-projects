from django import template
from django.db.models import Count

from ..models import Post

register = template.Library()


# Custom tag by using simple_tag 
@register.simple_tag
def total_posts():
    return Post.published.count()


# Custom tag by inclusion_tag
@register.inclusion_tag('blog/post/lates_posts.html')
def show_latest_posts(count=5):
    lates_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': lates_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(
        total_comments=Count('comments')
    ).order_by('-total_comments')[:count]