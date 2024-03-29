# Generated by Django 4.0.5 on 2022-06-05 11:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indexing', '0005_checkpoint_formholding_gradeitem_gradeservice_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='formholding',
            options={'verbose_name': 'Форма проведения', 'verbose_name_plural': 'Формы проведения'},
        ),
        migrations.AlterModelOptions(
            name='gradeserviceset',
            options={'verbose_name': 'Группа оценочных средств', 'verbose_name_plural': 'Группы оценочных средств'},
        ),
        migrations.AlterModelOptions(
            name='orderholding',
            options={'verbose_name': 'Порядок проведения', 'verbose_name_plural': 'Порядки проведения'},
        ),
        migrations.RemoveField(
            model_name='gradeserviceset',
            name='evaluation_pattern',
        ),
        migrations.AddField(
            model_name='gradeserviceset',
            name='evaluation_scale',
            field=models.TextField(blank=True, null=True, verbose_name='Шкала оценивания'),
        ),
        migrations.AlterField(
            model_name='formholding',
            name='description',
            field=models.TextField(unique=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='gradeitem',
            name='grade_service_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lca_grade_items', to='indexing.gradeserviceset', verbose_name='Группа оценочных стредств'),
        ),
        migrations.AlterField(
            model_name='graderesult',
            name='grade_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexing.gradeitem', verbose_name='занятие'),
        ),
        migrations.AlterField(
            model_name='graderesult',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexing.students', verbose_name='студент'),
        ),
        migrations.AlterField(
            model_name='gradeservice',
            name='name',
            field=models.CharField(max_length=350, unique=True, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='gradeserviceset',
            name='evaluation_rate',
            field=models.FloatField(verbose_name='Баллов за единицу'),
        ),
        migrations.AlterField(
            model_name='orderholding',
            name='description',
            field=models.TextField(unique=True, verbose_name='Описание'),
        ),
    ]
