from django.shortcuts import render
from django.views.generic import ListView
from main.models import Question



class QazaqstanTarihy(ListView):
	model = Question
	ordering = '-id'
	template_name = 'courses/qazaq.html'