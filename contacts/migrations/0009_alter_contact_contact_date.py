# Generated by Django 3.2 on 2022-07-23 10:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0008_alter_contact_contact_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2022, 7, 23, 12, 6, 29, 114112)),
        ),
    ]
