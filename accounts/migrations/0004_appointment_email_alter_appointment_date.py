# Generated by Django 4.0.3 on 2022-04-05 09:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='email',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='appointment',
            name='date',
            field=models.TimeField(default=datetime.datetime(2022, 4, 5, 11, 57, 27, 612954)),
        ),
    ]