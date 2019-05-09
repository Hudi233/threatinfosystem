import os 
os.environ.setdefault("DJANGO_SETTINGS_MODULE","iplist.settings")

import django
django.setup()


from django.utils import timezone
import xlrd
from F5.models import F5


def input(VS,pool_text,port,idc_text):
	i = F5(
		VS = vs,
		pool = pool_text,
		pool_port = port,
		idc = idc_text
		)
	i.save()

f5file = xlrd.open_workbook('f4.xls')
sh = f5file.sheet_by_index(0)
n = 0
for i in range(1,sh.nrows):

	vs = sh.cell(i,0).value
	pool_text = sh.cell(i,1).value
	port = sh.cell(i,2).value
	idc = sh.cell(i,3).value
	input(vs,pool_text,port,idc)
	n += 1
print n
