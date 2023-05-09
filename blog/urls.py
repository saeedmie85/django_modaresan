from django.urls import path, re_path
from .views import  category_list, PostList, PostDetail

app_name = "blog"

urlpatterns = [
    # path("", post_list, name="post_list"),
    path("", PostList.as_view(), name="post_list"),
    path("post/page/<int:number>", PostList.as_view(), name="post_list"),
    # path("post/page/<int:number>", post_list, name="post_list"),
    # re_path(r"post/(?P<slug>[-\w]+)", post_detail, name="post_detail"),
    re_path(r"post/(?P<slug>[-\w]+)", PostDetail.as_view(), name="post_detail"),
    path("category/<slug:slug>", category_list, name="category_list"),
    path("category/<slug:slug>/page/<int:number>", category_list, name="category_list"),
]
