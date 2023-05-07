from django.urls import path
from .views import post_list, post_detail, category_list

app_name = "blog"

urlpatterns = [
    path("", post_list, name="post_list"),
    path("page/<int:number>", post_list, name="post_list"),
    path("post/<slug:slug>", post_detail, name="post_detail"),
    path("category/<slug:slug>", category_list, name="category_list"),
]
