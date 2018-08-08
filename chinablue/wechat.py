# coding=utf-8

import urllib
import json
import requests
import datetime

access_token = ""
appid = 'wxa78ef8ee14d6f558'
secret = '790edb24393439119b60ad25fd69bdf4'

def getAccessToken():
    url = "https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={}&secret={}".format(appid,secret)
    res = urllib.urlopen(url).read()
    res = json.loads(res)
    global access_token
    access_token = res['access_token']
    return res['access_token']

getAccessToken()

def sendworkcheckmsg(openid,formid):
    url = 'https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token={}'.format(access_token)
    parmas = {
  "touser":openid,
  "template_id": "7lolvrloIN8zqjFGbvM8gxbrBCGr-9vVVOmSUBZla4s",
  "page": "pages/chinablue/chinablue",
  "form_id": formid,
  "data": {
      "keyword1": {
          "value": "智渔实习生考勤登记"
      },
      "keyword2": {
          "value": str(datetime.date.today())
      }
  },
  "emphasis_keyword":"抓紧时间！！！"
    }


    res = requests.post(url, json=parmas, timeout=3, verify=False).text
    res = json.loads(res)
    if res['errcode']!=0:
        url = 'https://api.weixin.qq.com/cgi-bin/message/wxopen/template/send?access_token={}'.format(getAccessToken())
        requests.post(url, json=parmas, timeout=3, verify=False).text



