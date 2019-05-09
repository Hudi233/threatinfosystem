# -*- coding: utf-8 -

from rest_framework import serializers
from threats.models import Threat
class ThreatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Threat
        fields = ('Threat_type','Malicious_IP','Inner_IP','Domain','Intelligence','Wiki','Time','Count')
