from django.contrib import admin
from django.utils.safestring import mark_safe

from apps.account.models import MyUser,GithubUser
from apps.product.models import Product


class ProductInline(admin.TabularInline):
    model = Product
    list_display = ('pid','name','digest',"user","public",)

class MyUserAdmin(admin.ModelAdmin):
    def avatar_view(self,obj):
        html_tag = """<div style="width:100px;"><img width=18px src='%s'></div>""" % obj.avatar
        return mark_safe(html_tag)
    avatar_view.short_description = "头像"

    inlines = [ProductInline]
    list_display = ('uid','username','nickname','avatar_view','is_active','is_staff',)


class GithubUserAdmin(admin.ModelAdmin):
    def avatar_view(self,obj):
        html_tag = """<div style="width:100px;"><img width=18px src='%s'></div>""" % obj.avatar_url
        return mark_safe(html_tag)
    avatar_view.short_description = "头像"
    list_display = ('user','avatar_view')

admin.site.register(MyUser,MyUserAdmin)
admin.site.register(GithubUser,GithubUserAdmin)
