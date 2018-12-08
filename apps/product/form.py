# coding:utf-8
__author__ = "ping"
__date__ = "2018/12/8 22:33"
from django import forms
from apps.product.models import Product

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('name','url','digest')

