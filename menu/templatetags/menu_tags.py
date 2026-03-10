# menu/templatetags/menu_tags.py
from django import template
from menu.models import Menu

register = template.Library()


@register.simple_tag
def get_menu(slug):
    try:
        return Menu.objects.get(slug=slug)
    except Menu.DoesNotExist:
        return None
