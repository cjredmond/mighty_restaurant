# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-21 13:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utility', '0006_food_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='finished',
            field=models.BooleanField(default=False),
        ),
    ]
