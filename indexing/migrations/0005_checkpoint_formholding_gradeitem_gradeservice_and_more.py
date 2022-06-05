# Generated by Django 4.0.5 on 2022-06-04 11:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('indexing', '0004_list_of_control_activities_date_of_approval_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CheckPoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.SmallIntegerField(verbose_name='Номер')),
                ('date', models.DateField(verbose_name='Дата')),
            ],
            options={
                'verbose_name': 'Контрольная точка',
                'verbose_name_plural': 'Контрольные точки',
            },
        ),
        migrations.CreateModel(
            name='FormHolding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Порядок проведения',
                'verbose_name_plural': 'Порядки проведения',
            },
        ),
        migrations.CreateModel(
            name='GradeItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True, verbose_name='Дата занятия')),
            ],
        ),
        migrations.CreateModel(
            name='GradeService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=350, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Оценочное средство',
                'verbose_name_plural': 'Оценочные средства',
            },
        ),
        migrations.CreateModel(
            name='OrderHolding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(verbose_name='Описание')),
            ],
            options={
                'verbose_name': 'Форма проведения',
                'verbose_name_plural': 'Формы проведения',
            },
        ),
        migrations.AlterModelOptions(
            name='list_of_control_activities',
            options={'verbose_name': 'Лист контрольных мероприятий', 'verbose_name_plural': 'Листы контрольных мероприятий'},
        ),
        migrations.RemoveField(
            model_name='list_of_control_activities',
            name='check_point_date_end',
        ),
        migrations.RemoveField(
            model_name='list_of_control_activities',
            name='check_point_date_start',
        ),
        migrations.AlterField(
            model_name='list_of_control_activities_value',
            name='value',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lca_items', to='indexing.list_of_control_activities', verbose_name='Содержание'),
        ),
        migrations.CreateModel(
            name='GradeServiceSet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('evaluation_quantity', models.IntegerField(verbose_name='Количество')),
                ('evaluation_rate', models.FloatField(verbose_name='Оценка за единицу')),
                ('evaluation_pattern', models.TextField(verbose_name='Шаблон')),
                ('evaluation_criteria', models.TextField(verbose_name='Критерии оценивания')),
                ('check_point', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexing.checkpoint', verbose_name='Контрольная точка')),
                ('form_holding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexing.formholding', verbose_name='Форма проведения')),
                ('grade_service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexing.gradeservice', verbose_name='Оценочное средство')),
                ('order_holding', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexing.orderholding', verbose_name='Порядок проведения')),
            ],
            options={
                'verbose_name': 'Запись в ЛКМ',
                'verbose_name_plural': 'Записи в ЛКМ',
            },
        ),
        migrations.CreateModel(
            name='GradeResult',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grade_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexing.gradeitem', verbose_name='')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='indexing.students', verbose_name='')),
            ],
        ),
        migrations.AddField(
            model_name='gradeitem',
            name='grade_service_set',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lca_grade_items', to='indexing.gradeserviceset', verbose_name=''),
        ),
        migrations.AddField(
            model_name='checkpoint',
            name='lca',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='lca_checkpoints', to='indexing.list_of_control_activities', verbose_name='ЛКМ'),
        ),
    ]