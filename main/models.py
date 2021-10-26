from django.db import models


class Question(models.Model):
	question = models.CharField('Сұрақ', max_length = 1000)
	answer   = models.CharField('Жауабы', max_length = 1000)

	def __str__(self):
		return self.question

	class Meta:
		verbose_name = 'Қазақстан тарихы'
		verbose_name_plural = 'Қазақстан тарихы'