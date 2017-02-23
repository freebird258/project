#coding=utf-8
from django.db import models
from django.contrib import admin

from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User) # 关联自带的User结构
    desc = models.TextField(blank=True, null=True)

admin.site.register(UserProfile)

