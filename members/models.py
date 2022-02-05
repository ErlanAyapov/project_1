from django.db import models
from django.contrib.auth.models import User


class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_day = models.IntegerField('Туылған күні')
    birth_mounth = models.CharField('Туылған айы', max_length = 10)
    birth_year = models.IntegerField('Туылған жылы')
    
    def __str__(self):
        return str(self.user)



class UserPicture(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    photo = models.TextField('Сурет: (Base 64) ')
    
    def __str__(self):
        return str(self.user)



class UserProgress(models.Model):

    COURSE_TYPE_KK = 'Қазақстан тарихы'
    COURSE_TYPE_DZH = 'Дүниежүзі тарихы'
    COURSE_TYPE_PHY = 'Физика'

    BUYING_TYPE_CHOICES = (
        (COURSE_TYPE_KK, 'Қазақстан тарихы'),
        (COURSE_TYPE_DZH, 'Дүниежүзі тарихы'),
        (COURSE_TYPE_PHY, 'Физика')
    )
    course = models.CharField(max_length=50,
        verbose_name='Тапсырған сабағы',
        choices=BUYING_TYPE_CHOICES,
        default=COURSE_TYPE_KK)

    user         = models.ForeignKey(User, on_delete=models.CASCADE)
    result_all   = models.IntegerField('Жалпы сұрақ')
    result_true  = models.IntegerField('Қате сұрақ')
    result_false = models.IntegerField('Дұрыс сұрақ')
    false_answers = models.TextField('Қате сұрақтар ', blank = True)
    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name} | Жалпы:{self.result_all}, Дұрыс:{self.result_true}, Қате:{self.result_false}'