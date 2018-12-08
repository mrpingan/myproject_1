# coding:utf-8
__author__ = "ping"
__date__ = "2018/12/6 23:34"
from django import forms

class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()