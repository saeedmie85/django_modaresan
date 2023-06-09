from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .mixins import FieldMixin, FormValidMixin, AuthorAccessMixin
from blog.models import Post

# Create your views here.
# @login_required()
# def home(request):
#     return render(request, 'registration/home.html')


class PostList(LoginRequiredMixin, ListView):
    # model = Post
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Post.objects.all()
        else:
            return Post.objects.filter(author=user)

    template_name = "registration\home.html"


class PostCreate(LoginRequiredMixin, FieldMixin, FormValidMixin, CreateView):
    model = Post
    template_name = "registration\post_create_update.html"
    success_url = reverse_lazy("account:post_list")


class PostUpdate(AuthorAccessMixin, FieldMixin, FormValidMixin, UpdateView):
    model = Post
    template_name = "registration\post_create_update.html"
    success_url = reverse_lazy("account:post_list")


class PostDelete(DeleteView):
    model = Post
    uccess_url = reverse_lazy("account:post_list")
