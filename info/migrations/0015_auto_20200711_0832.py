# Generated by Django 2.2.8 on 2020-07-11 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0014_auto_20200707_1720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='date',
            field=models.DateField(default='2018-10-23'),
        ),
        migrations.AlterField(
            model_name='marks',
            name='name',
            field=models.CharField(choices=[('Internal test 1', 'Internal test 1'), ('Internal test 2', 'Internal test 2'), ('Internal test 3', 'Internal test 3'), ('Event 1', 'Event 1'), ('Event 2', 'Event 2'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
        migrations.AlterField(
            model_name='marksclass',
            name='name',
            field=models.CharField(choices=[('Internal test 1', 'Internal test 1'), ('Internal test 2', 'Internal test 2'), ('Internal test 3', 'Internal test 3'), ('Event 1', 'Event 1'), ('Event 2', 'Event 2'), ('Semester End Exam', 'Semester End Exam')], default='Internal test 1', max_length=50),
        ),
    ]
