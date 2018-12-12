# coding:utf-8
__author__ = "ping"
__date__ = "2018/12/1 22:01"

from .base import *

DEBUG = True

INSTALLED_APPS.append("debug_toolbar.apps.DebugToolbarConfig",)

MIDDLEWARE.append("debug_toolbar.middleware.DebugToolbarMiddleware",)

INTERNAL_IPS = ('127.0.0.1',)
