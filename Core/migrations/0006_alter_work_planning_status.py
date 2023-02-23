# Generated by Django 4.1.6 on 2023-02-19 15:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0005_employees_remove_work_planning_name_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='work_planning',
            name='status',
            field=models.IntegerField(choices=[(1, 'on_side'), (2, 'remote')], default=1),
        ),
    ]
