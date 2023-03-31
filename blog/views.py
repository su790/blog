from django.shortcuts import render
from .models import Post
from django.http import Http404


def post_detail(request, id):
    try:
        post = Post.published.get(id=id)
    except:
        raise Http404("No post found")

    return render(request, "blog/post/detail.html", {'post': post})


def post_list(request):
    post = Post.published.all()
    return render(request, "blog/post/list.html", {'post': post})
