"""myproject_1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from apps.views import index_view
from apps.account.views import login_view,logout_view,auth_github_view,auth_github_callback_view
from apps.product.views import new_product_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index_view,name="index"),
    path('login/',login_view,name='login'),
    path('logout/',logout_view,name='logout'),
    path('auth/github/',auth_github_view,name='auth_github'),
    path('auth/github/callback',auth_github_callback_view,name='auth_github_callback'),

    path('product/new/',new_product_view,name='new_product'),
]
