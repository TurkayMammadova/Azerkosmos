# Generated by Django 4.1.6 on 2023-03-02 18:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0027_department_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='department',
            name='table',
        ),
        migrations.AddField(
            model_name='thetable',
            name='table',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Core.thetable'),
        ),
    ]
