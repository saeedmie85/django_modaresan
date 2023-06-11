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
        "is_special",
    ]
    list_filter = ["publish", "status", "is_special"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ["title"]}

    actions = ["make_published", "make_draft"]

    def make_published(self, request, queryset):
        row_updated = queryset.update(status="published")
        if row_updated == 1:
            message_bit = "منتشر شد"
        else:
            message_bit = "منتشر شدند"
        self.message_user(request, f"{row_updated} مقاله {message_bit}")

    make_published.short_description = "تغییر به منتشر شده"

    def make_draft(self, request, queryset):
        row_updated = queryset.update(status="draft")
        if row_updated == 1:
            message_bit = "پیش نویس شد"
        else:
            message_bit = "پیش نویس شدند"
        self.message_user(request, f"{row_updated} مقاله {message_bit}")

    make_draft.short_description = "تغییر به پیش نویس"

    def get_category(self, obj):
        return "، ".join([cat.title for cat in obj.category.all()])

    get_category.short_description = "دسته بندی"


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "status", "position"]
    prepopulated_fields = {"slug": ["title"]}
