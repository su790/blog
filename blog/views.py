from django.shortcuts import render
from .models import Post
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage

def post_detail(request, year,month,day,post):
    try:
        post = Post.published.get(slug=post,
                                  publish__year=year,
                                  publish__month=month,
                                  publish__day=day)
    except:
        raise Http404("No post found")

    return render(request, "blog/post/detail.html", {'post': post})


def post_list(request):
    posts = Post.published.all()
    paginator = Paginator(posts,3)
    page_number = request.GET.get('page')
    post = paginator.get_page(page_number)

        # try:
        #     post = paginator.get_page(page_number)
        # except EmptyPage:
        #     post = paginator.get_page(paginator.num_pages)
    return render(request, "blog/post/list.html", {'post': post})
