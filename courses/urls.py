from django.urls import path 
from .views import *

urlpatterns = [
	path('Қазақстан-тарихы/', QazaqstanTarihy.as_view(), name = 'q_tarih'),
	path('дүниежүзі-тарихы/', WorldHistory.as_view(), name = 'w_tarih'),
]