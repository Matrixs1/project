# Generated by Django 4.0.3 on 2022-04-05 11:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0008_alter_appointment_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='appointment',
            name='department_name',
        ),
        migrations.RemoveField(
            model_name='appointment',
            name='doctor_name',
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.TimeField(default=datetime.datetime(2022, 4, 5, 13, 6, 20, 277235)),
        ),
    ]