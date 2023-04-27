from django.shortcuts import render
from .models import Post

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(status="published")
    return render(request, "blog\posts\home.html", {"posts": posts})


def post_detail(request, slug):
    post = Post.objects.get(slug=slug, status="published")
    return render(request, "blog\posts\detail_post.html", {"post": post})
