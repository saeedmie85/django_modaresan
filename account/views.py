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
    # model = Post
    def get_queryset(self):
        user = self.request.user
        if user.is_superuser:
            return Post.objects.all()
        else:
            return Post.objects.filter(author=user)

    template_name = "registration\home.html"
