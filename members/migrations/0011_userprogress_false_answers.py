# Generated by Django 3.2.8 on 2021-11-19 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0010_alter_userpicture_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprogress',
            name='false_answers',
            field=models.TextField(blank=True, verbose_name='Қате сұрақтар '),
        ),
    ]