from django import template

register = template.Library()

@register.simple_tag
def set_showActionSheet(value):
    return value