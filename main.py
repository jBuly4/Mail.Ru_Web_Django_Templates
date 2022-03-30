""" Solutions """
""" views.py """

from django.shortcuts import render

def echo(request):
    context = {
        'get': request.GET,
        'post': request.POST,
        'meta': request.META
    }
    return render(request, 'echo.html', context=context)


def filters(request):
    return render(request, 'filters.html', context={
        'a': request.GET.get('a', 1),
        'b': request.GET.get('b', 1)
    })


def extend(request):
    return render(request, 'extend.html', context={
        'a': request.GET.get('a'),
        'b': request.GET.get('b')
    })

""" echo.html """
<!--echo.html-->

{% for k, v in get.items %}
    get {{ k }}: {{ v }}
{% endfor %}

{% for k, v in post.items %}
    post {{ k }}: {{ v }}
{% endfor %}

{% if meta.HTTP_X_PRINT_STATEMENT %}
    statement is {{ meta.HTTP_X_PRINT_STATEMENT }}
{% else %}
    statement is empty
{% endif %}


""" extras.py """
# extras.py

from django import template

register = template.Library()


@register.filter
def inc(value, arg):
    return int(value) + int(arg)


@register.simple_tag
def division(a, b, to_int=False):
    res = int(a) / int(b)
    return int(res) if to_int else res


""" extend.html """
<!--extend.html-->

{% extends "base.html" %}

{% block block_a %}
    {{ block.super }} {{ a }}
{% endblock %}

{% block block_b %}
    {{ block.super }} {{ b }}
{% endblock %}