from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from extensions.utils import jalali_convertor


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=250, verbose_name="عنوان دسته بندی")
    slug = models.SlugField(max_length=250, verbose_name="آدرس")
    status = models.BooleanField(default=True, verbose_name="آیا نمایش داده شود؟")
    position = models.IntegerField(verbose_name="موقعیت نمایش")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"
        ordering = ("-position",)

    def __str__(self):
        return self.title


class Post(models.Model):
    STATUS_CHOICES = (("published", "منتشر شده"), ("draft", "پیش نویس"))
    title = models.CharField(max_length=200, verbose_name="عنوان")
    category = models.ManyToManyField(Category, verbose_name="دسته بندی")
    thumbnail = models.ImageField(
        upload_to="images", null=True, blank=True, verbose_name="تصویر"
    )
    slug = models.SlugField(max_length=250, verbose_name="آدرس")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_post", verbose_name="نویسنده"
    )
    body = models.TextField(null=True, blank=True, verbose_name="محتوی")
    status = models.CharField(
        max_length=15, choices=STATUS_CHOICES, default="draft", verbose_name="وضعیت"
    )
    created = models.DateTimeField(
        auto_now_add=timezone.now, verbose_name="تاریخ ایجاد"
    )
    updated = models.DateTimeField(
        auto_now=timezone.now, verbose_name="تاریخ بروز رسانی"
    )
    publish = models.DateTimeField(default=timezone.now, verbose_name="تاریخ انتشار")

    def jalali_publish(self):
        return jalali_convertor(self.publish)

    jalali_publish.short_description = "تاریخ انتشار"

    class Meta:
        ordering = ("status", "-publish")
        verbose_name = "پست"
        verbose_name_plural = "پست ها"

    def __str__(self):
        return self.title
