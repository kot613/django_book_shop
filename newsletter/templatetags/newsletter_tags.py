from django import template
from newsletter.forms import EmailForm

register = template.Library()


@register.inclusion_tag('newsletter/tags/form.html')
def newsletter_form():
    return {'newsletter_form': EmailForm()}
