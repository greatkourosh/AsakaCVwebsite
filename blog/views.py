from django.utils import timezone

from django.shortcuts import get_list_or_404, render, get_object_or_404

from blog.models import Post


# Create your views here.


def blog(request):

    # posts = get_object_or_404(Post, status=1)
    posts = get_list_or_404(Post, status=1)
    contex = {'posts': posts}
    return render(request, 'blog/blog.html', contex)


def single_blog(request, post_id):

    post = get_object_or_404(Post, pk=post_id)
    post.count_views += 1
    post.save()
    contex = {'post': post}
    return render(request, 'blog/single-blog.html', contex)
