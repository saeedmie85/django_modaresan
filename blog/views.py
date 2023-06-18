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


from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_str
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.contrib.auth.models import User
from django.core.mail import EmailMessage


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            mail_subject = "Activate your blog account."
            message = render_to_string(
                "blog/posts/acc_active_email.html",
                {
                    "user": user,
                    "domain": current_site.domain,
                    "uid": urlsafe_base64_encode(force_bytes(user.pk)),
                    "token": account_activation_token.make_token(user),
                },
            )
            to_email = form.cleaned_data.get("email")
            email = EmailMessage(mail_subject, message, to=[to_email])
            email.send()
            return HttpResponse(
                "Please confirm your email address to complete the registration"
            )
    else:
        form = SignupForm()
    return render(request, "blog/posts/signup.html", {"form": form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        login(request, user)
        # return redirect('home')
        return HttpResponse(
            "Thank you for your email confirmation. Now you can login your account."
        )
    else:
        return HttpResponse("Activation link is invalid!")
