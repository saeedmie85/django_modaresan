from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Post, Category
from django.views.generic import ListView, DetailView
from django.contrib.auth.models import User

# Create your views here.


def post_list(request, number=1):
    posts_list = Post.objects.filter(status="published")
    paginator = Paginator(posts_list, 2)
    posts = paginator.get_page(number)
    return render(request, "blog\posts\home.html", {"posts": posts})


# class PostList(ListView):
#     model = Post
#     # queryset = Post.objects.filter(status="published")
#     context_object_name = "posts"
#     paginate_by = 1
#     template_name = "blog\posts\home.html"


# def post_detail(request, slug):
#     post = Post.objects.get(slug=slug, status="published")
#     return render(request, "blog\posts\post_detail.html", {"post": post})


class PostDetail(DetailView):
    def get_object(self):
        slug = self.kwargs.get("slug")
        return get_object_or_404(Post, slug=slug, status="published")

    context_object_name = "post"
    template_name = "blog\posts\post_detail.html"


def category_list(request, slug, number=1):
    category = get_object_or_404(Category, slug=slug)
    posts_list = category.post_set.filter(status="published")
    paginator = Paginator(posts_list, 2)
    posts = paginator.get_page(number)
    return render(
        request, "blog\posts\category_list.html", {"posts": posts, "category": category}
    )


def author_list(request, user_name, number=1):
    author = get_object_or_404(User, username=user_name)
    posts_list = author.blog_post.filter(status="published")
    paginator = Paginator(posts_list, 2)
    posts = paginator.get_page(number)
    return render(
        request, "blog/posts/author_list.html", {"posts": posts, "author": author}
    )
