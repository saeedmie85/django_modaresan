from django import template
from ..models import Category

register = template.Library()

@register.inclusion_tag('blog/posts/partials/category.html')
def category_navbar():
    return {'categories': Category.objects.filter(status=True)}