from django.template import Library
from djangomako.shortcuts import render_to_response

register = Library()

@register.simple_tag(takes_context=True)
def include_mako_template(context, template):
    context_dict = {}
    for c in context:
        context_dict.update(c)
    return render_to_response(template, context_dict).content
