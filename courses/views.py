from django.shortcuts import render
from django.views.generic import ListView
from main.models import Question
from .models import WorldHistory, Physic




class QazaqstanTarihy(ListView):
	model = Question
	ordering = '-id'
	template_name = 'courses/qazaq.html'


class WorldHistory(ListView):
	model = WorldHistory
	ordering = '-id'
	template_name = 'courses/world.html'


class Physic(ListView):
	model = Physic
	ordering = '-id'
	template_name = 'courses/physic.html'