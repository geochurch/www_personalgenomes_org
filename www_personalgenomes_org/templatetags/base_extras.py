from django.template import Library

register = Library()

@register.filter
def split_on_space(string):
    return string.split(' ')
