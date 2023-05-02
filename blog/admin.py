from django.contrib import admin
from .models import Post, Category

# Register your models here.
# admin.site.register(Post)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "slug",
        "get_category",
        "author",
        "jalali_publish",
        "status",
    ]
    list_filter = ["publish", "status"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ["title"]}

    def get_category(self, obj):
        return "، ".join([cat.title for cat in obj.category.all()])

    get_category.short_description = "دسته بندی"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "status", "position"]
    prepopulated_fields = {"slug": ["title"]}
