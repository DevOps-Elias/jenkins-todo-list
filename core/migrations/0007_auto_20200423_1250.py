# Generated by Django 2.1.7 on 2020-04-23 15:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20200423_1243'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='created_at',
            field=models.DateField(blank=True, default=datetime.datetime(2020, 4, 23, 12, 50, 14, 591367)),
        ),
    ]
