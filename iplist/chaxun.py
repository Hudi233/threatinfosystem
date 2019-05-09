import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE","iplist.settings")

import django
django.setup()
from ips.models import IPlist

#print IPlist.objects.all()

test1=IPlist.objects.get(ip_text='xxx',port_text='443')
print test1

#ips1 = Entry.objects.filter(ip_text="114.113.67.42",port_text="443")
#print ips1




