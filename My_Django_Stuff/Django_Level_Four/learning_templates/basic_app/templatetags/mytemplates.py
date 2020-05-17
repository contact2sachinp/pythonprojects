from django import template

register = template.Library()

@register.filter(name="cutCustom")
def cut(value, str):
    return value.replace(str, '')

#register.filter('cutCustom', cut)