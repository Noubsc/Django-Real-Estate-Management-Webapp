# Generated by Django 3.2.22 on 2023-10-28 03:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2023, 10, 28, 10, 50, 7, 938073)),
        ),
    ]
