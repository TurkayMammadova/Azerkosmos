# Generated by Django 4.1.6 on 2023-02-19 10:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Core', '0004_alter_work_planning_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='işçilərin siyahısı')),
            ],
        ),
        migrations.RemoveField(
            model_name='work_planning',
            name='name',
        ),
        migrations.AddField(
            model_name='work_planning',
            name='name_id',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Core.employees'),
        ),
    ]
