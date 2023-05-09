from django.urls import path, re_path
from .views import post_list, post_detail, category_list

app_name = "blog"

urlpatterns = [
    path("", post_list, name="post_list"),
    path("post/page/<int:number>", post_list, name="post_list"),
    re_path(r"post/(?P<slug>[-\w]+)", post_detail, name="post_detail"),
    path("category/<slug:slug>", category_list, name="category_list"),
    path("category/<slug:slug>/page/<int:number>", category_list, name="category_list"),
]
