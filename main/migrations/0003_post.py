# Generated by Django 3.2.8 on 2021-12-12 04:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0002_auto_20211026_1642'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500, verbose_name='Тақырып')),
                ('body', models.TextField(verbose_name='Мәтін')),
                ('image', models.TextField(blank=True, verbose_name='Сурет (Base64)')),
                ('date', models.CharField(max_length=50, verbose_name='Уақыты')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Автор')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Пост',
            },
        ),
    ]
