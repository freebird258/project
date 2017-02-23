#coding=utf-8
from django.contrib import admin

from django.contrib.auth.models import User
from .models import UserProfile

class ProfileInline(admin.StackedInline):
    model = UserProfile
    verbose_name = 'profile'


class UserAdmin(admin.ModelAdmin):
    inlines = (ProfileInline,)

admin.site.unregister(User) # User是已经注册过的，所以首先需要解绑注册
admin.site.register(User, UserAdmin)
