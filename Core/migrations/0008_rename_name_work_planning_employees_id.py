# Generated by Django 4.1.6 on 2023-02-19 15:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0007_remove_work_planning_name_id_work_planning_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='work_planning',
            old_name='name',
            new_name='employees_id',
        ),
    ]