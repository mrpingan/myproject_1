# coding:utf-8
__author__ = "ping"
__date__ = "2018/12/2 14:38"
from datetime import timedelta
from collections import OrderedDict
from django.shortcuts import render

from apps.product.models import Product
from apps.product.form import ProductForm

from utils.time_utils import date,str2date

def index_view(request,days=4):
    last_dt = request.GET.get('last_dt',None)
    if not last_dt:
        product = OrderedDict()
        for i in range(days):
            _date = date(-i).date()
            product[_date.strftime('%Y-%m-%d')] = Product.objects.filter(public=True,created_at__contains=_date).order_by('-created_at')
        context = {
            'products':product,
            'form':ProductForm
        }
        return render(request,'index.html',context)

    else:   #渲染前一天数据
        print(last_dt)
        _date = str2date(last_dt) + timedelta(-1)

        context = {
            'date':_date.strftime('%Y-%m-%d'),
            'products':Product.objects.filter(public=True,created_at__contains=_date).order_by('-vote_count','-created_at')
        }

        return render(request,'components/products.tpl.html',context)