from django.urls import path 
from .views import *


urlpatterns = [
	path('kazakhstan-history-pro/', QazaqstanTarihyPro.as_view(), name = 'pro_tarih'),
	path('kazakhstan-history/', QazaqstanTarihyView.as_view(), name = 'q_tarih'),
	path('world-history/', WorldHistoryView.as_view(), name = 'w_tarih'),
	path('physic/', PhysicView.as_view(), name = 'physic'),
]