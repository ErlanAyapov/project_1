from django.shortcuts import render
from django.views.generic import ListView
from main.models import Question
from .models import WorldHistory, Physic, QazaqstanHistory




class QazaqstanTarihyView(ListView):
	model = Question
	ordering = '-id'
	template_name = 'courses/qazaq.html'


class WorldHistoryView(ListView):
	model = WorldHistory
	ordering = '-id'
	template_name = 'courses/world.html'


class PhysicView(ListView):
	model = Physic
	ordering = '-id'
	template_name = 'courses/physic.html'

class QazaqstanTarihyPro(ListView):
	model = QazaqstanHistory
	ordering = '-id'
	template_name = 'courses/qazaq_pro.html'