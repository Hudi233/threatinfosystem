from django.conf.urls import url
from threats import views

urlpatterns = [
    url(r'^threatinfo/search/$', views.threat_list),
    url(r'^download/sysmonconfig.xml',views.file_down_for_sysmon),
    url(r'^download/winlogbeat.yml',views.file_down_for_winlogbeat),
    #url(r'^threatinfo/(?P<pk>[0-9]+)/$',views.threat_detail),
    #url(r'^threatinfo/$', views.ThreatListView.as_view()),
    #url(r'^test/$', views.first_page)
]
