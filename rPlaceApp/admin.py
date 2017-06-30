# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from rPlaceApp.models import CanPlace
# Register your models here.

# class CanPlaceInLine(admin.StackedInline) :
# 	model = CanPlace
# 	can_delete = False
# 	verbose_name_plural = 'can_place'

# class UserAdmin(BaseUserAdmin) :
# 	inlines = (CanPlaceInLine,)

# admin.site.unregister(User)
# admin.site.register(User, UserAdmin)