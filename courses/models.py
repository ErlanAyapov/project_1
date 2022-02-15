from django.db import models


class WorldHistory(models.Model):
	question = models.CharField('Сұрақ', max_length = 1000)
	answer   = models.CharField('Жауабы', max_length = 1000)

	def __str__(self):
		return self.question

	class Meta:
		verbose_name = 'Дүниежүзі тарихы'
		verbose_name_plural = 'Дүниежүзі тарихы'


class Physic(models.Model):
	question = models.CharField('Сұрақ', max_length = 1000)
	answer   = models.CharField('Жауабы', max_length = 1000)

	def __str__(self):
		return self.question

	class Meta:
		verbose_name = 'Физика'
		verbose_name_plural = 'Физика'


class QazaqstanHistory(models.Model):
	question 	   = models.CharField('Сұрақ', max_length = 500)
	answer_true	   = models.CharField('Жауабы (Дұрыс)', max_length = 100)
	answer_false_1 = models.CharField('Жауабы (Бұрыс)', max_length = 100)
	answer_false_2 = models.CharField('Жауабы (Бұрыс)', max_length = 100)
	answer_false_3 = models.CharField('Жауабы (Бұрыс)', max_length = 100)

	def __str__(self):
		return self.question

	class Meta:
		verbose_name = 'Қазақстан тарихы (Pro)'
		verbose_name_plural = 'Қазақстан тарихы (Pro)'  