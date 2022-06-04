# Generated by Django 4.0.5 on 2022-06-03 06:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('indexing', '0003_alter_grade_options_alter_lecture_title_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='list_of_control_activities',
            name='date_of_approval',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='дата утверждения'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list_of_control_activities',
            name='dean',
            field=models.CharField(default='Тищенко Е.Н.', max_length=350, verbose_name='декан'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='list_of_control_activities',
            name='faculty',
            field=models.CharField(default='КТ и ИБ', max_length=350, verbose_name='факультет'),
            preserve_default=False,
        ),
    ]
