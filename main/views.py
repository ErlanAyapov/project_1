from django.shortcuts import render
from django.views.generic import ListView
from .models import Question

class MainView(ListView):
	model = Question
	ordering = '-id'
	template_name = 'main/index.html'