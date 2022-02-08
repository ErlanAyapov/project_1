from django.urls import path 
from .views import *

urlpatterns = [
	path('', main_view, name = 'main'),
	path('post/create', post_add, name = 'post_add'),
	path('post/delete/<int:pk>', PostDeleteView.as_view(), name = 'post_delete'),
]