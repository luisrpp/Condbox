from django import template

register = template.Library()


@register.simple_tag
def active(request, pattern):
    if request.path.startswith(pattern):
        return 'active'
    return ''


@register.simple_tag
def re_active(request, pattern):
    import re
    if re.search(pattern, request.path):
        return 'active'
    return ''
