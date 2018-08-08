# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import *

# Register your models here.

class AttenceInforAdmin(admin.ModelAdmin):
	list_display = ['trainee','date','attenceArr']
	list_filter = ['trainee']


class LunchInforAdmin(admin.ModelAdmin):
	list_display = ['date','lunchInforArr']


class FormIdInforAdmin(admin.ModelAdmin):
	list_display = ['time','formid','chinablueuser']


admin.site.register(TraineeInfor)
admin.site.register(AttenceInfor,AttenceInforAdmin)
admin.site.register(ChinablueUserInfor)
admin.site.register(LunchUserInfor)
admin.site.register(LunchInfor,LunchInforAdmin)
admin.site.register(FormIdInfor,FormIdInforAdmin)
