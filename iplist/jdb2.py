# -*- coding: utf-8 -*-
"""
Created on Sun Sep 18 14:16:22 2016

@author: lenovo
"""

import urllib
import urllib2
import time
import datetime
import sys, os, re, urlparse  
import smtplib  
import traceback  
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart  


def sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password):  
    ''''' 
    @subject:邮件主题 
    @msg:邮件内容 
    @toaddrs:收信人的邮箱地址 
    @fromaddr:发信人的邮箱地址 
    @smtpaddr:smtp服务地址，可以在邮箱看，比如163邮箱为smtp.163.com 
    @password:发信人的邮箱密码 
    '''  
    mail_msg = MIMEMultipart()  
    if not isinstance(subject,unicode):  
        subject = unicode(subject, 'utf-8')  
    mail_msg['Subject'] = subject  
    mail_msg['From'] =fromaddr  
    mail_msg['To'] = ','.join(toaddrs)  
    mail_msg.attach(MIMEText(msg,_subtype='plain',_charset='utf-8'))
    try:  
        s = smtplib.SMTP()  
        s.connect(smtpaddr)  #连接smtp服务器  
        s.login(fromaddr,password)  #登录邮箱  
        s.sendmail(fromaddr, toaddrs, mail_msg.as_string()) #发送邮件  
        s.quit()  
    except Exception,e:  
       print "Error: unable to send email"  
       print traceback.format_exc()  

def Checkjdb(name,mobile):
	url = "http://check.office.jiedaibao.com/kaohe/query"
	d1 = datetime.datetime.now()
	week_day = d1.weekday()              #判断当天是星期几
	if week_day == 0:
		start_time = d1.strftime('%Y-%m-%d') 
		Mon = d1 + datetime.timedelta(days=6)
		end_time = Mon.strftime('%Y-%m-%d') 
	elif week_day == 1:
		Tus_S = d1 - datetime.timedelta(days=1)
		start_time = Tus_S.strftime('%Y-%m-%d') 
		Tus_E = d1 + datetime.timedelta(days=5)
		end_time = Tus_E.strftime('%Y-%m-%d') 
	elif week_day == 2:
		Wen_S = d1 - datetime.timedelta(days=2)
		start_time = Wen_S.strftime('%Y-%m-%d') 
		Wen_E = d1 + datetime.timedelta(days=4)
		end_time = Wen_E.strftime('%Y-%m-%d')
	elif week_day == 3:
		Thes_S = d1 - datetime.timedelta(days=3)
		start_time = Thes_S.strftime('%Y-%m-%d')
		Thes_E = d1 + datetime.timedelta(days=3)
		end_time = Thes_E.strftime('%Y-%m-%d')
	elif week_day == 4:
		Fri_S = d1 - datetime.timedelta(days=4)
		start_time = Fri_S.strftime('%Y-%m-%d')
		Fri_E = d1 + datetime.timedelta(days=2)
		end_time = Fri_E.strftime('%Y-%m-%d')
	elif week_day == 5:
		Sat_S = d1 - datetime.timedelta(days=5)
		start_time = Sat_S.strftime('%Y-%m-%d')
		Sat_E = d1 + datetime.timedelta(days=1)
		end_time = Sat_E.strftime('%Y-%m-%d')
	elif week_day == 6:
		Sun_S = d1 - datetime.timedelta(days=6)
		start_time = Sun_S.strftime('%Y-%m-%d')
		end_time = d1.strftime('%Y-%m-%d')
	
	value = {"mobile":mobile,"start_time":start_time,"end_time":end_time} #得到post参数      
	data = urllib.urlencode(value) #对参数进行URL编码
	request = urllib2.Request(url,data) #post请求
	response = urllib2.urlopen(request) #获得响应
	s = response.read()
	count = s.count("是")               #测试发现，当合格的时候页面有两个“是”，不合格只有一个，所以直接数“是”的个数
	"""if count == 2:
		return name,"pass"
	else:
		return name,mobile"""
	if count !=2:
		return name,mobile
		
n1 = "hudi"      
m1 = "18518135404"  

n2 = "shanwen" 
m2= "18701328801"

n3 = "yaozw" 
m3 = "13910534367"


n5 = "chendong"
m5 = "18610313906"

n6 = "renhj"
m6= "13671220192"

n7 = "luyg"
m7 = "18701435505"

n8 = "wanggl"
m8 = "15210996923"

n9 = "gengdy"
m9 = "18514472971"

n10 = "zhangsong"
m10 = "18883287192"



if __name__ == '__main__':  
    fromaddr = "hudi@jiedaibao.com"  
    smtpaddr = "smtp.exmail.qq.com"  
    toaddrs = ["hudi@jiedaibao.com"]  
    subject = "借贷宝每周7次操作检测"  
    password = "M2xoJ2bKk8dLl8jS"  
    i1 = Checkjdb(n1,m1)
    i2 = Checkjdb(n2,m2)
    i3 = Checkjdb(n3,m3)
    i5 = Checkjdb(n5,m5)
    i6 = Checkjdb(n6,m6)
    i7 = Checkjdb(n7,m7)
    i8 = Checkjdb(n8,m8)
    i9 = Checkjdb(n9,m9)
    i10 = Checkjdb(n10,m10)
    message = [i1,i2,i3,i5,i6,i7,i8,i9,i10]   
    message1 = str(message)
    msg = message1
    print message1
    sendmail(subject,msg,toaddrs,fromaddr,smtpaddr,password)  