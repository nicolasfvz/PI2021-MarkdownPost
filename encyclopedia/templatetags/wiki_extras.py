import markdown

from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def convert_markdown(value):
    a = markdown.markdown(value)
    new = a.replace("<code>", "<pre>")
    a = new.replace("</code>", "</pre>")
    return a