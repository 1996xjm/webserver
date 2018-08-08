# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse

from models import *

import datetime

import time

import urllib

import json

import pandas as pd

from createexcel import createExcel

import wechat



import calendar
from threading import Timer

def loopfunc(msg,starttime):
    if time.strftime('%H:%M')=="17:59":
		sendworkcheckmsg()
    Timer(60, loopfunc, ("90", time.time())).start()

appid = 'wxa78ef8ee14d6f558'
secret = '790edb24393439119b60ad25fd69bdf4'
# Create your views here.
def nihao(request):
	response = HttpResponse("890897765")
	response.status_code = 200
	response.set_cookie('age',34,600)
	response.set_cookie('name','dsafdsaf',600)
	response.write("sdkfhdfd")
	return response
def addTrainee(request):
	name = request.GET['name']
	trainee=TraineeInfor.objects.filter(name=name)
	if trainee.exists():
		print(trainee)
		return HttpResponse("exist")
	else:
		trainee = TraineeInfor()
		trainee.name = name
		trainee.save()                                                    
		return HttpResponse("success")

def deleteTrainee(request):
	name = request.GET['name']
	trainee=TraineeInfor.objects.filter(name=name)
	if trainee.exists():
		trainee[0].delete()
		print(trainee)
		return HttpResponse("success")
	else:
		return HttpResponse("nosuchname")
		
def addAttenceInfor(request):
	name = request.GET['name']
	arr = request.GET['arr']
	dayNum = request.GET['dayNum']
	timestamp = request.GET['timestamp'] 
	print(name,arr,dayNum,timestamp)
	trainee=TraineeInfor.objects.filter(name=name)
	if trainee.exists():
		print(trainee)
		attence = trainee[0].attenceinfor_set.filter(date=datetime.date.fromtimestamp(float(timestamp)))
		if attence.exists():
			attence.update(attenceArr=arr) 
			return HttpResponse("changed")
		else:
			new_attence = trainee[0].attenceinfor_set.create(date=datetime.date.fromtimestamp(float(timestamp)),attenceArr=arr)

			return HttpResponse("success")
	else:
		return HttpResponse("nosuchname")
def gettraineename(request):
	trainee = TraineeInfor.objects.values()
	return JsonResponse(list(trainee), safe=False) 

def getcheckinfor(request):
	name = request.GET['name']
	mytype = request.GET['type']
	dateArr = request.GET['date'].split("-")
	for i in range(len(dateArr)):
		dateArr[i]=int(dateArr[i])
	print(name,mytype,dateArr)
	if name=='所有人':
		if mytype == '按天':
			attence = AttenceInfor.objects.filter(date=datetime.date(dateArr[0],dateArr[1],dateArr[2])).values('attenceArr','trainee__name')
			data_list = list(attence)
			for i in range(len(data_list)):
				
				cui = ChinablueUserInfor.objects.filter(name=data_list[i]['trainee__name']).values()
				if cui.exists():
					data_list[i]['userInfor'] = list(cui)[0]
				else:
					data_list[i]['userInfor'] = ''
					
			return JsonResponse(data_list,safe=False)
		else:
			attence = AttenceInfor.objects.filter(date__year=dateArr[0],date__month=dateArr[1]).values('attenceArr','trainee__name','date')
			return JsonResponse(list(attence),safe=False)
	else:
		if mytype == '按天':
			attence = AttenceInfor.objects.filter(trainee__name=name,date=datetime.date(dateArr[0],dateArr[1],dateArr[2])).values('attenceArr','trainee__name')
			data_list = list(attence)
			for i in range(len(data_list)):
				cui = ChinablueUserInfor.objects.filter(name=data_list[i]['trainee__name']).values()
				if cui.exists():
					data_list[i]['userInfor'] = list(cui)[0]
				else:
					data_list[i]['userInfor'] = ''
					
			return JsonResponse(data_list,safe=False)
		else:
			attence = AttenceInfor.objects.filter(trainee__name=name,date__year=dateArr[0],date__month=dateArr[1]).values('attenceArr','trainee__name','date')
			return JsonResponse(list(attence),safe=False)


def setchinablueuserinfor(request):
	name = request.GET['name']
	userid = request.GET['userid']
	wxInfor = request.GET['wxInfor']
	cui = ChinablueUserInfor()
	cui.name = name
	cui.userid = userid
	cui.wxInfor = wxInfor
	cui.save()
	return HttpResponse('success')


def getopenid(request):
	code = request.GET['code']
	url = 'https://api.weixin.qq.com/sns/jscode2session?appid={}&secret={}&js_code={}&grant_type=authorization_code'.format(appid, secret, code)
	res = urllib.urlopen(url)
	return HttpResponse(res.read())


def findopenid(request):
	openid = request.GET['openid']
	cui = ChinablueUserInfor.objects.filter(userid=openid)
	if cui.exists():
		return JsonResponse(list(cui.values()),safe=False)
	else:
		return HttpResponse('fail')


def getchinablueuser(request):
	cui = ChinablueUserInfor.objects.values('name')
	return JsonResponse(list(cui),safe=False)



def addlunchuser(request):
	name = request.GET['name']
	lui = LunchUserInfor.objects.filter(name=name)
	if lui.exists():
		return HttpResponse("exist")
	else:
		lui = LunchUserInfor()
		lui.name = name
		lui.save()
		return HttpResponse("success")


def addlunchinfor(request):
	dataDict = request.GET["dataDict"]
	dateArr = request.GET["date"].split("-")
	li = LunchInfor.objects.filter(date=datetime.date(int(dateArr[0]),int(dateArr[1]),int(dateArr[2])))
	if li.exists():
		li.update(lunchInforArr=dataDict)
		return HttpResponse("changed")
	else:
		li = LunchInfor()
		li.lunchInforArr = dataDict
		li.date = datetime.date(int(dateArr[0]),int(dateArr[1]),int(dateArr[2]))
		li.save()
		return HttpResponse("success")

def getlunchuser(request):
	lui = LunchUserInfor.objects.values("name")
	return JsonResponse(list(lui),safe=False)

def deletelunchuser(request):
	name = request.GET['name']
	lui = LunchUserInfor.objects.filter(name=name)
	if lui.exists():
		lui[0].delete()
		return HttpResponse("success")
	else:
		return HttpResponse("nosuchname")


def getlunchinfor(request):
	dateArr = [int(i) for i in request.GET['date'].split('-')]
	mytype = request.GET['type']
	if mytype=='按天':
		li = LunchInfor.objects.filter(date=datetime.date(int(dateArr[0]),int(dateArr[1]),int(dateArr[2]))).values('lunchInforArr')
		return JsonResponse(list(li),safe=False)
	elif mytype=='按月':
		
		li = LunchInfor.objects.filter(date__year=dateArr[0],date__month=dateArr[1]).values()
		if li.exists():
			mylist = [json.loads(i['lunchInforArr']) for i in list(li)]
			df = pd.DataFrame(mylist)
			print(df.sum().tolist())
			print(df)
			mydict = {}
			for i in range(len(df.sum().index)):
				mydict[df.sum().index[i]] = df.sum().values[i]
			return JsonResponse(mydict,safe=False)
		else:
			return HttpResponse("nodata")

def getlunchexcel(request):
	dateArr = [int(i) for i in request.GET['date'].split('-')]
	li = LunchInfor.objects.filter(date__year=dateArr[0], date__month=dateArr[1]).values()
	if li.exists():
		li = list(li)
		mylist = []
		for i in range(len(li)):
			new_dict = json.loads(li[i]['lunchInforArr'])
			new_dict['date'] = str(li[i]['date'])
			mylist.append(new_dict)
		createExcel(dateArr[0], dateArr[1], mylist)
		return HttpResponse("https://chifei3d.com/static/lunchexcel/{}-{}.xlsx".format(dateArr[0],dateArr[1]))
	else:
		return HttpResponse("nodata")


def saveformid(request):
	openid = request.GET['openid']
	formid = request.GET['formid']
	mytime = request.GET['time']
	cui = ChinablueUserInfor.objects.filter(userid=openid)
	if cui.exists():
		if formid!="the formId is a mock one":
			cui[0].formidinfor_set.create(formid=formid,time=mytime)
		return HttpResponse("success")
	else:
		return HttpResponse("nosuchopenid")


def sendworkcheckmsg():
	ti = TraineeInfor.objects.values('name')
	for i in list(ti):
		print(i['name'])
		name = i['name']
		cui = ChinablueUserInfor.objects.filter(name=name)[0]
		openid = cui.userid
		formidArr = cui.formidinfor_set.filter()
		if formidArr.exists():
			for i in formidArr:
				mytime = int(i.time)/1000
				formid = i.formid
				if((time.time()-mytime)/86400<7):
					print("this formid is ok")
					wechat.sendworkcheckmsg(openid,formid)
					i.delete()
					break
				else:
					i.delete()


def templatetest(request):
	def showname():
		return "小红"
	return render(request,"index.html",{"var":[12,12,12,34,46,57,67,7]})
Timer(6, loopfunc, ("89", time.time())).start()
