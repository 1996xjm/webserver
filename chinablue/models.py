# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class TraineeInfor(models.Model):
	name = models.CharField(max_length=20)
	openid = models.CharField(max_length=60,null=True)
	wxInfor = models.CharField(max_length=400,null=True)
	def __str__(self):
		return self.name.encode("utf-8")

class AttenceInfor(models.Model):
	date = models.DateField()
	attenceArr = models.CharField(max_length=160)
	trainee = models.ForeignKey(TraineeInfor)
	def __str__(self):
		return self.attenceArr.encode("utf-8")

class ChinablueUserInfor(models.Model):
	name = models.CharField(max_length=200)
	userid = models.CharField(max_length=200,null=True)
	wxInfor = models.CharField(max_length=400,null=True)
	def __str__(self):
		return self.name.encode("utf-8")




class LunchUserInfor(models.Model):
	name = models.CharField(max_length=60)
	def __str__(self):
		return self.name.encode("utf-8")



class LunchInfor(models.Model):
	date = models.DateField()
	lunchInforArr = models.CharField(max_length=600)
	def __str__(self):
		return self.lunchInforArr.encode("utf-8")



class FormIdInfor(models.Model):
	time = models.CharField(max_length=100)
	formid = models.CharField(max_length=100)
	chinablueuser = models.ForeignKey(ChinablueUserInfor)
	def __str__(self):
		return self.formid.encode("utf-8")
