# Generated by Django 3.2.8 on 2021-11-01 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0002_alter_customer_birth_mounth'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='image',
            field=models.ImageField(blank=True, upload_to='user', verbose_name='Сурет: '),
        ),
    ]
