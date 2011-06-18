from django import template

register = template.Library()

@register.inclusion_tag('list_event.html')
def list_event(event):
    return {'event': event}

