from django.shortcuts import render, get_object_or_404
from .models import Post, Category

# Create your views here.


def post_list(request):
    posts = Post.objects.filter(status="published")
    categories = Category.objects.filter(status=True)
    return render(request, "blog\posts\home.html", 
                    {"posts": posts,
                    'categories':categories
                    }
    )


def post_detail(request, slug):
    post = Post.objects.get(slug=slug, status="published")
    categories = Category.objects.filter(status=True)
    return render(request, "blog\posts\post_detail.html", {"post": post,
    'categories':categories}
    )


def category_list(request, slug):
    category = get_object_or_404(Category, slug=slug)
    posts = category.post_set.filter(status="published")
    return render(
        request, "blog\posts\category_list.html", {"posts": posts, "category": category}
    )
