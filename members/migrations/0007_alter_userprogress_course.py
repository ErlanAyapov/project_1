# Generated by Django 3.2.8 on 2021-11-12 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0006_rename_prduct_type_userprogress_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprogress',
            name='course',
            field=models.CharField(choices=[('Қазақстан тарихы', 'Қазақстан тарихы'), ('Дүниежүзі тарихы', 'Дүниежүзі тарихы')], default='Қазақстан тарихы', max_length=50, verbose_name='Тапсырған сабағы'),
        ),
    ]
