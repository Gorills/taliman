from django import template
from contact.forms import ContactForm, RestContactsForm, FullContactsForm

register = template.Library()


@register.inclusion_tag('contact/tags/form.html')
def contact_form():
    return {'contact_form': ContactForm()}


@register.inclusion_tag('contact/tags/rest_form.html')
def rest_form():
    return {'rest_form': RestContactsForm()}

@register.inclusion_tag('contact/tags/full_form.html')
def full_form():
    return {'full_form': FullContactsForm()}
