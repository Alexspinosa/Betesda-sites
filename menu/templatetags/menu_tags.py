# menu/templatetags/menu_tags.py
from django import template
from menu.models import Menu
from contact.models import ContactPage

register = template.Library()


@register.simple_tag
def get_menu(slug):
    try:
        return Menu.objects.get(slug=slug)
    except Menu.DoesNotExist:
        return None


@register.simple_tag
def get_contacto():
    try:
        return ContactPage.objects.live().first()
    except ContactPage.DoesNotExist:
        return None
