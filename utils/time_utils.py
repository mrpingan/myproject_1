# coding:utf-8
__author__ = "ping"
__date__ = "2018/12/2 16:59"

from datetime import datetime,timedelta

def date(delta=-1):
    return datetime.today() + timedelta(delta)

def str2date(dt,ft="%Y-%m-%d"):
    return datetime.strptime(dt,ft).date()