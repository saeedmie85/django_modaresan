from django.contrib import admin
from .models import Post

# Register your models here.
# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "author", "jalali_publish", "status"]
    list_filter = ["publish", "status"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ["title"]}


