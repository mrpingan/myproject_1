# coding:utf-8
__author__ = "ping"
__date__ = "2018/12/9 18:11"

from django import template

from apps.product.models import ProductVote

register = template.Library()

@register.inclusion_tag('tags/vote_button.html',takes_context=True)
def vote_button(context,product):
    user = context['user']
    if user.is_authenticated:
        result = {
            'voted':ProductVote.voted(user,product),
            'pid':product.pid,
            'vote_count':product.vote_count
        }

        return result

    return {'vote':False,'pid':product.pid,'vote_count':product.vote_count}


