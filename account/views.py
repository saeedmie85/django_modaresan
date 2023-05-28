from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from blog.models import Post

# Create your views here.
# @login_required()
# def home(request):
#     return render(request, 'registration/home.html')


class PostList(LoginRequiredMixin, ListView):
    model = Post
    template_name = "registration\home.html"
