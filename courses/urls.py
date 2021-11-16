from django.urls import path 
from .views import *


urlpatterns = [
	path('kazakhstan-history/', QazaqstanTarihy.as_view(), name = 'q_tarih'),
	path('world-history/', WorldHistory.as_view(), name = 'w_tarih'),
	path('physic/', Physic.as_view(), name = 'physic'),
]