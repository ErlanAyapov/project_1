# Generated by Django 3.2.8 on 2021-10-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'verbose_name': 'Қазақстан тарихы', 'verbose_name_plural': 'Қазақстан тарихы'},
        ),
        migrations.AlterField(
            model_name='question',
            name='answer',
            field=models.CharField(max_length=1000, verbose_name='Жауабы'),
        ),
        migrations.AlterField(
            model_name='question',
            name='question',
            field=models.CharField(max_length=1000, verbose_name='Сұрақ'),
        ),
    ]
