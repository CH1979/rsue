# Generated by Django 4.0.5 on 2022-06-06 10:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('indexing', '0009_alter_graderesult_options_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='graderesult',
            old_name='value',
            new_name='score',
        ),
    ]
