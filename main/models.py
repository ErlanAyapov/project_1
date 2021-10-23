from django.db import models


class Question(models.Model):
	question = models.CharField('Сұрақтар', max_length = 1000)
	answer   = models.CharField('Жауаптары', max_length = 1000)

	def __str__(self):
		return self.question