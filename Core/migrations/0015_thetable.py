# Generated by Django 4.1.6 on 2023-02-28 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0014_rename_work_planning_workplanning'),
    ]

    operations = [
        migrations.CreateModel(
            name='TheTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField()),
            ],
        ),
    ]
