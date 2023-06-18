from django.http import Http404
from blog.models import Post
from django.shortcuts import get_object_or_404


class FieldMixin:
    def dispatch(self, request, *args, **kwargs):
        if self.request.user.is_superuser:
            self.fields = [
                "title",
                "is_special",
                "slug",
                "category",
                "thumbnail",
                "body",
                "author",
                "status",
            ]
        else:
            self.fields = [
                "title",
                "is_special",
                "slug",
                "category",
                "thumbnail",
                "body",
            ]

        return super().dispatch(request, *args, **kwargs)


class FormValidMixin:
    def form_valid(self, form):
        if self.request.user.is_superuser:
            form.save()
        else:
            self.obj = form.save(commit=False)
            self.obj.author = self.request.user
            self.obj.status = "draft"
        return super().form_valid(form)


class AuthorAccessMixin:
    def dispatch(self, request, pk, *args, **kwargs):
        post = get_object_or_404(Post, pk=pk)
        if request.user.is_superuser or post.author == request.user:
            return super().dispatch(request, *args, **kwargs)
        else:
            raise Http404("دسترسی غیر مجاز")
