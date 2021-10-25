from django.urls import path 
from .views import *

urlpatterns = [
	path('tarih', QazaqstanTarihy.as_view(), name = 'q_tarih')
]