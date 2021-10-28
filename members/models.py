from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_day = models.IntegerField('Туылған күні')
    birth_mounth = models.CharField('Туылған айы', max_length = 10)
    birth_year = models.IntegerField('Туылған жылы')
    profile_photo = models.TextField('Сурет (Base 64) ')

    def __str__(self):
        return str(self.user)