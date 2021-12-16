from django.db import models
from django.contrib.auth.models import User


class Question(models.Model):
	question = models.CharField('Сұрақ', max_length = 1000)
	answer   = models.CharField('Жауабы', max_length = 1000)

	def __str__(self):
		return self.question

	class Meta:
		verbose_name = 'Қазақстан тарихы'
		verbose_name_plural = 'Қазақстан тарихы'



class Post(models.Model):
	author = models.ForeignKey(User, verbose_name='Автор', on_delete=models.CASCADE, null=True)
	title  = models.CharField('Тақырып', max_length = 500)
	body   = models.TextField('Мәтін')
	image  = models.TextField('Сурет (Base64)', blank = True)
	date   = models.CharField('Уақыты', max_length = 50)

	def __str__(self):
		return self.title

	class Meta:
		verbose_name = 'Пост'
		verbose_name_plural = 'Пост'