# Generated by Django 4.1.6 on 2023-02-19 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0008_rename_name_work_planning_employees_id'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='work_planning',
            name='department',
        ),
        migrations.AddField(
            model_name='employees',
            name='department',
            field=models.CharField(max_length=50, null=True, verbose_name='Departament'),
        ),
    ]