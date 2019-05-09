# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from rest_framework.decorators import parser_classes
from rest_framework.parsers import JSONParser

#from rest_framework import generics
#from rest_framework_word_filter import FullWordSearchFilter

from threats.models import Threat
from threats.serializers import ThreatSerializer

#from django.shortcuts import render
from django.db.models import Q
import re

from django.http import FileResponse

@api_view(['GET','POST'])
@parser_classes((JSONParser,))
def threat_list(request):

#    if request.method == 'GET':
#        threats = Threat.objects.all()
#        serializer = ThreatSerializer(threats, many=True)
#        return Response(serializer.data)

    if request.method == 'POST':
        search_ip = request.data.get("ip")
        if search_ip is not None:
            ip_check = re.compile(r"^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$")
            if ip_check.match(search_ip):
                try:
                    threat_search = Threat.objects.get(Q(Malicious_IP__contains=search_ip) | Q(Inner_IP__contains=search_ip))
                    type_info = threat_search.Threat_type
		    intelligence_info = threat_search.Intelligence
                    threat_search.Count += 1
                    threat_search.save()
                    return Response({"danger": 1, "type": type_info, "intelligence":intelligence_info, "error": 0})
                except:
                    return Response({"danger": 0, "type": [], "error": 0})

            else:
                return Response({"danger": 0, "type": [], "error": 1})


def file_down_for_sysmon(request):
	file = open('/root/sysmonconfig.xml','rb')
	response = FileResponse(file)
	response['Content-Type'] = 'application/octet-stream'
	response['Content-Disposition'] = 'attachment;filename="sysmonconfig.xml"'
	return response 

def file_down_for_winlogbeat(request):
        file = open('/root/winlogbeat.yml','rb')
        response = FileResponse(file)
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="winlogbeat.yml"'
        return response



#@api_view(['GET', 'PUT'])
#def threat_detail(request, pk):

#    try:
        threat = Threat.objects.get(pk=pk)
#    except Threat.DoesNotExist:
#        return Response(status=status.HTTP_404_NOT_FOUND)

#    if request.method == 'GET':
#        serializer = ThreatSerializer(threat)
#        #return =  Response(serializer.data)
#        return render(request,'threats/index.html',{'threat':threat})

#    elif request.method == 'PUT':
#        serializer = ThreatSerializer(threat, data=request.data)
#        if serializer.is_valid():
#            serializer.save()
#            return Response(serializer.data)
#        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
