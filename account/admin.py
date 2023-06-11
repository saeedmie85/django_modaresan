from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

# Register your models here.

admin.site.register(User, UserAdmin)
UserAdmin.fieldsets += (
    (
        "فیلدهای اختصاصی",
        {
            "fields": ("is_author", "special_user"),
        },
    ),
)

UserAdmin.list_display = (
    "username",
    "is_author",
    "email",
    "first_name",
    "last_name",
    "is_staff",
    "is_special_user",
)
