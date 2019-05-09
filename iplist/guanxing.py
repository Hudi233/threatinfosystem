# -*- coding:utf-8 -*-
#!/usr/bin/python

import requests
import json
import datetime

import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE","iplist.settings")

import django
django.setup()
from ips.models import IPlist


import sys, os, re, urlparse  
import smtplib  
import traceback  
from email.mime.text import MIMEText  
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def sendmail(subject,attfile,toaddrs,fromaddr,smtpaddr,password,content):  
    ''''' 
    @subject:邮件主题 
    @attfile:邮件附件 
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
    mail_msg.attach(MIMEText(content,_subtype='plain',_charset='utf-8'))
    basename = os.path.basename(attfile)
    att = MIMEText(open(attfile,'rb').read(),'base64','gb2312')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment; filename=%s' % basename.encode('gb2312')
    mail_msg.attach(att)
    try:  
        s = smtplib.SMTP()  
        s.connect(smtpaddr)  #连接smtp服务器  
        s.login(fromaddr,password)  #登录邮箱  
        s.sendmail(fromaddr, toaddrs, mail_msg.as_string()) #发送邮件  
        s.quit()  
    except Exception,e:  
       print "Error: unable to send email"  
       print traceback.format_exc() 



today = str(datetime.date.today())
output = open('./guanxing.log','w+')
output.write('\n========'+today+'========\n')
s = requests.session()
header1 = {
"Accept":"*/*",
"Accept-Encoding":"gzip, deflate, sdch, br",
"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
"Access-Control-Request-Headers":"content-type",
"Access-Control-Request-Method":"POST",
"Cache-Control":"no-cache",
"Connection":"keep-alive",
"Host":"api.guanxingtai.net",
"Origin":"https://guanxingtai.net",
"Pragma":"no-cache",
"Referer":"https://guanxingtai.net/admin/",
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"
}
header2 = {
"Accept":"application/json, text/plain, */*",
"Accept-Encoding":"gzip, deflate, br",
"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
"Cache-Control":"no-cache",
"Connection":"keep-alive",
"Content-Length":"68",
"Content-Type":"application/json;charset=UTF-8",
"Host":"api.guanxingtai.net",
"Origin":"https://guanxingtai.net",
"Pragma":"no-cache",
"Referer":"https://guanxingtai.net/admin/",
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"
}

headers = {
"Accept":"application/json, text/plain, */*",
"Accept-Encoding":"gzip, deflate, sdch, br",
"Accept-Language":"zh-CN,zh;q=0.8,en;q=0.6",
"Cache-Control":"no-cache",
"Connection":"keep-alive",
"Content-Type":"application/json;charset=UTF-8",
"Host":"api.guanxingtai.net",
"Origin":"https://guanxingtai.net",
"Pragma":"no-cache",
"Referer":"https://guanxingtai.net/admin/",
"User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36"
}

# login_data = {'%s':"luyg@jiedaibao.com",'%s':'%s','%s':"feixia2009"} %('account','from','null','password')
login_data = '{account: "security@jiedaibao.com", password: "JDBxtAqb(666)!@", from: null}'
r=s.options("https://api.guanxingtai.net/portal/user/check-login.html",headers=header1, verify=False)
# print r.headers

# content = s.post('https://api.guanxingtai.net/portal/user/check-login.html',headers = headers ,data=json.dumps(login_data), verify=False)
content = s.post('https://api.guanxingtai.net/portal/user/check-login.html',headers = header2 , data=login_data, verify=False)

#s.get('https://guanxingtai.net/admin/#/home',verify=False)
#content=s.get('https://api.guanxingtai.net/portal/snapshot/vul-white-type.html?&type=1',verify=False)
# print content.headers
auth_content = content.content.split('"')
authorization_content = 'Bearer '+auth_content[3]
#print authorization_content
headers["Authorization"]= authorization_content
#print headers


#print auth.content
# content = s.get('https://guanxingtai.net/admin/#/home/moniter/port',verify=False)
# print content.content
r = s.get('https://guanxingtai.net/admin/#/home/moniter/port', headers=headers,verify=False)
r = s.get('https://api.guanxingtai.net/portal/snapshot/port-all.html?&type=all',headers=headers, verify=False)
ips = json.loads(r.content)
ports = ips['data']
# print type(ports)
# print len(ports)
# print ports['reduce']
# print ips.keys()
for k,v  in ports.iteritems():
    # print '%s:%s' %(k,v)
    pass
    #print ports[key]
print ports.keys()
change = ports['childs']
print change[0]
for i in range(len(change)):
    if len(change[i][u'adds']) >0:
        print '--adds_ip_ports:--'
        output.write('--adds_ip_ports:--\n')
        #print change[i]
        print change[i][u'ip']
        output.write(change[i][u'ip']+'\n')
        for j in range(len(change[i][u'adds'])):
            print change[i][u'adds'][j][u'port']
            output.write(change[i][u'adds'][j][u'port']+'\n')
	#begin search in django
	addip=change[i][u'ip']
	addport=change[i][u'adds'][j][u'port']
	try:	
		addbusiness = IPlist.objects.filter(ip_text=addip, port_text=addport)
		print addbusiness
		output.write(str(addbusiness) + '\n')
	except Exception,e:
       		print e

	#end


        # print change[i][u'adds']
        print '--------------'
        # print change[i][u'adds']
    elif len(change[i][u'reduces'])>0:
        print '--reduce_ip_ports:--'
        output.write('--reduce_ip_ports:--\n')
        #print change[i]
        print change[i][u'ip']
        output.write(change[i][u'ip'] + '\n')
        for j in range(len(change[i][u'reduces'])):
            print change[i][u'reduces'][j][u'port']
            output.write(change[i][u'reduces'][j][u'port'] + '\n')

	#begin search in django
	reduceip=change[i][u'ip']
	reduceport=change[i][u'reduces'][j][u'port']
	try:	
		reducebusiness=IPlist.objects.get(ip_text=reduceip, port_text=reduceport)
		print reducebusiness
		output.write(str(reducebusiness) + '\n')
	except Exception,e:
        	print e

	#end

        # print change[i][u'reduces']
        print '--------------'
        output.write('------------------\n')

output.close()

if __name__=='__main__':
    fromaddr = "xxx"  
    smtpaddr = "xxx"  
    toaddrs = ["xxx"]  
    subject = "观星台每日端口监测"  
    password = "xxx"
   
    sendmail(subject,u"guanxing.log",toaddrs,fromaddr,smtpaddr,password,"观星台审计")

