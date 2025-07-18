from django.shortcuts import render
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.views.generic import ListView

from .models import Post


def post_list(request):
    posts = Post.published.all()

    page_number = request.GET.get("page", 1)
    paginator = Paginator(posts, 5)
    
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'blog/post/list.html', {'posts': posts})


class PostListView(ListView):
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'


def post_details(requst, year, month, day, post):
    post = get_object_or_404(
        Post.published, slug=post,
        publish__year=year, 
        publish__month=month, 
        publish__day=day
    )
    return render(requst, 'blog/post/detail.html', {'post': post})